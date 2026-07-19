# Independent Exercise — Lesson 05: Capstone — Prove the Convention Generalizes

## Goal

Prove your merged convention is genuinely reusable, not just a good fit
for the one scenario you wrote it against.

## Task

Apply `sandbox/_templates/CONFIGURATION_CONVENTION.md` to a **second,
different hypothetical scenario** — not Checkpoint 4's API+PostgreSQL
ingestion, but something shaped differently, e.g. a Checkpoint 6-style
batch/Airflow job (different config needs: a schedule, a source file path,
a Spark executor count, instead of an API endpoint). Write out what that
scenario's config would look like using your convention's schema template,
precedence order, and environment-variant approach unchanged. Where the
convention doesn't quite fit, that's a real finding — either propose a
small, real amendment (a second small PR against the convention) or
explicitly document the limitation.

## Constraints

- The second scenario must be meaningfully different in shape from
  Checkpoint 4's (not just a renamed copy of the same API+DB config).
- If you amend the convention, do it as a real, separate, small PR — not
  bundled into unrelated changes.

## Expected Behavior

A worked example showing the convention applied to the second scenario,
and an honest verdict: did it generalize cleanly, or did it need a real
amendment? Either answer is acceptable — the exercise is testing whether
you can tell the difference, not requiring a perfect-fit convention.

## Validation Commands

- If you amended the convention: `git log --oneline -- sandbox/_templates/CONFIGURATION_CONVENTION.md` should show a second real commit/PR, separate from the guided exercise's.

## Evidence to Submit

In `notes/lesson_05_evidence.md`: the second scenario's worked-out config
using your convention, your honest generalization verdict, and (if
applicable) the amendment PR's URL and description.

## Do Not

- Do not declare the convention "reusable" without actually testing it
  against a genuinely different second scenario.
