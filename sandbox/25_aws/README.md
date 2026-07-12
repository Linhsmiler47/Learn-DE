# Phase 25 — AWS Data Engineering

## Learning Objectives

- Map local Data Engineering concepts to AWS-managed equivalents.
- Understand IAM, VPC fundamentals, and the core DE-relevant AWS services.

## Prerequisites

- Phase 24 — Azure (for a comparative baseline)
- Phase 19 — Modern Lakehouse

## Reference Materials (`ref roadmap/`, read-only)

- [MinIO vs S3 conceptual comparison](../../ref%20roadmap/My%20mentor/BUỔI%207/BÀI%20GIẢNG/MINIO%20-%20S3%20-%20AWS/LESSON%207%20-%20So%20sánh%20HDFS%20và%20S3.docx)
- [Computed/Storage separation example (relevant to S3+Athena/Redshift Spectrum thinking)](../../ref%20roadmap/My%20mentor/BUỔI%207/BÀI%20GIẢNG/MINIO%20-%20S3%20-%20AWS/LESSON%207%20-%20Ví%20dụ%20về%20tách%20biệt%20giữa%20Computed%20và%20Storage.docx)

> Only conceptual MinIO-vs-S3 comparisons exist in the reference material — no real AWS service walkthroughs. This phase is built from external AWS documentation, using Phase 19's MinIO/Iceberg/Trino work as the direct conceptual bridge (MinIO -> S3, Trino -> Athena, Hive Metastore -> Glue Catalog).

## Core Concepts

- AWS architecture fundamentals, IAM, VPC fundamentals
- S3, RDS, Lambda, Glue, Athena, Redshift
- ECS, ECR, CloudWatch, Secrets Manager

## Exercises

- Map Phase 19's MinIO + Iceberg + Hive Metastore + Trino stack onto S3 + Iceberg + Glue Catalog + Athena.
- Map every component of your Phase 20 final project onto an AWS equivalent (table format, same as Phase 24).
- Using a free-tier AWS account, provision one small piece (e.g., an S3 bucket + an Athena query) as a conceptual proof.

## Expected Output

- A mapping table: local stack component -> AWS service -> why, alongside Phase 24's Azure mapping for comparison.

## Validation Checklist

- [ ] You can explain the difference between Glue Catalog and Hive Metastore in your own words.

## Common Mistakes

- Provisioning resources without an IAM least-privilege policy (using root/admin credentials for everything).
- Forgetting to tear down free-tier resources, risking unexpected charges.

## Optional Challenges

- Compare AWS Glue (serverless Spark) against your own Phase 16 Spark setup for the same job.

## Reflection Questions

- Given Phases 24 and 25, would you pick Azure or AWS for a hypothetical employer, and why — is the answer 'it depends on the org', not the tech?
