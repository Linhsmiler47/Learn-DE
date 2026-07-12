# Phase 12 — ETL, ELT, and Data Integration

## Learning Objectives

- Understand ETL vs ELT and the mechanics of extraction, transformation, and loading.
- Design reliable ingestion: full vs incremental load, change tracking, retries, idempotency.
- Understand data lineage, metadata, and data contracts fundamentals.

## Prerequisites

- Phase 11 — Data Architecture and Modeling

## Reference Materials (`ref roadmap/`, read-only)

- [Why ETL matters for a Data Engineer](../../ref%20roadmap/My%20mentor/BUỔI%202/BÀI%20GIẢNG/LESSON%202%20-%20Tầm%20Quan%20Trọng%20của%20ETL%20với%20Data%20Engineer.docx)
- [ETL tools overview: Talend vs Pentaho](../../ref%20roadmap/My%20mentor/BUỔI%202/BÀI%20GIẢNG/LESSON%202%20-%20ETL%20Tools%20Talend%20-%20Pentaho.xlsx)

> Talend is **not** a core dependency here — treat it as read-only conceptual reference. Do the small required comparison exercise in [`talend_vs_python_comparison/`](talend_vs_python_comparison/README.md), and save deeper Talend hands-on work for the optional [`26_electives/talend`](../26_electives/talend/README.md) module.

## Core Concepts

- ETL vs ELT, extraction, transformation, loading
- Full load vs incremental load, change tracking (CDC previewed, covered fully in Phase 18)
- Data validation, error handling, retry mechanisms, idempotency
- Data lineage, metadata, data contracts fundamentals

## Exercises

- Design an idempotent incremental-load strategy for a sample source table (watermark column or CDC-lite).
- Implement a Python ELT script: extract from a file/API, load raw, transform in SQL/pandas.
- Add retry-with-backoff and structured error logging to the extraction step.
- Complete the Talend-vs-Python comparison exercise in the subfolder.

## Expected Output

- A working Python ELT script with idempotent incremental loading.
- The completed comparison write-up in `talend_vs_python_comparison/`.

## Validation Checklist

- [ ] Re-running the ELT script on the same source data does not duplicate rows.
- [ ] A simulated source failure is retried and logged, not silently swallowed.

## Common Mistakes

- Confusing 'idempotent' with 'safe to run once' — it must be safe to run *any* number of times.
- Treating data validation as optional instead of a pipeline gate.

## Optional Challenges

- Add a simple data lineage log (source -> transform -> destination) as structured metadata.

## Reflection Questions

- What made Talend's GUI-based approach easier or harder than code for the same pipeline?
