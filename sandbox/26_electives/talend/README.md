# Elective — Talend (Enterprise GUI ETL)

## Learning Objectives

- Understand Talend's job model (components, connections, contexts) beyond
  the conceptual comparison done in [`12_etl_elt/talend_vs_python_comparison`](../../12_etl_elt/talend_vs_python_comparison/README.md).
- Optionally install Talend and build one real job end-to-end.

## Prerequisites

- Completed [`12_etl_elt`](../../12_etl_elt/README.md), including the required
  Talend-vs-Python comparison.

## Reference Materials (`ref roadmap/`, read-only)

- [Installing Talend](../../../ref%20roadmap/My%20mentor/BUỔI%202/BÀI%20GIẢNG/TALEND/LESSON%202%20-%20Hướng%20dẫn%20cài%20đặt%20Talend.docx)
- [Talend templates and examples A-Z](../../../ref%20roadmap/My%20mentor/BUỔI%202/BÀI%20GIẢNG/TALEND/LESSON%202%20-%20Talend%20Template%20and%20Examples%20A-Z.docx)
- [MySQL-to-DWH job (packaged Talend project)](../../../ref%20roadmap/My%20mentor/BUỔI%202/BÀI%20GIẢNG/TALEND/ETL%20MYSQL%20TO%20DWH/Sync_Mysql_to_DWH_0.1.zip)
- [API JSON/XML-to-DWH job](../../../ref%20roadmap/My%20mentor/BUỔI%202/BÀI%20GIẢNG/TALEND/ETL%20API%20JSON%20-%20XML%20TO%20DWH/Sync_API_to_DWH_0.1.zip)
- Additional source-specific jobs exist for Google Drive, OneDrive, Redis,
  Snowflake, NoSQL (Mongo/Cassandra), and Hadoop — browse
  `ref roadmap/My mentor/BUỔI 2/BÀI GIẢNG/TALEND/` for the full set.

## Concepts

- Talend Studio: jobs, components (tInput/tMap/tOutput family), contexts
  (environment variables inside Talend), and job scheduling via Airflow.

## Exercises

- Install Talend Open Studio locally.
- Open one of the packaged reference jobs (e.g., MySQL-to-DWH) and trace
  its components without running it first — predict what it does.
- Run it against a local MySQL instance and verify the output.
- Optionally, rebuild one job from scratch instead of opening the packaged
  version.

## Expected Output

- A running Talend job against a local database, with notes on what each
  component did.

## Validation Checklist

- [ ] You can explain every component in the job you opened.
- [ ] The job runs successfully against local test data.

## Common Mistakes

- Treating the packaged `.zip` jobs as something to copy into a "real"
  project — they're for exploration only.

## Optional Challenges

- Trigger the Talend job from an Airflow DAG, following the pattern in
  [`17_airflow`](../../17_airflow/README.md)'s reference material.

## Reflection Questions

- Now that you've seen a real Talend job, does it change your answer from
  the Phase 12 comparison write-up?
