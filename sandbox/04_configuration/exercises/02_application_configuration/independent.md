# Independent Exercise — Lesson 02: Application Configuration

## Goal

Add a new required config value with its own validation rule, and prove
the fail-fast principle catches an invalid (not just missing) value.

## Task

Extend your `load_config.py` from the guided exercise with a new required
value — e.g., `STORAGE_PATH` (a directory the pipeline writes output to).
Add validation beyond "is it present": confirm it's non-empty and (your
choice) either that the path exists or that it's an absolute path — reject
otherwise with a clear, fail-fast error message. Test both a missing value
and a present-but-invalid value (e.g., a relative path if you chose to
require absolute).

## Constraints

- The new validation must reject something more than "empty string" — it
  should catch a plausible-looking but actually-wrong value.

## Expected Behavior

Three test cases, all producing correct behavior: valid value (succeeds),
missing value (fails fast, clear message), present-but-invalid value
(fails fast, a *different* clear message explaining what's wrong with it).

## Validation Commands

- Three separate runs of your updated `load_config.py`, one per test case, with real output for each.

## Evidence to Submit

In `notes/lesson_02_evidence.md`: the updated loader code, and all three
test cases' real output, with the two failure messages clearly
distinguishable from each other (missing vs. invalid).

## Do Not

- Do not just re-test the missing-value case from the guided exercise —
  this exercise specifically requires a present-but-invalid case too.
