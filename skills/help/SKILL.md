---
name: help
description: Explain the game-dev plugin: its commands, its roles, how work moves, and what to do next in this repo. Use when the user asks for help with game-dev, or what it can do.
---

# game-dev help

Show the user the guide below, as it stands. Then look at this repo and end with one line on what to do next:

- no `docs/design/` and no game code: run `/game-dev:kickstart`;
- game code but no `docs/design/` or `docs/team/`: run `/game-dev:migrate`;
- set up: run `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/design-status.py"`, show its counts, and name the next item in
  `docs/design/plan.md` and the role that takes it.

If the user asked about one thing, answer only that.

## Commands

| Command | Use it to |
|---|---|
| `/game-dev:kickstart` | Start a new game: vision, platform, core loop, art style, sound, methods, team, first plan |
| `/game-dev:migrate` | Bring an existing game onto this setup, without losing anything |
| `/game-dev:choose-art-style` | Pick or change the art style, by testing the same scene in each |
| `/game-dev:choose-models` | See the recommended model for each role, and change them |
| `/game-dev:plan-phase` | Plan the next phase, write its plan file and cut tasks |
| `/game-dev:close` | Close a task: check it against the design, mark items Built, run the reviewers |
| `/game-dev:decide` | Record an owner's ruling in `decisions.md` and relabel what it settles |
| `/game-dev:upgrade` | Bring a game's copies of the templates up to date with the plugin |
| `/game-dev:help` | Show this guide |

## Roles

Sessions delegate to these. Ask for one by name, such as "use `game-dev:level-designer`".

| Role | Does |
|---|---|
| `developer` | Implements a planned task, test-first |
| `level-designer` | Levels, traversal, puzzles, pacing |
| `encounter-designer` | Creatures, bosses, set pieces, one stage at a time |
| `game-artist` | Production art in the game's chosen style |
| `sound-designer` | Sound effects, ambience, music |
| `narrative-writer` | Story, lore, every word the player reads |
| `balance-analyst` | Economy, difficulty and pacing numbers |
| `code-reviewer` | Read-only review against the architecture rules |
| `design-guardian` | Read-only audit of a change against the design |
| `playtester` | Plays blind, and reports what it understood |

## How work moves

1. **Design** through a method in `docs/process/`, with the owner's gates.
2. **Plan** a phase, with a role and a proof for each step.
3. **Build** by delegating each step to its role.
4. **Close** the task: mark items Built, then run the two reviewers.
5. **Playtest** blind, sized to the change.

## Where things live

| Path | Holds |
|---|---|
| `docs/design/` | The design and the tracker. It's the source of truth |
| `docs/process/` | How each kind of thing gets designed |
| `docs/team/` | What each role needs for this game, and "Who does what" |
| `docs/plans/` | A plan file per phase |
| `CLAUDE.md` | What every session needs |
