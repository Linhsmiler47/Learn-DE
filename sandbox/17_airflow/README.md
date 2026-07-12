# Phase 17 — Workflow Orchestration

## Learning Objectives

- Understand why orchestration exists beyond cron: dependencies, retries, backfills.
- Build Airflow DAGs with tasks, operators, and scheduling.
- Monitor and log pipeline runs.

## Prerequisites

- Phase 12 — ETL/ELT
- Phase 16 — Spark/Hadoop

## Reference Materials (`ref roadmap/`, read-only)

- [Introduction to Airflow](../../ref%20roadmap/My%20mentor/BUỔI%203/BÀI%20GIẢNG/SCHEDULER/AIRFLOW/LESSON%203%20-%20INTRO%20-%20Giới%20thiệu%20Airflow.xlsx)
- [Installing Apache Airflow 3.0 with PostgreSQL on Ubuntu](../../ref%20roadmap/My%20mentor/BUỔI%203/BÀI%20GIẢNG/SCHEDULER/AIRFLOW/LESSON%203%20-%20MAIN%20step%201%20-%20Hướng%20dẫn%20cài%20đặt%20Apache%20Airflow%203.0%20với%20PostgreSQL%20trên%20Ubuntu.docx)
- [Deploying a job as an Airflow DAG](../../ref%20roadmap/My%20mentor/BUỔI%203/BÀI%20GIẢNG/SCHEDULER/AIRFLOW/LESSON%203%20-%20MAIN%20step%202%20-%20Deploy%20Talend%20lên%20Airflow%20chạy%20thông%20qua%20DAG.docx)
- [Sample DAG file](../../ref%20roadmap/My%20mentor/BUỔI%203/BÀI%20GIẢNG/SCHEDULER/AIRFLOW/talend_job_dag.py)

> The reference DAG deploys a Talend job — read it for the DAG/operator pattern, but your own exercises should orchestrate the Python/Spark pipelines from Phases 12/16, not Talend.

## Core Concepts

- Why orchestration: idempotency, backfill, dynamic pipelines, beyond-cronjob thinking
- Airflow architecture, DAGs, tasks, operators
- Scheduling, dependencies, retries, backfills
- Logging and monitoring of pipeline runs

## Exercises

- Install Airflow locally and write a DAG that runs Checkpoint 4/Phase 15's ingestion script on a schedule.
- Add a downstream task depending on the ingestion task's success (e.g., trigger dbt after ingestion).
- Deliberately fail a task and observe/configure the retry policy.
- Backfill the DAG for a past date range and confirm idempotent, correct results.

## Expected Output

- A working Airflow DAG orchestrating at least two dependent tasks, feeding Checkpoint 6.

## Validation Checklist

- [ ] The DAG's retry policy is demonstrated recovering from a transient failure.
- [ ] A backfill for 3 past dates produces correct, non-duplicated results for each.

## Common Mistakes

- Writing non-idempotent tasks that break on backfill or retry.
- Putting heavy computation directly in the DAG file instead of calling out to a script/operator.

## Optional Challenges

- Add a Slack/webhook-style notification (can be a local log or dummy endpoint) on DAG failure.

## Reflection Questions

- What's the smallest change that would make Phase 12's cron-based script Airflow-worthy?
