#!/usr/bin/env python3
"""PostToolUse(Edit|Write|MultiEdit) hook. Only acts inside a game set up by the kickstart.

After an edit under docs/design/ or docs/team/, runs the game's own scripts/check-design.py or scripts/check-team.py.
A failing check is fed back to the session (exit 2) so it fixes the drift now.
"""
import json
import os
import subprocess
import sys

try:
    event = json.load(sys.stdin)
except ValueError:
    sys.exit(0)

path = (event.get("tool_input") or {}).get("file_path", "")
root = event.get("cwd") or os.getcwd()
rel = os.path.relpath(path, root) if path else ""

checks = {"docs/design/": "scripts/check-design.py", "docs/team/": "scripts/check-team.py"}
for prefix, script in checks.items():
    if rel.startswith(prefix) and os.path.exists(os.path.join(root, script)):
        result = subprocess.run(["python3", script], cwd=root, capture_output=True, text=True, timeout=60)
        if result.returncode != 0:
            print((result.stderr or result.stdout).strip() or f"{script} failed", file=sys.stderr)
            sys.exit(2)
