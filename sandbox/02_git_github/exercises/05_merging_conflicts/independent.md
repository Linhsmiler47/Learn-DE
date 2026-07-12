# Independent Exercise — Lesson 05: Merging & Resolving Conflicts

## Goal

Resolve a harder conflict than the guided one — one where blindly picking
a side is more obviously wrong.

## Task

Create two new temporary practice branches from `main`. This time, both
branches should edit a small file with **multiple lines**, each changing
a *different* line in a way that only makes sense if both changes survive
(e.g., a short list where branch A adds one item and branch B adds a
different item, both to the same list — not just replacing one line
outright). Trigger the conflict, and resolve it so that **both** real
changes are preserved correctly, not just one side chosen.

## Constraints

- Both branches are throwaway — delete them (not merge) when finished.
- The conflict must be non-trivial enough that "just pick one side" would
  be visibly wrong (i.e., both sides added something that should exist in
  the final result).

## Expected Behavior

The resolved file contains both branches' real additions, correctly
combined — not just one side's version.

## Validation Commands

- `git show <merge-commit>` — inspect the final resolved content
- `git log --graph --oneline` on the (now-merged, still-local) practice branch, before cleanup

## Evidence to Submit

In `notes/lesson_05_evidence.md`: the two branches' original changes, the
conflict markers you saw, your resolution, and an explicit statement of
why "just picking one side" would have been wrong here — proving you
understood both changes, not just avoided guessing by luck.

## Do Not

- Do not merge either branch into `main` — delete both when done.
- Do not resolve by discarding one side without a documented reason.
