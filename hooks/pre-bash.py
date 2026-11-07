#!/usr/bin/env python3
"""PreToolUse(Bash) hook. Only acts inside a game set up by the kickstart (it has docs/design/README.md).

- Blocks `git commit` and `git push` while on main or master, and any push that names main or master.
- On `git commit`, if staged files include code but none under docs/design/, adds a reminder to update the status.
"""
import json
import os
import re
import subprocess
import sys

try:
    event = json.load(sys.stdin)
except ValueError:
    sys.exit(0)

command = (event.get("tool_input") or {}).get("command", "")
cwd = event.get("cwd") or os.getcwd()
if not re.search(r"\bgit\s+(?:-C\s+\S+\s+)?(commit|push)\b", command):
    sys.exit(0)


def git(*args):
    result = subprocess.run(["git", "-C", cwd, *args], capture_output=True, text=True)
    return result.stdout.strip() if result.returncode == 0 else ""


root = git("rev-parse", "--show-toplevel")
if not root or not os.path.exists(os.path.join(root, "docs/design/README.md")):
    sys.exit(0)

branch = git("branch", "--show-current")
pushes_main = re.search(r"\bgit\b.*\bpush\b.*\b(?:HEAD:)?(?:main|master)\b", command)
if branch in ("main", "master") or pushes_main:
    print(
        "game-dev: no commits or pushes to main. Create a feature/<desc> or fix/<desc> branch, push it and open a PR.",
        file=sys.stderr,
    )
    sys.exit(2)

if re.search(r"\bgit\b.*\bcommit\b", command):
    staged = git("diff", "--cached", "--name-only").splitlines()
    code = [f for f in staged if not f.startswith(("docs/", "scripts/")) and not f.endswith((".md", ".json", ".png"))]
    if code and not any(f.startswith("docs/design/") for f in staged):
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "additionalContext": (
                    "game-dev: this commit changes code but nothing under docs/design/. If it builds, changes or "
                    "drops a guideline item, update that item's status in the same commit."
                ),
            }
        }))
