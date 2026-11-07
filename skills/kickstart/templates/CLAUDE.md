# <Game>

<Two or three sentences: what the game is and what the player does. Task key: **<KEY>**.>

The design is the source of truth. Start at the **design guideline**:
1. Always read `docs/design/README.md`, the index: the status labels, the vision, the house rules, and "What to read for
   a task".
2. Then read every file its routing table lists for your task.
3. Then your method, from `docs/process/README.md`.

## Tech stack

<Engine, language, platforms, test framework. What content and art are authored in.>

## Build and test

<The full check, the fast check, how to run one suite, how to regenerate content, how to build art.>

## Architecture

<The folder tree, one line each.>

**The core decides and the app shows.** Game rules, state and numbers live in code that doesn't import the renderer. The
app reads state and reacts to events to draw, play sound and fire feedback. If a scene needs to decide something, that
logic belongs in the core, with a test. *(Default: change it only with the owner.)*

**Determinism.** All gameplay randomness comes from one seeded generator, with a child stream per system. The same seed
gives the same run. That's how bugs reproduce. *(For any game with generated content.)*

## Game rules that shape code

- **Proved, not hoped.** Every generated level is proved playable by a bot that drives the real player controller. Every
  puzzle is proved solvable, and proved to need reasoning, by a solver.
- **Understanding beats brute force.** A puzzle that opens by trying combinations is a failure.
- **Everything audible is also visible.**
- **A new control gets a lesson** before anything needs it.
- <The rules this game adds.>

## Conventions

- **Tuning numbers** are named constants with a comment on what each is and its unit. No magic numbers in logic.
- **Generated output** is never edited by hand: <list it>.
- **Inventories never drift.** Catalogues and lists are updated in the same PR as the change. Where a test can catch
  drift, add one.
- **Docs and PR text:** plain, short sentences. In specs, mark anything the owner didn't say as *(builder's call)*.

## Keep the design guideline current

- `docs/design/` is the source of truth, edited by hand. Any design document or published page is a one-way copy.
- Every item carries **[Built]**, **[Approved]**, **[Draft]** or **[Proposal]**.
- A PR that builds an item marks it **[Built, <KEY>-N]** and updates `docs/design/status.md`. The session does this when
  it closes the task, from what the role reports.
- A PR that changes a rule, a number or a look updates the section that holds it.
- A ruling by the owner changes the item's label and quotes the ruling where the item lives.

## Verifying work

- The full check green is the floor, not the proof. Give the test count in the PR.
- For anything visible, run it and attach a screenshot or a short video to the PR.
- Feel and "does this read" are the owner's calls on a device. Say what you couldn't check.
- When the plan doesn't settle something, decide, and record it in the PR as a ruling with what it costs if wrong.

## Agents

**Delegate by default.** Work goes to the `game-dev` plugin's role agents (`game-dev:<role>`), not to the session. Before
you start a piece of work, check "Who does what" in `docs/team/README.md`, and say which role takes it. Design work
counts, not only code: blocking out a level, drawing an asset, writing a line.

Do it yourself only if it's a handful of tool calls, or no role fits, and say so in one line.

Pass the role's Model from `docs/team/README.md` as `model` on the Agent call. `/game-dev:choose-models` changes them.

The session keeps the decisions: talking with the owner, the gates, the plan, the tracker, git, the PR, the review, and
updating the guideline. It doesn't keep the making. A role stops at an owner's gate and hands back what the session needs
to ask.

Hand off as `docs/team/README.md` says: resume an agent for follow-up work, batch findings, and brief it narrowly.

Review findings go back to the role that made the work, in one message. Don't make them yourself, even small ones.

Stay in the turn until every role has reported back. Ending the turn can stop a role that's still running: a headless
run stops it about ten minutes later, and its work is lost.

Run one command per call, from the repo root, with no `cd` and no chaining.

Before a PR is marked ready, run `game-dev:code-reviewer` and `game-dev:design-guardian`.

## Playtesting

A change the player sees gets a blind playtest, sized to the change: run `/game-dev:playtest`. It briefs
`game-dev:playtester` with only `docs/team/playtester-controls.md`, sorts the findings (Critical, Worth doing, Noise),
fixes the critical ones through the role that made the work, and ranks the rest in "Optional". A playtest that couldn't run
goes in the PR as not done, never as a pass.

## Pull requests

- Title and body lead with the task: `## <KEY>-N · <what changed>`. Then what changed and why, `### Tests`, `### Demo`.

## Lessons learned

Add a line here whenever a mistake costs time and a rule here would have prevented it.
