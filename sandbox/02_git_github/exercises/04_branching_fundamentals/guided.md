# Guided Exercise — Lesson 04: Branching Fundamentals & the HEAD Pointer

## Steps

1. ```bash
   cd ~/Projects/Learn-DE
   git branch
   git log --graph --oneline --all
   ```
2. Confirm your `docs/improve-root-readme` branch (from Lesson 03) has
   diverged from `main`:
   ```bash
   git log main..docs/improve-root-readme --oneline
   git log docs/improve-root-readme..main --oneline
   ```
3. Practice switching:
   ```bash
   git switch main
   cat README.md
   git switch docs/improve-root-readme
   cat README.md
   ```
4. Create a throwaway branch purely to practice creation/deletion mechanics:
   ```bash
   git switch -c practice/branch-mechanics
   git branch
   git switch main
   git branch -d practice/branch-mechanics
   ```

## Evidence to Record

In `notes/lesson_04_evidence.md`: all four steps' output, and a short
explanation of what `git log main..docs/improve-root-readme --oneline`
is actually showing (commits reachable from the second ref but not the
first).

## Validation

- Step 2's two commands should show asymmetric results: commits on your
  branch that aren't on `main`, and (likely) nothing the other direction
  since `main` hasn't moved.
- `git branch -d practice/branch-mechanics` should succeed without
  complaint (since it was never diverged with unmerged work of value).

## When You're Done

Move to [`independent.md`](independent.md).
