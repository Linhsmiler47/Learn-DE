# Checkpoint 2 — Containerized Python Application with CI

**Builds on:** [`04_configuration`](../../04_configuration/README.md), [`05_docker`](../../05_docker/README.md), [`06_github_actions_cicd`](../../06_github_actions_cicd/README.md)

## Business / Learning Problem

A small Python application must behave the same on your laptop, a
teammate's laptop, and in an automated pipeline — and be verified
automatically, not by hand, before it's considered "done."

## Requirements

- A small Python app (a CLI tool or minimal API — pick something simple; the
  point is the packaging and pipeline, not the app's complexity).
- Configuration externalized via environment variables / `.env` (never
  hardcoded, never committed).
- A `Dockerfile` producing a minimal, working image.
- A GitHub Actions workflow that: installs dependencies, lints, runs tests,
  and builds the Docker image on every push.

## Milestones

1. Architecture docs completed.
2. App runs locally via `python -m ...` with config from `.env`.
3. App runs identically via `docker run`, config passed as env vars.
4. CI workflow passes on a pushed branch and on a PR.

## Expected Outputs

- `Dockerfile`, `.dockerignore`, `.env.example` (never a real `.env`).
- `.github/workflows/ci.yml`.
- At least one automated test that CI actually runs.

## Testing Requirements

- Unit tests for the app's core logic.
- CI must fail on a deliberately broken commit (prove the pipeline catches
  regressions, then revert the breakage).

## Documentation Requirements

- Full `architecture/` folder, including an ADR on your base image choice
  (e.g., `python:slim` vs `python:alpine` vs distroless) and the trade-offs.

## Validation Checklist

- [ ] `docker build` and `docker run` work from a clean checkout.
- [ ] No secrets committed anywhere in git history.
- [ ] CI workflow is green on the default branch.
- [ ] A deliberately broken commit was shown to fail CI, then fixed.

## Completion Criteria

A reviewer can clone the repo, run one Docker command, and get a working app
with zero manual configuration steps — and CI proves it on every push.
