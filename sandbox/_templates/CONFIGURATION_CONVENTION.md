# Learn-DE Configuration Convention

## 1. Purpose

This document defines the repository-wide configuration convention for
Learn-DE projects and checkpoints.

Its goals are to ensure that applications:

* use a consistent configuration schema;
* separate configuration from application logic;
* support dev, test, staging, production, and CI environments;
* resolve multiple configuration sources using a documented precedence order;
* keep secrets out of committed configuration files;
* validate the final resolved configuration before pipeline work begins;
* use reproducible dependency management.

This convention is intended to be reused by future phases and checkpoints,
beginning with Checkpoint 4.

---

## 2. Core Principles

### 2.1 One codebase, multiple environments

Development, testing, staging, production, and CI use the same application
code.

Environment differences must be represented through configuration rather
than separate implementations such as:

```text
pipeline_dev.py
pipeline_test.py
pipeline_prod.py
```

The preferred model is:

```text
Same application code
+ environment-specific configuration
+ environment-specific secrets
= environment-specific behavior
```

### 2.2 Configuration is a resolved result

Configuration is not necessarily one file.

The application builds one final configuration by resolving several layers:

```text
Hardcoded defaults
        ↓
Shared base configuration
        ↓
Environment-specific configuration
        ↓
Environment variables
        ↓
CLI arguments
        ↓
Final resolved configuration
        ↓
Validation
        ↓
Pipeline execution
```

### 2.3 Validate once, after resolution

Partial configuration sources must not be validated as though they were
complete configurations.

The application must:

1. load every configuration layer;
2. merge them according to precedence;
3. validate the final resolved configuration once;
4. begin pipeline work only after successful validation.

### 2.4 Secrets are not committed

Secrets such as passwords, API keys, access tokens, and private connection
strings must not be committed to YAML, JSON, TOML, Python source files, or
real `.env` files.

Committed `.env.example` files contain variable names and safe placeholders
only.

---

## 3. Standard Configuration Schema

The following schema is the baseline template for Learn-DE data projects.
Projects may extend it when their workloads require additional sections.

```yaml
environment: dev

database:
  host: localhost
  port: 5432
  name: learn_de
  user: learn_de_user

api:
  base_url: https://api.example.com
  timeout_seconds: 30

storage:
  path: /tmp/learn-de
  format: parquet

pipeline:
  batch_size: 500

retry_policy:
  max_attempts: 3

logging:
  log_level: INFO
  format: json
```

### 3.1 Field definitions

| Path                        | Type    |              Required | Constraint                                |
| --------------------------- | ------- | --------------------: | ----------------------------------------- |
| `environment`               | string  |                   Yes | `dev`, `test`, `staging`, `prod`, or `ci` |
| `database.host`             | string  | When database is used | Non-empty                                 |
| `database.port`             | integer | When database is used | Between 1 and 65535                       |
| `database.name`             | string  | When database is used | Non-empty                                 |
| `database.user`             | string  | When database is used | Non-empty                                 |
| `api.base_url`              | string  |      When API is used | Valid project endpoint                    |
| `api.timeout_seconds`       | integer |      When API is used | Greater than zero                         |
| `storage.path`              | string  |                   Yes | Absolute path or supported URI            |
| `storage.format`            | string  |                   Yes | Project-supported format                  |
| `pipeline.batch_size`       | integer |                   Yes | Positive integer                          |
| `retry_policy.max_attempts` | integer |                   Yes | Between 0 and 10                          |
| `logging.log_level`         | string  |                   Yes | `DEBUG`, `INFO`, `WARNING`, or `ERROR`    |
| `logging.format`            | string  |                   Yes | `text` or `json`                          |

### 3.2 Optional workload-specific sections

Projects may add sections when their workload needs them, for example:

```yaml
schedule:
  cron: "0 2 * * *"

spark:
  executor_count: 4
  executor_memory: 4g

source:
  path: /data/input
  format: csv
```

An unused generic section should not be filled with meaningless placeholder
values merely to preserve a rigid schema.

The stable requirement is that all environments of the same project resolve
to the same project-specific schema.

---

## 4. Recommended File Layout

```text
project/
├── config/
│   ├── base.yaml
│   ├── dev.yaml
│   ├── test.yaml
│   ├── staging.yaml
│   ├── prod.yaml
│   └── ci.yaml
├── .env.example
├── src/
│   └── config.py
├── pyproject.toml
└── uv.lock
```

`base.yaml` contains shared non-secret values.

Environment-specific files contain only values that differ from the shared
base configuration.

Example:

