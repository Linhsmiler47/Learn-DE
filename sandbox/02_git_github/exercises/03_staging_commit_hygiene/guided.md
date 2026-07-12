# Guided Exercise — Lesson 03: Staging, Committing & Commit Hygiene

## Steps

1. ```bash
   cd ~/Projects/Learn-DE
   git switch -c docs/improve-root-readme
   ```
2. Improve the real root README:
   ```bash
   cat README.md
   ```
   Edit it to add a short, real description (2-4 sentences) of what this
   repository is — you can draw on `CLAUDE.md`'s own framing.
3. Inspect before committing:
   ```bash
   git status
   git diff
   ```
4. Stage and commit:
   ```bash
   git add README.md
   git diff --staged
   git commit -m "Add a real description to the root README"
   ```
5. Make a second, genuinely separate atomic commit — add one more small,
   distinct improvement (e.g., a "See LEARNING_PATH.md for the full
   learning path" pointer, once you're comfortable it'll make sense even
   before that file is merged elsewhere):
   ```bash
   git add README.md
   git commit -m "Point the root README at LEARNING_PATH.md"
   ```

## Evidence to Record

In `notes/lesson_03_evidence.md`: the `git status`/`git diff`/`git diff
--staged` output before each commit, and both commits' final `git log
--oneline -2` confirmation.

## Validation

- `git log --oneline -2` should show two distinct, clearly-different commit
  messages — not two commits both saying the same thing.

## When You're Done

Keep this branch — it continues in Lessons 04, 06, 07, and 08. Move to
[`independent.md`](independent.md).
