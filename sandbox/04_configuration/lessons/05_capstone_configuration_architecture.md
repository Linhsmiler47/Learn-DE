# Lesson 05 — Capstone: Production-Style Configuration Architecture

**Estimated effort:** Theory ~45 min · Guided practice ~45 min · Independent practice ~40 min

## Why This Matters

Lessons 01–04 taught the pieces. This lesson's job is different: **produce
one real, documented, reusable configuration convention, committed to
`Learn-DE`, that Checkpoint 4 (and every checkpoint after it) will actually
build on** — not a summary of what you learned, an artifact with lasting
engineering value, per the Repository Usage Policy.

## Learning Objectives

- Synthesize file formats (01), application config (02), multi-environment
  handling (03), and architecture (04) into one coherent, documented convention.
- Produce a convention specific enough that Checkpoint 4 can adopt it
  without re-deciding anything, but general enough that Checkpoint 6 and
  Checkpoint 8 can extend it rather than replace it.
- Understand, at an overview level only, the modern Python dependency
  management landscape — enough to make an informed choice later, not to
  implement one now.

## What "Reusable Convention" Means Here

Not a one-off example — a **template and a written standard** that a
future checkpoint can literally copy and fill in. Concretely, this lesson
produces:

1. A documented config schema template (per Lesson 04) with realistic DE
   fields already modeled: database connection, API endpoint, storage
   location, batch size, retry policy, log level.
2. A documented precedence order (per Lesson 02) stated once, referenced everywhere.
3. Documented dev/test/staging/prod/CI variants (per Lesson 03) with an
   explicit statement of what varies and what's fixed.
4. A short, real `.env.example` matching the schema.
5. A brief, honest dependency-management comparison note (see below) —
   comparison only, no tool adopted yet.

This lives in the real repository, in a location future checkpoints can
find and reference — propose the exact location as part of your guided
exercise (a natural fit is alongside the other reusable framework
artifacts already established for this repo).

## Dependency Management: Architectural Overview Only

You will meet `requirements.txt`, `pyproject.toml`, `uv`, and Poetry for
real, hands-on, in **Phase 09 (Python)**. This lesson's scope is strictly
narrower: understand what problem each solves and how they compare, so
your capstone convention can note *which direction* this repository will
likely go, without committing to or implementing any of them yet.

| Tool | What it is | Trade-off, at a glance |
|---|---|---|
| `requirements.txt` | A flat list of package names/versions | Simplest, oldest, no dependency resolution guarantees between installs |
| `pyproject.toml` (with `pip`) | The modern standard packaging metadata file (also where tool config like `black`/`ruff` often lives) | Standardized, but dependency locking still needs another tool layered on top |
| Poetry | A full dependency manager: resolves, locks, and manages virtual environments | Mature, widely used, adds its own workflow on top of `pyproject.toml` |
| `uv` | A newer, very fast dependency manager/resolver, increasingly used alongside or instead of Poetry | Fast-moving tool; check current adoption before committing a real project to it |

Your capstone's dependency-management note should say, in a sentence or
two: which of these this repository will likely adopt in Phase 09, and
why — a decision recorded now, implemented later.

## Guided Practice

See [`exercises/05_capstone_configuration_architecture/guided.md`](../exercises/05_capstone_configuration_architecture/guided.md).

## Common Mistakes

- Writing a convention so specific to one hypothetical use case that
  Checkpoint 6/8 can't reuse it without rewriting it.
- Writing a convention so generic it doesn't actually save Checkpoint 4 any decisions.
- Implementing a dependency-management tool now instead of just comparing them.

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| Unsure if the convention is "reusable enough" | No second scenario tested against it yet | This is exactly what the independent exercise checks — apply it to a second, different hypothetical checkpoint before considering it done |
| Convention feels redundant with Lessons 01–04 | It's meant to be the synthesis, not new content | Reference back to each lesson rather than re-explaining; the value is in the combination and the real, committed template |

## Knowledge Check

1. **What makes a configuration convention "reusable" rather than just "documented"?**
   *Answer: It generalizes past the one scenario it was written for — provably, by successfully applying it to a second, different scenario without rewriting it.*
2. **Why does this lesson only compare dependency-management tools instead of adopting one?**
   *Answer: Tool implementation is Phase 09's job; this phase's scope is the architectural decision, recorded for later, not hands-on tool usage now.*
3. **What are the five pieces this capstone's convention must include?**
   *Answer: A documented schema template, a documented precedence order, documented environment variants, a real `.env.example`, and a brief dependency-management comparison note.*

## Completion Checklist

- [ ] The convention is committed for real to `Learn-DE` via a proper branch + PR.
- [ ] It includes all five required pieces.
- [ ] You've proven it generalizes by applying it to a second hypothetical scenario (the independent exercise).
- [ ] The dependency-management section is a comparison only — no tool implemented.

## Connects to Later Phases

This is not a "connects to" note — this lesson's output **is** what
Checkpoint 4 uses on day one, and what Checkpoint 6 and Checkpoint 8
extend rather than reinvent. Phase 09 implements the dependency-management
choice this lesson only records.

## Reference Materials

No dedicated lesson exists in `ref roadmap/` — authored fresh, synthesizing Lessons 01–04.

## Next

Guided practice: [`exercises/05_capstone_configuration_architecture/guided.md`](../exercises/05_capstone_configuration_architecture/guided.md)
Independent exercise: [`exercises/05_capstone_configuration_architecture/independent.md`](../exercises/05_capstone_configuration_architecture/independent.md)
Next: [`../assessment/README.md`](../assessment/README.md) — the Phase 04 practical assessment.
