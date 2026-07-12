# Elective — Elasticsearch

## Learning Objectives

- Understand Elasticsearch's storage model and why it excels at full-text
  search compared to relational databases.
- Build a simple search-backed feature over pipeline output.

## Prerequisites

- [`10_sql_postgresql`](../../10_sql_postgresql/README.md) (for a meaningful
  comparison against relational querying)

## Reference Materials (`ref roadmap/`, read-only)

- [What Elasticsearch is and why it matters in the enterprise](../../../ref%20roadmap/My%20mentor/BUỔI%205/BÀI%20GIẢNG/Elastic%20Search/LESSON%205%20-%20Elastic%20Search%20là%20gì%2C%20vì%20sao%20nó%20lại%20quan%20trọng%20trong%20doanh%20nghiệp.docx)
- [Elasticsearch storage architecture and full-text query advantages](../../../ref%20roadmap/My%20mentor/BUỔI%205/BÀI%20GIẢNG/Elastic%20Search/LESSON%205%20-%20ADVANCE%20-%20Kiến%20trúc%20lưu%20trữ%20của%20Elastic%20Search%20vì%20sao%20có%20thể%20truy%20vấn%20về%20full%20text%20tốt%20hơn%20các%20hệ%20quản%20trị%20dữ%20liệu%20khác.docx)
- [E-commerce search demo](../../../ref%20roadmap/My%20mentor/BUỔI%205/BÀI%20GIẢNG/Elastic%20Search/LESSON%205%20-%20MAIN%20-%20Demo%20Tăng%20cường%20tìm%20kiếm%20trong%20thương%20mại%20điện%20tử%20với%20Elastic%20Search.docx)
- [Data-loading script example](../../../ref%20roadmap/My%20mentor/BUỔI%205/BÀI%20GIẢNG/Elastic%20Search/LESSON%205%20-%20CODE%20-%20import_data_pg.sh)

## Concepts

- Inverted indexes and why they make full-text search fast
- Indices, documents, mappings (Elasticsearch's schema concept)
- When to use Elasticsearch alongside (not instead of) a relational database

## Exercises

- Install Elasticsearch locally and index a sample dataset (e.g., from your
  Checkpoint 4/5 PostgreSQL data).
- Build a full-text search query and compare its relevance ranking to an
  equivalent `LIKE`/`ILIKE` query in PostgreSQL.
- Read the e-commerce demo material and describe how you'd wire
  Elasticsearch into a real ingestion pipeline (e.g., dual-write from Kafka).

## Expected Output

- A running local Elasticsearch instance with indexed sample data and at
  least one working full-text query.

## Validation Checklist

- [ ] A search query returns relevance-ranked results that a plain SQL
      `LIKE` query could not produce as usefully.

## Common Mistakes

- Using Elasticsearch as a system of record instead of a search layer fed by
  one.

## Optional Challenges

- Feed Elasticsearch from the Kafka topic built in
  [`18_kafka_cdc_flink`](../../18_kafka_cdc_flink/README.md) for a near-real-time
  search index.

## Reflection Questions

- Why doesn't the core learning path require this — what problem does it
  solve that the rest of the path doesn't already cover?
