# Checkpoint 5 — Analytics Engineering Project

**Builds on:** [`11_data_architecture_modeling`](../../11_data_architecture_modeling/README.md), [`12_etl_elt`](../../12_etl_elt/README.md), [`13_dbt`](../../13_dbt/README.md), [`14_data_quality_testing`](../../14_data_quality_testing/README.md)

## Business / Learning Problem

Checkpoint 4's raw ingested data is not yet trustworthy or analyst-friendly.
It needs a dimensional model, transformation layers, and automated quality
checks before anyone should build a report on top of it.

## Requirements

- A dimensional model (star or galaxy schema — your choice, documented as
  an ADR) for the Checkpoint 4 data: at least one fact table and two
  dimension tables.
- A dbt project with staging → intermediate → marts layers.
- At least 5 dbt tests (schema + custom) covering completeness, uniqueness,
  and referential integrity.
- Generated dbt documentation (`dbt docs generate`).

## Milestones

1. Architecture docs completed, including the dimensional model diagram.
2. dbt staging models cleaning the raw Checkpoint 4 data.
3. dbt marts models implementing the fact/dimension design.
4. Tests written and passing; a deliberately broken test proven to fail.

## Expected Outputs

- `models/staging/`, `models/marts/` dbt projects.
- `schema.yml` files with tests and documentation.
- A short data dictionary (can be dbt-generated docs).

## Testing Requirements

- `dbt test` passes on the full project.
- At least one test is shown catching a real (or deliberately introduced)
  data quality problem.

## Documentation Requirements

- Full `architecture/` folder, with an ADR justifying star vs snowflake vs
  galaxy schema for this specific dataset.

## Validation Checklist

- [ ] Fact table grain is explicitly documented (one row = what?).
- [ ] All dimension tables have a clear primary/surrogate key strategy.
- [ ] `dbt test` and `dbt docs generate` both run clean.
- [ ] A broken data quality scenario was demonstrated to fail a test.

## Completion Criteria

An analyst (hypothetical, or you wearing that hat) can query the marts layer
and trust the numbers without needing to read the ingestion code.
