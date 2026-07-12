# Independent Exercise — Lesson 11: Scheduling with Cron

## Goal

Design your own cron expression for a specific, non-trivial schedule, and
prove it's correct without waiting hours for it to fire naturally.

## Task

Pick a schedule that isn't "every minute" — for example, "every 5 minutes
during a specific hour" or "twice an hour, at :10 and :40." Write the
correct 5-field cron expression yourself (don't just copy an example from
the lesson). Schedule a script (reuse or adapt Lesson 11's heartbeat
pattern) with it. Since waiting for a real multi-minute/hour schedule to
prove itself is slow, also verify your expression's *correctness*
independently — e.g., by reasoning through the next 3 times it would fire
and checking that logic against the actual cron field definitions in the
lesson.

## Constraints

- Use only your own user crontab.
- Use absolute paths and explicit output redirection, as in the guided exercise.
- Remove the crontab entry when finished.

## Expected Behavior

You can state, in writing, the next 3 times your cron expression would
fire from a given starting point, and you've let it run at least once for
real to confirm the mechanism works end-to-end (even if the full interval
hasn't fully elapsed by the time you wrap up — one real firing plus your
reasoning for the rest is sufficient evidence).

## Validation Commands

- `crontab -l` (confirm the exact expression registered)
- The script's own log file, to catch any real firing that occurred

## Evidence to Submit

In `notes/lesson_11_evidence.md`: your chosen schedule and why, the exact
cron expression, your written reasoning for the next 3 fire times, any
real log evidence of it firing, and confirmation of cleanup.

## Do Not

- Do not reuse the exact "every minute" expression from the guided exercise — design a genuinely different schedule.
- Do not leave the crontab entry in place after this exercise.
