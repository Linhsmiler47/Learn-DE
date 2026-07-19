# Phase 04 — Configuration

This phase is a full guided learning module. If you're starting fresh, go
straight to [`lessons/01_configuration_file_formats.md`](lessons/01_configuration_file_formats.md)
— the rest of this README is the map, not the content itself.

This is the **first phase built with the 5-core-lesson model**: fewer,
longer lessons instead of 10–12 smaller ones (Phase 01/02 remain on the
original model, unchanged). Same framework otherwise — see
[`../_templates/PHASE_STRUCTURE.md`](../_templates/PHASE_STRUCTURE.md). No
quizzes, no answer keys. Understanding is demonstrated through an
**Evidence Review** at the end of every lesson, captured in `notes/`.

## Learning Objectives

- Read/write YAML, JSON, TOML, INI confidently; recognize XML.
- Build a validated, fail-fast config loader for a single application instance.
- Design dev/test/staging/prod/CI variants of the same config with
  correct per-environment secret handling.
- Design a layered, validated configuration architecture — with logging as
  one config concern among others, not the focus.
- Produce one real, reusable configuration convention that Checkpoint 4
  (and beyond) directly builds on.

## Prerequisites

- Phase 01 (env vars, `set -euo pipefail`'s fail-fast spirit)
- Phase 02 (`.env`/`.env.example`, secret hygiene, real branch+PR discipline)

## How This Module Is Organized

```
04_configuration/
├── README.md            <- you are here — navigation only
├── lessons/              5 lessons: theory, mental model, terminology,
│                         realistic DE examples (DB connections, API
│                         endpoints, batch sizes, retry policies), safety
│                         notes, troubleshooting, knowledge checks
├── exercises/            guided.md + independent.md per lesson
├── assessment/           the ONE practical assessment for this phase + rubric
├── cheatsheet/            one consolidated quick-reference
├── notes/                 your evidence log + free-form notes (graded)
├── workspace/             disposable scratch space (Lessons 01–04)
└── reflection.md          completed after the assessment
```

## This Phase Uses the Real `Learn-DE` Repository

Per the Repository Usage Policy: Lessons 01–04's practice happens mostly
in `workspace/` (config file drafting, loader iteration) since it's not
yet meant to last. **Lesson 05's capstone and the practical assessment are
real, committed work** — a reusable convention document at
`sandbox/_templates/CONFIGURATION_CONVENTION.md`, and real configuration
scaffolding for Checkpoint 4 — both via proper feature branches and PRs.

## Lesson Sequence

| # | Lesson | Est. effort (theory/guided/independent) |
|---|---|---|
| 01 | [Configuration File Formats: YAML, JSON, TOML, INI & XML](lessons/01_configuration_file_formats.md) | 45 / 40 / 30 min |
| 02 | [Application Configuration](lessons/02_application_configuration.md) | 40 / 35 / 30 min |
| 03 | [Multi-Environment Configuration & Secrets](lessons/03_multi_environment_configuration.md) | 45 / 40 / 35 min |
| 04 | [Configuration Architecture](lessons/04_configuration_architecture.md) | 50 / 40 / 35 min |
| 05 | [Capstone: Production-Style Configuration Architecture](lessons/05_capstone_configuration_architecture.md) | 45 / 45 / 40 min |

Total estimated effort: roughly **12–15 hours**.

## The Learning Cycle (per lesson)

`Learn → Observe → Guided practice → Independent exercise → Validate → Debug → Evidence Review`
— then, at the phase level: `Practical assessment → Reflect`.

## Assessment and Scoring

100 points total — see [`assessment/rubric.md`](assessment/rubric.md).
One practical assessment (no exam): apply Lesson 05's capstone convention
for real to Checkpoint 4 — format choice, `.env.example`, multi-environment
variants, a working layered/validated loader, logging as configuration,
and a dependency-management reference. See [`assessment/README.md`](assessment/README.md).

| Category | Points |
|---|---|
| Guided exercises | 25 |
| Independent exercises | 30 |
| Practical assessment | 35 |
| Documentation and reflection | 10 |

**80–100**: pass, continue. **70–79**: review weak categories, reassess.
**Below 70**: repeat the weakest lessons and exercises.

## Data Engineering Context

Every lesson ties back to real tools, not generic app examples:

| Lesson | Docker | dbt | Airflow | Terraform | CI/CD | Cloud |
|---|---|---|---|---|---|---|
| 01 | Compose YAML | `dbt_project.yml` | `airflow.cfg` (INI) | JSON output | Actions YAML | — |
| 02 | `env_file:`/`environment:` | `profiles.yml` env vars | Connections/Variables | Provider creds via env | Repo secrets | — |
| 03 | `docker-compose.override.yml` | `profiles.yml` targets | Env-specific DAG behavior | Per-env `.tfvars` | Per-env Actions secrets | Key Vault / Secrets Manager (previewed) |
| 04 | Layered env resolution | `vars` layering | Variables/Connections as config-as-code | `variables.tf` validation | Required-secret checks pre-run | — |
| 05 | — | — | — | — | — | **The literal config pattern Checkpoint 4 uses** |

## Reference Materials (`ref roadmap/`, read-only)

No dedicated configuration lesson exists in `ref roadmap/`. Tangential
real examples: [PostgreSQL WAL configuration](../../ref%20roadmap/My%20mentor/BUỔI%204/BÀI%20GIẢNG/LESSON%204%20-%20MAIN%20-%20INCLUDE%20-%20Ý%20nghĩa%20cấu%20hình%20WAL%20trong%20Postgresql.docx) and [Airflow enterprise deployment config](../../ref%20roadmap/My%20mentor/BUỔI%203/BÀI%20GIẢNG/SCHEDULER/AIRFLOW/LESSON%203%20-%20ADVANCE%20-%20Cấu%20hình%20Airflow%20cho%20việc%20triển%20khai%20trong%20doanh%20nghiệp.docx).

## When You're Done

Complete [`reflection.md`](reflection.md), self-score against
[`assessment/rubric.md`](assessment/rubric.md), then continue per your
Progress Tracking plan in `LEARNING_PATH.md`.
