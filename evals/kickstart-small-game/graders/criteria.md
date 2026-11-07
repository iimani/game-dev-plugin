---
type: llm
weight: 1
---

The response follows the game-dev kickstart. It passes only if ALL are true:
- It uses or follows the kickstart (invokes the `kickstart` skill, or clearly describes its stages), and does not invent a
  different setup.
- It recognises this as a small game and recommends or offers the shorter small-game path (fewer docs, one gate), leaving
  the choice to the owner.
- It asks for or names what it needs from the owner (such as vision, platform or engine) and stops for them instead of
  deciding silently.
- It does not claim to have written files.
