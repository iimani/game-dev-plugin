#!/usr/bin/env python3
"""Tests the plugin's scripts against a throwaway game built from its own templates. No model calls, no network."""
import pathlib
import shutil
import subprocess
import sys
import tempfile

plugin = pathlib.Path(__file__).resolve().parent.parent
templates = plugin / "skills/kickstart/templates"
failures = []


def run(game, script, *args):
    r = subprocess.run(["python3", str(plugin / "scripts" / script), *args], cwd=game, capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def git(game, *args):
    subprocess.run(["git", "-c", "user.email=t@t", "-c", "user.name=t", *args], cwd=game, check=True, capture_output=True)


def expect(name, cond, detail=""):
    if not cond:
        failures.append(f"{name}: {detail.strip()[:300]}")


with tempfile.TemporaryDirectory() as tmp:
    game = pathlib.Path(tmp)
    shutil.copytree(templates / "design", game / "docs/design")
    shutil.copytree(templates / "process", game / "docs/process")
    (game / "docs/team").mkdir()
    shutil.copy(templates / "team/README.md", game / "docs/team/README.md")
    shutil.copy(templates / "CLAUDE.md", game / "CLAUDE.md")
    (game / "scripts").mkdir()
    (game / "docs/art").mkdir()
    (game / "docs/plans").mkdir()
    (game / "docs/art/catalogue.md").write_text("# Art catalogue\n")
    (game / "src").mkdir()
    shutil.copy(plugin / "scripts/check-design.py", game / "scripts/check-design.py")
    mech = game / "docs/design/mechanics.md"
    mech.write_text(mech.read_text() + "\n- Keys open doors **[Approved]**\n- Doors lock **[Draft]**\n- Jump **[Built, T-1]**\n")
    git(game, "init", "-q", "-b", "main"); git(game, "add", "-A"); git(game, "commit", "-qm", "init")

    # design-status
    code, out = run(game, "design-status.py")
    expect("design-status runs", code == 0, out)
    expect("design-status counts mechanics.md", any(l.startswith("mechanics.md") and l.split()[1:] == ["1", "1", "1", "0"] for l in out.splitlines()), out)
    expect("design-status lists the draft", "Doors lock" in out, out)

    # close-task: code changed and nothing else
    git(game, "switch", "-qc", "feature/t-2")
    (game / "src/a.gd").write_text("x\n"); git(game, "add", "-A"); git(game, "commit", "-qm", "code")
    code, out = run(game, "close-task.py", "T-2", "--base", "main")
    expect("close-task fails without status", code == 1 and "status.md" in out and "[Built, T-2]" in out, out)

    # close-task: now mark it built
    mech.write_text(mech.read_text() + "- Dash **[Built, T-2]**\n")
    status = game / "docs/design/status.md"
    status.write_text(status.read_text() + "| Dash | **Built** | src/a.gd | |\n")
    git(game, "add", "-A"); git(game, "commit", "-qm", "design")
    code, out = run(game, "close-task.py", "T-2", "--base", "main")
    expect("close-task passes", code == 0 and "TODO" in out and "FIX" not in out, out)

    # close-task: a mention that isn't built
    mech.write_text(mech.read_text() + "- Wall slide **[Approved]** T-2\n")
    git(game, "add", "-A"); git(game, "commit", "-qm", "oops")
    code, out = run(game, "close-task.py", "T-2", "--base", "main")
    expect("close-task flags an unbuilt mention", code == 1 and "Wall slide" in out, out)

    # decide
    (game / "docs/design/decisions.md").write_text(
        (game / "docs/design/decisions.md").read_text().replace("| <id> | | | |", "| D3 | Do keys carry? | yes | low |"))
    code, out = run(game, "decide.py", "--id", "D3", "--ruling", "Keys carry", "--quote", "keys carry over", "--touches", "mechanics.md")
    text = (game / "docs/design/decisions.md").read_text()
    expect("decide removes the open row", code == 0 and "| D3 | Do keys carry?" not in text, out + text)
    expect("decide adds the ruling", '"keys carry over"' in text and "| Keys carry |" in text, text)
    code, out = run(game, "design-status.py")
    expect("open decisions now zero", "Open decisions: 0" in out, out)

    # upgrade-diff
    (game / "scripts/check-design.py").write_text("old\n")
    (game / "docs/process/README.md").write_text("# x\n")
    code, out = run(game, "upgrade-diff.py")
    expect("upgrade-diff flags a stale script", "scripts/check-design.py" in out.split("Template files")[0], out)
    expect("upgrade-diff flags a new file", "scripts/check-team.py" in out and "docs/design/tech.md" not in out, out)
    expect("upgrade-diff flags a missing heading", "docs/process/README.md: ## 1. Which method for what" in out, out)

if failures:
    sys.exit("test-scripts:\n  " + "\n  ".join(failures))
print("test-scripts: design-status, close-task, decide and upgrade-diff pass")
