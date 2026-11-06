# Designing procedural content: pools, layouts and generators

Use when: any part of a run, level, reward or puzzle is drawn by the game rather than placed by hand.
Skip if: all content is authored and fixed (most linear and narrative games).

Status: **[Draft]** until the owner has used it. Anything the owner didn't say is *(builder's call)*.

Read with the design guideline (`docs/design/README.md`). Where this method and the guideline disagree, the guideline and
the owner's newer ruling win. It sits above `level-design.md` (one level) and `puzzle-design.md` (one mechanic), and says
how they combine into a run.

## 1. What it covers

| Layer | The design question |
|---|---|
| The run | What does a run draw: mechanics, structure, events? |
| The levels | Which pieces fill it, and which layouts does a puzzle sit in? |
| The rewards | What can each source give? |
| The instances | What does each puzzle generator draw within its tier? |
| The save | What's fixed for a save, so learning pays off on every run? |

## 2. What good looks like

1. **Three levels of random, kept apart.** Per save: the rules. Per run: the content. Per level: the fills. A draw at the
   wrong level breaks learning or variety.
2. **Variety the player feels.** A difference counts when it changes the route, the puzzle or the look.
3. **Pools, not lists.** Every draw comes from a pool with a stated size, a minimum, weights and gates.
4. **Authored members, drawn combinations.** A generator never invents geometry the bot hasn't seen.
5. **Built valid, then proved.** Construct tidy, then test. A reject-and-redraw loop is a backstop with a measured rate.
6. **Deterministic.** One seed, one run, on every device. Resumes and bug reports depend on it.
7. **Fair across the draw.** The hardest draw is still proved, and pacing holds however the dice fall.
8. **The save pays.** What a run draws from grows with what the save has cleared.
9. **Small to save.** A saved run is its seed, its fills and its rule state. A content change drops the run rather than
   corrupting it.
10. **Measured.** Variety is a number with a floor, checked by a test.

**One stream per draw.** Each draw takes its own forked random stream, so adding a draw in one place doesn't reshuffle what
follows. Draw the structure first and the details after. Write one row per draw: what's drawn, from what, on which stream,
proved by what.

**The pool card.**

| Field | What it says |
|---|---|
| Purpose | What the slot or draw is for |
| Members | Their ids, grouped by role |
| Distinctness | How a player tells two members apart |
| Fits | How many members fit each slot, mirrors counted separately |
| Weight | Equal unless a reason is written |
| Gates | What unlocks a member |
| Anti-repeat | What stops the same draw twice in a row, within a run and across runs |
| Floor | The smallest size the pool may have and still ship |

Pool rules:
- A mirror is a free variant only when the member isn't one-sided. It doesn't count as a new member. Count geometry, not ids.
- A member earns its place. If two play the same, merge them.
- Gates are explicit, with a test that each holds.
- Anti-repeat is a design choice, not an accident of the dice.
- Weight by role, not by feel, and write the weight on the card.
- Every member is proved alone and in context.
- Pools are data keyed by area. A later area adds members, and nothing in the core is named for one area.

**Layouts.** A frame is a level's shape: its role, entry, exit and slots. A block is a local challenge that fills a slot. A
layout is the frame plus its fills.
- The frame decides the flow, and the blocks decide the beats.
- A layout serves its job. One generic layout for several mechanics is a compromise.
- Entries and exits are the join. A new kind of opening multiplies the stitcher's work.
- Slots carry tags, and tags carry the rule. A tag is a contract.

**A new generator:**
1. Write what's drawn, from what, in what order.
2. Choose a structure that can't be invalid, and draw the details inside it. Reject only for what construction can't
   guarantee.
3. Give it its own stream, with a salt nobody else uses.
4. Sort before you draw. Never rely on hash order.
5. Budget the retries and record the rate. Zero is fine; unknown is not.
6. Give the backstop the same bar. Otherwise the generator ships what its own tests would refuse.
7. Fail loudly on content and quietly on dice. A pool that can never fill a slot is an error. A bad draw is retried.
8. Keep it fast. Generate off the main thread, or a stretch ahead.
9. Test the seed contract: the same seed gives the same layout, and a new draw doesn't change layouts that don't use it.

## 3. The stages

| Stage | What | Tool | Gate |
|---|---|---|---|
| 1. Card | The pool or draw card | the spec | the owner, for a new layer |
| 2. Members | Each member through its own method | their tools | their gates |
| 3. Counts | Fits per slot, distinct fills, pigeonhole checks | `<fill: pool counter>` | the floors hold |
| 4. Generator | The draw: constructed valid, forked, sorted, with a retry budget | test-first | |
| 5. Proof | The bot on every level, over many seeds; determinism; the seed contract; the rejection rate | `<fill: tests>` | green |
| 6. Variety | The variety report, before and after | `<fill: variety report>` | the floors hold |
| 7. Pace | Time per area from the bot's route | `<fill: time estimate>` | in target |
| 8. Playtest | Two or three runs in a row: do they feel different? | the `playtester` agent, then the owner | the verdict |

A new member of a known pool skips the owner's gates. A new pool, layer or gate goes through all of them.

**The two-run playtest.** A blind agent plays a run, then a second on a new seed, and reports what felt familiar. This
checks that the numbers measure what a player feels. Say what a step-based playtest hides: pace.

## 4. The proof

- A bot that drives the real player controller crosses every generated level, over many seeds.
- A solver proves every puzzle instance (`puzzle-design.md`).
- The same seed gives the same run, and a test pins it.
- A test fails if a pool falls below its floor.
- The rejection rate is measured and in the PR.
- Generated output is checked against its source, so it can't drift.

## 5. Numbers

Measure over many seeds. All floors are *(builder's call)*, to calibrate with the owner.

| Measure | Question | Floor |
|---|---|---|
| Fits per slot | How many members fit a slot? | 3, or 5 for slots drawn several times a run |
| Skeletons | How many run structures exist? | 100 or more |
| Sequences | How many level orders over the sweep? | `<fill>` |
| Signatures | How many distinct levels by geometry, mirrors folded? | `<fill>` |
| Pool coverage | What share has a player seen after 10 runs? | 90% of main pools |
| Repeat rate | How often do two runs in a row share a set, an order or several levels? | under 25% |
| Streaks | Longest run of one member in a slot across runs | 2 |
| Feel gap | Levels that play the same by the bot's route | none in a pool |

Ids overstate variety. Geometry is the honest count.

## 6. Lessons

- "Runs feel the same" is measured, not argued.
- Tidy by construction beats generate-and-reject.
- A filter on a draw gets its own stream, so every other level draws as it would without it.
- A pool is data, and its source is a script. Hand-edited output drifts.
- A pool's size and a run's length are one design: short levels make a corridor.
- A run saved before the content changed can load broken. Check that a saved run still lines up, and drop it if not.
- Bias in a pick changes every seed when fixed. Fix it before any public seed codes ship.
- A pool smaller than the slots it fills repeats by pigeonhole. Do the count first.

## 7. Open for the owner

- `<fill: open questions for this game>`
- The floors above aren't calibrated. Measure first, then adjust.
- Anti-repeat may be impossible with a small pool. Prefer a repeat over a failed draw. *(builder's call)*
- Whether seeds are public. If so, freeze the seed contract before they ship.
