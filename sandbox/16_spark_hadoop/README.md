# Phase 16 — Big Data Processing

## Learning Objectives

- Understand distributed storage concepts (HDFS) and when big data tooling is actually needed.
- Understand Spark's architecture and write PySpark DataFrame transformations.
- Understand partitions, shuffle, and basic Spark performance considerations.

## Prerequisites

- Phase 09 — Python
- Phase 10 — SQL

## Reference Materials (`ref roadmap/`, read-only)

- [Why big data needs HDFS](../../ref%20roadmap/My%20mentor/BUỔI%203/BÀI%20GIẢNG/BIGDATA/LESSON%203%20-%20Big%20data%20là%20gì,%20vì%20sao%20phải%20sử%20dụng%20HDFS%20để%20phục%20vụ%20cho%20big%20data.docx)
- [Installing single-node Hadoop on Ubuntu](../../ref%20roadmap/My%20mentor/BUỔI%203/BÀI%20GIẢNG/BIGDATA/Hadoop%20-%20Yarn%20Cluster/LESSON%203%20-%20MAIN%20-%20STEP%201%20-%20Cài%20đặt%20Hadoop%20Cluster%20cho%201%20Master%202%20Slaves.docx)
- [How Spark works](../../ref%20roadmap/My%20mentor/BUỔI%203/BÀI%20GIẢNG/BIGDATA/SPARK/LESSON%203%20-%20ADVANCE%20-%20Cách%20mà%20Spark%20hoạt%20động.docx)
- [Spark vs pandas comparison](../../ref%20roadmap/My%20mentor/BUỔI%203/BÀI%20GIẢNG/BIGDATA/SPARK/LESSON%203%20-%20So%20sánh%20giữa%20pandas%20và%20spark.docx)
- [Understanding shuffle in Spark](../../ref%20roadmap/My%20mentor/BUỔI%203/BÀI%20GIẢNG/BIGDATA/SPARK/LESSON%203%20-%20Tìm%20hiểu%20về%20Shuffle%20trong%20Spark.docx)
- [PySpark code sample](../../ref%20roadmap/My%20mentor/BUỔI%203/BÀI%20GIẢNG/BIGDATA/SPARK/CODE%20SAMPLE/test_pyspark.py)

> Treat single-node Hadoop as the required hands-on target for this phase. Multi-node cluster setup (ZooKeeper, Kerberos, Ranger) is deferred to [`26_electives/advanced_hadoop`](../26_electives/advanced_hadoop/README.md) — it's enterprise-ops territory, not a prerequisite for learning Spark.

## Core Concepts

- Big Data fundamentals, distributed storage, HDFS concepts (YARN mentioned only conceptually here)
- Spark architecture, PySpark DataFrames, transformations vs actions
- Partitions and shuffle
- Spark SQL, basic performance fundamentals

## Exercises

- Install Spark locally (standalone, no cluster needed) and run a PySpark job over a multi-hundred-MB dataset.
- Compare a pandas transformation and the equivalent PySpark transformation on the same data — measure the difference and explain why it's not always faster.
- Deliberately trigger a wide shuffle (e.g., a `groupBy` on a high-cardinality key) and inspect the Spark UI's stages.
- Repartition the data to reduce shuffle and measure the improvement.

## Expected Output

- A PySpark script with a documented before/after optimization, and Spark UI notes explaining what changed.

## Validation Checklist

- [ ] You can explain, using your own Spark UI screenshots/notes, what a shuffle is and why it's expensive.
- [ ] The optimized job is measurably faster or uses fewer resources than the naive version.

## Common Mistakes

- Reaching for Spark on data that fits comfortably in pandas — know the crossover point.
- Ignoring partition count and ending up with too many small tasks or too few large ones.

## Optional Challenges

- Read directly from HDFS in a PySpark job using a local single-node Hadoop install.

## Reflection Questions

- At what data size did Spark actually start winning over pandas in your own test?
