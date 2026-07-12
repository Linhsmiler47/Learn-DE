# Independent Exercise — Lesson 09: Logs & Monitoring

## Goal

Build a minimal log rotation mechanism — the same underlying problem real
log rotation tools solve, just small enough to reason about by hand.

## Task

Write a script in `workspace/logs_practice/` that appends timestamped
lines to a log file each time it runs, but when the log file exceeds a
size or line-count threshold you choose (e.g., 5 lines, for fast testing),
renames the current log to an archived name (e.g., `app.log.1`) and starts
a fresh `app.log`. Run it enough times to trigger at least one rotation.

## Constraints

- Everything lives under `workspace/logs_practice/`.
- Don't use an existing log-rotation tool (`logrotate`) — the point is to
  understand the mechanism by building a simplified version yourself.

## Expected Behavior

After enough runs, you should have both a fresh, small `app.log` and at
least one archived `app.log.1` (or similar) containing the older lines.

## Validation Commands

- `wc -l workspace/logs_practice/app.log` (should stay under your threshold)
- `ls -la workspace/logs_practice/` (should show the archived file exists)
- `cat workspace/logs_practice/app.log.1` (should contain the older lines)

## Evidence to Submit

In `notes/lesson_09_evidence.md`: your script, the run-by-run line counts
showing the rotation trigger point, and the final directory listing
proving both files exist with the expected contents.

## Do Not

- Do not use `logrotate` or another pre-built rotation tool for this exercise.
- Do not let the log grow unbounded — the whole point is triggering the rotation.
