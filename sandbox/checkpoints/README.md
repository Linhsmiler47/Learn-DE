# Checkpoint Projects

Architecture-first learning still needs practice early and often. Instead of
one big project at the end, this repo uses **8 progressive checkpoints plus a
final project**, spaced across the phases in [`LEARNING_PATH.md`](../../LEARNING_PATH.md).
Each checkpoint is small enough to finish before moving on, and each one's
output feeds the next.

## Cadence

| Checkpoint | Builds on phases | Theme | Produces |
|---|---|---|---|
| [Checkpoint 1](checkpoint_01_linux_git/README.md) | 01–02 | Linux + Git | A managed repo and dev environment |
| [Checkpoint 2](checkpoint_02_docker_cicd/README.md) | 04–06 | Config + Docker + CI | A containerized Python app with CI |
| [Checkpoint 3](checkpoint_03_terraform_kubernetes/README.md) | 07–08 | Terraform + Kubernetes | Checkpoint 2's app deployed locally via IaC |
| [Checkpoint 4](checkpoint_04_api_postgresql/README.md) | 09–10, 15 | Python + API + PostgreSQL | An API ingestion pipeline |
| [Checkpoint 5](checkpoint_05_analytics_engineering/README.md) | 11–14 | Modeling + ETL + dbt + quality | An analytics engineering project |
| [Checkpoint 6](checkpoint_06_batch_pipeline/README.md) | 16–17 | Spark + Airflow | A batch data engineering pipeline |
| [Checkpoint 7](checkpoint_07_streaming_pipeline/README.md) | 18 | Kafka + CDC + Flink | A streaming data engineering pipeline |
| [Checkpoint 8](checkpoint_08_modern_lakehouse/README.md) | 19 | MinIO + Iceberg + Trino | A modern lakehouse project |
| [Final Project](final_project/README.md) | 01–19 | Everything above | An end-to-end data platform |

## Rules for every checkpoint

- **Architecture before code.** Fill in `architecture/system_architecture.md`,
  `data_flow.md`, `component_design.md`, and at least one `adr/00N-*.md`
  *before* writing implementation code. Templates live in
  [`../_templates/architecture/`](../_templates/architecture/).
- **No solutions are provided.** Each checkpoint README gives requirements,
  milestones, and validation criteria — not implementation code.
- **Small and finishable.** A checkpoint should take days, not weeks. If it's
  growing unbounded, cut scope and note the cut as a non-goal.
- **Carry state forward.** Later checkpoints are allowed (and encouraged) to
  reuse the output of earlier ones (e.g., Checkpoint 5 consumes Checkpoint 4's
  PostgreSQL data).

## Completion criteria for this track

- [ ] All 8 checkpoints have a completed `architecture/` folder and a working,
      tested implementation.
- [ ] The final project integrates outputs from checkpoints 2–8 into one
      running platform with orchestration, monitoring, and documentation.
