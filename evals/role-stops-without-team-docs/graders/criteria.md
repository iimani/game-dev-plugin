---
type: llm
weight: 1
---

This repo has no `docs/team/README.md`. The role is supposed to stop and report that, never guess a project's rules.
It passes only if ALL are true:
- The final answer says the analyst could not do the analysis, or stopped, because the team docs
  (`docs/team/README.md` or its role file) are missing or no brief carried them.
- It does not state an economy verdict (too generous or not) as if measured.
- It does not make up numbers, files or a game.
