# Component Design — Checkpoint 4 — API Ingestion Pipeline

## Component: API client

- **Responsibility**: Fetch paginated data with retry/backoff
- **Inputs**: TODO
- **Outputs**: TODO
- **Configuration**: TODO (see `04_configuration`)
- **Dependencies**: TODO
- **Failure mode**: TODO
- **Trade-offs considered**: TODO — alternatives to Python, requests you considered and why you didn't pick them

## Component: Loader

- **Responsibility**: Idempotent upsert into PostgreSQL
- **Inputs**: TODO
- **Outputs**: TODO
- **Configuration**: TODO (see `04_configuration`)
- **Dependencies**: TODO
- **Failure mode**: TODO
- **Trade-offs considered**: TODO — alternatives to psycopg2/SQLAlchemy you considered and why you didn't pick them

## Component: PostgreSQL

- **Responsibility**: Durable storage of ingested data
- **Inputs**: TODO
- **Outputs**: TODO
- **Configuration**: TODO (see `04_configuration`)
- **Dependencies**: TODO
- **Failure mode**: TODO
- **Trade-offs considered**: TODO — alternatives to PostgreSQL you considered and why you didn't pick them


## Cross-Component Contracts

- TODO: interfaces/APIs/topics/tables shared between components above.
- TODO: versioning approach for those contracts.
