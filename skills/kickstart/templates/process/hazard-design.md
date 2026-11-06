# Designing hazards and health

Use when: you design anything that hurts or limits the player: traps, pits, timers, moving dangers.
Skip if: the player can't be hurt or limited by the world (most card, puzzle-only and narrative games).

Status: **[Draft]** until the owner has used it. Anything the owner didn't say is *(builder's call)*.

Read with the design guideline (`docs/design/README.md`). Where this method and the guideline disagree, the guideline and
the owner's newer ruling win. Enemy attacks follow `encounter-design.md`. Hazards in levels use this with `level-design.md`.

## 1. What it covers

How a hazard asks for a skill, reads at a glance and stays fair, and how health and limits work with it.

## 2. What good looks like

- **It asks for a skill the player has,** proved by the bot.
- **It reads at a glance,** in the game's real light. What must read gets its own layer or treatment.
- **It hurts once, then lets go.** One hit costs a set amount, then a short calm ignores input, so a held stick doesn't
  walk straight back in.
- **It's tight where it hurts.** Generous player hitbox, tight hazard hitbox.
- **It's forgiving afterwards.** A checkpoint before the hard part, and a way back from every fall.
- **Its colour is reserved.** Hazard colours appear only on hazards, and nothing else borrows them.
- **It isn't a puzzle.** A hazard is crossed by skill. A reasoning error never costs health.
- **A limit stays generous.** A timer or a resource refills soon, and running out costs part of the run, not the run.

**The family.** Keep one table of the game's hazards. A new hazard joins with a row here, an art catalogue row, a colour
check and a bot rule.

| Hazard | Where | Rule |
|---|---|---|
| `<fill: hazard>` | `<fill: where it appears>` | `<fill: its rule>` |

## 3. The stages

| Stage | What | Tool | Gate |
|---|---|---|---|
| 1. Brief | What it does, what skill it asks for, its tell | the task | the owner, for a new kind |
| 2. Numbers | Hitbox, damage, calm, spare in the tightest move | `<fill: reach estimate>` | |
| 3. Blockout | The hazard and its footing, also checked with the key move off | `<fill: reach estimate>` | |
| 4. Readability | In the game's light, then on the real screen | `<fill: level mock>` | the owner, for a new kind |
| 5. Proof | The bot crosses it with the player's moves | `<fill: tests>` | |
| 6. Playtest | Health lost and deaths per level | the `playtester` agent | the verdict |

## 4. The proof

- A bot that drives the real player controller crosses it with the moves the player has then.
- A section meant to need a move is proved impossible without it. Prove "can't be bypassed", not just the crossing.
- A moving hazard or platform's whole path is modelled in the proof.
- Any limited resource is proved within budget on the main route.

## 5. Numbers

| Number | Starting value | Where it lives |
|---|---|---|
| Spare in the main route's tightest jump | `<fill>` | `<fill>` |
| Spare in a bonus area | `<fill: can be much tighter>` | `<fill>` |
| Calm after a hit | 0.6 s *(builder's call)* | `<fill>` |
| Budget a main route may use of a limited resource | 60% *(builder's call)* | `<fill>` |
| Shortest tell in a fight | 0.6 s *(builder's call)* | `encounter-design.md` |

## 6. Lessons

- Hazards can vanish in a dark scene. Judge them in the game's light, not as bare sprites.
- A new player's first level has no hazards, by construction.
- After a respawn, a held stick walks straight back into the hazard. Ignore input for a moment.
- A reserved colour can leak through glow and lighting. Check it on screen.
- Prove the "can't be bypassed" case. A ledge in the wrong place can turn a jump into a walk.
- A limit added late can reverse an earlier ruling. Say so, and keep it generous.

## 7. Open for the owner

- `<fill: open questions for this game>`
- Whether later areas raise the cost of a hit, or keep it and grow the difficulty of the crossing.
