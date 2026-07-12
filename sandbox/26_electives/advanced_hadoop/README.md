# Elective — Advanced/Multi-Node Hadoop

## Learning Objectives

- Extend the single-node Hadoop knowledge from
  [`16_spark_hadoop`](../../16_spark_hadoop/README.md) to a real multi-node
  cluster.
- Understand ZooKeeper's coordination role and enterprise-grade security
  (Kerberos, Apache Ranger) for a Hadoop cluster.

## Prerequisites

- [`16_spark_hadoop`](../../16_spark_hadoop/README.md) — single-node Hadoop
  and Spark fundamentals.

## Reference Materials (`ref roadmap/`, read-only)

- [Installing a Hadoop cluster (1 master, 2 slaves)](../../../ref%20roadmap/My%20mentor/BUỔI%203/BÀI%20GIẢNG/BIGDATA/Hadoop%20-%20Yarn%20Cluster/LESSON%203%20-%20MAIN%20-%20STEP%201%20-%20Cài%20đặt%20Hadoop%20Cluster%20cho%201%20Master%202%20Slaves.docx)
- [Installing YARN for the Hadoop cluster](../../../ref%20roadmap/My%20mentor/BUỔI%203/BÀI%20GIẢNG/BIGDATA/Hadoop%20-%20Yarn%20Cluster/LESSON%203%20-%20MAIN%20-%20STEP%202%20-%20Cài%20Yarn%20cho%20cụm%20Hadoop.docx)
- [Installing Spark integrated with YARN](../../../ref%20roadmap/My%20mentor/BUỔI%203/BÀI%20GIẢNG/BIGDATA/Hadoop%20-%20Yarn%20Cluster/LESSON%203%20-%20MAIN%20-%20STEP%203%20-%20Cài%20Spark%20tích%20hợp%20vào%20Yarn.docx)
- [Installing ZooKeeper on at least 3 nodes](../../../ref%20roadmap/My%20mentor/BUỔI%203/BÀI%20GIẢNG/BIGDATA/Hadoop%20-%20Yarn%20Cluster/LESSON%203%20-%20ADVANCE%20-%20Cài%20đặt%20ZooKeeper%20trên%20ít%20nhất%203%20node%20%28%201%20master%202%20slaves%20%29.docx)
- [Securing the Hadoop cluster with Kerberos / Apache Ranger](../../../ref%20roadmap/My%20mentor/BUỔI%203/BÀI%20GIẢNG/BIGDATA/Hadoop%20-%20Yarn%20Cluster/LESSON%203%20-%20ADVANCE%20-%20Cấu%20hình%20Kerberos%20hoặc%20sử%20dụng%20các%20công%20cụ%20như%20Apache%20Ranger%20để%20bảo%20mật%20cho%20cụm%20Hadoop.docx)
- [Adding a new node to an existing Hadoop cluster](../../../ref%20roadmap/My%20mentor/BUỔI%203/BÀI%20GIẢNG/BIGDATA/Hadoop%20-%20Yarn%20Cluster/LESSON%203%20-%20ADVANCE%20-%20Thêm%20node%20mới%20vào%20hệ%20thống%20Hadoop%20—%20bao%20gồm%20HDFS%20%28DataNode%29%20và%20YARN%20%28NodeManager%29.docx)
- [Processing a 15GB file end-to-end as a capstone-style exercise](../../../ref%20roadmap/My%20mentor/BUỔI%203/BÀI%20GIẢNG/BIGDATA/Hadoop%20-%20Yarn%20Cluster/LESSON%203%20-%20ADVANCE%20-%20BÀI%20TOÁN%20XỬ%20LÝ%20FILE%20BIG%20DATA%20DUNG%20LƯỢNG%2015GB.docx)

## Concepts

- Multi-node HDFS/YARN cluster topology (master/slave roles)
- ZooKeeper's role in coordination and leader election
- Kerberos authentication and Apache Ranger authorization for Hadoop
- Adding nodes to a running cluster without downtime

## Exercises

- Stand up a 3-node (can be VMs or containers) Hadoop cluster with YARN.
- Add ZooKeeper and explain what it's coordinating in this cluster.
- Process a large file (the reference material uses 15GB) across the
  cluster and observe how work is distributed.
- Optionally configure Kerberos and prove an unauthenticated request is
  rejected.

## Expected Output

- A running multi-node cluster with a demonstrated large-file processing
  job and cluster-topology notes.

## Validation Checklist

- [ ] The cluster survives a worker node going down (job redistributes).
- [ ] A new node can be added to the running cluster without restarting it.

## Common Mistakes

- Treating this as a prerequisite for Spark/PySpark fluency — it isn't;
  single-node Hadoop (core Phase 16) is enough for that.
- Underestimating the operational overhead this introduces versus the
  learning value for a personal/laptop-scale project.

## Optional Challenges

- Configure Apache Ranger and define a policy restricting one user's HDFS
  access.

## Reflection Questions

- At what team/data size would this operational complexity actually be
  justified, versus just using a managed service (EMR, Dataproc, HDInsight)?
