# The team

How the agents work on <Game>. Every agent reads this file, then its own file here.

## Two layers

- **The role** comes from the `game-dev` plugin. It says how that job is done on any game.
- **The project** is in `docs/team/<role>.md`. It says what the role needs for this game: what to read, where things
  live, which commands prove the work, and where the owner decides.

A file here points to the docs that hold the rules. It never copies them. `scripts/check-team.py` fails if a file here
names a path that doesn't exist.

## The roles

| Role | Does | Method |
|---|---|---|
| `developer` | implements a planned task | <the plan> |
| `level-designer` | levels, traversal, puzzles, pacing | `docs/process/level-design.md` |
| `encounter-designer` | creatures, bosses, set pieces | `docs/process/encounter-design.md` |
| `game-artist` | production art, in the game's chosen style | `docs/process/art-style.md` |
| `sound-designer` | sound effects, ambience, music | `docs/process/sound-design.md` |
| `narrative-writer` | story, lore, and every word the player reads | `docs/process/lore-design.md` |
| `balance-analyst` | economy, difficulty and pacing numbers | `docs/process/progression-design.md` |
| `code-reviewer` | read-only review against the architecture rules | CLAUDE.md |
| `design-guardian` | read-only audit of a change against the design | `docs/design/README.md` |
| `playtester` | plays blind | `docs/team/playtester-controls.md` |

## Rules for every role

- **Read the design first.** Read `docs/design/README.md`, then every file its routing table lists for your task, then
  your method from `docs/process/README.md`. Where a method disagrees with the guideline or a newer owner ruling, those
  win.
- **The calling session owns** the tracker, git, the PR, published pages and every question to the owner. When you reach
  an owner's gate, stop and return what the session needs to put the question.
- **Leave generated files alone.** If your work changes an item's status or a rule, say so in your report.
- **Quote the owner.** Their words go in quotes. Anything they didn't say is marked *(builder's call)*.
- **Don't re-decide rulings.** When something is open, decide, and report it as a ruling with what it costs if wrong.
- **Keep inventories current.** A new kind of thing gets its catalogue row in the same change.
- **Write plainly.** Short sentences, in reports as well as docs.
