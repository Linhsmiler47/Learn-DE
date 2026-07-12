# Component Design — Checkpoint 6 — Batch Data Engineering Pipeline

## Component: Spark job

- **Responsibility**: Distributed transformation of a batch dataset
- **Inputs**: TODO
- **Outputs**: TODO
- **Configuration**: TODO (see `04_configuration`)
- **Dependencies**: TODO
- **Failure mode**: TODO
- **Trade-offs considered**: TODO — alternatives to PySpark you considered and why you didn't pick them

## Component: Airflow DAG

- **Responsibility**: Schedule, retry, and monitor the pipeline
- **Inputs**: TODO
- **Outputs**: TODO
- **Configuration**: TODO (see `04_configuration`)
- **Dependencies**: TODO
- **Failure mode**: TODO
- **Trade-offs considered**: TODO — alternatives to Apache Airflow you considered and why you didn't pick them

## Component: Storage layer

- **Responsibility**: Where batch input/output lives
- **Inputs**: TODO
- **Outputs**: TODO
- **Configuration**: TODO (see `04_configuration`)
- **Dependencies**: TODO
- **Failure mode**: TODO
- **Trade-offs considered**: TODO — alternatives to Local filesystem / PostgreSQL you considered and why you didn't pick them


## Cross-Component Contracts

- TODO: interfaces/APIs/topics/tables shared between components above.
- TODO: versioning approach for those contracts.
