# Independent Exercise — Lesson 10: Undoing Things Safely: Reset, Revert & Reflog

## Goal

Recover a commit using only `reflog`, without being told the exact
commands — and without knowing the commit's hash in advance.

## Task

On a new temporary practice branch, make three commits. Note nothing down
about their hashes. Then do something that makes the most recent commit
unreachable from any branch (e.g., `reset --hard` two commits back, then
switch away and delete the branch pointer entirely by checking out `main`
and force-deleting the practice branch with `-D`). Using only `git
reflog` (searched across the whole repo, since the branch itself no longer
exists to scope it), find and recover the "lost" commit's content into a
new branch.

## Constraints

- Don't write down the commit hash before it's "lost" — the exercise is
  finding it via `reflog` cold, not confirming a hash you already knew.
- This is throwaway practice — once you've proven recovery works, delete
  everything again; nothing here needs to persist.

## Expected Behavior

You can locate and recover a commit that no branch currently points to,
using `git reflog` and `git show`/`git reset`/`git cherry-pick` (your
choice of recovery mechanism) — without having recorded its hash ahead of
time.

## Validation Commands

- `git reflog` (the full local reflog, not scoped to a branch that no longer exists)
- `git branch --contains <recovered-hash>` (before and after recovery)

## Evidence to Submit

In `notes/lesson_10_evidence.md`: how you made the commit unreachable,
your process searching `reflog` to find it (including any dead ends), and
proof you recovered the correct content (not just any commit).

## Do Not

- Do not note the commit hash down before "losing" it — that defeats the
  point of practicing recovery from a cold start.
