# Comparison — Talend ETL Pipeline vs. Python Code-Based ETL Pipeline

## Purpose

Understand GUI-based enterprise ETL architecture well enough to talk about
its trade-offs — without making Talend a dependency of your core learning
path. This is a small, bounded comparison exercise, not a Talend course.

## Prerequisites

- [`12_etl_elt`](../README.md) core concepts
- Read (don't build yet): [Talend job install guide](../../../ref%20roadmap/My%20mentor/BUỔI%202/BÀI%20GIẢNG/TALEND/LESSON%202%20-%20Hướng%20dẫn%20cài%20đặt%20Talend.docx)
- Read: [MySQL-to-DWH ETL steps (Talend job reference)](../../../ref%20roadmap/My%20mentor/BUỔI%202/BÀI%20GIẢNG/TALEND/ETL%20MYSQL%20TO%20DWH/LESSON%202%20-%20Các%20bước%20thực%20hiện%20etl%20từ%20mysql%20to%20dwh.txt)

## Task

Pick one small, identical pipeline: extract from a source table (or file),
apply one transformation, load into a destination table. Build it two ways:

1. **Conceptually walk through the Talend version.** You do not need to
   install Talend for this — read the reference material above and diagram
   what the Talend job would look like: what components it uses (tFileInput,
   tMap, tDBOutput, etc.), how scheduling/logging/notification would be
   wired in (per the reference material's pattern of Airflow-triggered
   Talend jobs).
2. **Build the real version in Python.** Use what you built in Phase 12's
   core exercises — a script or small module doing the same extract →
   transform → load.

## Comparison Write-Up (required deliverable)

Produce a short document (`comparison.md` in this folder) answering:

| Dimension | Talend (GUI) | Python (code) |
|---|---|---|
| Time to build a first working version | | |
| How you'd code-review a change | | |
| How you'd version-control it (jobs are XML/zip, not readable diffs) | | |
| How you'd test it | | |
| How you'd debug a production failure at 2am | | |
| Learning curve for a new team member | | |
| Licensing/cost model | | |

Close with a one-paragraph recommendation: for *your* current skill set and
goals, which would you reach for, and in what scenario would the other one
actually be the better choice (e.g., a non-technical ops team maintaining
simple jobs long-term)?

## Validation Checklist

- [ ] The Talend job is diagrammed/described, not necessarily installed.
- [ ] The Python version actually runs and produces correct output.
- [ ] `comparison.md` fills in every row of the table above with your own
      reasoning, not a generic answer.

## Completion Criteria

You can explain to someone else, in plain language, why an enterprise might
choose a GUI ETL tool over code — and why this learning path chooses code
as the default anyway.
