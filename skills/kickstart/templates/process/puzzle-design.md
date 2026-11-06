# Designing puzzles: mechanics, instances and tiers

Use when: you design a puzzle mechanic, or a new tier of one.
Skip if: the game has no puzzles the player must reason through (most action, sim and pure narrative games).

Status: **[Draft]** until the owner has used it. Anything the owner didn't say is *(builder's call)*.

Read with the design guideline (`docs/design/README.md`). Where this method and the guideline disagree, the guideline and
the owner's newer ruling win. The level a puzzle sits in uses `level-design.md`.

## 1. What it covers

How to make puzzles better by method rather than by playtest rescue. Common proofs answer "can it be solved?" and "what's
the cheapest solution?". They don't answer "how hard is it to solve without understanding?" or "does this instance need
the insight?". This method adds those, as numbers computed before any art exists.

## 2. What good looks like

1. **One insight.** You can finish the sentence "the player realises that ___". If you can't, it's a chore.
2. **Knowable.** Everything needed to reach the insight is on the screen. No outside help, no sound.
3. **Reasoned before tried.** The best blind strategy, using only the feedback the player gets, costs at least 3 times
   what reasoning costs *(builder's call, to calibrate)*. Thinking must be the faster way.
4. **Not an oracle.** No free, incremental feedback that lets the player hill-climb to the answer without the insight.
5. **Fixed rules, fresh answers.** Each instance changes the answer, not only the numbers. If one line solves every
   instance, it's a fact to learn once.
6. **Grows by ideas.** A tier adds a new reasoning step. More pieces alone just make a longer chore.
7. **Proved and timed.** Solvable, needs reasoning, readable, and it fits the time budget.

**The puzzle card.** Stage 1 writes this, and every level built on the mechanic inherits it.

| Field | What it says |
|---|---|
| Insight | "The player realises that ___." |
| Naive approach | What a player does before the insight, and why it's slow or fails |
| Rules (fixed) | What the player learns for good. Few, learnable one at a time |
| Instance (drawn) | What changes each time, and why it changes the answer |
| Information | What's shown, where, and what's hidden on purpose |
| Verbs | What the player does, and what each costs |
| Feedback | What a probe shows, and when |
| Cost of error | What a wrong attempt costs: time, travel, a reset. Never health for a reasoning error |
| Goal | What opens, and how the player sees it open |
| Visible twin | For each sound, the visual that carries the same information |
| Heuristic | The one-line rule a good player will derive |
| Ladder | The tiers, one new idea each |

**Kinds of insight.** A mechanic belongs to one kind. The kind says how it usually fails.

| Kind | The player realises | Usual failure |
|---|---|---|
| Trace | what an object does to a signal, then works backward | the trace is unreadable, or a preview does the tracing |
| Assemble | separate clues join into one answer | it's transcription, or a probe reveals the answer step by step |
| Plan | an order or route beats a decay | one heuristic solves everything |
| Perceive | where to aim or stand to reveal | it's a dexterity skill dressed as a puzzle |
| Deduce | which of several candidates fits the clues | a trial beats the clues |
| Constrain | a limit forces a choice | the limit is a timer, so it's a reflex test |

**Feedback.** Half the design. Decide it in stage 2, before any art.

| Feedback | Effect |
|---|---|
| About the rule | Good. A probe teaches how pieces work |
| About the whole attempt | Good. Wrong doesn't say where |
| About progress | An oracle when a wrong try is cheap. Fine for a teaching tier, never for the full one |
| About the answer | An oracle. The player cycles until it's right |
| Costly | Makes a probe worth thinking about first |

- A crutch is a tier, not a feature: it drops out with the base tier.
- An error teaches. After a wrong attempt the player sees what happened, not only that it failed.
- A display ends when its cause ends.
- Every verb has an affordance.

**Heuristics and twists.** Write the shortest rule a good player will find, then build it as a bot that plays every
instance with only that rule.
- It solves every instance: the mechanic is a rule at that tier. Right for the base tier, a defect above it.
- It solves none: the heuristic is wrong or the instance is unfair. Fix the card.
- It solves most: the remainder is the twist. Design it on purpose. A twist is an instance where the obvious rule fails
  and the cues still show why.

**The ladder.** Tier 0 is one simple instance. Each tier has one new idea, what the player already knows, the heuristic
bot's hit rate, the blind prober's ratio, and a time target. Growth axes, in order of preference *(builder's call)*: a
new interaction between known pieces, a decoy, a constraint, two mechanics at once. A bigger instance is the last choice.
Any item that touches a puzzle is audited with it on.

## 3. The stages

| Stage | What | Tool | Gate |
|---|---|---|---|
| 1. Card | The card, its kind, its anti-goals | this method | the owner, for a new mechanic |
| 2. Hands | Easy, mid and hard instances solved by hand: the insight path and the naive path, with each probe's feedback | a page, ASCII or a mock | the owner picks the feedback and the twist |
| 3. Model | State types, solver, blind prober, heuristic bot, and the numbers, before art | `<fill: audit tool>` | the numbers pass |
| 4. Ladder | The tiers, one new idea each, the twist named | the card | the owner, for a new mechanic |
| 5. Level | Layout, cues and text on the real screen | `level-design.md` stages 3 and 4 | the owner looks, for a new kind |
| 6. Proof | Generation by construction, tests, rejection rate, time, items on | `<fill: tests>` | green, plus the audit |
| 7. Playtest | A blind player, sized to the change, with the metrics below | the `playtester` agent | the verdict |

A new tier of a known mechanic can skip the owner's gates. A new mechanic goes through all seven.

**Stage 2 in practice.** Solve the easy instance as the player would, and write each thought. The first thought is the
insight. Solve it again without the insight, and count the probes. If the count is under 10, change the feedback or a
probe's cost, not the numbers. Draw the mid instance so the heuristic fails once: that's the twist.

## 4. The proof

| Check | Question | How |
|---|---|---|
| Solvable | Is there an answer, with the player's moves? | A solver, and a bot that drives the real player controller |
| Needs reasoning | Is the cheapest answer at least two real steps? | The solver's bar |
| Beats a blind prober | Does reasoning win by 3x or more? | A blind prober per mechanic |
| Needs the insight | Is the heuristic's hit rate what the ladder says? | The heuristic bot, per tier |

**The blind prober** plays with the player's feedback only. It tries a probe, reads exactly what the game shows, and picks
the next probe from that. It counts actions and adds travel time. Report the mean and worst case over many seeds, and the
ratio to the reasoning cost. A puzzle that opens by trying combinations fails, even if it works.

Also check: generation is by construction, and a backstop returns only an instance that clears the same bar; the same
seed gives the same instance; every cue reads on the real screen; the time fits the budget.

**Playtest metrics.** Probes per solve; first and second solve (the second should be faster, or the level didn't teach);
solves by accident; the player's final rule against the real one, which is the main result; unknown words; would-quit
moments. Say what a step-based playtest hides: timing.

**Review checklist, one sentence each in the PR:**
- [ ] The insight is one sentence, and the card is in the spec.
- [ ] The hand instances are solved, and the naive path costs more than 10 probes.
- [ ] The blind prober ratio passes (numbers in the PR).
- [ ] The heuristic hit rate matches the tier.
- [ ] No feedback is an oracle at this tier, or the tier says when the crutch drops out.
- [ ] The backstop clears the bar, and its rejection rate is in the PR.
- [ ] Nothing needs sound, and every failure shows what happened.
- [ ] Every item that touches it has been audited.

## 5. Numbers

| Number | Starting value | Where it lives |
|---|---|---|
| Blind cost against reasoning | at least 3x *(builder's call)* | `<fill>` |
| Heuristic hit rate | 100% at the base tier, under about 75% above *(builder's call)* | `<fill>` |
| Naive path, in probes | more than 10 | this method |
| First solve | 2 to 4 minutes *(builder's call, calibrate in playtests)* | `<fill>` |
| Solve with known rules | 30 to 90 seconds *(builder's call, calibrate in playtests)* | `<fill>` |
| Solves before the base tier drops out | 3 *(builder's call)* | `<fill>` |
| Seeds in a sweep | `<fill: 50 is a good start>` | `<fill>` |

## 6. Lessons

- Binary states you can click through are not a puzzle. Count the probes.
- A new mechanic starts with one piece and grows.
- Tidy by construction beats generate-and-reject.
- A display that outlives its cause is worse than none. Blind players read it as a broken signal.
- A preview that's exact makes the full puzzle an oracle.
- Name what's drawn. No jargon for things the player hasn't seen.
- A fallback that skips the bar is a hole in the proof.
- An item that does the puzzle's action for the player removes the puzzle.
- Decide feedback before art. Added late, it tends to be an oracle.
- Too many per-save rules to hold at once is a design failure, not a learning curve.

## 7. Open for the owner

- `<fill: open questions for this game>`
- The 3x bar and hit-rate floors are guesses. Calibrate them against blind playtests.
- This method may be heavy for a small tier. A new tier of a known mechanic skips the owner's gates.
