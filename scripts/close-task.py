#!/usr/bin/env python3
"""The mechanical half of closing a task. Run from the game's repo root: close-task.py <KEY-N> [--base <branch>]

Checks the branch against its base and prints a checklist: FIX is a failure (exit 1), TODO is a step for the session,
OK passed. It reads git and the docs, spends no model tokens, and changes nothing.
"""
import pathlib
import re
import subprocess
import sys

args = sys.argv[1:]
if not args or args[0].startswith("-"):
    sys.exit("usage: close-task.py <KEY-N> [--base <branch>]")
key = args[0]
root = pathlib.Path.cwd()


def git(*a):
    r = subprocess.run(["git", *a], capture_output=True, text=True, cwd=root)
    return r.stdout if r.returncode == 0 else None


base = args[args.index("--base") + 1] if "--base" in args else next(
    (b for b in ("origin/main", "main", "origin/master", "master") if git("rev-parse", "--verify", "-q", b)), None)
if not base or git("merge-base", "HEAD", base) is None:
    sys.exit("close-task: can't find the base branch. Pass --base <branch>.")

changed = git("diff", "--name-only", f"{base}...HEAD").split()
added = [l[1:] for l in git("diff", "-U0", f"{base}...HEAD", "--", "docs").splitlines() if l.startswith("+") and not l.startswith("+++")]
code = [f for f in changed if not f.startswith(("docs/", "scripts/")) and not f.endswith((".md", ".png", ".json", ".import"))]
results = []


def check(ok, name, fix):
    results.append(("OK" if ok else "FIX", name if ok else fix))


check(bool(changed), "branch has changes", f"no changes against {base}")
if code:
    check("docs/design/status.md" in changed, "status.md updated", "code changed but docs/design/status.md didn't")
    check(any(re.search(rf"\[Built,\s*{re.escape(key)}\]", l) for l in added),
          f"an item marked [Built, {key}]", f"no item marked **[Built, {key}]** in docs/design/")
if any("builder's call" in l.lower() for l in added):
    check("docs/design/decisions.md" in changed, "builder's calls recorded in decisions.md",
          "a builder's call was added but docs/design/decisions.md wasn't updated")

left = []
for path in sorted((root / "docs/design").glob("*.md")):
    for number, line in enumerate(path.read_text().splitlines(), 1):
        if key in line and not re.search(rf"\[Built,\s*{re.escape(key)}\]", line):
            left.append(f"{path.name}:{number}  {line.strip()[:80]}")
check(not left, f"every {key} mention in docs/design/ is Built", f"{key} appears but isn't Built:\n      " + "\n      ".join(left))

for script in ("check-design.py", "check-team.py"):
    if (root / "scripts" / script).exists():
        r = subprocess.run(["python3", f"scripts/{script}"], capture_output=True, text=True, cwd=root)
        check(r.returncode == 0, script, f"{script} failed: {(r.stderr or r.stdout).strip()[:300]}")

todo = ["update the catalogues this task touched (docs/art/catalogue.md and the like)",
        "add the playtest's Worth doing findings to Optional in the plan file, if the player sees this change",
        "run game-dev:code-reviewer and game-dev:design-guardian"]
for tag, text in results:
    print(f"{tag:<5}{text}")
for text in todo:
    print(f"TODO {text}")
sys.exit(1 if any(t == "FIX" for t, _ in results) else 0)
