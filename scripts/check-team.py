#!/usr/bin/env python3
"""Fails if a game's docs/team/ has drifted. Copied into a game's scripts/ by the kickstart.

- Every role file has a row in docs/team/README.md.
- Every repo path a team file names exists. A path counts when its first folder is in the repo, so a command or a
  placeholder (<kind>) isn't read as one.
"""
import pathlib
import re
import sys

root = pathlib.Path(__file__).resolve().parent.parent
# Paths a team file names that aren't built yet. Remove an entry once the path exists.
PLANNED = set()
team = root / "docs/team"
index = (team / "README.md").read_text()

problems = []
for path in sorted(team.glob("*.md")):
    if path.name != "README.md" and path.stem not in index and path.name not in index:
        problems.append(f"docs/team/{path.name} has no row in docs/team/README.md")
    for span in re.findall(r"`([^`\n]+)`", path.read_text()):
        for token in span.split():
            if token in PLANNED or "/" not in token or re.search(r"[<>*…:{}$]", token) or token.startswith(("~", "-", "http")):
                continue
            if (root / token.split("/")[0]).exists() and not (root / token).exists():
                problems.append(f"docs/team/{path.name} names `{token}`, which isn't in the repo")

if problems:
    sys.exit("check-team:\n  " + "\n  ".join(problems))
print("check-team: every team file is indexed and its paths exist")
