# Lesson 01 — Configuration File Formats: YAML, JSON, TOML, INI & XML

**Estimated effort:** Theory ~45 min · Guided practice ~40 min · Independent practice ~30 min

## Why This Matters

You cannot avoid these formats in Data Engineering — you can only get fluent
in them or keep guessing at syntax every time. Docker Compose is YAML.
dbt's `dbt_project.yml` and `sources.yml` are YAML. GitHub Actions
workflows are YAML. `pyproject.toml` is TOML. `airflow.cfg` is INI-style.
Terraform can emit JSON. Every one of these appears in this learning path
from Phase 05 onward — this lesson is what makes them all readable on sight.

## Learning Objectives

- Read and write YAML, JSON, TOML, and INI confidently.
- Recognize XML well enough to work with it when a tool requires it.
- Choose the right format for a given tool's config, when you have a choice.
- Represent the same realistic pipeline configuration correctly in each format.

## Terminology

| Term | Definition |
|---|---|
| YAML | "YAML Ain't Markup Language" — indentation-based, human-friendly, supports comments; the most common DE tool config format. |
| JSON | Strict, bracket-based, no comments allowed; the universal data-interchange format, also valid as config. |
| TOML | "Tom's Obvious Minimal Language" — section-based (`[section]`), designed specifically for config files; used by modern Python tooling. |
| INI | Simple `key=value` under `[section]` headers; older but still common (`airflow.cfg`, many legacy tools). |
| XML | Tag-based, verbose; declining in new tools but still required by some enterprise systems. |

## Mental Model

All five formats represent the same underlying idea — nested key/value
data — with different syntax trade-offs:

```
YAML:  readable, supports comments, indentation-sensitive (whitespace bugs are real)
JSON:  strict, no comments, universally parseable, verbose for humans
TOML:  explicit sections, no indentation ambiguity, growing in Python tooling
INI:   simplest, but weak on nested/structured data
XML:   most verbose, strongest for document-shaped (not just data-shaped) content
```

## Theory: The Same Config, Five Ways

A realistic Data Engineering pipeline config — a database connection, an
API endpoint, a batch size, and a retry policy — looks like this in each
format:

**YAML** (what Docker Compose, dbt, and GitHub Actions all use):

```yaml
database:
  host: localhost
  port: 5432
  name: pipeline_db

api:
  endpoint: https://api.example.com/v1/orders
  timeout_seconds: 30

batch_size: 500

retry_policy:
  max_attempts: 3
  backoff_seconds: 5
```

**JSON** (what Terraform can emit, and most REST APIs speak):

```json
{
  "database": { "host": "localhost", "port": 5432, "name": "pipeline_db" },
  "api": { "endpoint": "https://api.example.com/v1/orders", "timeout_seconds": 30 },
  "batch_size": 500,
  "retry_policy": { "max_attempts": 3, "backoff_seconds": 5 }
}
```

