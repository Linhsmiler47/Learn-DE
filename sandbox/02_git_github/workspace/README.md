# workspace/

Your safe, disposable practice area for Phase 02 — scratch `git init`
demos, temporary conflict/rebase/reset practice files, and anything else
that doesn't need to survive.

## How this differs from Phase 02's real-repo work

Most of Phase 02's exercises operate on the **real `Learn-DE` repository**
via temporary or real feature branches (per the Repository Usage Policy in
`LEARNING_PATH.md`) — that's deliberate, not a mistake. This folder is for
the smaller number of cases where a lesson needs truly disposable,
never-committed scratch space:

- Lesson 02's one-time `git init` demonstration (`workspace/init_demo/`).
- Any scratch file you want to experiment with before deciding whether it
  belongs in a real commit.

Destructive Git practice (rebase, reset, conflicts) still happens on
**temporary branches within the real repository**, not in this folder —
see each lesson's Safety Notes. This folder is for files, not for where
branch-level practice happens.

## What NOT to put here

- Anything that should persist as a graded artifact — evidence belongs in
  [`../notes/`](../notes/README.md).
- Real credentials or private key material.

## Version control

Everything under `workspace/` except this README is gitignored — see the
root [`.gitignore`](../../../.gitignore).
