# Independent Exercise — Lesson 04: Branching Fundamentals & the HEAD Pointer

## Goal

Design your own two-branch scenario and explain the pointer model in your
own words, using your own example rather than the lesson's.

## Task

Create two branches from `main`, each with one small, real, throwaway
commit (use `sandbox/02_git_github/` for any scratch content, and delete
both branches without merging when you're done — this is a pointer-model
demonstration, not real repo work). Diagram (in text/ASCII, in your
evidence file) what `main`, each branch, and HEAD point to at each stage:
before either branch exists, after creating branch A, after committing on
branch A, after creating branch B from `main` (not from A), and after
committing on branch B.

## Constraints

- Both branches are throwaway — delete them (not merge) when finished.
- Diagram each stage yourself; don't copy Lesson 04's diagram structure
  verbatim — use your own commit messages/content as the concrete example.

## Expected Behavior

Your diagrams should correctly show that branch A's commit has no effect
on branch B or `main`, and vice versa — they're independent pointers from
the same starting point.

## Validation Commands

- `git log --graph --oneline --all` at each stage, compared against your diagram

## Evidence to Submit

In `notes/lesson_04_evidence.md`: your five-stage diagram, the actual
`git log --graph` output at each stage for comparison, and a short
explanation of any point where your diagram and the real output didn't
initially match (if any).

## Do Not

- Do not merge either practice branch into `main` — delete both when done.
