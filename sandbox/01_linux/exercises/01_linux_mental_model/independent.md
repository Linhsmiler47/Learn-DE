# Independent Exercise — Lesson 01: Linux & Ubuntu/WSL Mental Model

## Goal

Produce your own side-by-side evidence that `/home/<user>` and `/mnt/c`
behave differently — don't just accept the lesson's claim.

## Task

Design and run your own small investigation that answers: **does changing
a file's permission bits behave the same way on `/home/<user>` as it does
on `/mnt/c`?** You decide exactly which commands to run — the lesson
already showed you `chmod`, `ls -l`, and where each filesystem lives.

Constraints:
- Only create files inside `sandbox/01_linux/workspace/` (on the Linux
  side) and, for comparison, inside a throwaway location under `/mnt/c`
  (e.g., a temp folder on your Windows desktop) — never inside an
  important Windows folder.
- Don't modify permissions on any file you didn't create yourself.

## Expected Behavior

You should end up able to state, with your own command output as evidence,
whether a permission change you made actually restricted access
differently on the two filesystems (it should — that's the whole point of
Lesson 01's WSL Context table).

## Validation Commands (you choose exact usage)

- `ls -l` on both files, before and after changing permissions.
- `stat` on both files for a fuller comparison, if you want more detail.

## Evidence to Submit

In `notes/lesson_01_evidence.md` (see the template), record:
- Commands used and full output for both filesystems.
- Your conclusion: what actually differed, and why (tie it back to `drvfs`
  vs. ext4 from the lesson's theory section).
- Any troubleshooting notes if something didn't behave as you expected.

## Do Not

- Do not change permissions on any pre-existing Windows file.
- Do not paste a full solution script here — this file intentionally gives
  you a goal, not a command sequence.
