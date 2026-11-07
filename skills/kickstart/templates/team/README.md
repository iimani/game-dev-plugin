# The team

How the agents work on <Game>. Every agent reads this file, then its own file here.

## Two layers

- **The role** comes from the `game-dev` plugin. It says how that job is done on any game.
- **The project** is in `docs/team/<role>.md`. It says what the role needs for this game: what to read, where things
  live, which commands prove the work, and where the owner decides.

On a small game, a role with one task has no file here, and its brief carries that detail. A file here points to the docs that hold the rules. It never copies them. `scripts/check-team.py` fails if a file here
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
| Review findings | The role that made the work, resumed |
| A change the player sees, sized to the change | `playtester` |
| Critical playtest findings | The role that made the work, resumed |

**The session keeps** the decisions: talking with the owner, the gates, the plan, the tracker, git, the PR, the review, and
updating the guideline. It doesn't keep the making.

## Handing work between roles

Handoffs cost the most time, so plan them.

- **Mostly one side, with a little of the other:** one role owns the step, such as level work that needs a small test fix.
- **Real work on both sides:** keep two roles, because a second eye finds things. Settle the shared format first, so
  they can overlap.
- **Resume, don't restart.** For follow-up work, send a message to the agent that did the first pass. It keeps its
  context, and costs a fraction of a new one. A resumed agent may not start until a running agent finishes, so start
  work that must overlap as new agents, in one message.
- **Send review fixes back.** They go to the role that made the work, even small ones. The session's context is the
  costliest place to make them.
- **Show the owner the real thing.** The owner doesn't see a role's report. At a gate, paste its mockups and drafts
  into the chat word for word, never a summary.
- **Small tweaks to a mockup stay in the session.** Once the owner has picked a variant, nudges like "door left" are
  edited here, not sent back. Resume the role for the next stage. This is for design feedback: review fixes still go
  back to the role.
- **Batch findings.** Send them back in one message, not one at a time.
- **Brief narrowly.** Name the sections and files from the step's **Read** line, so the role reads only those. Give
  `code-reviewer` the diff and the rules, not the guideline.
- **Mind the shared machine.** Two roles running heavy tests at once slow each other down.

## Rules for every role

- **Read the design first.** If the brief names sections and files, read those and nothing else. Otherwise read `docs/design/README.md`,
  then every file its routing table lists for your task, then your method from `docs/process/README.md`. Where a method disagrees with the guideline or a newer owner ruling, those
  win.
- **The calling session owns** the tracker, git, the PR, published pages, the guideline and every question to the owner. When you reach
  an owner's gate, stop and return what the session needs to put the question.
- **Leave generated files alone.** If your work builds an item or changes a rule, name it in your report, so the session
  can mark it.
- **Quote the owner.** Their words go in quotes. Anything they didn't say is marked *(builder's call)*.
- **Don't re-decide rulings.** When something is open, decide, and report it as a ruling with what it costs if wrong.
- **Fix what blocks your proof.** You may change tests and proof tools when they stand between you and a correct proof, and
  say so in your report. You never change the game's rules that way.
- **Test narrowly while you iterate.** Run the suite you're working on, and the full check once at the end.
- **One command per call, from the repo root.** No `cd`, and no chaining with `&&`, `;` or `|`. A narrow permission list
  denies those, and each denial costs a round trip. If a command is denied, use another tool or report it: don't retry
  variations.
- **Keep inventories current.** A new kind of thing gets its catalogue row in the same change.
- **Write plainly.** Short sentences, in reports as well as docs.
