# Phase 04 — Configuration Cheatsheet

A consolidated quick-reference across all 5 lessons. Lookup tool, not a
teaching document — see `lessons/` for explanations.

## File Formats (Lesson 01)

| Format | Real tool | Quick syntax check |
|---|---|---|
| YAML | Docker Compose, dbt, GitHub Actions, Kubernetes | `python3 -c "import yaml; yaml.safe_load(open('f.yaml'))"` |
| JSON | Terraform output, REST APIs | `python3 -m json.tool f.json` |
| TOML | `pyproject.toml` | `python3 -c "import tomllib; tomllib.load(open('f.toml','rb'))"` |
| INI | `airflow.cfg` | No standard CLI validator — inspect manually |
| XML | Some enterprise source systems | No standard CLI validator — inspect manually |

## Application Configuration (Lesson 02)

```
Precedence (highest to lowest):
  CLI argument > environment variable > .env file > hardcoded default

Fail fast: missing required config = refuse to start, loudly, immediately.
```

| Anti-pattern | Fix |
|---|---|
| Hardcoded "temporary" value | Externalize immediately |
| Silent default for a required value | No default — fail fast instead |
| Config scattered with no precedence | One documented order |
| Real `.env` committed "just once" | Gitignore from day one; only `.env.example` is committed |
| Same env var parsed differently in different places | One loader function, called once |

## Multi-Environment Configuration & Secrets (Lesson 03)

```
Schema (keys/types)  -> IDENTICAL across dev/test/staging/prod/ci
Values                -> DIFFER across environments
Secrets source        -> local .env (dev/test) vs. secrets manager (staging/prod)
                       -> repository secrets (ci — no persistent filesystem)
```

## Configuration Architecture (Lesson 04)

```
1. Hardcoded defaults
2. config/base.yaml
3. Environment-specific override file
4. Environment variables / .env
5. CLI arguments
        |
        v
Schema validation (ONCE, on the final resolved config)
        |
        v
Validated config passed to the pipeline
```

Logging = ordinary config values (`log_level`, `log_format`), validated
like anything else — not a separate system. Deeper observability is a
later-phase topic.

| Architecture anti-pattern | Fix |
|---|---|
| Config sprawl, no defined precedence | One documented layering order |
| Per-layer validation | Validate once, after full resolution |
| Schema/value drift | One schema definition, referenced everywhere |
| Config changes skip review | Configuration as code — same PR discipline as app code |

## Capstone Convention (Lesson 05)

Reusable artifact: `sandbox/_templates/CONFIGURATION_CONVENTION.md` —
schema template + precedence order + environment variants +
`.env.example` + dependency-management note. First real consumer:
Checkpoint 4.

| Dependency tool | One-line take |
|---|---|
| `requirements.txt` | Simplest, no resolution guarantees |
| `pyproject.toml` (+ pip) | Modern standard metadata, needs a locking tool alongside |
| Poetry | Full resolver + lockfile + venv management |
| `uv` | Newer, very fast; check current adoption before committing |

(Comparison only — Phase 09 implements the actual choice.)
