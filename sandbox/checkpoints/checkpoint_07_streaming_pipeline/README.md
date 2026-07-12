# Checkpoint 7 — Streaming Data Engineering Pipeline

**Builds on:** [`18_kafka_cdc_flink`](../../18_kafka_cdc_flink/README.md)

## Business / Learning Problem

Some changes need to reach downstream systems in near real time — waiting
for the next batch window isn't good enough. This checkpoint captures
changes from a database and streams them through processing to a
destination.

## Requirements

- PostgreSQL with logical replication/WAL enabled as the CDC source.
- Debezium (or an equivalent CDC connector) capturing row-level changes into
  Kafka topics.
- A Flink job consuming the Kafka topic, applying at least one
  transformation (filter, enrich, or windowed aggregation).
- A defined output sink (can be as simple as another Postgres table, a
  file, or console output for learning purposes).

## Milestones

1. Architecture docs completed, including event time vs processing time
   decisions.
2. WAL/CDC capturing real changes made to the source table into Kafka.
3. Flink job consuming and transforming the stream.
4. End-to-end change (an `UPDATE` in Postgres) observed flowing through to
   the sink within seconds.

## Expected Outputs

- Docker Compose stack for Kafka + Debezium connector config.
- Flink job source code.
- A short log/screenshot trail showing a change propagating end-to-end.

## Testing Requirements

- Demonstrate at-least-once (or better) delivery: kill a component mid-flow
  and show no permanent data loss.
- Demonstrate correct handling of at least one late/out-of-order event.

## Documentation Requirements

- Full `architecture/` folder, with an ADR on your windowing/watermark
  strategy and why it fits this use case.

## Validation Checklist

- [ ] A change in Postgres is visible in the sink within a defined SLA
      (state the number you're targeting and whether you hit it).
- [ ] Consumer restart resumes without reprocessing the entire topic from
      scratch (offsets/checkpointing works).
- [ ] Schema Registry (or equivalent) prevents an incompatible schema change
      from silently corrupting downstream data.

## Completion Criteria

You can make a change in the source database and demonstrate, end-to-end,
where it appears downstream and how long it took.