**TOML** (what `pyproject.toml` uses — you'll see this again in Phase 09):

```toml
[database]
host = "localhost"
port = 5432
name = "pipeline_db"

[api]
endpoint = "https://api.example.com/v1/orders"
timeout_seconds = 30

batch_size = 500

[retry_policy]
max_attempts = 3
backoff_seconds = 5
```

**INI** (what `airflow.cfg` looks like — note it struggles with nesting):

```ini
[database]
host = localhost
port = 5432
name = pipeline_db

[api]
endpoint = https://api.example.com/v1/orders
timeout_seconds = 30

[retry_policy]
max_attempts = 3
backoff_seconds = 5
; batch_size doesn't belong to any section — INI has no top-level scalars
; convention: put it in a [general] or [defaults] section instead
```

**XML** (verbose, but what some enterprise tools still expect):

```xml
<config>
  <database host="localhost" port="5432" name="pipeline_db"/>
  <api endpoint="https://api.example.com/v1/orders" timeoutSeconds="30"/>
  <batchSize>500</batchSize>
  <retryPolicy maxAttempts="3" backoffSeconds="5"/>
</config>
```

## Command Syntax

| Task | Tool/Approach |
|---|---|
| Validate YAML syntax | `python3 -c "import yaml; yaml.safe_load(open('file.yaml'))"` or a linter |
| Validate JSON syntax | `python3 -m json.tool file.json` |
| Validate TOML syntax | `python3 -c "import tomllib; tomllib.load(open('file.toml','rb'))"` (Python 3.11+) |
| Pretty-print JSON | `cat file.json \| python3 -m json.tool` |

## Where Each Format Actually Shows Up

| Format | Real tool in this learning path |
|---|---|
| YAML | Docker Compose (Phase 05), dbt `dbt_project.yml`/`sources.yml` (Phase 13), GitHub Actions workflows (Phase 02/06), Kubernetes manifests (Phase 08) |
| JSON | Terraform state/JSON output (Phase 07), most REST API payloads (Checkpoint 4) |
| TOML | `pyproject.toml` (Phase 09 — Python packaging) |
| INI | `airflow.cfg` (Phase 17) |
| XML | Less common in this path, but some enterprise source systems (per `ref roadmap/`'s OneDrive/Azure API examples) still use it |

## Guided Practice

See [`exercises/01_configuration_file_formats/guided.md`](../exercises/01_configuration_file_formats/guided.md).

## Common Mistakes

- YAML indentation errors (tabs vs. spaces, inconsistent indent levels) —
  the single most common YAML bug.
- Adding comments to JSON — not supported, will fail to parse.
- Forgetting TOML requires quoted strings (`host = localhost` fails;
  `host = "localhost"` is required).
- Assuming INI supports nested structures the way YAML/JSON/TOML do — it
  doesn't, natively.

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| YAML parses incorrectly or throws an indentation error | Mixed tabs/spaces, or inconsistent indent width | Use a consistent 2-space indent throughout; configure your editor to show whitespace |
| JSON fails to parse | Trailing comma, comment, or unquoted key | JSON is strict — no trailing commas, no comments, all keys quoted |
| TOML value looks like it's the wrong type | Missing quotes around a string, or wrong section nesting | Check the TOML spec's type rules — bare words aren't strings |

## Knowledge Check

1. **Why does YAML cause more real-world bugs than JSON, despite being more readable?**
   *Answer: YAML is indentation-sensitive and whitespace errors (tabs vs. spaces, wrong indent level) are easy to introduce and hard to spot visually.*
2. **Which of these five formats is used by `pyproject.toml`, and where will you see that again?**
   *Answer: TOML — you'll use it directly in Phase 09 for Python packaging/dependency declaration.*
3. **Why does INI struggle with the `batch_size` value in this lesson's example?**
   *Answer: INI has no concept of top-level scalars outside a section — everything must live under a `[section]` heading, so a lone value needs a home section by convention.*

## Completion Checklist

- [ ] You can write the same realistic pipeline config correctly in YAML, JSON, and TOML.
- [ ] You can name which real DE tool in this path uses each format.
- [ ] You can spot a YAML indentation bug on sight.

## Connects to Later Phases

Every tool from Phase 05 onward hands you one of these formats without
asking permission — Docker Compose, dbt, GitHub Actions, Terraform,
Airflow all speak one of these natively, and you now read all of them.

## Reference Materials

No dedicated formats lesson exists in `ref roadmap/` — authored fresh.
Tangential: [PostgreSQL WAL configuration](../../../ref%20roadmap/My%20mentor/BUỔI%204/BÀI%20GIẢNG/LESSON%204%20-%20MAIN%20-%20INCLUDE%20-%20Ý%20nghĩa%20cấu%20hình%20WAL%20trong%20Postgresql.docx) and [Airflow enterprise deployment config](../../../ref%20roadmap/My%20mentor/BUỔI%203/BÀI%20GIẢNG/SCHEDULER/AIRFLOW/LESSON%203%20-%20ADVANCE%20-%20Cấu%20hình%20Airflow%20cho%20việc%20triển%20khai%20trong%20doanh%20nghiệp.docx) are real config examples worth a look, format aside.

## Next

Guided practice: [`exercises/01_configuration_file_formats/guided.md`](../exercises/01_configuration_file_formats/guided.md)
Independent exercise: [`exercises/01_configuration_file_formats/independent.md`](../exercises/01_configuration_file_formats/independent.md)
Next lesson: [02 — Application Configuration](02_application_configuration.md)
