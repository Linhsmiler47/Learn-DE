# Elective — Apache NiFi

## Learning Objectives

- Understand NiFi's flow-based, GUI-driven data-movement model.
- Compare NiFi to Airflow and understand when each is the better fit.

## Prerequisites

- [`17_airflow`](../../17_airflow/README.md) (for a meaningful comparison)

## Reference Materials (`ref roadmap/`, read-only)

- [Installing NiFi 2.3 with Single User config](../../../ref%20roadmap/My%20mentor/BUỔI%206/BÀI%20GIẢNG/NIFI%20-%20STREAMING/LESSON%206%20-%20Hướng%20dẫn%20cài%20đặt%20NIFI%202.3%20và%20cấu%20hình%20Single%20User.docx)
- [Managing Source Group Processor with NiFi Registry](../../../ref%20roadmap/My%20mentor/BUỔI%206/BÀI%20GIẢNG/NIFI%20-%20STREAMING/LESSON%206%20-%20Hướng%20dẫn%20quản%20lý%20Source%20Group%20Processor%20trên%20Nifi%202.3%20với%20Nifi%20Registry.docx)
- [NiFi vs Airflow comparison](../../../ref%20roadmap/My%20mentor/BUỔI%206/BÀI%20GIẢNG/NIFI%20-%20STREAMING/LESSON%206%20-%20SO%20SÁNH%20APACHE%20NIFI%20VÀ%20APACHE%20AIRFLOW.docx)
- [NiFi and schema evolution](../../../ref%20roadmap/My%20mentor/BUỔI%206/BÀI%20GIẢNG/NIFI%20-%20STREAMING/LESSON%206%20-%20ADVANCE%20-%20Nifi%20với%20vấn%20đề%20Schema%20Evolution.docx)

## Concepts

- Flow-based programming: processors, connections, flowfiles, process groups
- NiFi Registry for versioning flows
- Where NiFi overlaps with (and differs from) Kafka Connect and Airflow

## Exercises

- Install NiFi locally with single-user auth.
- Build a simple flow: read a local file, apply one transformation
  processor, write to another location.
- Read the NiFi-vs-Airflow comparison, then write your own two-paragraph
  opinion on which you'd use for a scheduled batch job vs. a continuous
  file-watching pipeline.

## Expected Output

- A working NiFi flow and your own written NiFi-vs-Airflow opinion.

## Validation Checklist

- [ ] The flow runs and correctly processes a test file end-to-end.

## Common Mistakes

- Using NiFi for complex business logic instead of simple flow-oriented
  data movement — that's a sign you should be using an orchestrator + code.

## Optional Challenges

- Version a flow with NiFi Registry and demonstrate rolling back a change.

## Reflection Questions

- What's the core conceptual difference between "orchestrating tasks"
  (Airflow) and "flowing data between processors" (NiFi)?
