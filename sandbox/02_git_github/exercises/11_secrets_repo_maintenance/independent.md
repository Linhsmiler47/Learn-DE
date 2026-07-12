# Independent Exercise — Lesson 11: Secret Management, Repository Hygiene & Maintenance

## Goal

Practice the actual mechanics of removing a secret from *unpushed* local
history — safely, on a throwaway branch — since you shouldn't do this for
real unless a real secret is actually exposed.

## Task

On a new temporary practice branch, commit a **fake** secret-looking value
(clearly fake — e.g., `FAKE_API_KEY=sk_test_this_is_not_real_1234567890`,
never anything resembling a real credential) to a scratch file. Then,
using interactive rebase (Lesson 06), remove that commit's sensitive
content before it would ever be pushed — either by editing the commit
during an interactive rebase `edit` stop, or by dropping and recreating
it cleanly. Confirm afterward that the fake secret doesn't appear anywhere
in the branch's history.

Separately (no need to actually do this destructively): write up, in your
evidence, what you'd do differently if this had already been **pushed and
merged** — walk through the rotation-first, cleanup-second priority from
the lesson, using your fake secret as the concrete example.

## Constraints

- Never use a real credential for this exercise, even briefly.
- This branch is throwaway — delete it once you've confirmed the history
  is clean; never push it.

## Expected Behavior

`git log -p` on the cleaned branch shows no trace of the fake secret at
any point in its history, not just in the latest state.

## Validation Commands

- `git log --all -p | grep -i "FAKE_API_KEY"` (should be empty after cleanup)
- `git log --oneline` (showing the cleaned history)

## Evidence to Submit

In `notes/lesson_11_evidence.md`: the fake secret you used (safe to
include, since it's clearly fake), your removal process, the `grep`
confirmation it's gone from history, and your written walkthrough of the
rotation-first/cleanup-second response for the "already pushed" scenario.

## Do Not

- Do not use a real credential, even a low-stakes one, for this exercise.
- Do not push this practice branch — delete it locally once confirmed clean.
