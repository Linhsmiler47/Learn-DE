# Independent Exercise — Lesson 10: Basic Shell Scripting

## Goal

Write a small, correctly-argument-validated script that does real work
against files in your workspace — a preview of the "process files
reliably" theme that runs through every later Data Engineering phase.

## Task

In `workspace/scripting_practice/`, write a script that:
- Accepts a directory path as its one argument.
- Validates the argument: fails with a clear message and non-zero exit
  code if no argument is given, or if the given path doesn't exist or
  isn't a directory.
- If valid, counts how many files of each extension exist in that
  directory (e.g., "3 .csv, 1 .log, 2 .txt") and prints the summary.
- Uses `set -euo pipefail` and a loop (`for`) as covered in the lesson.

## Constraints

- The script and any test directories live under `workspace/scripting_practice/`.
- Must produce a non-zero exit code on invalid input and `0` on success.

## Expected Behavior

Running the script against a real directory with mixed file types prints
an accurate per-extension count; running it with a bad argument fails
loudly with a clear message, not a cryptic bash error.

## Validation Commands

- Run against a valid test directory you create yourself; check the counts by hand with `ls` to confirm accuracy.
- Run with no argument, and with a nonexistent path, and check `echo $?` after each.

## Evidence to Submit

In `notes/lesson_10_evidence.md`: the script's contents, at least three
test runs (valid input, missing argument, invalid path) with their full
output and exit codes, and a short explanation of your validation logic.

## Do Not

- Do not skip argument validation — a script that only works with "happy path" input doesn't meet the goal.
- Do not hardcode a specific directory path inside the script itself.
