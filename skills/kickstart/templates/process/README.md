# Design methodologies

How each part of the game is designed. Every methodology is staged, checked the way the player sees it, proved by a
tool where one exists, and gated by the owner where a decision is theirs. They share one shape, so a new one is easy to
write (§2).

## 0. How this relates to the design guideline

The **design guideline** (`docs/design/README.md`) is the design: what the game is, what is built, approved, drafted or
proposed, and what is open. These methodologies are the **how**: the stages, the gates and the proofs for designing one
kind of thing. They use the guideline's labels (**[Built]**, **[Approved]**, **[Draft]**, **[Proposal]**). Where they
disagree, the guideline and the owner's newer ruling win, and both are corrected in the same change.

- A method names the guideline files to read with it (its first lines).
- An owner ruling made while using a method is quoted in the method and in the guideline, in the same change.

## 1. Which method for what

Delete the rows this game doesn't need. Set each row's status as you start using it: **draft**, then **in use**.

| You are designing | Method | Status |
|---|---|---|
| A creature, a boss, a set piece | `encounter-design.md` | <fill: status> |
| A room, a level, an arena, traversal, pacing | `level-design.md` | <fill: status> |
| A puzzle mechanic, its instances and tiers | `puzzle-design.md` | <fill: status> |
| What a run draws: pools, layouts, generators, variety, rewards | `procgen-design.md` | <fill: status> |
| A move, a control, feel | `movement-design.md` | <fill: status> |
| A hazard, health, any survival limit | `hazard-design.md` | <fill: status> |
| Lessons, signs, hints, the in-game record | `teaching-and-text.md` | <fill: status> |
| Currency, upgrades, abilities, optional rooms | `progression-design.md` | <fill: status> |
| Tools: what the player carries or equips | `tool-design.md` | <fill: status> |
| The HUD, controls on screen, camera, banners, hit feedback | `hud-and-feedback-design.md` | <fill: status> |
| Sound and music | `sound-design.md` | <fill: status> |
| Story, lore, world text | `lore-design.md` | <fill: status> |
| The art style, and the tool that makes it | `art-style.md` | <fill: status> |

A piece of work often needs two: a new puzzle room uses `puzzle-design.md` for the mechanic and `level-design.md` for
the room; a new creature uses `encounter-design.md`, and `hazard-design.md` for what it does to the player.

## 2. How to write one

Each methodology has these parts, in this order:

1. **What it covers,** with the owner's words that asked for it and the spec it serves.
2. **What good looks like:** five to eight rules, each testable.
3. **The stages,** as a table: *stage, what, tool, gate*. Gates are the owner's go, only where a decision is theirs.
4. **The proof:** what a tool or a test checks before a person looks. Name the tool.
5. **Numbers:** the constants, with units and where they live.
6. **Lessons:** only things that cost time, with the change that taught them.
7. **Open for the owner:** questions the owner hasn't answered.

Conventions: plain short sentences; the owner's words in quotes; *(builder's call)* on anything they didn't say; no
commented-out ideas. Name the guideline files to read with it. Update the table in §1 in the same change as a new method
(the inventory rule), and the guideline's routing table ("What to read for a task").

## 3. Order of use

1. Read the spec for the part.
2. Read the method for the part, and any it names.
3. Write stage 1 in the task or the spec.
4. Stop at each gate for the owner.
5. At the end, add what cost time to the method's lessons.
