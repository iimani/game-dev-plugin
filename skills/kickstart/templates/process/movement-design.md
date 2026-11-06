# Designing movement: moves, controls and feel

Use when: you add or change a move or a control.
Skip if: the player doesn't directly control a character or vehicle (most card, turn-based and menu-driven games).

Status: **[Draft]** until the owner has used it. Anything the owner didn't say is *(builder's call)*.

Read with the design guideline (`docs/design/README.md`). Where this method and the guideline disagree, the guideline and
the owner's newer ruling win.

## 1. What it covers

How to change feel by method, so the content built on a move stays valid. The owner calls feel on a device. This method
gets to that call with the numbers right.

## 2. What good looks like

- **It opens something and costs something.** Say which levels it opens, which it makes trivial, and what it trades.
- **It's taught before it's needed.** A teaching level comes first.
- **It's forgiving where it can be.** Coyote time, a jump buffer, generous player hitboxes, tight hazard hitboxes.
- **It fits the input.** A new move reuses a button by context before it adds one.
- **It's deterministic.** Fixed timestep, custom movement code. The same input gives the same path.
- **It's proved.** The bot knows it, or the content doesn't need it.
- **Input is never lost.** A press on a frame with no simulation step still counts.

## 3. The stages

| Stage | What | Tool | Gate |
|---|---|---|---|
| 1. Brief | What it is, what it opens, what it trades, where it's first needed | the task | the owner, for a new move |
| 2. Numbers | Height, reach, speed and timings on paper, against the moves you have | `<fill: move numbers table>` | |
| 3. Core | The move in the player controller, test-first, with named constants | `<fill: tests>` | |
| 4. Bot | The bot and generator know the move, and the main route is re-proved | `<fill: reachability tests>` | |
| 5. Teach | A level that needs only this move; the bot proves it needs it | `<fill: tests>` | the owner, for a new move |
| 6. Controls | Where it sits on each input device, and what it covers | `<fill: screen mock>` | |
| 7. Feel | The owner on a device with live tuning, then bake the values in | `<fill: tuning panel>` | the owner |
| 8. Playtest | A blind run through the levels that lean on it | the `playtester` agent | the verdict |

**Stage 2, numbers.** Read them from the tool, never from memory. Compare with every other move. If a move changes
another's numbers, list the levels that break. State each constant's unit and where it lives.

**Stage 4, the bot.** A move the player can't be assumed to have stays out of the main route. A changed constant can make
levels unreachable, so run the movement and reachability tests.

**Stage 7, feel.** Live tuning needs: sliders that apply as you drag, values kept until reset, a way to copy what changed,
and a visible mark while anything is tuned. The bot and generation always use the defaults, so a tuned value can't change
a seed. Report which moves changed and which levels are now tight.

**Controls.** A control the level needs is taught in the level. Signs and prompts name the real buttons. All input devices
reach the core through one input type.

## 4. The proof

- Unit tests on the player controller, with the constants pinned.
- A bot that drives the real player controller re-proves the main route after any change, over many seeds.
- A teaching level is proved to need its move.
- Before trusting a playtest trend, check the tool's input against what a real thumb does.

## 5. Numbers

| Number | Starting value | Where it lives |
|---|---|---|
| Simulation step | `<fill: for example 1/120 s>` | `<fill>` |
| Coyote time | 0.10 s *(builder's call)* | `<fill>` |
| Jump buffer | 0.12 s *(builder's call)* | `<fill>` |
| Jump peak and reach | `<fill>` | `<fill>` |
| Most buttons on screen | `<fill: for example five on a phone>` | `<fill>` |
| "Tight" spare in a jump | `<fill>` | `<fill>` |

## 6. Lessons

- A move can buy far less than it feels like it should. Check the numbers before building a level around it.
- Space surfaces against a jump that isn't held to its peak.
- A move that comes naturally needs no sign. Cut text that the controls already teach.
- Taps can be lost on frames with no step. Latch them.
- A rule that seems harmless can make surfaces unusable. Check new rules against the bot first.
- A level that quietly needs a move the route doesn't assume is a bug. Move the platforms, not the rule.
- A test tool that presses buttons differently from a player fakes results.

## 7. Open for the owner

- `<fill: open questions for this game>`
- Which moves each area of the game adds.
- Which input device is the reference for feel.
