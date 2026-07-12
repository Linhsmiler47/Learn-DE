# Guided Exercise — Lesson 08: Pull Requests & Code Review Workflow

## Steps

1. Open a real PR from your (pushed, cleaned-up) branch:
   ```bash
   cd ~/Projects/Learn-DE
   git switch docs/improve-root-readme
   gh pr create --title "Add a real description to the root README" \
       --body "The root README was just a title. This adds a short, real description of the repository."
   gh pr view
   ```
2. Review it for real, via the web UI: open the PR, look at "Files
   changed," leave at least one real comment explaining a choice you made,
   then formally Approve (or Request Changes if you spot something —
   either is legitimate).
3. Merge with a deliberate strategy choice:
   ```bash
   gh pr merge --squash --delete-branch
   ```
4. Confirm the result on `main`:
   ```bash
   git switch main
   git pull
   git log --oneline -3
   cat README.md
   ```

## Evidence to Record

In `notes/lesson_08_evidence.md`: the PR URL, the PR description you
wrote, the real review comment text, your Approve/Request Changes
decision and why, the merge confirmation, and the final `README.md`
content now on `main`.

## Validation

- `main`'s `git log --oneline` should show your (squashed) commit.
- The root `README.md` should now contain your real description, on `main`.

## When You're Done

Move to [`independent.md`](independent.md) — you'll do this again for the
`phase-02/gitattributes` branch from Lesson 02.
