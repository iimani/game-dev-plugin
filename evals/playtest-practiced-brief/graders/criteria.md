---
type: llm
weight: 1
---

The response follows the game-dev `playtest` skill. It passes only if ALL are true:
- It picks the practiced profile: the tester gets the controls sheet and the player's guide, and no journal.
- The brief it writes for the tester never says what changed or why: no mention of the wind-up, of the slam being
  changed, of the task or the PR, and no hint that the tester should watch the boss's timing. Naming a place as the goal
  is fine. Saying so outside the brief, to the user, is fine.
- Because the verdict gates a merge, it rests on three runs of the same brief, not one.
- It says the verdict is written as a count across the runs (such as "2 of 3"), not as one tester's story.
