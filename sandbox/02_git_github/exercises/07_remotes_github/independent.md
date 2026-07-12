# Independent Exercise — Lesson 07: Remotes & Connecting to GitHub

## Goal

Understand `fetch` vs. `pull` by causing a real (harmless) divergence and
watching each command's different effect.

## Task

Using the GitHub web UI, make a tiny, harmless edit directly to some file
on `origin` (e.g., a one-word edit to a file via GitHub's web editor, on a
throwaway branch on the remote, not `main`) — this simulates "someone else
pushed something." Back in your local clone, run `git fetch` first and
show that your local branch/working directory doesn't change, only your
knowledge of the remote does (`git log origin/<branch> --oneline` shows
the new commit even though your local branch doesn't). Then run `git pull`
(or `git merge origin/<branch>`) and show the difference.

If you'd rather not create a throwaway remote branch via the web UI,
an equally valid version of this exercise: push `docs/improve-root-readme`
from two different local vantage points (e.g., simulate it by cloning the
repo fresh into `workspace/`, making a small commit there, pushing, then
`fetch` vs. `pull` from your original clone) — pick whichever is more
convenient, but actually do it for real.

## Constraints

- Any throwaway branch created on the remote for this exercise gets
  deleted afterward (`git push origin --delete <branch>`).

## Expected Behavior

You can show, with real command output, the exact moment `fetch` updated
your knowledge of the remote without touching your working files, and the
separate moment `pull`/`merge` actually changed something locally.

## Validation Commands

- `git log origin/<branch> --oneline` immediately after `fetch` (before any pull/merge)
- `git log <local-branch> --oneline` at the same moment (should NOT yet show the new commit)
- Same two commands again, after `pull`/`merge`

## Evidence to Submit

In `notes/lesson_07_evidence.md`: the setup you used, and the four log
outputs (local vs. remote-tracking, before and after) proving `fetch`
alone doesn't change your local branch but `pull` does.

## Do Not

- Do not leave a throwaway remote branch lingering — delete it after the exercise.
