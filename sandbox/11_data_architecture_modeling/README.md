# Phase 11 — Data Architecture and Modeling

## Learning Objectives

- Distinguish OLTP vs OLAP, Data Warehouse, Data Lake, Lakehouse, Data Mart.
- Design dimensional models: star schema, snowflake schema, fact/dimension tables, SCDs.
- Understand Medallion, Lambda, and Kappa architectures, and batch vs streaming design.

## Prerequisites

- Phase 10 — SQL/PostgreSQL

## Reference Materials (`ref roadmap/`, read-only)

- [DWH / Data Lake / Lakehouse in the enterprise](../../ref%20roadmap/My%20mentor/BUỔI%201/LESSON%201%20-%20DWH%20-%20Data%20lake%20-%20Lakehouse%20trong%20doanh%20nghiệp.docx)
- [Star Schema & Galaxy Schema introduction](../../ref%20roadmap/My%20mentor/BUỔI%201/LESSON%201%20-%20Giới%20thiệu%20về%20kiến%20trúc%20DWH%20-%20Star%20Schema%20&%20Galaxy%20Schema.xlsx)
- [Why DWH matters in the enterprise](../../ref%20roadmap/My%20mentor/BUỔI%206/BÀI%20GIẢNG/DWH/LESSON%206%20-%20DWH%20là%20gì%20và%20vì%20sao%20phải%20có%20trong%20Doanh%20nghiệp.docx)
- [DWH architecture explained layer by layer](../../ref%20roadmap/My%20mentor/BUỔI%206/BÀI%20GIẢNG/DWH/LESSON%206%20-%20Giải%20thích%20chi%20tiết%20từng%20Layer%20trong%20DWH.docx)
- [Data Vault 2.0 vs Galaxy schema](../../ref%20roadmap/My%20mentor/BUỔI%206/BÀI%20GIẢNG/DWH/LESSON%206%20-%20Data%20Vault%202.0%20so%20với%20galaxy%20schema%20trong%20DWH.docx)
- [DIM/FACT table design techniques](../../ref%20roadmap/My%20mentor/BUỔI%206/BÀI%20GIẢNG/DWH/LESSON%206%20-%20Các%20kỹ%20thuật%20xây%20dựng%20bảng%20DIM%20và%20FACT.xlsx)
- [ERP vs DWH vs ODS trade-offs](../../ref%20roadmap/My%20mentor/BUỔI%206/BÀI%20GIẢNG/DWH/LESSON%206%20-%20So%20sánh%20ưu%20nhược%20điểm%20về%20việc%20tập%20trung%20dữ%20liệu%20về%203%20nơi%20-%20ERP%20vs%20DWH%20vs%20ODS.docx)

> This phase consolidates DWH/modeling material that is spread across Buổi 1, 6, and 7 in the source — read it as one coherent topic here rather than three separate sessions.

## Core Concepts

- OLTP vs OLAP, Data Warehouse, Data Lake, Lakehouse, Data Mart
- Dimensional modeling: star schema, snowflake schema, galaxy schema, fact and dimension tables
- Slowly Changing Dimensions (Types 1/2/3)
- Data Vault as an alternative modeling approach
- Medallion architecture (bronze/silver/gold), Lambda vs Kappa architecture
- Batch vs streaming architecture trade-offs

## Exercises

- Take a sample business process (e.g., orders) and design a star schema: identify the grain, facts, and dimensions.
- Implement a Type 2 SCD for one dimension and demonstrate a historical change being tracked correctly.
- Write a one-page comparison: when would you choose Data Vault over a star schema for the same data?
- Diagram a Medallion architecture (bronze/silver/gold) for a dataset of your choice.

## Expected Output

- A dimensional model diagram and DDL for a star schema with one SCD Type 2 dimension.

## Validation Checklist

- [ ] The fact table's grain is explicitly stated and every fact row respects it.
- [ ] The SCD Type 2 dimension correctly preserves history on an update.

## Common Mistakes

- Mixing grains in a single fact table (e.g., daily and monthly facts together).
- Implementing SCD Type 1 (overwrite) when history actually needs to be preserved.

## Optional Challenges

- Sketch what a Lambda architecture would add on top of your Medallion design, and whether Kappa would be simpler for the same use case.

## Reflection Questions

- Which of these architectures did the `ref roadmap/` capstone project (Westmead Hospital) actually use, and why?
