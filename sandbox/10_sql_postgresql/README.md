# Phase 10 — SQL and Database Engineering

## Learning Objectives

- Understand relational database concepts and write solid SQL: joins, CTEs, window functions.
- Understand transactions, indexes, and query execution/optimization basics.
- Understand database design and basic administration.

## Prerequisites

- Phase 09 — Python (for DB-API connections)

## Reference Materials (`ref roadmap/`, read-only)

- [MySQL cheat sheet (Vietnamese, v8.0)](../../ref%20roadmap/My%20mentor/BUỔI%202/BÀI%20GIẢNG/TALEND/ETL%20MYSQL%20TO%20DWH/LESSON%202%20-%20Cheatsheet%20tiếng%20việt%20cho%20Mysql%20ver%208.0.docx)
- [Example STG/DWH table creation script](../../ref%20roadmap/My%20mentor/BUỔI%202/BÀI%20GIẢNG/TALEND/ETL%20MYSQL%20TO%20DWH/LESSON%202%20-%20Script%20create%20table%20STG%20-%20DWH.sql)
- [PostgreSQL WAL configuration meaning](../../ref%20roadmap/My%20mentor/BUỔI%204/BÀI%20GIẢNG/LESSON%204%20-%20MAIN%20-%20INCLUDE%20-%20Ý%20nghĩa%20cấu%20hình%20WAL%20trong%20Postgresql.docx)
- [Remote-connecting to PostgreSQL/MySQL with DBeaver](../../ref%20roadmap/My%20mentor/BUỔI%204/BÀI%20GIẢNG/LESSON%204%20-%20MAIN%20-%20INCLUDE%20-%20Cấu%20hình%20để%20máy%20nội%20bộ%20dùng%20dbeaver%20connect%20remote%20vào%20postgresql%20và%20mysql.docx)

> Standardize on PostgreSQL for hands-on exercises (per the requirements doc) even though several reference files use MySQL — the SQL concepts transfer directly.

## Core Concepts

- Relational model, PostgreSQL basics
- Joins, CTEs, window functions, views
- Transactions and isolation, indexes, query execution plans, optimization
- Stored procedures fundamentals, database design, basic administration (WAL, backups)

## Exercises

- Design a small normalized schema (3NF) for a sample domain, then write the DDL.
- Write queries using CTEs and window functions to answer analytical questions over sample data.
- Use `EXPLAIN ANALYZE` to find a slow query and fix it with an index.
- Wrap a multi-statement operation in a transaction and demonstrate a rollback on failure.

## Expected Output

- A schema DDL file and a set of queries with `EXPLAIN ANALYZE` before/after an optimization.

## Validation Checklist

- [ ] You can explain what an index does to a query plan and when it hurts rather than helps.
- [ ] A demonstrated transaction rollback leaves the database in a consistent state.

## Common Mistakes

- Adding an index without checking whether it's actually used by the planner.
- Ignoring transaction isolation and being surprised by a race condition.

## Optional Challenges

- Write a stored procedure and compare it conceptually to doing the same transform in dbt (sets up Phase 13).

## Reflection Questions

- What did the WAL configuration note teach you about how PostgreSQL supports CDC (this connects to Phase 18)?
