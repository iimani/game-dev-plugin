---
type: llm
weight: 1
---

The response points an existing game at the migrate path. It passes only if ALL are true:
- It names or uses the `migrate` skill (`/game-dev:migrate`), and does not suggest kickstart as the way to bring in
  existing code.
- It says nothing existing is thrown away or overwritten.
- It does not claim to have changed any files.
