# The team

How the agents work on <Game>. Every agent reads this file, then its own file here.

## Two layers

- **The role** comes from the `game-dev` plugin. It says how that job is done on any game.
- **The project** is in `docs/team/<role>.md`. It says what the role needs for this game: what to read, where things
  live, which commands prove the work, and where the owner decides.

A file here points to the docs that hold the rules. It never copies them. `scripts/check-team.py` fails if a file here
names a path that doesn't exist.

## The roles

| Role | Does | Method | Model |
|---|---|---|---|
| `developer` | implements a planned task | the phase's plan in `docs/plans/` | `opus` |
| `level-designer` | levels, traversal, puzzles, pacing | `docs/process/level-design.md` | `opus` |
| `encounter-designer` | creatures, bosses, set pieces | `docs/process/encounter-design.md` | `opus` |
| `game-artist` | production art, in the game's chosen style | `docs/process/art-style.md` | `sonnet` |
| `sound-designer` | sound effects, ambience, music | `docs/process/sound-design.md` | `sonnet` |
| `narrative-writer` | story, lore, and every word the player reads | `docs/process/lore-design.md` | `opus` |
| `balance-analyst` | economy, difficulty and pacing numbers | `docs/process/progression-design.md` | `sonnet` |
| `code-reviewer` | read-only review against the architecture rules | CLAUDE.md | `opus` |
| `design-guardian` | read-only audit of a change against the design | `docs/design/README.md` | `sonnet` |
| `playtester` | plays blind | `docs/team/playtester-controls.md` | `sonnet` |

The session passes the Model value as `model` on the Agent call. `/game-dev:choose-models` shows why each is recommended, and changes them.

## Who does what

The session checks this table before it starts a piece of work, and says which role takes it. Design work counts, not
only code. The session does the work itself only if it's a handful of tool calls or no role fits, and says so in a line.

| Work | Role |
|---|---|
| Code from an approved plan | `developer` |
| Blocking out a level, authoring it, proving it | `level-designer` |
| A creature or boss, stage by stage | `encounter-designer` |
| Any asset, including style tests and mocks | `game-artist` |
| Any sound | `sound-designer` |
| Story, lore, signs, hints, any text the player reads | `narrative-writer` |
| A question about numbers, difficulty or length | `balance-analyst` |
| Before a PR is marked ready | `code-reviewer` and `design-guardian` |
| A change the player sees, sized to the change | `playtester` |

**The session keeps** the decisions: talking with the owner, the gates, the plan, the tracker, git, the PR, the review, and
updating the guideline. It doesn't keep the making.

## Rules for every role

- **Read the design first.** Read `docs/design/README.md`, then every file its routing table lists for your task, then
  your method from `docs/process/README.md`. Where a method disagrees with the guideline or a newer owner ruling, those
  win.
- **The calling session owns** the tracker, git, the PR, published pages, the guideline and every question to the owner. When you reach
  an owner's gate, stop and return what the session needs to put the question.
- **Leave generated files alone.** If your work builds an item or changes a rule, name it in your report, so the session
  can mark it.
- **Quote the owner.** Their words go in quotes. Anything they didn't say is marked *(builder's call)*.
- **Don't re-decide rulings.** When something is open, decide, and report it as a ruling with what it costs if wrong.
- **Keep inventories current.** A new kind of thing gets its catalogue row in the same change.
- **Write plainly.** Short sentences, in reports as well as docs.
