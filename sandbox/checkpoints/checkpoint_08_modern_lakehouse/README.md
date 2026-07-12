# Checkpoint 8 — Modern Lakehouse Project

**Builds on:** [`19_modern_lakehouse`](../../19_modern_lakehouse/README.md)

## Business / Learning Problem

Object storage is cheap but "dumb" (no ACID, no schema enforcement, no time
travel) on its own. This checkpoint builds a lakehouse — table-format
guarantees layered on top of object storage — and proves those guarantees
actually hold.

## Requirements

- MinIO running locally as S3-compatible object storage.
- At least one Iceberg table registered in a Hive Metastore (or equivalent
  catalog) on top of that storage.
- Trino configured to query the Iceberg table via SQL.
- Demonstrated: a schema evolution (add a column, old data still readable),
  a time-travel query (read a prior snapshot), and a concurrent-write
  scenario reasoned about (even if not literally concurrent — explain what
  would happen).

## Milestones

1. Architecture docs completed.
2. MinIO + Hive Metastore + Iceberg + Trino stack running (Docker Compose).
3. Data loaded into an Iceberg table, queryable via Trino SQL.
4. Schema evolution and time-travel both demonstrated with actual queries.

## Expected Outputs

- Docker Compose stack definition.
- SQL scripts showing table creation, schema evolution, and a time-travel
  query (`SELECT * FROM table FOR VERSION AS OF ...` or equivalent).

## Testing Requirements

- Prove old queries against the table still work after a schema change
  (backward compatibility).
- Prove a time-travel query returns the pre-change data correctly.

## Documentation Requirements

- Full `architecture/` folder, with an ADR comparing Iceberg vs plain
  Parquet-on-S3 vs a traditional data warehouse for this use case, and one
  covering partitioning strategy chosen for the table.

## Validation Checklist

- [ ] Trino can query the Iceberg table with standard SQL.
- [ ] A schema evolution (added column) doesn't break reads of old data.
- [ ] A time-travel query successfully retrieves a prior table snapshot.
- [ ] Partitioning choice is documented with a reason tied to expected query
      patterns.

## Completion Criteria

You can explain, with a live demo, why this table has stronger guarantees
than a folder of raw Parquet files on the same object storage.