```yaml
# config/base.yaml
database:
  port: 5432
  name: learn_de

pipeline:
  batch_size: 500

retry_policy:
  max_attempts: 3

logging:
  log_level: INFO
  format: json
```

```yaml
# config/dev.yaml
environment: dev

database:
  host: localhost

pipeline:
  batch_size: 100

logging:
  log_level: DEBUG
  format: text
```

```yaml
# config/prod.yaml
environment: prod

database:
  host: prod-db.internal

pipeline:
  batch_size: 5000

retry_policy:
  max_attempts: 5

logging:
  log_level: WARNING
```

---

## 5. Precedence Order

Configuration sources are resolved from lowest to highest priority:

| Priority | Source                      | Typical purpose               |
| -------: | --------------------------- | ----------------------------- |
|        1 | Hardcoded defaults          | Safe application fallback     |
|        2 | `config/base.yaml`          | Shared repository values      |
|        3 | `config/<environment>.yaml` | Environment-specific behavior |
|        4 | Environment variables       | Deployment values and secrets |
|        5 | CLI arguments               | One-run operational overrides |

A higher-priority source overrides a lower-priority source.

Example resolution:

```text
Hardcoded default:       batch_size = 100
base.yaml:               batch_size = 500
prod.yaml:               batch_size = 5000
PIPELINE_BATCH_SIZE:     batch_size = 1000
--batch-size:            batch_size = 250
```

The final resolved value is:

```text
batch_size = 250
```

because the CLI argument has the highest priority.

### 5.1 CLI overrides

CLI overrides should be used for intentional one-run operations such as:

* reduced batch size during an incident;
* controlled backfills;
* temporary debugging;
* selecting a specific input date;
* manually testing a retry boundary.

Permanent environment behavior belongs in reviewed configuration files, not
in undocumented recurring CLI commands.

---

## 6. Environment Variants

### 6.1 What remains fixed

Across dev, test, staging, production, and CI:

* the application code remains the same;
* configuration keys retain the same meaning;
* the final project-specific schema remains the same;
* validation rules remain the same;
* secret names remain stable;
* pipeline stages and business logic remain stable unless explicitly
  controlled by a documented feature flag.

### 6.2 What varies

Environment-specific values may vary when operational requirements differ:

* hostnames and service endpoints;
* database names or schemas;
* storage locations;
* batch sizes;
* retry counts;
* timeouts;
* logging verbosity and format;
* schedule enablement;
* resource sizing;
* secret values and secret providers.

### 6.3 Variant table

| Environment | Purpose                                 | Typical resources                      | Batch/retry behavior                    | Logging                   | Secret source                 |
| ----------- | --------------------------------------- | -------------------------------------- | --------------------------------------- | ------------------------- | ----------------------------- |
| `dev`       | Local development and debugging         | Local services or developer sandbox    | Small batches, low retry count          | `DEBUG`, usually text     | Local `.env`, never committed |
| `test`      | Deterministic automated tests           | Temporary DB, fixtures, mocks          | Very small batches, zero or low retries | `DEBUG` or `INFO`         | Test-only values or mocks     |
| `staging`   | Deployment and integration verification | Staging services resembling production | Production-like but controlled          | `INFO`, usually JSON      | Staging secrets manager       |
| `prod`      | Real workloads                          | Production services and storage        | Throughput-oriented, resilient retries  | `INFO` or `WARNING`, JSON | Production secrets manager    |
| `ci`        | Pull-request and commit validation      | Ephemeral runner services              | Small batches, fail-fast retries        | `INFO`                    | CI secret store               |

Environment files should contain only the values that legitimately differ.

For example, `dev.yaml` should not repeat `database.port: 5432` when that
value is already defined in `base.yaml` and is identical in every
environment.

---

## 7. Environment Variable Contract

The repository template is:

```dotenv
# Runtime environment
APP_ENV=dev

# Database
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=learn_de
DATABASE_USER=learn_de_user
DATABASE_PASSWORD=replace_me

# API
API_BASE_URL=https://api.example.com
API_KEY=replace_me
API_TIMEOUT_SECONDS=30

# Storage
STORAGE_PATH=/tmp/learn-de
STORAGE_FORMAT=parquet

# Pipeline
PIPELINE_BATCH_SIZE=500
PIPELINE_MAX_ATTEMPTS=3

# Logging
LOG_LEVEL=INFO
LOG_FORMAT=json
```

Rules:

1. A real `.env` file must not be committed.
2. `.env.example` must be committed.
3. Placeholder values must not be usable production credentials.
4. Required variable names must match the configuration loader.
5. Numeric environment variables must be converted and validated explicitly.
6. Secrets must not be printed in resolved-config logs.

