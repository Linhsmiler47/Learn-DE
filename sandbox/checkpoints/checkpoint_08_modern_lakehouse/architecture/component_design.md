# Component Design — Checkpoint 8 — Modern Lakehouse Project

## Component: MinIO

- **Responsibility**: S3-compatible object storage
- **Inputs**: TODO
- **Outputs**: TODO
- **Configuration**: TODO (see `04_configuration`)
- **Dependencies**: TODO
- **Failure mode**: TODO
- **Trade-offs considered**: TODO — alternatives to MinIO you considered and why you didn't pick them

## Component: Iceberg table

- **Responsibility**: Table format providing ACID/schema evolution/time travel
- **Inputs**: TODO
- **Outputs**: TODO
- **Configuration**: TODO (see `04_configuration`)
- **Dependencies**: TODO
- **Failure mode**: TODO
- **Trade-offs considered**: TODO — alternatives to Apache Iceberg you considered and why you didn't pick them

## Component: Catalog

- **Responsibility**: Table/schema metadata
- **Inputs**: TODO
- **Outputs**: TODO
- **Configuration**: TODO (see `04_configuration`)
- **Dependencies**: TODO
- **Failure mode**: TODO
- **Trade-offs considered**: TODO — alternatives to Hive Metastore you considered and why you didn't pick them

## Component: Trino

- **Responsibility**: SQL query engine over the lakehouse
- **Inputs**: TODO
- **Outputs**: TODO
- **Configuration**: TODO (see `04_configuration`)
- **Dependencies**: TODO
- **Failure mode**: TODO
- **Trade-offs considered**: TODO — alternatives to Trino you considered and why you didn't pick them


## Cross-Component Contracts

- TODO: interfaces/APIs/topics/tables shared between components above.
- TODO: versioning approach for those contracts.
