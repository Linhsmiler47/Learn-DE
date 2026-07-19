# Lesson 03 — Multi-Environment Configuration & Secrets

**Estimated effort:** Theory ~45 min · Guided practice ~40 min · Independent practice ~35 min

## Why This Matters

Lesson 02 answered "how does one instance read its config correctly?"
This lesson answers a different question: **how does the same pipeline
behave correctly in dev, test, staging, and prod — without four separate
codebases, and without dev credentials ever touching prod data?** This is
also where secrets management (Phase 02 L11) grows from "don't commit a
secret" into "manage different real secrets correctly across environments."

## Learning Objectives

- Design dev/test/staging/prod variants of the same pipeline config.
- Decide, explicitly, what must change per environment and what must stay fixed.
- Handle secrets differently per environment (local `.env` in dev vs. a
  secrets-manager reference in staging/prod).
- Explain why CI needs its own environment variant, distinct from all four above.

## Terminology

| Term | Definition |
|---|---|
| Environment | A distinct deployment context (dev, test, staging, prod, CI) with its own config values but the same application logic. |
| Config schema | The fixed *shape* of configuration (which keys exist, what type each is) — this should not change per environment. |
| Config values | The actual data filling that shape — these *do* change per environment. |
| Secrets manager | A dedicated service (conceptually: AWS Secrets Manager, Azure Key Vault, HashiCorp Vault) that stores and serves real credentials, referenced rather than embedded. |

## Mental Model

```
Fixed across every environment (the schema):
  database.host, database.port, database.name, api.endpoint,
  batch_size, retry_policy.max_attempts

Varies per environment (the values):

              dev                 test              staging            prod
DB host       localhost           test-db.internal   staging-db...      prod-db... (managed, cloud)
Batch size    50 (fast iteration) 50                 500                500
Retries       1 (fail fast!)      1                  3                  5
Secrets       local .env          local .env         secrets manager    secrets manager
Log level     DEBUG               DEBUG               INFO               WARNING
```

The **schema stays identical** — that's what makes the pipeline code
itself environment-agnostic. Only the **values**, and *how secrets are
supplied*, change.

## Theory: Secrets Change *How* They're Handled, Not Just *What* They Are

In dev, a local `.env` file (gitignored, per Phase 02 L11) holding a
throwaway local database password is fine — low stakes, fast iteration.
In staging and production, that same *kind* of secret (a database
password) should come from a secrets manager the deployment environment
queries at runtime, never a file sitting on disk or in an environment
variable set by a human. This is why cloud platforms (Phase 24 Azure Key
Vault, Phase 25 AWS Secrets Manager) exist — this lesson previews *why*
they matter before you touch either service for real.

## Theory: Why CI Needs Its Own Variant

CI (Phase 02's GitHub Actions, deepened in Phase 06) isn't dev, isn't test,
isn't prod — it's an ephemeral environment that spins up, runs a pipeline
against disposable/mocked resources, and disappears. It typically needs:
short timeouts (fail fast on a hanging job), its own disposable database
(or none at all, using mocks), and secrets injected as GitHub Actions
repository secrets, not `.env` files at all (there's no persistent
filesystem to keep one on).

## Command Syntax / Config Patterns

| Pattern | Purpose |
|---|---|
| `config/base.yaml` + `config/dev.yaml` + `config/prod.yaml` | Common pattern: shared defaults in `base`, environment-specific overrides layered on top |
| `ENVIRONMENT=staging python3 pipeline.py` | Select which environment's config to load at runtime |
| `.env.dev`, `.env.test` (never `.env.prod` as a file) | Per-environment local files for non-production; production never has a plain-text secrets file |

## Guided Practice

See [`exercises/03_multi_environment_configuration/guided.md`](../exercises/03_multi_environment_configuration/guided.md).

## Common Mistakes

- Letting the config *schema* drift between environments (a key that only
  exists in prod's config) — this means the code paths were never actually
  tested the way prod runs them.
- Using the same low-stakes secret-handling approach (plain `.env`) in
  staging/prod as in dev.
- Forgetting CI needs its own variant and awkwardly reusing "test."
- Retry policies that are *more* aggressive in dev than prod (backwards —
  dev should fail fast to give quick feedback; prod can afford more retries).

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| "Works in dev, breaks in staging" | Config schema or values diverged more than intended, or a secret wasn't provisioned in staging | Diff the environments' config explicitly; confirm the schema is identical |
| CI job hangs | Retry policy or timeout not overridden for CI's disposable/mocked resources | Give CI its own short-timeout, low-retry variant |
| Secret works locally but not in staging | Local `.env` value vs. secrets-manager reference mismatch, or staging secret never provisioned | Confirm the staging environment is actually pulling from its intended secret source |

## Knowledge Check

1. **What should stay identical across dev/test/staging/prod, and what should differ?**
   *Answer: The config schema (keys and types) stays identical; the values (and how secrets are supplied) differ.*
2. **Why shouldn't production secrets live in a `.env` file?**
   *Answer: A plain-text file on disk is a weaker security boundary than a secrets manager queried at runtime — and `.env` files are the exact pattern Phase 02 L11 established as gitignored-but-still-a-file, which is acceptable for low-stakes dev secrets but not for production credentials.*
3. **Why does CI need its own environment variant instead of reusing "test"?**
   *Answer: CI is ephemeral, uses disposable/mocked resources, has no persistent filesystem for a `.env` file, and typically needs shorter timeouts — genuinely different constraints from a persistent test environment.*

## Completion Checklist

- [ ] You've designed at least dev/staging/prod variants of one config with an unchanged schema.
- [ ] You can explain why secrets are handled differently per environment, not just valued differently.
- [ ] You've explained why CI is its own environment, not a rename of "test."

## Connects to Later Phases

Docker Compose's `docker-compose.override.yml` pattern (Phase 05) is this
exact idea implemented for containers. dbt's `profiles.yml` targets
(dev/prod, Phase 13) are this exact idea for a transformation tool.
Terraform's per-environment `.tfvars` (Phase 07) is this exact idea for
infrastructure. Azure Key Vault (Phase 24) and AWS Secrets Manager (Phase
25) are the real secrets-manager services this lesson previews.

## Reference Materials

No dedicated lesson exists in `ref roadmap/` — authored fresh.

## Next

Guided practice: [`exercises/03_multi_environment_configuration/guided.md`](../exercises/03_multi_environment_configuration/guided.md)
Independent exercise: [`exercises/03_multi_environment_configuration/independent.md`](../exercises/03_multi_environment_configuration/independent.md)
Next lesson: [04 — Configuration Architecture](04_configuration_architecture.md)
