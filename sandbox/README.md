# sandbox/

This is the **working learning workspace** for the Data Engineering path
defined in [`../LEARNING_PATH.md`](../LEARNING_PATH.md). Everything here is
yours to edit, break, and rebuild.

`ref roadmap/` (repo root) is **read-only reference material** — never
modify, move, rename, or delete anything there. This folder is where actual
exercises, code, configuration, infrastructure, and projects live.

## How this folder is organized

```
sandbox/
├── _templates/architecture/   # Shared architecture doc templates — copy, don't edit in place
├── checkpoints/                # The progressive project track (see checkpoints/README.md)
│   ├── checkpoint_01_linux_git/
│   ├── checkpoint_02_docker_cicd/
│   ├── checkpoint_03_terraform_kubernetes/
│   ├── checkpoint_04_api_postgresql/
│   ├── checkpoint_05_analytics_engineering/
│   ├── checkpoint_06_batch_pipeline/
│   ├── checkpoint_07_streaming_pipeline/
│   ├── checkpoint_08_modern_lakehouse/
│   └── final_project/
├── 01_linux/  02_git_github/  03_networking_system_architecture/
├── 04_configuration/  05_docker/  06_github_actions_cicd/
├── 07_terraform/  08_kubernetes/  09_python/  10_sql_postgresql/
├── 11_data_architecture_modeling/  12_etl_elt/  13_dbt/
├── 14_data_quality_testing/  15_api_ingestion/  16_spark_hadoop/
├── 17_airflow/  18_kafka_cdc_flink/  19_modern_lakehouse/
├── 20_data_engineering_projects/  21_fastapi/  22_web_application/
├── 23_deployment/  24_azure/  25_aws/
└── 26_electives/  (talend/  nifi/  elasticsearch/  advanced_hadoop/)
```

Numbered folders (`01_...` through `26_...`) are the **phases** — study
material, concepts, and small drills, one topic at a time, in order.
`checkpoints/` is the **project track** — larger, integrative builds spaced
across the phases, so you're building real things throughout, not only at
the end.

## Two tracks, one path

- **Phases** teach a topic in isolation with guided exercises.
- **Checkpoints** force you to combine several phases into something that
  actually runs end-to-end, with architecture documented before code is
  written.

Follow the cadence in [`checkpoints/README.md`](checkpoints/README.md) —
don't wait until Phase 20 to start building.

## Architecture-first, every time

Every checkpoint (and the final project) requires an `architecture/` folder
before implementation:

```
architecture/
├── system_architecture.md
├── data_flow.md
├── component_design.md
└── adr/
    └── 001-technology-selection.md
```

Copy the blank versions from [`_templates/architecture/`](_templates/architecture/)
into a new project's `architecture/` folder, then fill them in — diagram,
components, trade-offs, ADRs — before writing implementation code.

## Rules

- No complete exercise solutions are provided anywhere in this repo — READMEs
  give objectives, concepts, exercises, and validation criteria, not answers.
- Prefer free, open-source, or free-tier tools that run locally on
  Ubuntu/WSL.
- Never commit secrets, credentials, `.env` files, or private keys.
- Read [`../CLAUDE.md`](../CLAUDE.md) and
  [`../docs/DE_LEARNING_PATH_REQUIREMENTS.md`](../docs/DE_LEARNING_PATH_REQUIREMENTS.md)
  before changing the structure of this path.

## Where to start

[`checkpoints/checkpoint_01_linux_git/README.md`](checkpoints/checkpoint_01_linux_git/README.md),
alongside [`01_linux/README.md`](01_linux/README.md) and
[`02_git_github/README.md`](02_git_github/README.md).
