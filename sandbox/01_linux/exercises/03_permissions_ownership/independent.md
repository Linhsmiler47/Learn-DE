# Independent Exercise — Lesson 03: File & Directory Permissions, Ownership

## Goal

Design and apply a permission scheme for a small 3-file scenario, without
being given the exact `chmod` values.

## Task

Inside `workspace/permissions_practice/scenario/`, create three files:
- `private_notes.txt` — should be readable and writable **only by you**.
- `team_readme.txt` — should be readable by you and (conceptually) a group,
  writable only by you.
- `public_info.txt` — should be readable by anyone, writable only by you.

Work out the correct octal (or symbolic) `chmod` value for each yourself
using the read/write/execute model from the lesson, apply it, and verify
with `ls -l`.

## Constraints

- Everything happens inside `workspace/permissions_practice/scenario/`.
- Do not use `chmod 777` anywhere in this exercise.

## Expected Behavior

`ls -l` on the three files should show three visibly different permission
strings, each matching the intent described above.

## Validation Commands

- `ls -l workspace/permissions_practice/scenario/`
- `stat -c "%a %n" workspace/permissions_practice/scenario/*` (prints the octal mode next to each filename — use this to double-check your own math)

## Evidence to Submit

In `notes/lesson_03_evidence.md`: the `chmod` command you chose for each
file, the `ls -l`/`stat` output proving it, and a one-sentence justification
per file for why that specific mode matches the stated intent.

## Do Not

- Do not use `chmod 777` on any file in this exercise.
- Do not run any command against files outside `scenario/`.
