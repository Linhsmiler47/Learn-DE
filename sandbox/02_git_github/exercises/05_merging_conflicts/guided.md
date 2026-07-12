# Guided Exercise — Lesson 05: Merging & Resolving Conflicts

## Safety Reminder

This exercise happens entirely on two temporary practice branches. Neither
gets merged to `main` — both get deleted at the end.

## Steps

1. ```bash
   cd ~/Projects/Learn-DE
   git switch main
   git switch -c practice/conflict-a
   echo "Version from branch A" > sandbox/02_git_github/CONFLICT_PRACTICE_SCRATCH.md
   git add sandbox/02_git_github/CONFLICT_PRACTICE_SCRATCH.md
   git commit -m "Practice: add scratch file, branch A version"
   ```
2. ```bash
   git switch main
   git switch -c practice/conflict-b
   echo "Version from branch B" > sandbox/02_git_github/CONFLICT_PRACTICE_SCRATCH.md
   git add sandbox/02_git_github/CONFLICT_PRACTICE_SCRATCH.md
   git commit -m "Practice: add scratch file, branch B version"
   ```
3. Trigger the conflict:
   ```bash
   git switch practice/conflict-a
   git merge practice/conflict-b
   ```
4. Read the conflict markers, resolve by hand (write something that shows
   you understood both sides, not just picked one):
   ```bash
   cat sandbox/02_git_github/CONFLICT_PRACTICE_SCRATCH.md
   # edit the file to resolve
   git add sandbox/02_git_github/CONFLICT_PRACTICE_SCRATCH.md
   git commit -m "Practice: resolve conflict in scratch file"
   ```
5. Clean up — delete both branches, confirm `main` is untouched:
   ```bash
   git switch main
   git branch -D practice/conflict-a practice/conflict-b
   git log --oneline -3
   ```

## Evidence to Record

In `notes/lesson_05_evidence.md`: the exact conflict markers you saw, your
resolution and why you chose it, and the final `git log --oneline -3` on
`main` proving nothing from this exercise landed there.

## Validation

- `main`'s `git log --oneline -3` must show no trace of the conflict
  practice commits.

## When You're Done

Move to [`independent.md`](independent.md).
