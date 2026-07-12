# Checkpoint 4 — API Ingestion Pipeline

**Builds on:** [`09_python`](../../09_python/README.md), [`10_sql_postgresql`](../../10_sql_postgresql/README.md), [`15_api_ingestion`](../../15_api_ingestion/README.md)

## Business / Learning Problem

Pick a free public REST API (weather, exchange rates, a public dataset —
your choice; record the choice as an ADR). Data from it needs to land
reliably in PostgreSQL: handling pagination, rate limits, and transient
failures, without producing duplicate rows on re-runs.

## Requirements

- A Python client that paginates through the chosen API and handles rate
  limiting and retries with backoff.
- A PostgreSQL schema designed for the ingested data (not just one giant
  JSON blob column).
- An idempotent load: running the pipeline twice must not duplicate rows.
- Basic logging of what was fetched, when, and any errors.

## Milestones

1. Architecture docs completed, including the API chosen and why.
2. API client working end-to-end against the live API with retry/backoff.
3. PostgreSQL schema created and loaded.
4. Idempotency proven: pipeline run twice, row count unchanged the second
   time.

## Expected Outputs

- `client.py` (or equivalent) for API access.
- `schema.sql` for the PostgreSQL tables.
- `load.py` (or equivalent) implementing the idempotent upsert.

## Testing Requirements

- Unit tests for pagination/retry logic (can mock the API).
- An integration test or manual proof that a second run doesn't duplicate
  data.

## Documentation Requirements

- Full `architecture/` folder, with an ADR on your idempotency strategy
  (upsert key, staging + merge, etc.) and why you chose it over alternatives.

## Validation Checklist

- [ ] Pipeline survives a simulated rate-limit response (429) without
      crashing.
- [ ] Running the pipeline twice produces the same row count both times.
- [ ] Credentials/API keys are not committed anywhere in git.
- [ ] Errors are logged with enough context to debug without re-running.

## Completion Criteria

The pipeline can be run on a schedule (even manually, for now) and always
converges to a correct, deduplicated PostgreSQL table — this becomes the
raw input for Checkpoint 5.
