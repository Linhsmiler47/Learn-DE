# Phase 13 — dbt and Analytics Engineering

## Learning Objectives

- Structure a dbt project: sources, staging, intermediate models, marts.
- Write dbt tests and documentation; use macros, Jinja, seeds, and snapshots.
- Build incremental models and wire dbt into CI/CD.

## Prerequisites

- Phase 12 — ETL/ELT
- Phase 10 — SQL/PostgreSQL

## Reference Materials (`ref roadmap/`, read-only)

- [dbt architecture and why it's used in the enterprise](../../ref%20roadmap/My%20mentor/BUỔI%206/BÀI%20GIẢNG/DBT/LESSON%206%20-%20Kiến%20trúc%20DBT%20và%20lý%20do%20vì%20sao%20DBT%20được%20sử%20dụng%20trong%20doanh%20nghiệp.docx)
- [Installing dbt with Python](../../ref%20roadmap/My%20mentor/BUỔI%206/BÀI%20GIẢNG/DBT/LESSON%206%20-%20DBT%20cài%20đặt%20trên%20Python.docx)
- [dbt cheat sheet](../../ref%20roadmap/My%20mentor/BUỔI%206/BÀI%20GIẢNG/DBT/LESSON%206%20-%20Cheatsheet%20về%20DBT.docx)
- [dbt vs stored procedures](../../ref%20roadmap/My%20mentor/BUỔI%206/BÀI%20GIẢNG/DBT/LESSON%206%20-%20Advance%20-%20So%20sánh%20giữa%20DBT%20và%20Procedure.docx)
- [Small-business demo: bookings, customers, operations data](../../ref%20roadmap/My%20mentor/BUỔI%206/BÀI%20GIẢNG/DBT/LESSON%206%20-%20Demo%20về%20giả%20lập%20trong%20một%20doanh%20nghiệp%20nhỏ%20xử%20lý%20dữ%20liệu%20từ%20các%20nguồn%20như%20đặt%20vé,%20khách%20hàng,%20vận%20hành.docx)

## Core Concepts

- dbt project structure: sources, staging, intermediate, marts
- Tests (schema + custom), documentation, macros, Jinja fundamentals
- Seeds, snapshots (for SCD-like tracking), incremental models
- Data lineage (via dbt's DAG), CI/CD for dbt

## Exercises

- Build a dbt project on top of Phase 12's loaded raw data with staging and marts layers.
- Add schema tests (`not_null`, `unique`, relationships) and at least one custom SQL test.
- Implement an incremental model and prove it doesn't fully reprocess on each run.
- Generate and browse `dbt docs` to see the lineage graph.

## Expected Output

- A dbt project with staging/marts models, tests, and generated documentation.

## Validation Checklist

- [ ] `dbt build` runs clean end-to-end.
- [ ] The incremental model's run time doesn't scale with full historical volume.

## Common Mistakes

- Putting business logic in staging models instead of marts.
- Skipping tests because 'the data looks right' during development.

## Optional Challenges

- Add a dbt snapshot to track a slowly changing dimension automatically.

## Reflection Questions

- This directly builds Checkpoint 5 — which of these dbt patterns will you reuse there?
