# Guided Exercise — Lesson 06: Rewriting History: Amend & Interactive Rebase

## Safety Reminder

You're rewriting `docs/improve-root-readme`, which is still unpushed and
unmerged — safe to rewrite per the golden rule of rebase.

## Steps

1. ```bash
   cd ~/Projects/Learn-DE
   git switch docs/improve-root-readme
   git log --oneline
   ```
2. Simulate real mess — make one more small follow-up commit fixing
   something trivial in what you wrote (a wording tweak, a typo):
   ```bash
   # edit README.md slightly
   git add README.md
   git commit -m "typo"
   ```
3. Clean it up with interactive rebase — squash the "typo" commit into the
   commit it's fixing:
   ```bash
   git log --oneline
   git rebase -i <the-commit-hash-right-before-your-branch-started>
   ```
   In the editor: mark the "typo" commit as `squash` (or `s`), keep the
   ones you want as `pick`. Save, then edit the combined commit message in
   the second editor screen that opens.
4. Confirm the result:
   ```bash
   git log --oneline
   ```

## Evidence to Record

In `notes/lesson_06_evidence.md`: the "before" `git log --oneline` (with
the messy "typo" commit visible), the rebase todo-list content you
submitted, and the "after" `git log --oneline` showing the cleaned-up
history.

## Validation

- The final `git log --oneline` for this branch must NOT contain a commit
  message like "typo" — it should read as a clean, intentional history.

## When You're Done

Keep this branch — it gets pushed in Lesson 07 and turned into a PR in
Lesson 08. Move to [`independent.md`](independent.md).
