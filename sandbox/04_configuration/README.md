# Phase 04 — Configuration and Application Structure

## Learning Objectives

- Read and write YAML, JSON, TOML, and `.env` configuration files fluently.
- Separate configuration from code across dev/test/staging/prod environments.
- Manage secrets safely and structure a project's dependencies and logging config.

## Prerequisites

- Phase 01 — Linux basics
- Phase 02 — Git (for `.gitignore` discipline)

## Reference Materials (`ref roadmap/`, read-only)

- [Real-world config example: PostgreSQL WAL configuration](../../ref%20roadmap/My%20mentor/BUỔI%204/BÀI%20GIẢNG/LESSON%204%20-%20MAIN%20-%20INCLUDE%20-%20Ý%20nghĩa%20cấu%20hình%20WAL%20trong%20Postgresql.docx)
- [Real-world config example: Airflow enterprise deployment config](../../ref%20roadmap/My%20mentor/BUỔI%203/BÀI%20GIẢNG/SCHEDULER/AIRFLOW/LESSON%203%20-%20ADVANCE%20-%20Cấu%20hình%20Airflow%20cho%20việc%20triển%20khai%20trong%20doanh%20nghiệp.docx)

> No lesson teaches configuration as its own topic — treat every tool-install doc across `ref roadmap/` (Kafka, Airflow, Talend, Postgres, etc.) as a source of real config-file examples once you reach this phase's exercises.

## Core Concepts

- YAML/JSON/TOML/INI syntax and when each is used
- `.env` files and environment variables; 12-factor config principles
- Dev/test/staging/prod environment separation
- Secrets management (never in git; env vars, secret files, vaults)
- Project folder structure conventions, dependency management, logging configuration

## Exercises

- Take one existing config file format from the reference material (e.g., Airflow or Postgres config) and rewrite its key settings as YAML with comments explaining each.
- Build a small app config loader in Python that reads from `.env` with sane defaults and fails loudly on missing required values.
- Design a folder structure for a project with dev/test/prod configs that never mixes secrets into version control.

## Expected Output

- A reusable config-loading pattern (Python module) you'll reuse in later checkpoints.
- A documented environment-variable naming convention for your own projects.

## Validation Checklist

- [ ] Your config loader fails clearly (not silently) when a required variable is missing.
- [ ] No `.env` file with real values exists anywhere in git history.

## Common Mistakes

- Hardcoding environment-specific values instead of externalizing them.
- Committing a `.env.example` that accidentally contains a real credential.

## Optional Challenges

- Add schema validation for your config file (e.g., with `pydantic-settings`).

## Reflection Questions

- What's the actual failure mode of a missing/misread config value in a production data pipeline?
