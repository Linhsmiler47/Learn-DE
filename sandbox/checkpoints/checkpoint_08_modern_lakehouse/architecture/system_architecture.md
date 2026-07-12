# System Architecture — Checkpoint 8 — Modern Lakehouse Project

## 1. Problem Statement

You need warehouse-like guarantees (ACID, schema evolution, time travel) on top of cheap object storage, queryable with SQL.

## 2. Scope and Non-Goals

- In scope: TODO — list what this checkpoint must deliver.
- Out of scope: TODO — list what is deferred to a later checkpoint/phase.

## 3. High-Level Architecture Diagram

TODO: replace this placeholder with your own diagram (Mermaid or ASCII) once
you understand how the components below connect.

```
[Source] -> [MinIO] -> [Iceberg table] -> [Catalog] -> [Trino] -> [Consumer]
```

## 4. Components

| Component | Responsibility | Technology | Why this technology |
|---|---|---|---|
| MinIO | S3-compatible object storage | MinIO | TODO |
| Iceberg table | Table format providing ACID/schema evolution/time travel | Apache Iceberg | TODO |
| Catalog | Table/schema metadata | Hive Metastore | TODO |
| Trino | SQL query engine over the lakehouse | Trino | TODO |

## 5. Scalability Considerations

- TODO: where does this design break first under 10x data volume or load?

## 6. Reliability Considerations

- TODO: what happens when each component fails? Retries? Idempotency?

## 7. Security Considerations

- TODO: what secrets/credentials exist here, and how are they kept out of git?

## 8. Open Questions

- TODO
