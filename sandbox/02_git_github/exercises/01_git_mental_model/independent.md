# Independent Exercise — Lesson 01: Git's Mental Model

## Goal

Predict the pointer model's behavior in writing before verifying it —
proving you understand the model, not just observed it once.

## Task

Without running any commands yet, write down (in your evidence file) what
you predict will happen to HEAD, `main`, and the commit graph if you:
1. Create a new branch called `practice/prediction-check` from `main`.
2. Make one commit on it.
3. Switch back to `main`.

Specifically predict: will `main` move? Will HEAD point at the same place
before and after step 3 as it did before step 1? Will the new commit still
exist after switching back to `main`?

Then actually run it (using a real, if small, real change — or a scratch
file inside `sandbox/02_git_github/` if you don't have a small real
improvement ready; delete the branch without merging when done, since this
is throwaway prediction-testing, not real work) and compare the real
`git log --graph --oneline --all` output against your prediction.

## Constraints

- Delete `practice/prediction-check` after this exercise — it's throwaway,
  not meant to merge.

## Expected Behavior

Your written prediction should match the actual `git log --graph` output
in every particular: whether `main` moved (it shouldn't have), where HEAD
ends up, and that the new commit still exists (just unreferenced by
`main`).

## Validation Commands

- `git log --graph --oneline --all` (before and after)
- `git rev-parse main` (before and after — should be identical)

## Evidence to Submit

In `notes/lesson_01_evidence.md`: your written prediction (made *before*
running anything), the actual output, and an honest note on whether your
prediction was fully correct — if it wasn't, explain what you misunderstood.

## Do Not

- Do not merge or keep `practice/prediction-check` — delete it once you've
  compared prediction to reality.
