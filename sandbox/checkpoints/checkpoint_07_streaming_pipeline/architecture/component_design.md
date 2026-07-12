# Component Design — Checkpoint 7 — Streaming Data Engineering Pipeline

## Component: Kafka

- **Responsibility**: Durable, ordered event log
- **Inputs**: TODO
- **Outputs**: TODO
- **Configuration**: TODO (see `04_configuration`)
- **Dependencies**: TODO
- **Failure mode**: TODO
- **Trade-offs considered**: TODO — alternatives to Apache Kafka you considered and why you didn't pick them

## Component: CDC connector

- **Responsibility**: Capture row-level changes from the source DB
- **Inputs**: TODO
- **Outputs**: TODO
- **Configuration**: TODO (see `04_configuration`)
- **Dependencies**: TODO
- **Failure mode**: TODO
- **Trade-offs considered**: TODO — alternatives to Debezium you considered and why you didn't pick them

## Component: Stream processor

- **Responsibility**: Transform/route events in-flight
- **Inputs**: TODO
- **Outputs**: TODO
- **Configuration**: TODO (see `04_configuration`)
- **Dependencies**: TODO
- **Failure mode**: TODO
- **Trade-offs considered**: TODO — alternatives to Apache Flink you considered and why you didn't pick them


## Cross-Component Contracts

- TODO: interfaces/APIs/topics/tables shared between components above.
- TODO: versioning approach for those contracts.
