# game-dev

A game development team and method for Claude Code. It gives a game role agents, staged design methods with the owner's
gates, and a kickstart that sets up its design, planning and documentation.

## Two layers

- **This plugin** holds how each job is done on any game. It names no game, engine or art tool.
- **The game's repo** holds what's true of that game: `docs/design/`, `docs/process/`, `docs/team/` and `CLAUDE.md`.

Delegation is the default: a game's `CLAUDE.md` tells sessions to hand work to the roles, using "Who does what" in
`docs/team/README.md`. Every role reads that file and `docs/team/<role>.md` first, and those win. Templates are copied into a game
at kickstart and belong to it from then on.

## What's in it

**Roles** (`game-dev:<role>`): `developer`, `level-designer`, `encounter-designer`, `game-artist`, `sound-designer`,
`narrative-writer`, `balance-analyst`, `code-reviewer`, `design-guardian`, `playtester`.

**Skills:**
- `kickstart` starts a new game: the scaffold, vision, platform, core loop, art style, sound, methods, team and first plan.
  A small game can take a shorter path with fewer docs and one gate.
- `migrate` brings an existing game onto this setup, without losing anything.
- `choose-art-style` picks a style and tool by making the same test asset in each and judging it on the real screen.
- `choose-models` recommends a model for each role, and records the owner's choice. `kickstart` and `migrate` run it.
- `plan-phase` plans the next phase, writes its plan file and cuts tasks. It checks the plan against the phase's exit.
- `playtest` runs one blind playtest from build to verdict: brief the tester, sort findings, fix the critical ones.
- `help` shows the commands and roles, and says what to do next in this repo.

**The method:**
- A design guideline in the repo that doubles as the implementation tracker. Every item is Built, Approved, Draft or
  Proposal. It's edited in the same PR as the change, so there's no sync step. A design document is optional: it's for
  reviewing a design, is imported once, and is then frozen.
- A staged method per kind of design work, each with its gates and proofs.
- Proved, not hoped: bots and solvers check content before a person plays it.
- A blind playtester that knows only what's on the screen. Critical findings are fixed in the same task, and the rest are
  ranked as optional work for the owner to pick.

## Install

```bash
claude plugin marketplace add iimani/game-dev-plugin
claude plugin install game-dev@game-dev-plugin
```

Keep it at user scope, as above: a project-scope install is tied to one folder.

Then run `/game-dev:help` in a game's repo. It says whether to kick off a new game or migrate an existing one.

Plugins declared in a repo's settings don't load in cloud sessions. Use a local session for this team.

## Hooks

Two hooks, active only in a game set up by the kickstart (a repo with `docs/design/README.md`), so other repos are
untouched. Each is a short Python script and costs no context unless it fires.

- Before a `git commit` or `git push` (`hooks/pre-bash.py`): blocks it on `main`, and reminds the session to update
  `docs/design/` when staged code has no design change.
- After an edit under `docs/design/` or `docs/team/` (`hooks/post-edit.py`): runs the game's `scripts/check-design.py`
  or `check-team.py` and feeds a failure back at once.

## Engine adapters

`skills/kickstart/templates/engines/` has a short adapter for Godot, Unity, Unreal, web and Bevy: the headless run, test
and export commands, how the playtester sees the game, and what to keep engine-free. The kickstart pastes the chosen one
into the game's `docs/design/tech.md`. The plugin itself stays engine-neutral.

## Telemetry

`skills/kickstart/templates/process/telemetry.md` defines a small run-recording format (JSON lines: places, deaths, items,
how runs ended). `scripts/telemetry-summary.py` summarises it, and `balance-analyst` reads it, so balance claims rest on
runs and their spread.

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

## License

MIT. See [LICENSE](LICENSE).
