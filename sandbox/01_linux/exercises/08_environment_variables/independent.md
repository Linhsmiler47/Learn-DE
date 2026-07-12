# Independent Exercise — Lesson 08: Environment Variables & Shell Configuration

## Goal

Build a tiny script that's configured entirely through environment
variables, with sane defaults — the exact pattern Phase 04 formalizes
later.

## Task

In `workspace/env_practice/`, write a small bash script that reads two or
three environment variables (you choose their names and purpose — e.g., a
greeting name, a log level, a target directory) and behaves differently
depending on whether they're set. Each variable should have a sensible
default if unset (using `${VAR:-default}` syntax). Test the script three
ways: with no variables set, with some set, and with all set.

## Constraints

- The script lives under `workspace/env_practice/`.
- Do not hardcode any of the configurable values directly in the script logic.

## Expected Behavior

Running the script with no environment variables set should still work
(using defaults), and setting the variables should visibly change its
behavior.

## Validation Commands

- Run the script directly (defaults apply).
- Run it again as `VAR1=x VAR2=y ./script.sh` (inline export for a single invocation) and confirm the behavior changes.

## Evidence to Submit

In `notes/lesson_08_evidence.md`: the script's contents, and the output of
all three test runs (no vars / some vars / all vars set), with a short
explanation of the `${VAR:-default}` pattern you used.

## Do Not

- Do not hardcode configuration values that should come from environment variables.
- Do not persist any new variables in `~/.bashrc` for this exercise — test them inline instead.
