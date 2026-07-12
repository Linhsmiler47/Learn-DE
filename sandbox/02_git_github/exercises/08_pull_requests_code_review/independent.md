# Independent Exercise — Lesson 08: Pull Requests & Code Review Workflow

## Goal

Run the full PR lifecycle again, independently, on your `.gitattributes`
branch from Lesson 02 — and this time, also configure and prove branch
protection.

## Task

1. Push `phase-02/gitattributes` and open a real PR for it (write your own
   description — don't copy the guided exercise's wording).
2. Before merging, configure branch protection on `main` requiring a PR
   (Settings → Branches, on GitHub) if you haven't already.
3. Prove the protection works: attempt a direct `git push origin main`
   with a trivial change and confirm GitHub rejects it.
4. Review and merge the `.gitattributes` PR through the proper channel,
   choosing (and justifying, in your evidence) a merge strategy — does
   squash still make sense here, or does merge/rebase fit better for a
   different reason than Lesson 08's guided example?

## Constraints

- The direct-push-to-main test in step 3 must use a trivial, harmless
  change (e.g., a whitespace tweak) specifically because you expect it to
  be rejected — don't risk anything real on an unprotected push attempt.

## Expected Behavior

Branch protection visibly rejects the direct push; the PR-based merge of
`.gitattributes` succeeds normally.

## Validation Commands

- The rejected push's actual error message
- `git log --oneline` on `main` after the PR merges, showing `.gitattributes` landed via PR

## Evidence to Submit

In `notes/lesson_08_evidence.md`: the PR description you wrote, the
branch protection configuration, the rejected direct-push error message
(real, not paraphrased), your merge strategy choice and justification, and
confirmation `.gitattributes` is now on `main`.

## Do Not

- Do not disable branch protection after proving it works "to make things
  easier" for the rest of this phase — keep it on; it's a real, lasting
  repository improvement.
