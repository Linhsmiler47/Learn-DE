# Lesson 04 — Configuration Architecture

**Estimated effort:** Theory ~50 min · Guided practice ~40 min · Independent practice ~35 min

## Why This Matters

Lessons 02 and 03 gave you the pieces — a validated loader, environment
variants. This lesson is about the **architecture** that holds those
pieces together as a system: a defined resolution order, a validated
schema, and configuration treated as a first-class design concern rather
than an afterthought scattered across a codebase. This is the level at
which Terraform's `variables.tf`, dbt's `vars`, and Airflow's
Variables/Connections all operate.

## Learning Objectives

- Design a layered configuration resolution architecture (defaults → file → env → CLI).
- Design a config schema with validation that catches bad config before anything runs.
- Understand configuration-as-code as a principle, not just a syntax choice.
- Configure logging as **one deliberate piece** of this architecture — not the focus of the lesson.
- Recognize architecture-level configuration anti-patterns.

## Terminology

| Term | Definition |
|---|---|
| Layered configuration | Multiple sources resolved in a defined order into one final, unambiguous config. |
| Schema validation | Checking that config values match expected types/constraints *before* the program uses them. |
| Configuration as code | Treating config the same way you treat application code: versioned, reviewed, tested — not edited ad hoc on a server. |

## Mental Model: The Full Layered Architecture

```
┌─────────────────────────────────────────┐
│ 1. Hardcoded defaults (in code)          │  lowest priority
├─────────────────────────────────────────┤
│ 2. Config file (config/base.yaml)        │
├─────────────────────────────────────────┤
│ 3. Environment-specific file/override    │  (Lesson 03's dev/test/staging/prod)
├─────────────────────────────────────────┤
│ 4. Environment variables / .env          │  (Lesson 02)
├─────────────────────────────────────────┤
│ 5. CLI arguments                         │  highest priority — this run only
└─────────────────────────────────────────┘
                    │
                    ▼
        ┌───────────────────────┐
        │  Schema validation     │  <- fail fast (Lesson 02) applied
        │  (types, required,     │     to the FINAL resolved config,
        │   allowed values)       │     not each layer individually
        └───────────────────────┘
                    │
                    ▼
           Final, validated config
           passed into the pipeline
```

Validation happens **once, after all layers are resolved** — not per
layer. Validating each layer separately would let an invalid default slip
through if a later layer happens to override it; validating only the
final result is both simpler and more correct.

## Theory: Schema Design

A config schema should specify, for every key: its type, whether it's
required, and (where relevant) an allowed set of values:

```
database.host      : string, required
database.port       : integer, required, default 5432
batch_size          : integer, optional, default 250, must be > 0
retry_policy.max_attempts : integer, optional, default 3, must be 0-10
log_level           : string, optional, default "INFO", must be one of [DEBUG, INFO, WARNING, ERROR]
```

This is exactly what Terraform's `variables.tf` type constraints and
dbt's `vars` validation aim to do for their own domains — you're learning
the general pattern once here, and you'll recognize it in both tools later.

## Logging: One Piece of This Architecture (Not the Focus)

Logging configuration belongs in this same layered system: `log_level`
and `log_format` are just more config values, resolved through the same
precedence, validated against the same kind of allowed-values constraint
(`log_level` must be one of a fixed set). That's the entire scope of
logging in this phase — **what** gets configured, not deep structured
logging design, log aggregation, or observability tooling, which belong to
later phases (data quality/observability work resumes this topic in depth
well beyond Phase 04).

```yaml
logging:
  level: INFO       # DEBUG in dev, WARNING in prod — an environment-specific value (Lesson 03)
  format: json       # a schema choice, validated like any other config value
```

## Architecture-Level Anti-Patterns

(Complementing Lesson 02's application-level anti-patterns — these are
about the *system*, not a single loader function.)

| Anti-pattern | Why it's a problem | Do instead |
|---|---|---|
| Config sprawl — settings scattered across many files with no defined precedence between them | Nobody can predict which file "wins," and the answer may differ per environment | One documented, consistent layering order, applied everywhere |
| Validating each config source separately instead of the final resolved result | A bad default can slip through if a later layer happens to override it during testing but not always | Validate once, after full resolution |
| Mixing schema definition with values (e.g., hardcoding allowed `log_level` values in three different places) | Schema drift — the "rules" and the "data" get out of sync | One schema definition, referenced everywhere values are validated |
| Treating config changes as exempt from review ("it's just config") | Config changes break production as often as code changes do | Configuration as code: versioned, reviewed via PR, same as Phase 02's discipline |

## Guided Practice

See [`exercises/04_configuration_architecture/guided.md`](../exercises/04_configuration_architecture/guided.md).

## Common Mistakes

- Validating too early (per-layer) or too late (after the pipeline has
  already started doing real work).
- Treating logging configuration as a separate, disconnected system instead
  of part of the same layered config.
- Skipping PR review for "just a config change."

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| Final config doesn't match any single source you can find | Layers resolved in an order you didn't expect | Trace top-to-bottom through your documented precedence, checking each layer's actual value |
| Validation passes but the pipeline still misbehaves | Validation checked structure/type but not a business-logic constraint (e.g., `max_attempts` is a valid integer but nonsensically large) | Add the missing constraint to the schema, not a one-off check buried in application code |

## Knowledge Check

1. **Why validate the final resolved config instead of each layer separately?**
   *Answer: Validating only the final result guarantees correctness regardless of which layer supplied which value; per-layer validation can miss a bad value that gets overridden in some paths but not others.*
2. **What's in scope for "logging" in this phase, and what isn't?**
   *Answer: In scope: log level and format as configuration values, resolved and validated like any other config. Out of scope: structured logging design, aggregation, and observability tooling — later phases.*
3. **What does "configuration as code" mean as a principle?**
   *Answer: Config changes are versioned, reviewed, and tested the same way application code changes are — not edited ad hoc outside that discipline.*

## Completion Checklist

- [ ] You've built a layered resolution architecture with validation applied once, at the end.
- [ ] You've included `log_level`/`log_format` as ordinary, validated config values.
- [ ] You can name at least two architecture-level anti-patterns distinct from Lesson 02's application-level ones.

## Connects to Later Phases

Terraform's `variables.tf` (Phase 07) and dbt's `vars` (Phase 13) are this
same layered-and-validated architecture in tool-specific form. Airflow's
Variables/Connections (Phase 17) are config-as-code applied to
orchestration. This lesson is the general pattern every one of those tools
turns out to already assume you know.

## Reference Materials

No dedicated lesson exists in `ref roadmap/` — authored fresh.

## Next

Guided practice: [`exercises/04_configuration_architecture/guided.md`](../exercises/04_configuration_architecture/guided.md)
Independent exercise: [`exercises/04_configuration_architecture/independent.md`](../exercises/04_configuration_architecture/independent.md)
Next: [05 — Capstone: Production-Style Configuration Architecture](05_capstone_configuration_architecture.md)
