# Data Engineering Learning Path

This is the master guide for this repository's learning journey: an
architecture-first path from Linux fundamentals through Data Engineering to
cloud deployment on Azure and AWS. It was designed by analyzing
[`ref roadmap/`](ref%20roadmap/) (read-only reference material) against
[`docs/DE_LEARNING_PATH_REQUIREMENTS.md`](docs/DE_LEARNING_PATH_REQUIREMENTS.md),
then adjusted per your review. See [`CLAUDE.md`](CLAUDE.md) for the standing
repository rules.

All hands-on work happens in [`sandbox/`](sandbox/README.md). This document
is the map; `sandbox/` is the territory.

## How to use this document

1. Work through the numbered phases in order — each has a concise README
   under `sandbox/NN_topic/README.md` with objectives, concepts, exercises,
   and a validation checklist until it's requested in detail (see
   [Phase Structure Standard](#phase-structure-standard) below for what a
   fully detailed phase looks like). No solutions are provided; you build them.
2. Don't wait for the end to build something real — follow the **checkpoint
   project track** (below) interleaved with the phases.
3. For every checkpoint and the final project, do architecture *before*
   code: see [Architecture-First Practice](#architecture-first-practice).

## Phase Structure Standard

Every phase, once you request its detailed content, is built to the same
structure — defined once in
[`sandbox/_templates/PHASE_STRUCTURE.md`](sandbox/_templates/PHASE_STRUCTURE.md)
so it doesn't need to be re-decided per phase:

```
NN_phase_name/
├── README.md       navigation only
├── lessons/        the actual teaching content
├── exercises/       guided.md + independent.md per lesson
├── assessment/      exactly ONE practical assessment + rubric (no exam)
├── cheatsheet/       quick-reference
├── notes/            the learner's evidence log (graded) + free notes
├── workspace/        disposable practice files only
└── reflection.md     completed after the assessment
```

**No quizzes, no answer keys, ever, unless explicitly requested.**
Understanding is demonstrated through an **Evidence Review** at the end of
every lesson (commands used, real terminal output, validation results,
written explanation, troubleshooting notes, overall understanding — all in
`notes/`) instead of a quiz, and through **one** practical assessment per
phase that simulates a real engineering scenario instead of an exam.
Phase 01 was refactored to this standard on 2026-07-12; it's the reference
implementation — look there for a worked example before building a new
phase.

**This framework is now stable (as of Phase 02's approval, 2026-07-12).**
Folder structure, the Evidence Review process, and the one-practical-
assessment philosophy are not to be redesigned again unless explicitly
requested — from here on, phase work means *creating content* inside this
structure, not revisiting the structure itself.

## Repository Usage Policy

**`Learn-DE` (this repository) is the primary engineering project for the
entire learning journey — Phase 01 through the final Data Engineering
project.** Do not create throwaway repositories for practice unless a
lesson explicitly requires isolated experimentation (e.g., a concept that
must be demonstrated on a disposable repo before it's safe to try on a
real one). The default is always: work happens here, for real.

**Rules every phase's exercises and assessments follow:**

- Use a dedicated feature branch per phase (or per meaningful unit of
  work within a phase) — never commit practice work directly to `main`.
- `main` stays stable at all times. It should be deployable/readable at
  any point in the journey, not mid-experiment.
- Each phase's `workspace/` folder is for disposable practice files only
  (per the Phase Structure Standard above) — never committed, never the
  place where "real" exercise output ends up long-term.
- Commit only artifacts with lasting learning or engineering value.
  Temporary practice artifacts (scratch scripts, half-finished
  experiments, throwaway test files) are removed before merging a
  feature branch, not left in for "completeness."
- The repository should read as **progressively cleaner, better
  organized, and more production-like** after every phase — if a phase's
  work leaves the repo messier than it found it, that's a signal to
  revisit how that phase was closed out, not just move on.

**Safe experimentation with destructive Git operations:** lessons that
teach interactive rebase, `reset`, cherry-pick, history rewriting,
`filter-repo`, or merge-conflict practice do so on **temporary practice
branches**, created specifically for that exercise and discarded
afterward. Never perform destructive history operations on `main`,
long-lived learning branches, or already-completed phase branches —
unless a lesson explicitly requires it on one of those and explains the
risk first (as Phase 01's SSH lesson did for `sshd_config`, this is the
same pattern: real risk gets named before it's ever invoked, and it's the
exception, not the default).

**Practical assessments improve the real repository** rather than
generating artificial work. Where possible, an assessment should: reuse
work that already exists, organize and clean up existing commits, improve
the repository's actual structure, file meaningful Issues, cut meaningful
Releases, and improve real documentation — the way Git is actually used
on a professional engineering team. Avoid fabricating commits or changes
solely to satisfy a rubric category; if a rubric category has nothing
real to attach to yet, that's worth naming in the assessment rather than
inventing filler.

## The Learning Cycle

Every phase and project follows the same cycle — don't skip straight to
"Build":

```
Understand -> Draw the architecture -> Configure -> Build -> Test -> Debug -> Document -> Reflect
```

## Progress Tracking

The numbered order in [Track 1](#track-1--phases-dependency-reference) below is
the **canonical dependency reference** — it shows what each phase actually
needs. It is not a mandate to proceed strictly in numeric order. This
section tracks the **actual order you're following**, which may skip
around, and is updated as you request or complete phases.

**Status definitions:**

| Status | Meaning |
|---|---|
| **In Progress** | Detailed learning content exists and you are actively working through it. |
| **Planned Next** | The next phase you intend to request detailed content for. |
| **Planned** | On your current route, but not yet requested/built in detail. |
| **Skipped Temporarily** | Deliberately deferred, not removed from the path — a specific point of return is planned. |
| **Not Started** | Not yet reached in your current plan; only a high-level syllabus README exists (if that). |
| **Complete** | The phase's practical assessment has been attempted and scored ≥80 against its own rubric. **Never set just because a README or lesson file exists** — file existence and phase completion are different things. |
| **Temporarily Completed** | You've deliberately stopped at a "good enough to move on" bar rather than the full rubric bar — reviewed against a bare-minimum standard, no blocking gaps found for the next phase, but specific lessons/topics and the full practical assessment are intentionally left for a later return pass. |

**Current plan and status** (as of your latest request):

| Order | Phase | Status | Note |
|---|---|---|---|
| 1 | 01 — Linux and Development Environment | **Temporarily Completed** | Reviewed against a bare-minimum standard on 2026-07-12 — see the review in conversation history for the full breakdown. Lessons 01, 03, 05 (independent), 09 (independent), 10, and 11 have strong, real evidence. Lessons 02 and 04 are adequately evidenced (workspace artifacts confirm the work; write-ups are thinner). Lessons 06, 07, 08, and 12 have correct command design but placeholder/unfilled evidence — deferred, not blocking. The full integrative practical assessment (`assessment/`) was not attempted and remains for the return pass. |
| 2 | 02 — Git and GitHub | **Temporarily Completed** | Reviewed against a bare-minimum standard on 2026-07-19 — real, externally-verified evidence (3 merged PRs, branch protection tested, a second clone used to prove fetch/pull) across all 12 lessons, no critical misconceptions found. Reflog recovery (10) and secret-history audit commands (11) have correct reasoning but thin captured output — deferred, not blocking. The practical assessment was not attempted; note its brief will need adjusting since the Phase 01 backlog it was designed around was already committed directly to `main` outside the branch→PR flow. |
| *(deferred)* | 03 — Networking and System Architecture | **Skipped Temporarily** | Deliberately deferred, not removed. Planned return point: **after Phase 07**. See [Handling the Skipped Phase 03](#handling-the-skipped-phase-03) below. |
| 3 | 04 — Configuration and Application Structure | **In Progress** | Full detailed learning module built on 2026-07-19 using the new 5-core-lesson model (first phase on this model; Phase 01/02 remain on the original 10–12-lesson model). Capstone produces a real, reusable `sandbox/_templates/CONFIGURATION_CONVENTION.md`; assessment applies it to Checkpoint 4. Not yet attempted. |
| 4 | 05 — Docker and Container Architecture | **Planned** | Syllabus only |
| 5 | 06 — GitHub Actions and CI/CD | **Planned** | Syllabus only |
| 6 | 07 — Infrastructure as Code with Terraform | **Planned** | Syllabus only |
| 7 | 03 — Networking and System Architecture *(resumed)* | — | Return here after Phase 07, per your plan |
| — | 08–26 | **Not Started** | Syllabus-only READMEs exist from the initial repository scaffold; no detailed content |

### Handling the Skipped Phase 03

Phase 03 does not appear as a formal prerequisite for Phases 04–07 in the
Track 1 dependency table — your planned skip is consistent with the
dependency graph as designed. It's still relevant background in places:

| Phase | Phase 03 relevance | Classification |
|---|---|---|
| 04 — Configuration | None — config file formats and env vars don't depend on networking concepts. | Not needed |
| 05 — Docker | Docker networks, published ports, and container-to-container communication are easier to reason about with Phase 03's client-server/ports mental model already in place. | Recommended, not required |
| 06 — GitHub Actions/CI/CD | Runners and workflow triggers are network-mediated but fully abstracted away by GitHub Actions itself. | Optional background |
| 07 — Terraform | Local/free-tier exercises in this path don't touch real network infrastructure (VPCs, subnets) — that only becomes relevant in Phases 08 and 24–25. | Not needed yet |

When you request detailed content for any of these phases, I'll check this
table first. If a phase's content touches something Phase 03 would
normally have covered (expected for Phase 05's networking/ports section),
I will add a short "Prerequisite Notice" with the minimum necessary recap
inline, explain what's harder to reason about without the full Phase 03
treatment, and point to the specific Phase 03 topics worth revisiting when
you return to it after Phase 07 — without generating the full Phase 03
module early.

## Track 1 — Phases (dependency reference)

This table shows each phase's formal prerequisites — the order that
guarantees every dependency is met. Your actual working order can differ
(see [Progress Tracking](#progress-tracking) above); use this table to
sanity-check any reordering, not as a mandatory sequence.

| # | Phase | Why it matters | Prerequisites | `ref roadmap/` coverage | Est. effort |
|---|---|---|---|---|---|
| 01 | [Linux and Development Environment](sandbox/01_linux/README.md) | Every later tool runs on Ubuntu/WSL — this is the floor everything else stands on. | None | Good (Ubuntu-specific lessons) | 3–5 days |
| 02 | [Git and GitHub](sandbox/02_git_github/README.md) | Professional code management; a hard prerequisite for CI/CD later. | 01 | None — built from scratch | 3–5 days |
| 03 | [Networking and System Architecture](sandbox/03_networking_system_architecture/README.md) | Explains how every component you'll build actually talks to every other one. | 01, 02 | Partial (HTTP/REST only) | 1 week |
| 04 | [Configuration and Application Structure](sandbox/04_configuration/README.md) | Every tool from here on is configured, not hardcoded. | 01, 02 | Incidental (real configs inside tool docs) | 3–5 days |
| 05 | [Docker and Container Architecture](sandbox/05_docker/README.md) | Reproducible environments for every project from here forward. | 01, 04 | Good | 1 week |
| 06 | [GitHub Actions and CI/CD](sandbox/06_github_actions_cicd/README.md) | Automated verification before anything is called "done." | 02, 05 | None — built from scratch | 1 week |
| 07 | [Infrastructure as Code with Terraform](sandbox/07_terraform/README.md) | Infrastructure as versioned, reviewable code instead of manual clicks. | 01, 04 | None — built from scratch | 1 week |
| 08 | [Kubernetes Fundamentals](sandbox/08_kubernetes/README.md) | Orchestration for when one container on one host isn't the whole story. | 05, 07 | None — built from scratch | 1–2 weeks |
| 09 | [Python for Data Engineering](sandbox/09_python/README.md) | The primary language for every pipeline you'll build. | 01 | Good (install notes, concurrency samples) | 1–2 weeks |
| 10 | [SQL and Database Engineering](sandbox/10_sql_postgresql/README.md) | Every warehouse, mart, and CDC source in this path is a SQL database. | 09 | Good (MySQL-focused; adapted to PostgreSQL) | 1 week |
| 11 | [Data Architecture and Modeling](sandbox/11_data_architecture_modeling/README.md) | The design layer underneath every DE project that follows. | 10 | Strong (consolidated from 3 sessions) | 1–2 weeks |
| 12 | [ETL, ELT, and Data Integration](sandbox/12_etl_elt/README.md) | Reliable data movement is the core Data Engineering skill. | 09, 11 | Strong (Talend-heavy; used as reference, not dependency) | 1 week |
| 13 | [dbt and Analytics Engineering](sandbox/13_dbt/README.md) | Tested, documented, version-controlled transformations. | 10, 12 | Good | 1 week |
| 14 | [Data Quality and Testing](sandbox/14_data_quality_testing/README.md) | Untested pipelines fail silently in production. | 13 | Minimal (adapted from EDAI testing lesson) | 3–5 days |
| 15 | [API and Data Ingestion](sandbox/15_api_ingestion/README.md) | Most real pipelines start at an API, not a clean CSV. | 09, 12 | Good | 1 week |
| 16 | [Big Data Processing](sandbox/16_spark_hadoop/README.md) | Distributed processing once data outgrows a single machine/pandas. | 09, 10 | Strong (single-node target; multi-node deferred) | 1–2 weeks |
| 17 | [Workflow Orchestration](sandbox/17_airflow/README.md) | Pipelines need scheduling, retries, and backfills, not just cron. | 12, 16 | Good | 1 week |
| 18 | [Streaming Data Engineering](sandbox/18_kafka_cdc_flink/README.md) | Some data can't wait for the next batch window. | 10, 17 | Strong | 1–2 weeks |
| 19 | [Modern Lakehouse](sandbox/19_modern_lakehouse/README.md) | ACID, schema evolution, and time travel on cheap object storage. **Moved into the core path** ahead of the final projects. | 11, 16, 18 | Strong | 1–2 weeks |
| 20 | [End-to-End Data Engineering Projects](sandbox/20_data_engineering_projects/README.md) | Integrates every phase above into one running platform. | 01–19 | Good (capstone brief as inspiration) | 2–3 weeks |
| 21 | [Backend API with FastAPI](sandbox/21_fastapi/README.md) | Exposes your pipeline's output as a real, documented API. | 09, 20 | Minimal (EDAI teaches it earlier; this path teaches it after DE) | 1 week |
| 22 | [Simple Web Application](sandbox/22_web_application/README.md) | Makes pipeline output visible and usable, not just queryable. | 21 | None | 1 week |
| 23 | [Open-Source and Low-Cost Deployment](sandbox/23_deployment/README.md) | Ships the platform somewhere real, cheaply. | 21, 22 | None | 3–5 days |
| 24 | [Azure Data Engineering](sandbox/24_azure/README.md) | Maps everything you built locally onto managed Azure services. | 19, 23 | Minimal (API-auth only) | 1–2 weeks |
| 25 | [AWS Data Engineering](sandbox/25_aws/README.md) | Same mapping exercise for AWS, using Phase 19 as the direct bridge. | 19, 24 | Minimal (conceptual comparisons only) | 1–2 weeks |
| 26 | [Electives](sandbox/26_electives/README.md) | Talend, NiFi, Elasticsearch, multi-node Hadoop — present in the source material, not required for the core path. | varies | Strong | optional |

Effort estimates are rough planning guides, not commitments — adjust to your
own pace.

## Track 2 — Checkpoint Projects (build, throughout)

Full detail: [`sandbox/checkpoints/README.md`](sandbox/checkpoints/README.md).

| Checkpoint | After phases | Builds |
|---|---|---|
| [1](sandbox/checkpoints/checkpoint_01_linux_git/README.md) | 01–02 | Repository & dev-environment management |
| [2](sandbox/checkpoints/checkpoint_02_docker_cicd/README.md) | 04–06 | Containerized Python app with CI |
| [3](sandbox/checkpoints/checkpoint_03_terraform_kubernetes/README.md) | 07–08 | Local infrastructure deployment lab |
| [4](sandbox/checkpoints/checkpoint_04_api_postgresql/README.md) | 09–10, 15 | API ingestion pipeline |
| [5](sandbox/checkpoints/checkpoint_05_analytics_engineering/README.md) | 11–14 | Analytics engineering project |
| [6](sandbox/checkpoints/checkpoint_06_batch_pipeline/README.md) | 16–17 | Batch data engineering pipeline |
| [7](sandbox/checkpoints/checkpoint_07_streaming_pipeline/README.md) | 18 | Streaming data engineering pipeline |
| [8](sandbox/checkpoints/checkpoint_08_modern_lakehouse/README.md) | 19 | Modern lakehouse project |
| [Final](sandbox/checkpoints/final_project/README.md) | 01–19 | End-to-end data platform |

Checkpoints reuse each other's outputs (e.g., Checkpoint 5 consumes
Checkpoint 4's PostgreSQL data) — they are one continuous build, not eight
disconnected toy projects.

## Architecture-First Practice

Reading about architecture in Phase 03 is not enough practice on its own.
**Every checkpoint and the final project requires an `architecture/`
folder, filled in before implementation begins:**

```
architecture/
├── system_architecture.md   # Problem, diagram, components, scalability/reliability/security
├── data_flow.md              # Source-to-destination trace, contracts, failure points
├── component_design.md       # Per-component responsibility, dependencies, trade-offs
└── adr/
    └── 001-technology-selection.md   # One ADR per major technology decision
```

Blank templates live in [`sandbox/_templates/architecture/`](sandbox/_templates/architecture/) —
copy them into a new project, then fill them in. Every project write-up
must address: system architecture diagram, data-flow diagram, component
responsibilities, technology selection, trade-off analysis, scalability,
reliability, and security considerations.

## Scope Notes and Assumptions

- **Talend** is treated as an optional, non-core GUI ETL tool. Phase 12
  includes one small required conceptual/practical comparison against a
  Python pipeline; deeper hands-on Talend work lives in
  [`26_electives/talend`](sandbox/26_electives/talend/README.md).
- **NiFi, Elasticsearch, and multi-node Hadoop (ZooKeeper/Kerberos/Ranger)**
  are electives (Phase 26) — present in `ref roadmap/`, not required for
  checkpoint or final-project completion.
- **Phase 19 (Modern Lakehouse)** was moved into the core path, before the
  final projects, since it builds directly on Phases 11/16/18 and is
  well-represented in the reference material.
- **Phases 02, 06, 07, 08, and most of 20–25** have little or no supporting
  material in `ref roadmap/` and are designed independently of it.
- **Azure and AWS phases (24–25)** are scoped to free-tier/conceptual
  exercises — no paid cloud spend is assumed or required.
- Reference links point into `ref roadmap/`, which is **read-only** —
  never edit, move, rename, or delete anything there.
- **Quizzes and answer keys were removed from the framework** (originally
  present in Phase 01, since removed) in favor of per-lesson Evidence
  Review and a single real-scenario practical assessment per phase — see
  [Phase Structure Standard](#phase-structure-standard).
- **This repository is used as the real, continuously-improving
  engineering project for the whole journey**, not a scaffold surrounding
  disposable practice repos — see
  [Repository Usage Policy](#repository-usage-policy).
- **The framework (folder structure, Evidence Review, one assessment per
  phase) is stable as of Phase 02's approval** — future work is content
  creation within it, not framework redesign.

## Where to Start

[`sandbox/checkpoints/checkpoint_01_linux_git/README.md`](sandbox/checkpoints/checkpoint_01_linux_git/README.md),
alongside [`sandbox/01_linux/README.md`](sandbox/01_linux/README.md) and
[`sandbox/02_git_github/README.md`](sandbox/02_git_github/README.md).
