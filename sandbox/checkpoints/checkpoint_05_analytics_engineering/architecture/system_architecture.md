# System Architecture — Checkpoint 5 — Analytics Engineering Project

## 1. Problem Statement

Raw ingested data (from Checkpoint 4) must be modeled, transformed, tested, and made trustworthy enough for analytics consumption.

## 2. Scope and Non-Goals

- In scope: TODO — list what this checkpoint must deliver.
- Out of scope: TODO — list what is deferred to a later checkpoint/phase.

## 3. High-Level Architecture Diagram

TODO: replace this placeholder with your own diagram (Mermaid or ASCII) once
you understand how the components below connect.

```
[Source] -> [Data model] -> [dbt project] -> [Data quality tests] -> [Consumer]
```

## 4. Components

| Component | Responsibility | Technology | Why this technology |
|---|---|---|---|
| Data model | Star/Galaxy schema design: facts and dimensions | Dimensional modeling | TODO |
| dbt project | Staging -> intermediate -> marts transformations | dbt | TODO |
| Data quality tests | Schema, uniqueness, not-null, referential checks | dbt tests / Great Expectations | TODO |

## 5. Scalability Considerations

- TODO: where does this design break first under 10x data volume or load?

## 6. Reliability Considerations

- TODO: what happens when each component fails? Retries? Idempotency?

## 7. Security Considerations

- TODO: what secrets/credentials exist here, and how are they kept out of git?

## 8. Open Questions

- TODO
