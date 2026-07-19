# Independent Exercise — Lesson 03: Multi-Environment Configuration & Secrets

## Goal

Add a fifth environment variant — `ci` — and decide deliberately what it
inherits and what it needs uniquely.

## Task

Using your dev/staging/prod configs from the guided exercise as the base,
design `config/ci.yaml` for the GitHub Actions context from Phase 02.
Decide, and document your reasoning for each: does `ci` copy `test`'s
values, `dev`'s, or need genuinely its own (e.g., a much shorter timeout,
zero retries so failures surface immediately, a mocked/disposable database
reference)? Also address, explicitly: where would `ci`'s secrets come from,
given there's no persistent filesystem for a `.env` file in a GitHub
Actions runner?

## Constraints

- `ci`'s schema must still match the other four exactly — only values (and
  the secrets-sourcing approach) can differ.

## Expected Behavior

`config/ci.yaml` exists, passes the same schema-comparison check as the
guided exercise, and your written reasoning explains at least two
deliberate departures from `test`'s values.

## Validation Commands

- The same schema-comparison script from the guided exercise, extended to include `ci.yaml`.

## Evidence to Submit

In `notes/lesson_03_evidence.md`: `config/ci.yaml`'s content, the
extended schema-comparison output, and your written reasoning for each
value that differs from `test` and for how CI secrets would actually be
supplied (GitHub Actions repository secrets, per Phase 02).

## Do Not

- Do not just copy `test.yaml` unchanged and call it `ci.yaml` — the
  point is deciding, with reasoning, what's actually different.
