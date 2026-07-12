# Independent Exercise — Lesson 09: Issues, Milestones & Release Management

## Goal

File a second real issue of your own choosing, and practice the
issue-closing keyword mechanism for real.

## Task

Identify one more genuinely pending piece of work in this learning path
(browse `LEARNING_PATH.md`'s Progress Tracking, or anything else you
know is actually unfinished) and file a real issue for it. Then, make a
real, small commit that actually addresses something trivial and
closeable right now (even something small and legitimate, like fixing a
typo you notice somewhere), and include a closing keyword (`Fixes #<N>`)
in that commit's message or PR description. Confirm the issue actually
auto-closes once the commit lands on `main`.

## Constraints

- The issue must be real and the fix must be real — don't file a
  placeholder issue just to close it for practice.
- Follow the proper branch + PR workflow (Lessons 03–08) for the fix, not
  a direct commit to `main`.

## Expected Behavior

The issue closes automatically when your PR merges, with GitHub showing
the commit that closed it.

## Validation Commands

- `gh issue view <number>` (before and after the merge — status changes from open to closed)
- `gh issue list --state closed`

## Evidence to Submit

In `notes/lesson_09_evidence.md`: the issue you filed and why it's real,
the commit/PR that closed it, the exact closing-keyword syntax you used,
and confirmation (via `gh issue view`) that it closed automatically rather
than being closed manually.

## Do Not

- Do not manually close the issue with `gh issue close` — the point is
  proving the automatic keyword-based closing works.
