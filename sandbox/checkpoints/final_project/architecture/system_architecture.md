# System Architecture — Final Project — End-to-End Data Platform

## 1. Problem Statement

Combine every prior checkpoint into a single coherent platform: ingestion through to analytics-ready, monitored, orchestrated data.

## 2. Scope and Non-Goals

- In scope: TODO — list what this checkpoint must deliver.
- Out of scope: TODO — list what is deferred to a later checkpoint/phase.

## 3. High-Level Architecture Diagram

TODO: replace this placeholder with your own diagram (Mermaid or ASCII) once
you understand how the components below connect.

```
[Source] -> [Ingestion] -> [Transformation] -> [Modeling & quality] -> [Orchestration] -> [Infrastructure] -> [Consumer]
```

## 4. Components

| Component | Responsibility | Technology | Why this technology |
|---|---|---|---|
| Ingestion | API/file/CDC sources landing in a raw layer | Checkpoints 4 & 7 | TODO |
| Transformation | Batch + streaming processing into curated data | Checkpoints 6 & 8 | TODO |
| Modeling & quality | Dimensional models with automated tests | Checkpoint 5 | TODO |
| Orchestration | End-to-end scheduling, retries, monitoring | Airflow | TODO |
| Infrastructure | Containerized, IaC-deployed, CI-tested | Checkpoints 2 & 3 | TODO |

## 5. Scalability Considerations

- TODO: where does this design break first under 10x data volume or load?

## 6. Reliability Considerations

- TODO: what happens when each component fails? Retries? Idempotency?

## 7. Security Considerations

- TODO: what secrets/credentials exist here, and how are they kept out of git?

## 8. Open Questions

- TODO
