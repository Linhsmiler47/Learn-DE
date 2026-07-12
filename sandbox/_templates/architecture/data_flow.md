# Data Flow — [Project Name]

> Template. Trace data from source to destination. Every arrow in the diagram
> should be explainable in one sentence.

## 1. Data Sources

| Source | Format | Volume/Frequency | Notes |
|---|---|---|---|
| | | | |

## 2. Data Flow Diagram

TODO: draw the end-to-end flow (Mermaid or ASCII).

```
Source -> Ingestion -> Raw -> Transform -> Serving -> Consumer
```

## 3. Transformations Applied

- Step-by-step: what changes at each stage, and why.

## 4. Data Contracts

- Schema at each boundary (source, raw, transformed, served).
- What happens on a schema change?

## 5. Failure Points

- Where can data loss or duplication occur?
- How is idempotency guaranteed at each stage?

## 6. Latency / Freshness

- Batch or streaming? What is the acceptable staleness?
