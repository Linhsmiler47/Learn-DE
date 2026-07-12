# Guided Exercise — Lesson 07: Remotes & Connecting to GitHub

## Steps

1. ```bash
   cd ~/Projects/Learn-DE
   git remote -v
   git fetch origin
   git log origin/main --oneline -3
   ```
2. Install and authenticate GitHub CLI:
   ```bash
   sudo apt install gh
   gh auth login
   gh repo view
   ```
3. Push your cleaned-up branch from Lesson 06, setting up tracking:
   ```bash
   git switch docs/improve-root-readme
   git push -u origin docs/improve-root-readme
   ```
4. Confirm the tracking relationship:
   ```bash
   git status
   git branch -vv
   ```

## Evidence to Record

In `notes/lesson_07_evidence.md`: the remote info, the `gh auth login`
confirmation (not any token/credential value — just the success message),
`gh repo view` output, and the push output showing the tracking branch
being set up.

## Validation

- `git branch -vv` should show `docs/improve-root-readme` tracking
  `origin/docs/improve-root-readme`.
- `gh repo view` should correctly show `Linhsmiler47/Learn-DE`.

## When You're Done

Move to [`independent.md`](independent.md).
