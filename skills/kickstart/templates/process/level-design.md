# Designing levels: traversal, platforming and pacing

Use when: you design a room, a level, an arena or a stretch of traversal.
Skip if: the game has no authored space (most card, text and pure management games).

Status: **[Draft]** until the owner has used it. Anything the owner didn't say is *(builder's call)*.

Read with the design guideline (`docs/design/README.md`). Where this method and the guideline disagree, the guideline and
the owner's newer ruling win. A puzzle's mechanic uses `puzzle-design.md`; drawn content uses `procgen-design.md`.

## 1. What it covers

How to make levels get better by method, not by luck: staged, checked as the player sees it, proved by tools, with the
owner's call at the gates.

## 2. What good looks like

- **It knows what it's for.** It teaches, tests or combines, or it's part of the journey. Not every level needs a lesson:
  some are there for density and rhythm. Say which before drawing it.
- **It adds at most one new piece** (a move, a mechanic, a hazard), and its first simple instance teaches it.
- **The player sees where to go.** The first view shows the goal, the first step toward it, or the teaching instance.
- **It gives a choice, not clutter.** At least two ways through where it isn't teaching, and few enough surfaces that the
  route reads at a glance.
- **It's generous.** A mistake costs seconds, not the run: a checkpoint before the hard part, a way back from every fall,
  generous player hitboxes, tight hazard hitboxes.
- **It's proved.** A bot crosses it with the moves the player has then. A section meant to need a move is also proved the
  other way: with that move off, the bot can't cross it.
- **It knows where it sits.** What came before, what's next. Levels in one stretch share an identity, and tension rises.
- **It's paced.** No two hard levels without a breather, and rest at the end of each stretch.

**Kinds of journey level.** These have no lesson, but they have a shape:

| Kind | Shape |
|---|---|
| Traversal | Build-up, one harder passage, a breather, using only moves the player has |
| Landmark | One set piece that tells the area's story, safe, nothing to solve |
| Side path | Branches to a reward, a secret or a shortcut, and is never needed |
| Rest | A checkpoint, some lore, nothing to do |

## 3. The stages

| Stage | What | Tool | Gate |
|---|---|---|---|
| 1. Brief | The level's job, its one new piece, the moves it allows | `<fill: move numbers table>` | |
| 2. Beats | The route as a few beats, in three variants | ASCII or a quick mock | the owner picks, for a new kind |
| 3. Blockout | The map, checked for reach, dead ends and choice | `<fill: fast reach estimate>` | |
| 4. Readability | Lit like the game, then on the real screen | `<fill: level mock>` | the owner looks, for a new kind |
| 5. Proof | The content, generated and proved | `<fill: content build, bot, solver, tests>` | |
| 6. Playtest | A blind player, sized to the change | the `playtester` agent | the verdict |

A new level in a known kind can skip the owner's gates. A new kind, a new mechanic's lesson or an arena goes through them.

**Stage 1, the brief.** A few lines in the task: what it's for and where it sits, the one new piece and what the player
already knows, the moves it allows, and the anti-goals (brute force, a hidden route, a cue only sound carries).

**Stage 2, beats.** Enter, see the goal, the first step, the twist, the payoff or breather. Draw three variants that put
the twist in different places. Pick the one where the first view teaches best.

**Stage 3, blockout.** Draw the map in the project's source format. Check every draft with the fast estimate: every
surface reachable, the route crossed both ways, no dead ends except rewards. It's an estimate. The bot is the proof.
Read the numbers as a guide, not a law. Rooms with several phases are drawn as a set, so what carries over is real.

**Stage 4, readability.** Check that every surface, hazard and cue reads in the game's real light. On the real screen,
check what the HUD and controls cover where the player stands, and that the first view shows the way on. A control the
level needs is taught in the level. Hints, not explanations.

**Stage 5, proof.** Regenerate, commit the source and the output together, and run the tests. Content is built tidy by
construction. A reject-and-redraw check is a backstop, and its rate goes in the PR.

## 4. The proof

- A bot that drives the real player controller crosses the level with the player's moves.
- A section that must need a move is also proved impossible without it.
- A solver proves any puzzle solvable, that it needs reasoning, and that it needs its rule (`puzzle-design.md`).
- A content test fails if generated output drifts from its source.
- A level's time is estimated from the bot's route, and added to the area's budget.

## 5. Numbers

| Number | Starting value | Where it lives |
|---|---|---|
| Length of an area, for a player who knows its rules | `<fill: minutes>` | `<fill>` |
| Vertical gap between stacked surfaces | `<fill: small enough that a short jump doesn't hit the one above>` | `<fill>` |
| Ways on from each surface, on average | 3 to 5 *(builder's call)* | `<fill>` |
| Fits per slot in a pool | at least 3 | `procgen-design.md` |
| Spare in the main route's tightest jump | `<fill>` | `hazard-design.md` |

## 6. Lessons

- Check the move numbers before building a level around a move. A move can buy far less than it feels like it should.
- Check spacing against a jump that isn't held to its peak. Players hit their heads on the surface above.
- Build layouts tidy by construction. Generating and rejecting wastes attempts and leaves tangled layouts.
- Measure an area's time. Short levels in a row can turn an area into a corridor to its boss.
- Draw a room's phases as a set. Drawn one at a time, they share almost nothing, and "the room changes" means nothing.
- A mirrored level is a free variant only when nothing in it is one-sided (text reads one way).

## 7. Open for the owner

- `<fill: open questions for this game>`
- Which moves the main route of each area may assume.
