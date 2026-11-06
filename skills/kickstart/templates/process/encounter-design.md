# Designing an encounter: creatures, bosses and set pieces

Use when: you design anything with a body and a fight, or a set piece that carries a mechanic.
Skip if: the game has no creatures or fights (most pure puzzle, narrative, sim and card games).

Status: **[Draft]** until the owner has used it. Anything the owner didn't say is *(builder's call)*.

Read with the design guideline (`docs/design/README.md`). Where this method and the guideline disagree, the guideline and
the owner's newer ruling win. Rooms and arenas have their own method: `level-design.md`.

## 1. What it covers

The look and the fight are designed together, one stage at a time, and the owner approves each stage before the next.
The body carries the rules: what the player hits is part of it, what it can do comes from what it can move, and its cues
are written on it. Every stage is checked the way the player will see it.

## 2. What good looks like

- **One body.** The silhouette reads as one thing. Parts that float read as a machine.
- **The target reads first.** The eye goes to the target and the cues, then the body, then the room.
- **Every action has a tell, a strike and a recovery,** and the body performs the tell.
- **What it can do comes from its body.** Each attack is something the body visibly does.
- **One new thing at a time.** Each phase teaches one attack or one rule, shown by what just changed.
- **Targets show only in their phase.** A hit on a later target has a clear, harmless result.
- **Every cue reads without sound and without colour,** on the body or in the room.
- **What's drawn makes physical sense.** Armour and restraints attach to something and hold a whole part. What breaks is
  removed from the scene.
- **A cue shows as many slots as it uses.** Spare slots confuse the reading.

## 3. The stages

| Stage | What | Tool | Gate |
|---|---|---|---|
| 1. Brief | What's already fixed, the lore, the rules, the anti-goals | the code and the specs | the owner agrees what it must carry |
| 2. Thumbnails | 12 to 16 silhouettes in the real room at the real scale | `<fill: art tool>` | the owner picks one or two |
| 3. Values | The picks in three or four tones, in the game's light | `<fill: art tool>` | the target and cues read first |
| 4. Colour | The pick in the game's palette, in each state | `<fill: colour check>` | the colours pass the rules and the owner |
| 5. Final art | Full size, every changing part separate, anchors exported | `<fill: art tool, room mock>` | it reads as one body, in the room |
| 6. Poses | A model sheet, then key frames of every action and break | `<fill: art tool>` | every action has a tell, a strike, a recovery |
| 7. In-game check | The real screen at the game's zoom, HUD and controls on | `<fill: screen mock>` | every cue reads by shape at that zoom |

**How a stage runs:**
- One stage at a time. Do it, look at every image it made, say plainly what's still weak, then stop for the owner.
- One review page per encounter, updated each stage: the stages with the current one marked, the newest image first,
  what changed and why, what's still weak, and the question for the owner. Keep older images lower down for comparison.
- Images go in `<fill: folder per encounter>`, named by stage and version. A stages log gets a short section per stage.
- A look that changes a rule (where the target is, what reads the cue) is a rule change. Record it in the fight's spec
  the same day.
- The PR stays open across the stages. Commit each stage's source and output together.

**Stage 1, the brief.** Read what the encounter already does: its target, cues, attacks, tells, timings, the room's size,
the camera's zoom. The look has to carry all of it. Add the lore in a short paragraph, the rules it must keep, the
anti-goals, and references in words.

**Stage 2, thumbnails.** Flat dark shapes, small and fast, each in the real room with the player at true size. Vary the
idea, not the details: different bodies, different places for the target. Number each one. The owner picks by number.

**Stage 5, final art.** If drawing straight at final resolution gives shapes the owner can't read, paint smooth first and
reduce to the game's style after. Every part that changes state is its own asset on one shared origin. Export the anchors
the game needs (targets, cue slots, attachment points), and add a test that the game's copy matches them, so art and
rules can't drift.

**Stage 6, poses.** A model sheet first, at one scale: mixed scales hide errors. Then key frames for each attack's tell,
strike and recovery, the stun, each break, the entrance and the exit. In-betweens are transforms of the same parts where
the engine allows it.

**Stage 7, in-game check.** Nothing important under the controls or the HUD where the player stands to use it. Nothing in
the room hides a cue. Say what a still can't show: motion, timing, feel.

## 4. The proof

Before a person looks:
- A bot that drives the real player controller reaches every target in every layout, with the moves the player has then.
- The vulnerable window beats the measured time to reach the target.
- A dodge test per phase shows no attack is unavoidable.
- A solver covers any puzzle inside the fight (`puzzle-design.md`).
- The rooms' phases are drawn as a set (`level-design.md`).

Then a blind playtest, sized to the change.

## 5. Numbers

| Number | Starting value | Where it lives |
|---|---|---|
| Shortest tell | 0.6 s *(builder's call)* | `<fill>` |
| Smallest cue detail at game zoom | `<fill: size that survives the real screen>` | `<fill>` |
| Smallest gap inside a cue at game zoom | `<fill>` | `<fill>` |
| Thumbnails per round | 12 to 16 | this method |

## 6. Lessons

- Check every line and stroke against what the palette or style does to it. A detail can turn into a shape you never drew.
- Show the face, if it has one. A body seen from the wrong side can read as the wrong creature.
- A part drawn as its own shape can read as detached. Keep one silhouette.
- Cues that read in a close-up can fail at the game's zoom. Stage 7 on the real screen, every time.
- Check room geometry against the art. A platform can cover the cue it was placed beside.
- If a cue looks unbalanced around a target, move the target, not the cue.

## 7. Open for the owner

- `<fill: open questions for this game>`
- How many stages a small creature really needs. A variant of a known creature may skip the owner's gates. *(builder's call)*
