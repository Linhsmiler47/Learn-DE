# Phase 20 — End-to-End Data Engineering Projects

## Learning Objectives

- Integrate everything from Phases 01-19 into a single, coherent, running data platform.
- Practice full-lifecycle documentation: architecture, requirements, milestones, testing, completion criteria.

## Prerequisites

- All of Phases 01-19

## Reference Materials (`ref roadmap/`, read-only)

- [Capstone project brief: Westmead Hospital DWH/ETL](../../ref%20roadmap/My%20mentor/BUỔI%208/BÀI%20GIẢNG/PROJECT%20CUỐI%20KHOÁ/de_tai_cuoi_khoa_DE%20-%20Westmead%20Hospital.txt)
- [Flowchart template for the final data-flow diagram](../../ref%20roadmap/My%20mentor/BUỔI%208/BÀI%20GIẢNG/PROJECT%20CUỐI%20KHOÁ/flow%20chart%20template.jpg)

> This phase's actual project work happens in [`../checkpoints/final_project/`](../checkpoints/final_project/README.md) — this README exists to document why this phase matters and how it maps to everything that came before. Do not reproduce the Westmead Hospital brief wholesale; use it as scope inspiration only, scaled to something finishable.

## Core Concepts

- End-to-end pipeline design: sources -> ingestion -> raw -> transform -> warehouse/lakehouse -> quality -> orchestration -> analytics-ready -> monitoring -> CI/CD
- Project scoping: choosing a finishable slice of an ambitious brief

## Exercises

- Read the Westmead Hospital brief and extract: what data domains, what report types, what technologies it assumes.
- Scope your own final project down to something achievable in the time you actually have.
- Complete the final project per [`../checkpoints/final_project/README.md`](../checkpoints/final_project/README.md).

## Expected Output

- A completed final project per the checkpoint's requirements.

## Validation Checklist

- [ ] See [`../checkpoints/final_project/README.md`](../checkpoints/final_project/README.md) validation checklist.

## Common Mistakes

- Copying the full Westmead Hospital scope (Talend + NiFi + Hadoop ML + Kafka + Elastic Search) instead of scoping down.

## Optional Challenges

- Add the ML forecasting element from the original brief as a stretch goal once the core platform works.

## Reflection Questions

- Looking back at Phase 01, what surprised you most about how far the path has come?
