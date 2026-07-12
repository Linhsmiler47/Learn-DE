# Phase 15 — API and Data Ingestion

## Learning Objectives

- Build reliable ingestion pipelines from APIs, files, and databases.
- Handle authentication, pagination, rate limits, retries, and timeouts correctly.
- Distinguish full vs incremental ingestion across source types.

## Prerequisites

- Phase 09 — Python
- Phase 12 — ETL/ELT

## Reference Materials (`ref roadmap/`, read-only)

- [API JSON/XML to DWH: components explained](../../ref%20roadmap/My%20mentor/BUỔI%202/BÀI%20GIẢNG/TALEND/ETL%20API%20JSON%20-%20XML%20TO%20DWH/LESSON%202%20-%20Giải%20thích%20các%20thành%20phần%20trong%20API%20JSON%20-%20XML%20to%20DWH.docx)
- [EDAI-1 curriculum: WebAPI lesson (API architecture, auth, FastAPI, performance testing)](../../ref%20roadmap/EDAI/Engineering%20for%20Data%20&%20AI%20%28EDAI%20-%20K9%29%20%28Official%29%20-%20Start%20Date_%2001_04_2026.xlsx)

> This phase is the foundation for Checkpoint 4 — read the API-ingestion reference material, but implement the pipeline in Python, not Talend.

## Core Concepts

- REST API authentication mechanisms (API keys, OAuth basics)
- Pagination, rate limits, retry, timeout handling
- JSON/XML parsing
- API, file, and database ingestion patterns; incremental ingestion strategies

## Exercises

- Build a paginated API client with retry/backoff and explicit timeout handling.
- Add incremental ingestion (e.g., `updated_since` parameter or watermark) to avoid full reloads.
- Ingest a flat file (CSV/JSON) and a database table using the same pipeline shape, noting what differs.

## Expected Output

- This phase's output feeds directly into Checkpoint 4 — a working, tested API client module.

## Validation Checklist

- [ ] The client handles a simulated 429 (rate limit) and 5xx response without crashing.
- [ ] Incremental ingestion only pulls new/changed records on a second run.

## Common Mistakes

- No timeout set on HTTP calls, causing the pipeline to hang indefinitely on a slow response.
- Retrying on 4xx client errors that will never succeed (e.g., 401/403).

## Optional Challenges

- Add exponential backoff with jitter instead of fixed-delay retries.

## Reflection Questions

- What's different about designing ingestion for a database source (CDC-friendly) vs. a REST API (poll-based)?
