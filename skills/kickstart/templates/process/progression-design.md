# Designing progression

Use when: the player earns, buys or finds anything that lasts: upgrades, abilities, currency, optional rooms.
Skip when: the game has no persistence or growth, such as a pure arcade or a single-session puzzle.

How to design anything the player earns, buys or finds. Tools the player carries have their own method: `tool-design.md`.

Status: **[Draft]**. *(Builder's call)* on anything the owner didn't say.

Read with the design guideline (`docs/design/README.md`): <fill: the guideline files on progression and the run>. Where
they disagree, the guideline and the owner's newer ruling win.

## 1. What good progression does

Defaults. The owner can change any of them at kickstart.

- **It is capped and felt.** Few permanent upgrades, each capped, each noticed. No small percentage drops.
- **Stopping costs nothing.** What the player carried is kept when they die or quit.
- **It makes a choice.** An item that's always better than nothing isn't a choice. It changes a decision or it's cut.
- **It never trivialises a challenge.** Challenges are checked with the player's full ability set, and with each item on.
- **It says what it does where it's offered.** One plain line, at the point of offer.
- **It unlocks when needed.** Not before the player can use it.
- **It grows the save, not the numbers.** Knowledge and abilities carry more than stats. Raw power is capped.

## 2. The kinds

Keep the kinds this game has.

| Kind | Lifetime | Design question |
|---|---|---|
| **Ability** | permanent, earned | what does it open, and what bonus content waits for it |
| **Upgrade** | permanent, bought | does it feel different the next run |
| **Run item** | one run, found | what decision does it change |
| **Optional room** | one visit | what does it offer that the main route doesn't |
| **Record** | permanent, knowledge | does it ever show the solution (it must not) |

## 3. The stages

| Stage | What | Tool | Gate |
|---|---|---|---|
| 1. Brief | The choice it creates, its kind, its cap | the task | the owner, for a new kind |
| 2. Interactions | Which challenges, moves and levels it touches; what it bypasses | <fill: the puzzle audit, the bot> | |
| 3. Numbers | Price, earn rate, number of runs to the cap | a short script over the real prices and earn rates | |
| 4. Core | The effect in the game's logic, with a test | <fill: test runner> | |
| 5. Offer | Its one-line summary, and where it's shown | <fill: where offer text lives> | |
| 6. Save | The save version bumped if its shape changes; a default for old saves | <fill: save tests> | |
| 7. Feel | The owner earns it and notices it | a device | the owner |

### Stage 2, interactions

Items are where puzzles break. For each thing an item bypasses, decide: keep the bypass as the point of the item, add a
cost, or change the effect. Write the decision in the item's brief.

### Stage 3, numbers

- Compute runs-to-cap from what a median run earns, and say it in the change.
- Keep each earn rate on the type that owns it, with its unit.

## 4. Optional rooms

- Each is never required, limited per area, and drawn with a weight.
- Each has a record entry on first meeting, and the same playability proof as any room.
- A merchant's prices are part of the economy, not decoration: buying mid-run trades permanent progress for this run.

## 5. The proof

- Every challenge is proved with the full ability set, and with each item on.
- An ability that gates optional content is proved never to be needed on the main route.
- An old save still loads, and keeps what the player earned.

## 6. Numbers

- Target for all caps: <fill: runs, such as 10 to 15>.
- Each cap: <fill: per upgrade>.
- Currencies: <fill: as few as possible, ideally one>.

## 7. Lessons

- Offering items before anything uses them confuses a new player.
- An item's summary belongs where it's offered, not only in a shop.
- When a save format changes, drop the in-progress run if you must, but keep everything the player earned.

## 8. Open for the owner

- <fill: which kinds this game has, and how many currencies>.
- <fill: what each boss or milestone gives, and what it opens>.
