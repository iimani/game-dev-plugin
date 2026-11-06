# Designing tools

Use when: the player carries, equips or finds something that changes what they can do: gear, weapons, passive items.
Skip when: the player's abilities are fixed, as in most pure puzzle games and many arcade games.

How to design what the player brings. `progression-design.md` covers upgrades, currency and optional rooms; this covers
tools.

Status: **[Draft]**. *(Builder's call)* on anything the owner didn't say.

Read with the design guideline (`docs/design/README.md`): <fill: the guideline files on progression, mechanics and
controls>. Where they disagree, the guideline and the owner's newer ruling win.

## 1. What good tools do

Seven tests. A tool that fails one has a known cost, written in its brief.

1. **One sentence of purpose.** "This lets the player ___, which they couldn't otherwise." If the sentence names a
   challenge step it skips, the tool is a bypass, not a tool.
2. **A verb or a decision, not a number.** It adds something to do or something to choose. A small bonus is a number.
3. **Felt in ten seconds.** The player can see what it did the first time it's used: a visible effect where it acts.
4. **Useful in every run, or honest about when it isn't.** Either it works with what every run has, or it's offered only
   when the run can use it.
5. **A real choice.** There's a situation where it beats another tool, and one where it loses. If a tool is always
   better, cut it. If it's never useful, cut it.
6. **It costs something.** A cooldown, a charge, a trade or a slot. Free and unlimited is a stat.
7. **It doesn't skip the test.** Every challenge is audited with the tool on. A tool that makes a challenge trivial is
   changed, not tuned.

Avoid tools bound to one mechanic. They're dead whenever that mechanic is absent, and each new mechanic would need its
own set.

## 2. The roles a tool can have

Pick one role. It says what the tool is for, and what it must not do.

| Role | What it does | Must not |
|---|---|---|
| **Reach** | opens a way the movement can't | skip a required traversal section |
| **Reveal** | shows something hidden, at a cost | show a puzzle's answer |
| **Control** | changes the pace or the danger | remove the hazard |
| **Break** | opens a secret | open the main route |
| **Shape** | changes how a mechanic reads, not how it's solved | solve it |
| **Trade** | takes something to give something | be mandatory |

## 3. The stages

| Stage | What | Tool | Gate |
|---|---|---|---|
| 1. Brief | The one-sentence purpose, the role, the slot, the cost | this document | the owner, for a new role |
| 2. Situations | Five places where it matters, and one where it loses to another tool | <fill: the content, a reach check> | |
| 3. Impact | How often it applies per run, over many seeds or levels, and the visible effect when it does | a count over generated or authored content | it applies in at least half of runs, or the offer says when |
| 4. Audit | Every challenge with the tool on: solvable, still needing reasoning, still crossable | <fill: puzzle audit, bot> | green |
| 5. Core | The effect in the game's logic, its cost, a test; a save field with a default | <fill: test runner> | |
| 6. Offer | The one-line summary where offered; the icon; the first-use cue | <fill: where offer text lives> | |
| 7. Feel | The owner uses it on a device and says what it did | a device | the owner |
| 8. Playtest | The blind player is asked what each tool did, in their own words | a blind playtest | the verdict |

A new member of a known role skips the owner's gate at stage 1.

### The impact table (stage 3)

One row per tool, filled from a count, not a feeling:

| Tool | Role | Applies in | Visible effect | Beats | Loses to | Cost |
|---|---|---|---|---|---|---|

A tool that applies in under half of runs, with no unlock rule, is a dead slot.

## 4. The proof

The stage 3 count and the stage 4 audit. Both run before a person plays.

## 5. Numbers

- Share of runs a tool must apply in: <fill: such as half>.
- Slots, cooldowns and charges: <fill: per tool>.

## 6. Lessons

- Offer a tool when the run can use it.
- Items bypass challenges unless the audit runs with them on.
- Tools that do the player's action for them only skip a step. Tools that hand over information the screen already shows
  change nothing.
- A choice made before the player can know what the run asks isn't a choice.
- If nothing on screen shows the tool helped, the player can't credit it. Check whether a tool is weak or only
  unexplained before you cut it.

## 7. Open for the owner

- <fill: which roles this game wants>.
- <fill: whether items are passive or active, and what the tool button holds>.
