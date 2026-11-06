#!/usr/bin/env python3
"""Fails if this plugin has stopped being generic.

- Roles, skills and templates name no specific game.
- Role files name no art or audio tool: the project file does that.
- Every role has a row in the team template.
"""
import pathlib
import re
import sys

root = pathlib.Path(__file__).resolve().parent.parent
GAME_WORDS = re.compile(r"drowned|\bDRS-|\bwarden|DiveSession|SpriteKit", re.I)
TOOL_WORDS = re.compile(r"\bpxl\b|\bvex\b|\bkiln\b|\bloom\b|\bchirp\b", re.I)

problems = []
for path in [*root.glob("agents/*.md"), *root.glob("skills/**/*.md")]:
    text = path.read_text()
    rel = path.relative_to(root)
    for match in GAME_WORDS.finditer(text):
        problems.append(f"{rel} names a game: {match.group(0)}")
    if path.parent.name == "agents":
        for match in TOOL_WORDS.finditer(text):
            problems.append(f"{rel} names a tool: {match.group(0)}")

index = (root / "skills/kickstart/templates/team/README.md").read_text()
for path in root.glob("agents/*.md"):
    if f"`{path.stem}`" not in index:
        problems.append(f"role {path.stem} has no row in the team template")

if problems:
    sys.exit("check-plugin:\n  " + "\n  ".join(problems))
print("check-plugin: generic, and every role is indexed")
