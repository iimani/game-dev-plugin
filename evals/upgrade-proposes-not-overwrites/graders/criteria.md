---
type: llm
weight: 1
---

The response follows the game-dev `upgrade` skill. It passes only if ALL are true:
- It runs, or says it will run, the `upgrade-diff.py` script to see what is out of date, rather than guessing.
- It proposes each change for the owner's approval and waits, and says the game's own wording wins over the template.
- It does not say it will overwrite the game's files wholesale, and does not claim to have changed anything.
