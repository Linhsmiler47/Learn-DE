# Phase 04 Practical Assessment

This is the **one** assessment for Phase 04 — no separate quiz or exam.
Lesson 05's capstone already produced the abstract, reusable convention
(`sandbox/_templates/CONFIGURATION_CONVENTION.md`). This assessment is
different and complementary: **apply that convention for real, concretely,
to Checkpoint 4** — giving your future self a genuine head start rather
than leaving the convention as a document nobody has actually used yet.

## Before You Start

Confirm the capstone convention exists and is merged:

```bash
cd ~/Projects/Learn-DE
cat sandbox/_templates/CONFIGURATION_CONVENTION.md
```

**No solution is provided.** You're evaluated on real, working scaffolding
and your own design choices — see [`rubric.md`](rubric.md).

## Scenario

Checkpoint 4 (`sandbox/checkpoints/checkpoint_04_api_postgresql/`) is
going to need real configuration the moment you start building it: a
database connection, an API endpoint, a batch size, a retry policy,
storage location, and logging — across dev/test/staging/prod/CI. Build
that configuration scaffolding now, for real, following the convention you
just wrote.

### 1. Format choice

Pick and justify a file format (Lesson 01) for Checkpoint 4's config —
state why, given what you now know about where each format shows up in
this learning path.

### 2. Real `.env.example`

A real `sandbox/checkpoints/checkpoint_04_api_postgresql/.env.example`
matching Checkpoint 4's actual anticipated needs (DB connection, API
credentials, batch size, retry policy, storage path).

### 3. Multi-environment variants

Real `config/base.<ext>`, `config/dev.<ext>`, `config/test.<ext>`,
`config/staging.<ext>`, `config/prod.<ext>`, and `config/ci.<ext>` files
under Checkpoint 4's folder, with an identical schema and genuinely
differing values, per Lesson 03.

### 4. A working layered, validated config loader stub

A real, runnable (even if minimal) config-resolution script implementing
the defaults → file → env → CLI layering and fail-fast schema validation
from Lessons 02 and 04 — it doesn't need to run a real pipeline yet (that's
Checkpoint 4's own future work), but it must actually execute and actually
validate.

### 5. Logging as configuration

`log_level`/`log_format` present as ordinary, validated config values
across the environment variants (Lesson 04's scope — configuration only).

### 6. Dependency-management note

A short, real reference in Checkpoint 4's README pointing back to the
capstone convention's dependency-management decision (Lesson 05) — not a
new decision, just a real, findable link for whoever (you) builds
Checkpoint 4 later.

## Constraints (Safety)

- Everything lands via a real feature branch + PR, per the Repository
  Usage Policy — never a direct commit to `main`.
- No real credentials anywhere — `.env.example` uses placeholders only.
- This assessment scaffolds Checkpoint 4's configuration; it does not
  build Checkpoint 4's actual ingestion pipeline — don't scope-creep into
  Phase 09/Checkpoint 4 work that belongs later.

## Evidence Requirements

For each of the 6 items above, record in `notes/assessment_evidence.md`
(use [`../notes/evidence_template.md`](../notes/evidence_template.md)):
commands used, real output, the real PR URL/description, and a short
explanation of each design choice. Points are awarded for evidence and
understanding — **a completed checklist with no evidence behind it earns
no credit.** See [`rubric.md`](rubric.md).

## When You're Done

- Confirm the scaffolding is merged and Checkpoint 4's README references it.
- Fill in [`../reflection.md`](../reflection.md).
- Self-score using [`rubric.md`](rubric.md) before continuing.
