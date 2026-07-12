# Phase 23 — Open-Source and Low-Cost Deployment

## Learning Objectives

- Evaluate free-tier/low-cost platforms for frontend, API, database, and containers.
- Design a deployment architecture for the full frontend -> API -> DB -> pipeline stack.

## Prerequisites

- Phase 21 — FastAPI
- Phase 22 — Web application

## Reference Materials (`ref roadmap/`, read-only)

_(see note below)_

> **No direct source material in `ref roadmap/`.** This phase is built from external documentation and hands-on practice rather than the reference folder — call this out in your own notes so it's clear this knowledge didn't come pre-packaged.

## Core Concepts

- Platform options: Vercel (frontend), Render/Railway/Fly.io (API/containers), managed free-tier Postgres
- Matching each component to the platform actually suited for it (not assuming one platform hosts everything)
- Deployment architecture: frontend -> FastAPI -> PostgreSQL -> data pipeline

## Exercises

- Deploy Phase 22's frontend to a free-tier static/frontend host.
- Deploy Phase 21's FastAPI service to a free-tier container/app platform.
- Point the deployed API at a free-tier managed Postgres instance.
- Document which platform you'd use for the batch/orchestration pipeline (Phases 16-19) and why most free frontend hosts can't run it.

## Expected Output

- A live (or documented dry-run, if avoiding any signups) deployment architecture diagram and rationale.

## Validation Checklist

- [ ] You can name, for each of frontend/API/DB/pipeline, a suitable free-tier or low-cost platform and why it fits.

## Common Mistakes

- Assuming a frontend platform (like Vercel) can also run a long-lived backend worker or scheduled pipeline.

## Optional Challenges

- Actually deploy the full stack end-to-end on free tiers and document any friction encountered.

## Reflection Questions

- What would change about this deployment architecture once Phase 24/25 introduces real cloud accounts?
