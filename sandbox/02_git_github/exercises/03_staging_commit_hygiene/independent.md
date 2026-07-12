# Independent Exercise — Lesson 03: Staging, Committing & Commit Hygiene

## Goal

Practice splitting mixed changes into separate atomic commits using
`git add -p` — a skill the guided exercise didn't need, since its two
changes were already separate edits.

## Task

On your `docs/improve-root-readme` branch (or a new small branch if you'd
rather keep this separate), make **two unrelated small edits to the same
file in one sitting** — for example, fixing a wording issue in one part of
`README.md` and adding an unrelated new line elsewhere. Then use `git add
-p` to stage and commit them as two separate atomic commits, even though
you made both edits before committing either.

## Constraints

- Both edits must be genuinely unrelated (not two parts of the same
  logical change) — otherwise there's nothing to prove by splitting them.
- Use real content — no placeholder "edit A" / "edit B" text.

## Expected Behavior

Two commits exist afterward, each containing exactly one of the two
edits — provable by showing each commit's diff contains only the
change it claims to.

## Validation Commands

- `git show <commit1>` and `git show <commit2>` — each should show only
  one of the two edits, not both.
- `git log --oneline -2`

## Evidence to Submit

In `notes/lesson_03_evidence.md`: the two edits you made, your `git add
-p` session (what you chose to stage at each hunk prompt), and the two
resulting commits' individual diffs proving they're properly separated.

## Do Not

- Do not use `git add <file>` (whole-file staging) for this exercise —
  the point is practicing hunk-level staging with `-p`.
