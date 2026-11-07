#!/usr/bin/env python3
"""Shows where a game's copies of the plugin's templates have fallen behind. Run from the game's repo root.

- scripts: a game's scripts/check-*.py and telemetry-summary.py are exact copies (apart from the PLANNED set), so a
  difference means the plugin changed them.
- new files: template files the game doesn't have.
- headings: "## " headings in a template that the game's copy of CLAUDE.md, a method or a team file lacks.
It lists, changes nothing, and spends no model tokens. The session then proposes each update for the owner.
"""
import pathlib
import re

plugin = pathlib.Path(__file__).resolve().parent.parent
templates = plugin / "skills/kickstart/templates"
root = pathlib.Path.cwd()


def headings(path):
    return {re.sub(r"\s+", " ", l[3:]).strip().lower(): l[3:].strip() for l in path.read_text().splitlines() if l.startswith("## ")}


def normal(path):
    return "\n".join(l for l in path.read_text().splitlines() if not l.startswith("PLANNED"))


stale, new, missing = [], [], []

scripts = ["check-team.py", "check-design.py"]
if (root / "docs/process/telemetry.md").exists():
    scripts.append("telemetry-summary.py")
for name in scripts:
    mine, theirs = plugin / "scripts" / name, root / "scripts" / name
    if not theirs.exists():
        new.append(f"scripts/{name}")
    elif normal(mine) != normal(theirs):
        stale.append(f"scripts/{name}")

pairs = [(templates / "CLAUDE.md", root / "CLAUDE.md")]
for folder, dest in (("design", "docs/design"), ("process", "docs/process"), ("team", "docs/team")):
    for template in sorted((templates / folder).glob("*.md")):
        pairs.append((template, root / dest / template.name))

for template, mine in pairs:
    rel = mine.relative_to(root)
    if not mine.exists():
        if str(rel) != "docs/team/role-template.md":
            new.append(str(rel))
    elif template.parent.name != "design":
        for key, title in headings(template).items():
            if key not in headings(mine):
                missing.append(f"{rel}: ## {title}")

for title, items in (("Scripts that differ from the plugin's", stale), ("Template files this game doesn't have", new),
                     ("Template headings missing from this game's copy", missing)):
    print(f"{title} ({len(items)}):")
    print("\n".join("  " + i for i in items) if items else "  none")
    print()
