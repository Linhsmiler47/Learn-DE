# Phase 18 — Streaming Data Engineering

## Learning Objectives

- Understand event-driven and streaming architecture fundamentals.
- Understand Kafka's architecture: producers, consumers, topics, partitions, consumer groups.
- Understand CDC with Debezium and stream processing with Flink (event time, windows, checkpoints).

## Prerequisites

- Phase 10 — SQL/PostgreSQL
- Phase 17 — Airflow (contrast batch vs streaming)

## Reference Materials (`ref roadmap/`, read-only)

- [What Kafka is and its architecture](../../ref%20roadmap/My%20mentor/BUỔI%204/BÀI%20GIẢNG/KAFKA/LESSON%204%20-%20KAFKA%20là%20gì%20-%20Kiến%20trúc%20của%20Kafka.docx)
- [Kafka Connect architecture](../../ref%20roadmap/My%20mentor/BUỔI%204/BÀI%20GIẢNG/KAFKA/LESSON%204%20-%20Kafka%20Connect%20là%20gì%20-%20Kiến%20trúc%20Kafka%20Connect.docx)
- [Kafka Schema Registry](../../ref%20roadmap/My%20mentor/BUỔI%204/BÀI%20GIẢNG/KAFKA/LESSON%204%20-%20ADVANCE%20-%20Schema%20Registry.docx)
- [Streaming/CDC concepts and replication](../../ref%20roadmap/My%20mentor/BUỔI%204/BÀI%20GIẢNG/LESSON%204%20-%20Tìm%20hiểu%20các%20khái%20niệm%20về%20streaming%20data%20và%20Change%20Data%20Capture%20%28%20CDC%20%29%20_%20Replicate%20của%20hệ%20quản%20trị%20dữ%20liệu.docx)
- [Enabling WAL + Flink + Kafka + Debezium for Postgres-to-MySQL sync](../../ref%20roadmap/My%20mentor/BUỔI%204/BÀI%20GIẢNG/LESSON%204%20-%20MAIN%20-%20STEP%201%20-%20Bật%20WAL%20cho%20Postgresql%20và%20sử%20dụng%20FLINK%20và%20KAFKA%20,%20DEBEZIUM%20để%20đồng%20bộ%20từ%20Postgresql%20sang%20MYSQL.docx)
- [How Apache Flink works](../../ref%20roadmap/My%20mentor/BUỔI%204/BÀI%20GIẢNG/FLINK/LESSON%204%20-%20Chi%20tiết%20cách%20hoạt%20động%20của%20Apache%20Flink.docx)
- [Fraud detection case study with Flink](../../ref%20roadmap/My%20mentor/BUỔI%204/BÀI%20GIẢNG/FLINK/LESSON%204%20-%20CASE%20STUDY%20-%20Phát%20hiện%20đơn%20hàng%20bị%20spam%20trong%20thời%20gian%20thực%20%28Fraud%20Detection%29.docx)

## Core Concepts

- Event-driven systems, streaming architecture
- Kafka: producers, consumers, topics, partitions, consumer groups, Kafka Connect, Schema Registry, Avro
- Change Data Capture with Debezium
- Apache Flink: stream processing, event time vs processing time, windows, checkpoints

## Exercises

- Stand up Kafka locally and write a producer/consumer pair with a defined Avro schema.
- Enable PostgreSQL logical replication and capture changes into Kafka via Debezium.
- Write a Flink job consuming the CDC topic and applying a windowed aggregation.
- Deliberately send an incompatible schema change and observe Schema Registry's enforcement (or lack of it if not configured).

## Expected Output

- This phase's output feeds Checkpoint 7 — a working Kafka + Debezium + Flink pipeline.

## Validation Checklist

- [ ] An `UPDATE` on the source Postgres table is observable in the Flink job's output within seconds.
- [ ] Schema Registry rejects (or you've documented why it doesn't) an incompatible schema change.

## Common Mistakes

- Confusing event time and processing time, leading to incorrect windowed results on late data.
- Not setting `replication factor` / `partition count` thoughtfully, even in a local single-broker setup.

## Optional Challenges

- Handle a deliberately late-arriving event correctly using watermarks.

## Reflection Questions

- Why can't Airflow (Phase 17) replace Kafka/Flink here — what's fundamentally different about the latency requirement?
