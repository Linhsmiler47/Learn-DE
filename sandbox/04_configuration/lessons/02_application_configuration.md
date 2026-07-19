# Lesson 02 — Application Configuration

**Estimated effort:** Theory ~40 min · Guided practice ~35 min · Independent practice ~30 min

## Why This Matters

This lesson answers one question: **how does a single running instance of
your pipeline correctly get its database connection string, API key, batch
size, and retry settings, without any of that being hardcoded?** Every
checkpoint from Checkpoint 4 onward starts exactly here — before an
ingestion script can do anything real, it has to load its own configuration
correctly.

## Learning Objectives

- Use `.env`/`.env.example` correctly (building on Phase 01 L08 and Phase 02 L11).
- Build a config loader with validated required values and sensible defaults.
- Understand and demonstrate configuration precedence.
- Apply the **fail-fast principle** to configuration validation.

## Terminology

| Term | Definition |
|---|---|
| `.env` | Real values for this machine/instance — never committed. |
| `.env.example` | Committed template naming required variables with placeholder values. |
| Precedence | The order in which conflicting config sources are resolved when more than one supplies the same value. |
| Fail fast | Detecting and reporting a configuration problem immediately at startup, loudly, rather than letting the program run partway and fail confusingly later. |

## Theory: Precedence

A realistic pipeline script has (at least) four possible sources for the
same setting, and needs a defined, predictable order among them:

```
CLI argument (--batch-size 1000)     <- highest priority: explicit, this run only
      overrides
Environment variable (BATCH_SIZE=750) <- this machine/session
      overrides
.env file (BATCH_SIZE=500)            <- this project's local default
      overrides
Hardcoded default in code (250)       <- lowest priority: last resort
```

Without a defined precedence, "why did it use that batch size?" becomes an
unanswerable question. With one, it's always traceable.

## Theory: Fail Fast

**Fail fast** means: if `DATABASE_URL` is missing, the pipeline should
refuse to start at all, with a clear error naming exactly what's missing —
not proceed, hit a cryptic connection error three steps into a batch job,
or worse, silently use an empty/`None` value that causes wrong behavior
downstream. The cost of a loud failure at startup is seconds; the cost of
a silent wrong value discovered after a batch job partially completes can
be a real data quality incident. Every config loader in this learning path
validates required values **before** any real work starts.

```python
import os
import sys

def load_config():
    required = ["DATABASE_URL", "API_KEY"]
    missing = [key for key in required if not os.environ.get(key)]
    if missing:
        print(f"FATAL: missing required config: {', '.join(missing)}", file=sys.stderr)
        sys.exit(1)  # fail fast — refuse to proceed at all

    return {
        "database_url": os.environ["DATABASE_URL"],
        "api_key": os.environ["API_KEY"],
        "batch_size": int(os.environ.get("BATCH_SIZE", "250")),
        "max_retries": int(os.environ.get("MAX_RETRIES", "3")),
    }
```

## Command Syntax

| Task | Approach |
|---|---|
| Load `.env` in a shell for testing | `export $(grep -v '^#' .env \| xargs)` (quick and dirty; real apps use a library) |
| Load `.env` in Python | `python-dotenv`'s `load_dotenv()` (mention only — Phase 09 covers Python libraries in depth) |
| Override for one run | `BATCH_SIZE=1000 python3 pipeline.py` |
| Check what's actually set | `env \| grep BATCH_SIZE` |

## Common Configuration Anti-Patterns

| Anti-pattern | Why it's a problem | Do instead |
|---|---|---|
| Hardcoding a value "temporarily" | Temporarily becomes permanently — and it's now scattered through code instead of one place | Externalize from the first line of code that needs it |
| Silent defaults for required values (e.g., defaulting `DATABASE_URL` to an empty string) | Violates fail-fast — the program runs, then fails confusingly downstream | Required values have no default; missing means refuse to start |
| Config values scattered across multiple files with no single source of truth | Nobody can answer "what's the actual batch size right now?" confidently | One documented precedence order, one loader function |
| Committing a real `.env` "just this once" | It's in git history forever, even if deleted next commit (Phase 02 L11) | `.env` is gitignored from day one; only `.env.example` is committed |
| Reading the same environment variable in five different places with five different parsing rules | Inconsistent types/defaults produce inconsistent behavior | One config-loading function, called once, passed down |

## Step-by-Step Example

```bash
$ cat .env.example
DATABASE_URL=postgresql://user:password@localhost:5432/pipeline_db
API_KEY=your-api-key-here
BATCH_SIZE=250
MAX_RETRIES=3

$ cp .env.example .env
# edit .env with real local values

$ python3 -c "
import os
print(os.environ.get('BATCH_SIZE', 'not set'))
"
not set   # .env isn't loaded automatically by the shell

$ export $(grep -v '^#' .env | xargs)
$ python3 -c "import os; print(os.environ.get('BATCH_SIZE'))"
250

$ BATCH_SIZE=1000 python3 -c "import os; print(os.environ.get('BATCH_SIZE'))"
1000   # environment variable override wins for this one run
```

## Guided Practice

See [`exercises/02_application_configuration/guided.md`](../exercises/02_application_configuration/guided.md).

## Common Mistakes

- Defaulting a required value instead of failing fast on it.
- No defined precedence — "it depends which file I edited last" is not an answer.
- Parsing the same env var differently in different parts of the codebase (e.g., `int()` in one place, left as a string in another).

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| Config loader doesn't see `.env` values | `.env` isn't loaded into the shell/process automatically | Use a loading mechanism explicitly (shell `export`, or a library in real code) |
| Wrong value used and you don't know why | No single precedence order, or didn't check higher-priority sources | Trace through your defined precedence order top to bottom |
| Program crashes deep in a batch job instead of at startup | Missing fail-fast validation | Validate all required config before any real work begins |

## Knowledge Check

1. **What does "fail fast" mean for configuration, specifically?**
   *Answer: Detecting and reporting missing/invalid required configuration immediately at startup, loudly, rather than letting the program proceed and fail confusingly later.*
2. **In the precedence order CLI > env var > `.env` > default, which wins if both an env var and a `.env` file set the same value?**
   *Answer: The environment variable — it's higher in the precedence order.*
3. **Why shouldn't a required config value have a silent default?**
   *Answer: It defeats fail-fast — the program would start successfully with an effectively broken configuration and fail unpredictably later instead of immediately.*

## Completion Checklist

- [ ] You've built a config loader that fails fast on a missing required value.
- [ ] You've demonstrated precedence with a real override.
- [ ] You can name at least three configuration anti-patterns without looking them up.

## Connects to Later Phases

This is the literal loader pattern Checkpoint 4's API ingestion pipeline
uses on day one. Docker (Phase 05) passes these same env vars via
`environment:`/`env_file:`; CI/CD (Phase 06) injects them as repository
secrets; Terraform (Phase 07) reads equivalents from `.tfvars`.

## Reference Materials

No dedicated lesson exists in `ref roadmap/` — authored fresh, building on
Phase 01 L08 and Phase 02 L11.

## Next

Guided practice: [`exercises/02_application_configuration/guided.md`](../exercises/02_application_configuration/guided.md)
Independent exercise: [`exercises/02_application_configuration/independent.md`](../exercises/02_application_configuration/independent.md)
Next lesson: [03 — Multi-Environment Configuration & Secrets](03_multi_environment_configuration.md)
