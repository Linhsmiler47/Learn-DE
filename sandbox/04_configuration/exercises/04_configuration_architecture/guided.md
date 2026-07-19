# Guided Exercise — Lesson 04: Configuration Architecture

## Goal

Build the full layered resolution architecture with validation applied
once, at the end — plus logging as one config value among others.

## Steps

1. ```bash
   mkdir -p ~/Projects/Learn-DE/sandbox/04_configuration/workspace/architecture_practice
   cd ~/Projects/Learn-DE/sandbox/04_configuration/workspace/architecture_practice
   ```
2. Write `resolve_config.py` implementing, in order: hardcoded defaults →
   `config/base.yaml` → environment-specific file (reuse Lesson 03's
   dev/staging/prod files, or new copies here) → environment variables →
   CLI argument (`argparse` or manual `sys.argv` parsing is fine).
3. Add a schema validation function run **once**, after all layers are
   resolved — checking types, required keys, and at least one
   allowed-values constraint (`log_level` must be one of `DEBUG/INFO/WARNING/ERROR`).
4. Test the full stack: run with just defaults+base, then add an
   environment file, then an env var override, then a CLI override —
   showing the final resolved value change at each step.
5. Test validation catching a bad value: pass an invalid `log_level`
   (e.g., `"VERBOSE"`) via CLI and confirm it's rejected with a clear message.

## Evidence to Record

In `notes/lesson_04_evidence.md`: `resolve_config.py`'s contents, the
four-step resolution demonstration (defaults → file → env → CLI, showing
the value changing at each layer), and the validation-rejection output
for the bad `log_level`.

## Validation

- Each layer's override must be individually demonstrated — not just the
  final result — so the resolution order is provably correct, not assumed.
- The invalid `log_level` must be rejected before any "pipeline work" runs.

## When You're Done

Move to [`independent.md`](independent.md).
