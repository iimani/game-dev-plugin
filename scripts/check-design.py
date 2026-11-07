#!/usr/bin/env python3
"""Fails if a game's design guideline has drifted. Copied into a game's scripts/ by the kickstart.

- Every repo path a guideline file names exists. A path counts when its first folder is in the repo. A file the design
  plans but nobody has written yet goes in PLANNED.
- The index's routing table ("What to read for a task") names every section file, so a session can always be sent to it.
"""
import pathlib
import re
import sys

root = pathlib.Path(__file__).resolve().parent.parent
design = root / "docs/design"

# Files the guideline names as planned, not yet written. Remove an entry once the file exists.
PLANNED = set()
# Section files a session reaches through another file, not through the routing table.
NOT_ROUTED = {"README.md"}

problems = []
for path in sorted(design.rglob("*.md")):
    for span in re.findall(r"`([^`\n]+)`", path.read_text()):
        if span in PLANNED or "/" not in span or re.search(r"[<>*…\s{}]", span):
            continue
        if (root / span.split("/")[0]).exists() and not (root / span).exists():
            problems.append(f"{path.relative_to(root)} names `{span}`, which isn't in the repo")

index = (design / "README.md").read_text()
routing = index[index.index("### What to read for a task"):index.index("## Vision")]
for path in sorted(design.glob("*.md")):
    if path.name not in NOT_ROUTED and f"`{path.name}`" not in routing:
        problems.append(f"docs/design/{path.name} is in no row of the routing table")

if problems:
    sys.exit("check-design:\n  " + "\n  ".join(problems))
print("check-design: paths exist and every section is routed")
