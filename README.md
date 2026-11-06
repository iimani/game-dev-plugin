# game-dev

A game development team and method for Claude Code. It gives a game role agents, staged design methods with the owner's
gates, and a kickstart that sets up its design, planning and documentation.

## Two layers

- **This plugin** holds how each job is done on any game. It names no game, engine or art tool.
- **The game's repo** holds what's true of that game: `docs/design/`, `docs/process/`, `docs/team/` and `CLAUDE.md`.

Every role reads `docs/team/README.md` and `docs/team/<role>.md` first, and those win. Templates are copied into a game
at kickstart and belong to it from then on.

## What's in it

**Roles** (`game-dev:<role>`): `developer`, `level-designer`, `encounter-designer`, `game-artist`, `sound-designer`,
`narrative-writer`, `balance-analyst`, `code-reviewer`, `design-guardian`, `playtester`.

**Skills:**
- `kickstart` sets up a game: vision, platform, core loop, art style, sound, methods, then the scaffold and first plan.
- `choose-art-style` picks a style and tool by making the same test asset in each and judging it on the real screen.
- `plan-phase` plans the next phase, writes its plan file and cuts tasks.

**The method:**
- A design guideline in the repo that doubles as the implementation tracker. Every item is Built, Approved, Draft or
  Proposal. It's edited in the same PR as the change, so there's no sync step. A design document is optional: it's for
  reviewing a design, is imported once, and is then frozen.
- A staged method per kind of design work, each with its gates and proofs.
- Proved, not hoped: bots and solvers check content before a person plays it.
- A blind playtester that knows only what's on the screen.

## Install

```bash
claude plugin marketplace add iimani/game-dev-plugin
claude plugin install game-dev@game-dev-plugin
```

Then, in a game's repo, ask Claude to kick off the game, or run `/game-dev:kickstart`.

Plugins declared in a repo's settings don't load in cloud sessions. Use a local session for this team.

## Art and sound tools

These are referenced, not bundled. `skills/kickstart/templates/process/art-style.md` compares them and says how to
install one: [pxl](https://github.com/uilianks/pxl) (pixel art), [vex](https://github.com/uilianks/vex) (2D vector),
[kiln](https://github.com/uilianks/kiln) (low-poly and voxel 3D), [loom](https://github.com/uilianks/loom) (textures and
materials), [chirp](https://github.com/uilianks/chirp) (sound).

## Checks

```bash
python3 scripts/check-plugin.py
claude plugin validate .
```
