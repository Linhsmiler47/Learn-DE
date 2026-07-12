# System Architecture — Checkpoint 7 — Streaming Data Engineering Pipeline

## 1. Problem Statement

Changes in a source database need to reach a downstream system in near real time instead of on a batch schedule.

## 2. Scope and Non-Goals

- In scope: TODO — list what this checkpoint must deliver.
- Out of scope: TODO — list what is deferred to a later checkpoint/phase.

## 3. High-Level Architecture Diagram

TODO: replace this placeholder with your own diagram (Mermaid or ASCII) once
you understand how the components below connect.

```
[Source] -> [Kafka] -> [CDC connector] -> [Stream processor] -> [Consumer]
```

## 4. Components

| Component | Responsibility | Technology | Why this technology |
|---|---|---|---|
| Kafka | Durable, ordered event log | Apache Kafka | TODO |
| CDC connector | Capture row-level changes from the source DB | Debezium | TODO |
| Stream processor | Transform/route events in-flight | Apache Flink | TODO |

## 5. Scalability Considerations

- TODO: where does this design break first under 10x data volume or load?

## 6. Reliability Considerations

- TODO: what happens when each component fails? Retries? Idempotency?

## 7. Security Considerations

- TODO: what secrets/credentials exist here, and how are they kept out of git?

## 8. Open Questions

- TODO
