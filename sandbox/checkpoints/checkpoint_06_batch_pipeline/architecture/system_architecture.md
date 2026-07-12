# System Architecture — Checkpoint 6 — Batch Data Engineering Pipeline

## 1. Problem Statement

A larger, scheduled batch workload needs distributed processing (Spark) and reliable orchestration (Airflow) instead of a single ad hoc script.

## 2. Scope and Non-Goals

- In scope: TODO — list what this checkpoint must deliver.
- Out of scope: TODO — list what is deferred to a later checkpoint/phase.

## 3. High-Level Architecture Diagram

TODO: replace this placeholder with your own diagram (Mermaid or ASCII) once
you understand how the components below connect.

```
[Source] -> [Spark job] -> [Airflow DAG] -> [Storage layer] -> [Consumer]
```

## 4. Components

| Component | Responsibility | Technology | Why this technology |
|---|---|---|---|
| Spark job | Distributed transformation of a batch dataset | PySpark | TODO |
| Airflow DAG | Schedule, retry, and monitor the pipeline | Apache Airflow | TODO |
| Storage layer | Where batch input/output lives | Local filesystem / PostgreSQL | TODO |

## 5. Scalability Considerations

- TODO: where does this design break first under 10x data volume or load?

## 6. Reliability Considerations

- TODO: what happens when each component fails? Retries? Idempotency?

## 7. Security Considerations

- TODO: what secrets/credentials exist here, and how are they kept out of git?

## 8. Open Questions

- TODO
