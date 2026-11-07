---
type: llm
weight: 1
---

The response follows the game-dev `close` skill. It passes only if ALL are true:
- It runs, or says it will run, the `close-task.py` script with the task key first, and fixes what it reports before
  anything else.
- It marks the task's items as built in the design (`[Built, KEY-5]`) and updates the status.
- It runs both `game-dev:code-reviewer` and `game-dev:design-guardian` before the PR is marked ready.
- It does not merge the PR, and does not mark it ready before the reviewers are clean.
