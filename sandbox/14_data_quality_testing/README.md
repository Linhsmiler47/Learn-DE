# Phase 14 — Data Quality and Testing

## Learning Objectives

- Understand the core data quality dimensions and how to measure them.
- Apply schema validation, unit/integration/pipeline testing to data pipelines.
- Understand data reconciliation and data observability fundamentals.

## Prerequisites

- Phase 13 — dbt
- Phase 09 — Python (pytest)

## Reference Materials (`ref roadmap/`, read-only)

- [EDAI-1 curriculum: Validation & Verification lesson (Software Testing fundamentals, TDD)](../../ref%20roadmap/EDAI/Engineering%20for%20Data%20&%20AI%20%28EDAI%20-%20K9%29%20%28Official%29%20-%20Start%20Date_%2001_04_2026.xlsx)

> The EDAI spreadsheet's 'Validation & Verification' lesson (sheet `EDAI-1 (Data Engineering)`) is the closest conceptual reference — it teaches testing on the API layer, not data pipelines specifically, so most exercises here are adapted rather than copied.

## Core Concepts

- Data quality dimensions: completeness, accuracy, validity, consistency, uniqueness, timeliness
- Schema validation
- Unit, integration, and pipeline testing for data code
- Data reconciliation (source vs destination row/aggregate checks)
- Data observability fundamentals (freshness, volume, schema-drift alerts)

## Exercises

- Define the data quality dimensions above for one real table from Checkpoint 4/5's data and write a check for each.
- Write a reconciliation check comparing source row counts/sums to loaded table row counts/sums.
- Add a schema-drift check that fails loudly if an upstream source adds/removes/renames a column.

## Expected Output

- A small data-quality check suite (can be dbt tests, Great Expectations, or plain Python assertions) covering all six dimensions above for one dataset.

## Validation Checklist

- [ ] Each of the six data quality dimensions has at least one concrete, automated check.
- [ ] A deliberately corrupted row is caught by at least one check.

## Common Mistakes

- Only checking for nulls and calling it 'data quality' — that's one dimension out of six.
- Writing checks that pass on empty data (a check that never actually ran isn't a check).

## Optional Challenges

- Build a simple freshness/volume alert (e.g., fail if the table hasn't been updated in N hours).

## Reflection Questions

- Which data quality dimension is hardest to automate, and why?
