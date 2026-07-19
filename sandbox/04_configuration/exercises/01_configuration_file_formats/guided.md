# Guided Exercise — Lesson 01: Configuration File Formats

## Goal

Represent one realistic pipeline configuration correctly in three formats.

## Steps

1. In `workspace/`, create the same configuration — a database connection,
   an API endpoint, a batch size, and a retry policy — as three separate
   files:
   ```bash
   mkdir -p ~/Projects/Learn-DE/sandbox/04_configuration/workspace/formats_practice
   cd ~/Projects/Learn-DE/sandbox/04_configuration/workspace/formats_practice
   ```
   - `pipeline_config.yaml`
   - `pipeline_config.json`
   - `pipeline_config.toml`
2. Validate each file parses correctly:
   ```bash
   python3 -c "import yaml; print(yaml.safe_load(open('pipeline_config.yaml')))"
   python3 -m json.tool pipeline_config.json
   python3 -c "import tomllib; print(tomllib.load(open('pipeline_config.toml','rb')))"
   ```
3. Deliberately introduce one YAML indentation bug, observe the error, then fix it.

## Evidence to Record

In `notes/lesson_01_evidence.md`: all three config files' contents, the
validation command output for each, and the exact error message from the
deliberate YAML bug plus your fix.

## Validation

- All three files must parse without error after your fix, and represent
  identical data (same database host, same batch size, etc. — provably,
  by comparing the parsed Python dicts).

## When You're Done

Move to [`independent.md`](independent.md).
