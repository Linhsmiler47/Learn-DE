# Guided Exercise — Lesson 10: Undoing Things Safely: Reset, Revert & Reflog

## Safety Reminder

Everything here happens on `practice/undo-demo`, deleted at the end.
Nothing touches `main`.

## Steps

1. ```bash
   cd ~/Projects/Learn-DE
   git switch main
   git switch -c practice/undo-demo
   echo "bad change" >> sandbox/02_git_github/UNDO_PRACTICE_SCRATCH.md
   git add sandbox/02_git_github/UNDO_PRACTICE_SCRATCH.md
   git commit -m "Practice: a commit we'll undo"
   git log --oneline -1
   ```
2. Reset hard, then recover with reflog:
   ```bash
   git reset --hard HEAD~1
   ls sandbox/02_git_github/UNDO_PRACTICE_SCRATCH.md   # should be gone
   git reflog
   git reset --hard <the-hash-from-reflog>
   cat sandbox/02_git_github/UNDO_PRACTICE_SCRATCH.md   # recovered
   ```
3. Now practice `revert` instead:
   ```bash
   git revert HEAD --no-edit
   cat sandbox/02_git_github/UNDO_PRACTICE_SCRATCH.md   # gone again, via a new commit
   git log --oneline
   ```
4. Clean up entirely:
   ```bash
   git switch main
   git branch -D practice/undo-demo
   ```

## Evidence to Record

In `notes/lesson_10_evidence.md`: the reflog output showing the "lost"
commit, the successful recovery, the revert's resulting log, and
confirmation the branch is deleted.

## Validation

- After recovery, the scratch file's content must match what you
  originally committed — proof `reflog` + `reset --hard` genuinely
  recovered it, not just recreated it by hand.

## When You're Done

Move to [`independent.md`](independent.md).
