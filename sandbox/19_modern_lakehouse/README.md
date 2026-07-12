# Phase 19 — Modern Lakehouse

## Learning Objectives

- Understand object storage concepts and MinIO as a local S3-compatible store.
- Understand table formats (Apache Iceberg) and what they add over raw files: ACID, schema evolution, time travel, partitioning.
- Understand catalog concepts (Hive Metastore) and query the lakehouse with Trino.

## Prerequisites

- Phase 11 — Data Architecture and Modeling
- Phase 16 — Spark/Hadoop
- Phase 18 — Kafka/CDC/Flink

## Reference Materials (`ref roadmap/`, read-only)

- [MinIO architecture](../../ref%20roadmap/My%20mentor/BUỔI%207/BÀI%20GIẢNG/MINIO%20-%20S3%20-%20AWS/LESSON%207%20-%20Kiến%20trúc%20MINIO.docx)
- [MinIO vs HDFS comparison](../../ref%20roadmap/My%20mentor/BUỔI%207/BÀI%20GIẢNG/MINIO%20-%20S3%20-%20AWS/LESSON%207%20-%20So%20Sánh%20MinIO%20và%20HDFS.docx)
- [HDFS vs S3 comparison](../../ref%20roadmap/My%20mentor/BUỔI%207/BÀI%20GIẢNG/MINIO%20-%20S3%20-%20AWS/LESSON%207%20-%20So%20sánh%20HDFS%20và%20S3.docx)
- [What Iceberg is and why enterprises use it](../../ref%20roadmap/My%20mentor/BUỔI%207/BÀI%20GIẢNG/ICEBERG%20-%20HIVE/LESSON%207%20-%20Iceberg%20là%20gì,%20vì%20sao%20nó%20lại%20được%20lựa%20chọn%20sử%20dụng%20trong%20doanh%20nghiệp.docx)
- [Iceberg architecture](../../ref%20roadmap/My%20mentor/BUỔI%207/BÀI%20GIẢNG/ICEBERG%20-%20HIVE/LESSON%207%20-%20Kiến%20trúc%20Iceberg.docx)
- [ACID in Iceberg](../../ref%20roadmap/My%20mentor/BUỔI%207/BÀI%20GIẢNG/ICEBERG%20-%20HIVE/LESSON%207%20-%20ACID%20trong%20Iceberg.docx)
- [Why Iceberg needs Hive Metastore](../../ref%20roadmap/My%20mentor/BUỔI%207/BÀI%20GIẢNG/ICEBERG%20-%20HIVE/LESSON%207%20-%20Hive%20metastore%20ở%20đây%20làm%20công%20việc%20gì,%20tại%20sao%20iceberg%20rest%20lại%20phải%20chọn%20hive%20metastore.docx)
- [Trino architecture](../../ref%20roadmap/My%20mentor/BUỔI%207/BÀI%20GIẢNG/TRINO/LESSON%207%20-%20Kiến%20trúc%20Trino.docx)
- [Trino vs Hive comparison](../../ref%20roadmap/My%20mentor/BUỔI%207/BÀI%20GIẢNG/TRINO/LESSON%207%20-%20So%20sánh%20Trino%20và%20Hive.docx)
- [Full lakehouse install walkthrough: Kafka+Minio -> Hadoop/Hive Metastore -> Iceberg REST -> Flink/Trino](../../ref%20roadmap/My%20mentor/BUỔI%207/BÀI%20GIẢNG/FLINK%20-%20SPARK%20-%20TRINO/STREAMING%20VỚI%20KAFKA%20-%20FLINK%20-%20ICEBERG%20-%20MINIO%20-%20TRINO/LESSON%207%20-%20MAIN%20-%20STEP%201%20-%20Cài%20đặt%20Kafka%20và%20Minio.docx)

> This phase is deliberately moved into the core path (before the final projects) rather than treated as an elective, per your directive — it's a natural extension of Phase 11's data architecture and Phase 16's big-data foundations. Gravitino (metadata catalog abstraction) is optional further reading, not required for this phase's exercises.

## Core Concepts

- Object storage concepts; MinIO as an S3-compatible local store; erasure coding basics
- Table formats: what Iceberg adds over plain Parquet-on-object-storage
- Hive Metastore and catalog concepts
- Trino as a SQL query engine over the lakehouse
- ACID transactions, schema evolution, time travel, partitioning strategy

## Exercises

- Stand up MinIO locally and create a bucket to act as your lakehouse storage.
- Register a Hive Metastore and create an Iceberg table on top of MinIO.
- Query the table via Trino; then add a column and prove old queries still work (schema evolution).
- Run a time-travel query against a prior snapshot of the table.
- Choose and justify a partitioning strategy for the table based on expected query patterns.

## Expected Output

- This phase's output feeds Checkpoint 8 — a working MinIO + Iceberg + Hive Metastore + Trino stack.

## Validation Checklist

- [ ] A schema evolution (added column) doesn't break reads of pre-existing data.
- [ ] A time-travel query correctly returns a prior snapshot.

## Common Mistakes

- Partitioning by a high-cardinality column, creating excessive small files.
- Treating Iceberg as 'just Parquet' and missing why the catalog/metadata layer matters.

## Optional Challenges

- Explore Gravitino as a catalog abstraction layer across Trino/Spark/Flink.

## Reflection Questions

- What does this stack give you that a plain folder of Parquet files on MinIO wouldn't?
