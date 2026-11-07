#!/usr/bin/env python3
"""Fails if this plugin has stopped being generic.

- Roles, skills and templates name no specific game.
- Role files name no art or audio tool: the project file does that.
- Every role has a row in the team template.
"""
import json
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

hooks_file = root / "hooks/hooks.json"
if hooks_file.exists():
    for entries in json.loads(hooks_file.read_text())["hooks"].values():
        for entry in entries:
            for hook in entry["hooks"]:
                for script in re.findall(r"\$\{CLAUDE_PLUGIN_ROOT\}/(\S+?)\"?(?:\s|$)", hook["command"]):
                    if not (root / script).exists():
                        problems.append(f"hooks/hooks.json runs {script}, which doesn't exist")

LABELS = ("**Version:**", "**Run:**", "**Test:**", "**Export:**", "**See it (playtester):**", "**Keep engine-free:**")
for path in root.glob("skills/kickstart/templates/engines/*.md"):
    for label in LABELS:
        if label not in path.read_text():
            problems.append(f"{path.relative_to(root)} has no {label}")

if problems:
    sys.exit("check-plugin:\n  " + "\n  ".join(problems))
print("check-plugin: generic, every role is indexed, hooks resolve, engine adapters complete")
