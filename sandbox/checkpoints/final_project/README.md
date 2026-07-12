# Final Project — End-to-End Data Platform

**Builds on:** everything in checkpoints 1–8 and phases 01–19.

## Business Problem

Design and build a small but complete data platform for a business domain of
your choice (a scaled-down version of the `ref roadmap/` capstone brief —
"Westmead Hospital" — is a reasonable inspiration, but pick a scope you can
actually finish; do not reproduce that brief wholesale). The platform should
take raw data from one or more sources and deliver analytics-ready,
quality-checked, monitored data.

## Required Data Flow

```
Data Sources
 -> Ingestion (Checkpoint 4 pattern: API/file; Checkpoint 7 pattern: CDC/streaming)
 -> Raw Layer
 -> Transformation (Checkpoint 5/6 patterns: dbt, Spark)
 -> Data Warehouse / Lakehouse (Checkpoint 8 pattern)
 -> Data Quality (Checkpoint 5 pattern: dbt tests)
 -> Workflow Orchestration (Checkpoint 6 pattern: Airflow)
 -> Analytics-Ready Data
 -> Monitoring
 -> CI/CD (Checkpoint 2/3 pattern)
```

## Requirements

- At least two source types feeding ingestion (e.g., one batch/API source
  and one streaming/CDC source).
- A defined raw → transformed → serving layering (medallion-style or your
  own, documented as an ADR).
- Automated data quality checks that would actually block bad data from
  reaching the serving layer.
- End-to-end orchestration: one Airflow DAG (or a small set of them) that
  represents the whole pipeline's schedule and dependencies.
- Containerized components, deployed via the IaC/Kubernetes patterns from
  Checkpoint 3.
- CI that lints/tests the codebase on every push.
- Basic monitoring: at minimum, pipeline success/failure is observable
  without reading raw logs (a dashboard, a status table, or a notification).

## Milestones

1. Architecture docs completed — this is the most important deliverable of
   the whole learning path; take real time on it.
2. Ingestion working end-to-end for all chosen sources.
3. Transformation + quality layer working, with tests that can fail.
4. Orchestration wired end-to-end with retries and backfill capability.
5. Deployment: the platform runs from IaC + containers, not ad hoc commands.
6. Monitoring in place and demonstrated by inducing a failure and observing
   it.

## Testing Requirements

- Unit tests for transformation logic.
- Data quality tests at the raw→serving boundary.
- At least one end-to-end test or documented manual test script proving the
  whole pipeline works from source to serving layer.

## Documentation Requirements

- Full `architecture/` folder: `system_architecture.md`, `data_flow.md`,
  `component_design.md`, and **multiple** ADRs (one per major technology
  decision — storage format, orchestrator, processing engine, etc.).
- A root `README.md` for the project explaining how to run it from scratch.

## Validation Checklist

- [ ] Two independent source types are ingested.
- [ ] Bad data is demonstrably blocked or flagged before reaching the
      serving layer.
- [ ] A failure anywhere in the pipeline is visible without log-diving.
- [ ] The whole stack can be brought up from a clean checkout via
      documented commands (Docker Compose / Terraform / kubectl).
- [ ] CI is green on the final state.

## Completion Criteria

A new reader (or future you, a year from now) can read the architecture
docs, understand every design decision and its trade-offs, and bring the
platform up from scratch using only what's documented here.
