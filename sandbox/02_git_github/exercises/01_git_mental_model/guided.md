# Guided Exercise — Lesson 01: Git's Mental Model

## Goal

See the pointer model (HEAD, branch, commit) directly on the real repo's
existing history — no scratch repo needed, `Learn-DE` already has commits.

## Steps

1. ```bash
   cd ~/Projects/Learn-DE
   git log --oneline
   git log --graph --oneline --all
   ```
2. Pick the most recent commit and inspect it fully:
   ```bash
   git show --stat HEAD
   ```
3. Confirm what HEAD currently points to:
   ```bash
   cat .git/HEAD
   git symbolic-ref HEAD
   ```
4. Confirm what `main` points to, and that it matches:
   ```bash
   git rev-parse main
   git rev-parse HEAD
   ```

## Evidence to Record

In `notes/lesson_01_evidence.md`: all four steps' output, and a one-paragraph
explanation of what `cat .git/HEAD` revealed (it should show something like
`ref: refs/heads/main` — HEAD pointing at a branch, not a commit directly).

## Validation

- `git rev-parse main` and `git rev-parse HEAD` must print the same hash —
  proof that HEAD, via `main`, resolves to the same commit.

## When You're Done

Move to [`independent.md`](independent.md).
