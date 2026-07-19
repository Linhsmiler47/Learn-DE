# Independent Exercise — Lesson 04: Configuration Architecture

## Goal

Add a validation rule not covered in the guided exercise, and demonstrate
an architecture-level anti-pattern being avoided, not just a value being wrong.

## Task

Add a new schema constraint to your `resolve_config.py` that isn't a
simple type/required check — e.g., `retry_policy.max_attempts` must be
between 0 and 10, or `batch_size` must be a positive integer. Demonstrate
it correctly rejecting an out-of-range value. Then, in writing, pick one
architecture-level anti-pattern from the lesson (config sprawl,
per-layer validation, schema/value drift, unreviewed config changes) and
explain, concretely, how your `resolve_config.py`'s design specifically
avoids it — not just define the anti-pattern, show where your code
structurally prevents it.

## Constraints

- The new constraint must be a range/business-logic check, not another
  simple presence check (the guided exercise already covered that shape).

## Expected Behavior

The out-of-range value is rejected with a clear message; your written
explanation references specific lines/structure in your own
`resolve_config.py`, not the lesson's generic description.

## Validation Commands

- A run with the out-of-range value, showing the rejection.
- A run with a valid boundary value (e.g., exactly 10, or exactly 0) to confirm the boundary itself is handled correctly.

## Evidence to Submit

In `notes/lesson_04_evidence.md`: the updated validation code, both test
runs (out-of-range rejected, boundary value accepted), and your written
anti-pattern-avoidance explanation tied to your actual code.

## Do Not

- Do not pick "config sprawl" as your anti-pattern unless your own design
  genuinely demonstrates avoiding it — pick whichever one your actual code shows.
