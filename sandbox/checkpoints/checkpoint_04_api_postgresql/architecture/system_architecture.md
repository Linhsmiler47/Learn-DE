# System Architecture — Checkpoint 4 — API Ingestion Pipeline

## 1. Problem Statement

Data from an external REST API needs to land reliably in PostgreSQL, handling pagination, rate limits, and failures without duplicating rows.

## 2. Scope and Non-Goals

- In scope: TODO — list what this checkpoint must deliver.
- Out of scope: TODO — list what is deferred to a later checkpoint/phase.

## 3. High-Level Architecture Diagram

TODO: replace this placeholder with your own diagram (Mermaid or ASCII) once
you understand how the components below connect.

```
[Source] -> [API client] -> [Loader] -> [PostgreSQL] -> [Consumer]
```

## 4. Components

| Component | Responsibility | Technology | Why this technology |
|---|---|---|---|
| API client | Fetch paginated data with retry/backoff | Python, requests | TODO |
| Loader | Idempotent upsert into PostgreSQL | psycopg2/SQLAlchemy | TODO |
| PostgreSQL | Durable storage of ingested data | PostgreSQL | TODO |

## 5. Scalability Considerations

- TODO: where does this design break first under 10x data volume or load?

## 6. Reliability Considerations

- TODO: what happens when each component fails? Retries? Idempotency?

## 7. Security Considerations

- TODO: what secrets/credentials exist here, and how are they kept out of git?

## 8. Open Questions

- TODO
