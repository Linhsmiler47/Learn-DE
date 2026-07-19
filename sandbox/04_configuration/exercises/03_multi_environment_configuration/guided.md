# Guided Exercise — Lesson 03: Multi-Environment Configuration & Secrets

## Goal

Design dev/test/staging/prod variants of one config with a fixed schema.

## Steps

1. ```bash
   mkdir -p ~/Projects/Learn-DE/sandbox/04_configuration/workspace/multi_env_practice
   cd ~/Projects/Learn-DE/sandbox/04_configuration/workspace/multi_env_practice
   ```
2. Write `config/base.yaml` with the fixed schema (keys only, sensible
   shared defaults where genuinely shared).
3. Write `config/dev.yaml`, `config/staging.yaml`, `config/prod.yaml` —
   each overriding only the values that should actually differ (DB host,
   batch size, retry count, log level) per the lesson's mental model table.
4. Write a one-page `SECRETS.md` in the same folder stating explicitly:
   how dev secrets are supplied (local `.env`), and how staging/prod
   secrets are supplied (a secrets manager reference — conceptual, not
   implemented).
5. Diff dev vs. prod to confirm the *keys* are identical and only values differ:
   ```bash
   python3 -c "
   import yaml
   dev = yaml.safe_load(open('config/dev.yaml'))
   prod = yaml.safe_load(open('config/prod.yaml'))
   print('dev keys:', sorted(dev.keys()))
   print('prod keys:', sorted(prod.keys()))
   print('same schema:', sorted(dev.keys()) == sorted(prod.keys()))
   "
   ```

## Evidence to Record

In `notes/lesson_03_evidence.md`: all four YAML files' contents,
`SECRETS.md`'s content, and the schema-comparison script's output
confirming identical keys.

## Validation

- The schema-comparison output must show `same schema: True`.
- Retry counts and log levels must differ meaningfully between dev and prod
  (not just database host).

## When You're Done

Move to [`independent.md`](independent.md).
