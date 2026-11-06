# Designing teaching and text

Use when: the player must learn a rule, a control or an item, or reads any word in the game.
Skip when: never for a game with rules to learn. A pure toy or a game built on a familiar genre can shrink it to the ledger.

How the game teaches, and how every word the player reads gets written. The rule is "hints, not explanations": the
first simple instance does the teaching, and the text points.

Status: **[Draft]**. *(Builder's call)* on anything the owner didn't say.

Read with the design guideline (`docs/design/README.md`): <fill: the guideline files on controls, mechanics and the world>.
Where they disagree, the guideline and the owner's newer ruling win.

## 1. What good teaching does

- **The instance teaches first.** The simplest instance of a rule, safe, in the world, before any word.
- **One new piece at a time.** A mechanic grows by tiers.
- **Cues live in the world,** where they can be re-read mid-challenge. They don't float and fade. What an item does is
  written where it's offered.
- **Teach, test, combine.** A lesson, then a test, then a combination with something known.
- **A rule is taught once.** Once mastered, its basic form drops out.
- **Unlock when needed.** An item or a UI offer appears when the player first needs it, not before.
- **Nothing needs sound** to be understood (a default the owner can change).

## 2. The teachers, in order of preference

1. The **instance** itself.
2. A **mark** in the world: an arrow, a blink, a shape.
3. A **control sign**: a few words, the real button names.
4. A **rule sign**: a few words, naming what is drawn.
5. The **in-game record** (a codex or journal): the record, never the first teacher.

Pick the highest that works. A rule sign is the last thing a player reads, not the first.

## 3. The voice

- Hints: a few words or a symbol pair.
- Name what is **drawn**, in the player's words. Don't use a designer's term before the player has seen the thing.
- Name the real buttons and say how: "aim it" fails if nothing says how to aim.
- Explain effects in words, not numbers.
- Set one style for each kind of text: <fill: banners, HUD lines, signs>. The HUD doesn't carry rules.
- Lore is separate (`lore-design.md`): lore never carries an instruction.

## 4. The stages

| Stage | What | Tool | Gate |
|---|---|---|---|
| 1. Ledger | Every rule, control, piece and item: where it's first taught, reinforced and tested | a table in the spec | |
| 2. Teacher | For each row, the highest teacher that works (§2) | the ledger | the owner, for a first-run change |
| 3. Words | The text, in the voice of §3; a count of words | <fill: text test> | |
| 4. Place | Where it sits: clear of the HUD, the controls and every cue, on the real screen | <fill: clearance check, screen mock> | |
| 5. Proof | A test that each rule has its sign, each lesson its teacher, and no jargon | <fill: tests> | |
| 6. Playtest | First launch, to just past the first challenge; words reported unknown | a blind playtest | the verdict |

### The ledger

One row per thing a player must know. Columns: *what*, *taught by*, *where*, *tested by*, *combined in*, *drops out
when*. A row with no "taught by" is a defect. A row taught only by a sign is a risk.

## 5. The proof

Checks to build before a person looks:
- Every sign is within the word limit and names what is drawn.
- Every rule has its sign, and every lesson its teacher. A sign placed inside solid geometry is a content error.
- Every sign reads whole from where the player stands, clear of everything else on screen.
- Items unlock when first needed.
- A button that can do nothing shows it, and doesn't fail silently.

## 6. Numbers

- Words per sign: <fill: limit, such as five>.
- Solves until a rule's basic form drops out: <fill: count, such as three>.
- Longest distance from a sign to the thing it teaches: <fill: limit>. A lesson far from its sign teaches nothing.

## 7. Lessons

- A floating, fading hint can't be re-read mid-puzzle. Put rules in the world.
- Signs that use words the player hasn't met teach nothing.
- A sign anchored out of the camera's frame doesn't exist. Check it with the camera where the player's camera will be.
- First challenges at full size overwhelm a new player. Start small and grow.
- A display that outlives its cause reads as a bug.

## 8. Open for the owner

- Whether a first lesson may carry more text than later ones.
- Whether the in-game record shows what the player hasn't met yet.
- The text style and font.
