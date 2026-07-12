# Phase 06 — GitHub Actions and CI/CD

## Learning Objectives

- Understand CI/CD concepts and GitHub Actions' workflow model.
- Write workflows with events/triggers, jobs, steps, and runners.
- Build pipelines that lint, test, build Docker images, and deploy across environments.

## Prerequisites

- Phase 02 — Git/GitHub
- Phase 05 — Docker

## Reference Materials (`ref roadmap/`, read-only)

_(see note below)_

> **No direct source material in `ref roadmap/`.** This phase is built from external documentation and hands-on practice rather than the reference folder — call this out in your own notes so it's clear this knowledge didn't come pre-packaged.

## Core Concepts

- CI vs CD, why automated pipelines exist
- GitHub Actions: workflow YAML syntax, events/triggers, jobs, steps, runners, marketplace actions
- Repository secrets, environment variables in CI
- Build pipelines: automated testing, linting, Docker image builds, deployment workflows
- Environment promotion (dev/test/prod) in a pipeline

## Exercises

- Write a workflow triggered on push and PR that installs deps, lints, and runs tests.
- Extend it to build and tag a Docker image, using GitHub Actions cache to speed up builds.
- Add a required-status-check branch protection rule tied to this workflow.
- Simulate an environment-specific secret and use it safely in a job (without ever printing it in logs).

## Expected Output

- A working `.github/workflows/*.yml` for a repo of your choice (can reuse Checkpoint 2's app).
- A screenshot/log of a failed run and the fix that turned it green.

## Validation Checklist

- [ ] The workflow fails correctly on a broken test and blocks merge via branch protection.
- [ ] No secret value appears in workflow logs, even on failure.

## Common Mistakes

- Printing secrets to logs for 'debugging' and forgetting to remove it.
- Not pinning action versions, leading to a workflow that silently changes behavior later.

## Optional Challenges

- Add a matrix build testing against two Python versions.

## Reflection Questions

- What's the smallest CI pipeline that would have caught a bug you introduced in an earlier phase?
