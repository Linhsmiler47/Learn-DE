# Checkpoint 6 — Batch Data Engineering Pipeline

**Builds on:** [`16_spark_hadoop`](../../16_spark_hadoop/README.md), [`17_airflow`](../../17_airflow/README.md)

## Business / Learning Problem

Some transformation is heavy enough (or the exercise demands it) to justify
distributed processing instead of a single-machine script, and needs to run
on a reliable, observable schedule instead of manually.

## Requirements

- A PySpark job performing a non-trivial transformation (joins, aggregation,
  window functions) over a dataset large enough that partitioning/shuffle
  behavior is observable (doesn't need to be "big data," just big enough to
  matter — a few hundred MB is plenty for a laptop).
- An Airflow DAG that runs the Spark job on a schedule, with retries and
  failure alerting (can be a log line or local notification — no paid
  services required).
- Idempotent output (safe to re-run for the same batch/date).

## Milestones

1. Architecture docs completed.
2. PySpark job runs standalone and produces correct output on sample data.
3. Airflow DAG wraps the job with retries and a defined schedule.
4. A deliberate task failure is shown triggering Airflow's retry policy.

## Expected Outputs

- `spark_job.py` (or equivalent) with clear stages.
- `dags/batch_pipeline_dag.py`.
- Spark UI screenshot or notes showing partition/shuffle behavior you
  investigated.

## Testing Requirements

- Unit tests for any pure transformation logic extracted from the Spark job.
- Proof of idempotent re-run: same input date, same output, run twice.

## Documentation Requirements

- Full `architecture/` folder, with an ADR on your partitioning strategy and
  why (e.g., partition by date vs by key).

## Validation Checklist

- [ ] DAG shows correct task dependencies and retry behavior on failure.
- [ ] Spark job's output is provably idempotent across repeated runs.
- [ ] Backfill for a past date works without code changes.
- [ ] Logs are sufficient to debug a failed run without re-running it blind.

## Completion Criteria

The DAG can be backfilled for an arbitrary past date and produce correct,
non-duplicated output, unattended.
