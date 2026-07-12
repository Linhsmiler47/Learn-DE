# Independent Exercise — Lesson 06: Rewriting History: Amend & Interactive Rebase

## Goal

Practice reordering commits, not just squashing — a scenario the guided
exercise didn't cover.

## Task

On a new temporary practice branch (from `main`), create three commits
where the logical order matters (e.g., commit 1 creates a scratch file,
commit 2 adds a line referencing something commit 3 introduces — so
committing in the original order 1-2-3 is technically fine, but you'll
practice reordering them to 1-3-2 without breaking anything). Use
interactive rebase to reorder them, and if reordering breaks something
(it might, if #2 truly depends on #3 existing first), resolve the problem
that surfaces rather than avoiding it.

## Constraints

- This is a throwaway branch — delete it when done, don't merge.
- The dependency between commits must be real enough that reordering
  actually risks breaking something — not just an arbitrary reorder with
  no consequence.

## Expected Behavior

You can explain, with real command output, either (a) the reorder worked
cleanly and why the dependency wasn't actually broken, or (b) it broke
something, you understood why, and you fixed it (or reverted the reorder).

## Validation Commands

- `git log --oneline` (before and after reordering)
- `git show` on each commit to confirm content after reordering

## Evidence to Submit

In `notes/lesson_06_evidence.md`: your three original commits, the
rebase todo-list reordering you specified, the result, and — if something
broke — your troubleshooting process fixing it.

## Do Not

- Do not merge this practice branch — delete it once you're done.