Recommended `.gitignore` entries:

```gitignore
.env
.env.*
!.env.example
!**/.env.example
```

---

## 8. Validation Contract

Validation must run once after all layers are resolved.

The final configuration should be checked for:

* required keys;
* expected value types;
* non-empty strings;
* allowed values;
* numeric ranges;
* business constraints;
* valid paths or supported URIs where applicable.

Minimum examples:

```text
database.port must be between 1 and 65535
pipeline.batch_size must be a positive integer
retry_policy.max_attempts must be between 0 and 10
logging.log_level must be one of DEBUG, INFO, WARNING, ERROR
logging.format must be one of text, json
```

When validation fails:

* the application prints a clear configuration error;
* the process exits with a non-zero exit code;
* no extraction, transformation, loading, scheduling, or other pipeline work
  begins.

---

## 9. Logging as Configuration

Logging is one configuration section among the other operational settings:

```yaml
logging:
  log_level: INFO
  format: json
```

Recommended usage:

| Environment | Level               | Format           |
| ----------- | ------------------- | ---------------- |
| Development | `DEBUG`             | `text`           |
| Test        | `DEBUG` or `INFO`   | `text`           |
| CI          | `INFO`              | `text` or `json` |
| Staging     | `INFO`              | `json`           |
| Production  | `INFO` or `WARNING` | `json`           |

Secret values, access tokens, passwords, and complete credential-bearing
connection strings must never be written to logs.

---

## 10. Dependency Management

### 10.1 Compared approaches

#### `pip` plus `requirements.txt`

Advantages:

* built into common Python workflows;
* simple and familiar;
* suitable for small exercises.

Limitations:

* a manually maintained requirements file does not by itself distinguish
  direct dependencies from transitive dependencies;
* environment synchronization and lock-file workflows require additional
  conventions or tools.

#### `pip-tools`

Advantages:

* keeps a simple pip-compatible workflow;
* `pip-compile` can generate pinned requirements from declared dependencies;
* `pip-sync` can align an environment with compiled requirements.

Limitations:

* dependency declaration, compilation, environment creation, and Python
  management remain separate concerns;
* compiled output can depend on the Python/platform environment used to
  produce it.

#### Poetry

Advantages:

* manages project metadata, dependencies, virtual environments, packaging,
  and a lock file;
* supports dependency groups and reproducible installation.

Limitations:

* introduces a Poetry-specific workflow and configuration surface;
* packaging behavior may be more than a data-pipeline training repository
  initially requires.

#### `uv`

Advantages:

* uses the standard `pyproject.toml` project model;
* manages project dependencies and virtual environments;
* creates a committed `uv.lock`;
* provides fast dependency resolution and installation;
* supports dependency groups for development and testing;
* can replace several separate environment and package-management commands.

### 10.2 Likely Phase 09 choice

Learn-DE will likely adopt **`uv` in Phase 09**, subject to the Phase 09
instructions being the final source of truth.

The reasons are:

* one tool can manage the project environment and dependencies;
* dependencies can be declared in `pyproject.toml`;
* `uv.lock` supports reproducible installations;
* the workflow is suitable for local development and CI;
* the repository can use concise commands such as:

```bash
uv sync
uv add pyyaml
uv add --dev pytest
uv run pytest
uv run python src/main.py
```

Until Phase 09 formally introduces that workflow, current phase exercises
may continue using the dependency mechanism explicitly required by their
instructions.

---

## 11. Review Requirements for Configuration Changes

Configuration changes are application changes and must be reviewed.

A pull request changing configuration should explain:

* which environments are affected;
* which values changed;
* why the change is needed;
* whether secrets or secret names change;
* how validation was performed;
* any expected operational impact;
* rollback considerations when applicable.

Production values must not be changed through an unrelated pull request.

---

## 12. Adoption Checklist

A Learn-DE project follows this convention when:

* [ ] it has documented defaults;
* [ ] it has a shared base configuration;
* [ ] it has environment-specific overrides where needed;
* [ ] the final schema is consistent across that project's environments;
* [ ] precedence is defaults → base → environment file → environment
  variables → CLI;
* [ ] secrets are supplied externally;
* [ ] a safe `.env.example` is committed;
* [ ] final configuration is validated once;
* [ ] pipeline work begins only after validation succeeds;
* [ ] logging level and format are configurable;
* [ ] dependencies use the phase-approved reproducible workflow;
* [ ] configuration changes are reviewed through Git.
