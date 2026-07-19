# Lesson 03 Evidence — Multi-Environment Configuration and Secrets

## Working Directory

```text
~/Projects/Learn-DE/sandbox/04_configuration/workspace/multi_env_practice
```

## Configuration Files

The project uses one shared base configuration and five environment-specific
configuration files:

```text
config/base.yaml
config/dev.yaml
config/test.yaml
config/staging.yaml
config/prod.yaml
config/ci.yaml
```

`base.yaml` defines the complete shared configuration and sensible defaults.

Each environment-specific file contains the same override schema. Only the
values change between environments.

---

# Guided Exercise

## 1. Base Configuration

### File: `config/base.yaml`

```yaml
application:
  name: learn-de-pipeline

database:
  host: localhost
  port: 5432
  name: pipeline_db

api:
  base_url: https://api.example.com/v1
  timeout_seconds: 30

pipeline:
  batch_size: 500
  max_retries: 3

logging:
  level: INFO

secrets:
  database_url_variable: DATABASE_URL
  api_key_variable: API_KEY
```

The base configuration contains settings that are shared across
environments.

The shared settings include:

* Application name
* Database port
* Database name
* API base URL
* Default API timeout
* Default batch size
* Default retry count
* Default logging level
* Names of the required secret environment variables

No real secret values are stored in this file.

---

## 2. Development Configuration

### File: `config/dev.yaml`

```yaml
environment: dev

database:
  host: localhost

api:
  timeout_seconds: 30

pipeline:
  batch_size: 100
  max_retries: 1

logging:
  level: DEBUG

secrets:
  source: local_env_file
```

Development uses a local database and a small batch size to make local
execution fast and easy to inspect.

It uses only one retry so that developers can see failures quickly without
waiting through repeated attempts.

The logging level is `DEBUG` to provide detailed diagnostic information.

Development secrets are supplied through a local `.env` file that is not
committed to Git.

---

## 3. Test Configuration

### File: `config/test.yaml`

```yaml
environment: test

database:
  host: test-db

api:
  timeout_seconds: 10

pipeline:
  batch_size: 50
  max_retries: 1

logging:
  level: DEBUG

secrets:
  source: test_environment
```

The test environment uses a separate test database host.

Its batch size is smaller than development because automated tests should
use small, predictable datasets.

Its timeout is shorter than development because tests should fail reasonably
quickly when a dependency does not respond.

The test environment allows one retry to support tests that verify retry
behavior while still avoiding long delays.

---

## 4. Staging Configuration

### File: `config/staging.yaml`

```yaml
environment: staging

database:
  host: staging-db.internal

api:
  timeout_seconds: 30

pipeline:
  batch_size: 500
  max_retries: 3

logging:
  level: INFO

secrets:
  source: secrets_manager
```

Staging is intended to resemble production without using production
resources or credentials.

It uses a larger batch size than development and test.

It uses three retries because temporary service or network failures are
possible in a deployed environment.

The logging level is `INFO`, providing useful operational information
without the volume of debug logging.

Staging secrets are supplied through a managed secrets system.

---

## 5. Production Configuration

### File: `config/prod.yaml`

```yaml
environment: prod

database:
  host: prod-db.internal

api:
  timeout_seconds: 60

pipeline:
  batch_size: 2000
  max_retries: 5

logging:
  level: WARNING

secrets:
  source: secrets_manager
```

Production uses a dedicated internal production database host.

Its batch size is significantly larger than development, test, and staging
because production workloads prioritize throughput.

Production uses five retries to tolerate temporary failures in external
services.

Its logging level is `WARNING` so routine debug and informational messages
do not overwhelm production logs.

Production secrets are retrieved from a managed secrets system and injected
at deployment or runtime.

No production credentials appear in the YAML file.

---

## 6. Secrets Documentation

### File: `SECRETS.md`

# Secrets Management

## Purpose

Configuration files may contain non-sensitive settings such as database
hosts, batch sizes, timeouts, retry counts, and logging levels.

Secrets must not be committed to Git. Examples of secrets include database
passwords, complete authenticated database URLs, API keys, access tokens,
and private credentials.

## Development

In the development environment, secrets are supplied through a local `.env`
file.

Example:

```dotenv
DATABASE_URL=postgresql://dev_user:dev_password@localhost:5432/pipeline_db
API_KEY=local-development-api-key
```

The real `.env` file must be excluded from version control with `.gitignore`.

```gitignore
.env
.env.*
!.env.example
```

A safe `.env.example` file may be committed, but it must contain placeholders
instead of real credentials.

```dotenv
DATABASE_URL=postgresql://user:password@localhost:5432/pipeline_db
API_KEY=replace-with-local-api-key
```

The application reads the values through the environment variable names
defined in `config/base.yaml`:

```yaml
secrets:
  database_url_variable: DATABASE_URL
  api_key_variable: API_KEY
```

## Test

Automated or local tests should use temporary test credentials, mocked
services, or a disposable test database.

Test secrets should be supplied through the test process environment. They
must not reuse production credentials.

## Staging

Staging secrets should be stored in a managed secrets system rather than in
`config/staging.yaml`.

Conceptually, the deployment system retrieves values such as `DATABASE_URL`
and `API_KEY` from a secrets manager and injects them into the staging
application as environment variables.

Possible systems include a cloud secrets manager, a deployment platform's
encrypted secret store, or Kubernetes Secrets integrated with an external
secrets provider.

The YAML file records only that the source is a secrets manager:

```yaml
secrets:
  source: secrets_manager
```

It does not contain the secret values.

## Production

Production secrets must be stored in a managed secrets service with strict
access control, audit logging, rotation policies, and separate permissions
from staging and development.

Production credentials must never be copied into `.env`, committed to Git,
or embedded directly in `config/prod.yaml`.

At deployment time, the production platform retrieves the required secrets
and supplies them as environment variables.

## Continuous Integration

A GitHub Actions runner has no persistent local `.env` file that should be
trusted across workflow runs.

CI secrets are stored as GitHub Actions repository secrets or environment
secrets. A workflow maps those encrypted secrets to environment variables.

Conceptual workflow example:

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    env:
      DATABASE_URL: ${{ secrets.CI_DATABASE_URL }}
      API_KEY: ${{ secrets.CI_API_KEY }}

    steps:
      - uses: actions/checkout@v4
      - run: python3 load_config.py
```

For pull requests from untrusted forks, repository secrets may not be
provided. Tests should therefore be designed to use mocks or disposable
services where possible.

## Rules

1. Never commit real secrets.
2. Keep `.env` files out of Git.
3. Commit only placeholder examples.
4. Use separate credentials for dev, test, CI, staging, and production.
5. Supply staging and production secrets through a managed secrets system.
6. Supply CI secrets through GitHub Actions repository or environment
   secrets.
7. Rotate credentials if they are accidentally exposed.

---

## 7. Guided Schema Comparison

### Command

```bash
python3 -c "
import yaml
dev = yaml.safe_load(open('config/dev.yaml'))
prod = yaml.safe_load(open('config/prod.yaml'))
print('dev keys:', sorted(dev.keys()))
print('prod keys:', sorted(prod.keys()))
print('same schema:', sorted(dev.keys()) == sorted(prod.keys()))
"
```

### Output

```text
dev keys: ['api', 'database', 'environment', 'logging', 'pipeline', 'secrets']
prod keys: ['api', 'database', 'environment', 'logging', 'pipeline', 'secrets']
same schema: True
```

The comparison confirms that development and production use the same
top-level schema.

The values differ meaningfully.

Development uses:

```text
database.host = localhost
pipeline.batch_size = 100
pipeline.max_retries = 1
logging.level = DEBUG
```

Production uses:

```text
database.host = prod-db.internal
pipeline.batch_size = 2000
pipeline.max_retries = 5
logging.level = WARNING
```

Therefore, the differences are not limited to the database hostname.

---

# Independent Exercise

## 8. CI Configuration

### File: `config/ci.yaml`

```yaml
environment: ci

database:
  host: postgres

api:
  timeout_seconds: 5

pipeline:
  batch_size: 20
  max_retries: 0

logging:
  level: INFO

secrets:
  source: github_actions_secrets
```

The CI configuration is intended for a GitHub Actions workflow.

It uses the same schema as development, test, staging, and production, but
several values are deliberately different from the test configuration.

---

## 9. CI Design Reasoning

### Environment name

Test uses:

```yaml
environment: test
```

CI uses:

```yaml
environment: ci
```

This lets logs and diagnostic output identify that the application is
running inside the continuous integration environment rather than a
developer's local test environment.

### Database host

Test uses:

```yaml
database:
  host: test-db
```

CI uses:

```yaml
database:
  host: postgres
```

In GitHub Actions, a PostgreSQL service container can be declared with the
service name `postgres`. Other containers or workflow steps can then refer
to that service by its configured hostname, depending on the workflow
network arrangement.

The CI database is disposable. It is created for the workflow run and is
not a persistent staging or production database.

### API timeout

Test uses:

```yaml
api:
  timeout_seconds: 10
```

CI uses:

```yaml
api:
  timeout_seconds: 5
```

CI has a shorter timeout so unavailable dependencies surface quickly.
A workflow should not spend a long time waiting for a service that is
misconfigured or unavailable.

This is a deliberate departure from test.

### Batch size

Test uses:

```yaml
pipeline:
  batch_size: 50
```

CI uses:

```yaml
pipeline:
  batch_size: 20
```

CI uses a smaller batch because its purpose is to verify correctness, not
production throughput. Smaller batches reduce test setup time and make
failures easier to isolate.

This is another deliberate departure from test.

### Retry count

Test uses:

```yaml
pipeline:
  max_retries: 1
```

CI uses:

```yaml
pipeline:
  max_retries: 0
```

CI disables retries so failures are immediately visible.

A retry can hide flaky behavior by allowing a failed operation to succeed
on a later attempt. For continuous integration, failing immediately makes
unstable tests and broken dependencies easier to detect.

This is a deliberate departure from test and satisfies the requirement that
CI not simply copy `test.yaml`.

### Logging level

Test uses:

```yaml
logging:
  level: DEBUG
```

CI uses:

```yaml
logging:
  level: INFO
```

CI logs must provide enough information to diagnose failures, but excessive
debug output can make workflow logs difficult to read.

`INFO` records important execution events while keeping the GitHub Actions
log reasonably compact.

### Secret source

Test uses:

```yaml
secrets:
  source: test_environment
```

CI uses:

```yaml
secrets:
  source: github_actions_secrets
```

A GitHub Actions runner is temporary and should not depend on a persistent
local `.env` file.

CI secrets would be configured as GitHub Actions repository secrets or
environment secrets, for example:

```text
CI_DATABASE_URL
CI_API_KEY
```

The workflow would expose those encrypted secret values to the application
as environment variables:

```yaml
env:
  DATABASE_URL: ${{ secrets.CI_DATABASE_URL }}
  API_KEY: ${{ secrets.CI_API_KEY }}
```

The secret values would not appear in `config/ci.yaml` or in the Git
repository.

---

## 10. Extended Schema Comparison Script

### File: `compare_schemas.py`

```python
from pathlib import Path

import yaml


CONFIG_DIRECTORY = Path("config")
ENVIRONMENTS = ["dev", "test", "staging", "prod", "ci"]


def load_yaml(path: Path) -> dict:
    with path.open(encoding="utf-8") as file:
        data = yaml.safe_load(file)

    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a YAML mapping")

    return data


def schema_paths(value, prefix=""):
    paths = set()

    if isinstance(value, dict):
        for key, nested_value in value.items():
            path = f"{prefix}.{key}" if prefix else key
            paths.add(path)
            paths.update(schema_paths(nested_value, path))

    return paths


configs = {
    environment: load_yaml(CONFIG_DIRECTORY / f"{environment}.yaml")
    for environment in ENVIRONMENTS
}

reference_environment = "dev"
reference_schema = schema_paths(configs[reference_environment])

print("Top-level keys:")

for environment, config in configs.items():
    print(f"{environment} keys: {sorted(config.keys())}")

print()

all_match = True

for environment, config in configs.items():
    matches = schema_paths(config) == reference_schema
    print(f"{environment} schema matches dev: {matches}")
    all_match = all_match and matches

print()
print("same schema:", all_match)

if not all_match:
    raise SystemExit(1)
```

### Command

```bash
python3 compare_schemas.py
```

### Output

```text
Top-level keys:
dev keys: ['api', 'database', 'environment', 'logging', 'pipeline', 'secrets']
test keys: ['api', 'database', 'environment', 'logging', 'pipeline', 'secrets']
staging keys: ['api', 'database', 'environment', 'logging', 'pipeline', 'secrets']
prod keys: ['api', 'database', 'environment', 'logging', 'pipeline', 'secrets']
ci keys: ['api', 'database', 'environment', 'logging', 'pipeline', 'secrets']

dev schema matches dev: True
test schema matches dev: True
staging schema matches dev: True
prod schema matches dev: True
ci schema matches dev: True

same schema: True
```

This script checks nested schema paths, not only top-level keys.

The output confirms that all environment-specific configurations contain
the same schema.

Only their values and secrets-sourcing approaches differ.

---

## 11. Final Validation Summary

The configuration design contains one shared base configuration and five
environment variants:

```text
base
dev
test
staging
prod
ci
```

Development uses local services, small batches, debug logging, and secrets
from a local `.env` file.

Test uses isolated test resources, short timeouts, small batches, and
temporary test credentials.

Staging resembles production while using separate infrastructure and
secrets.

Production uses larger batches, more retries, less verbose logging, and a
managed secrets system.

CI uses a disposable database, a five-second timeout, a batch size of 20,
zero retries, and secrets supplied through GitHub Actions repository or
environment secrets.

The final schema validation produced:

```text
same schema: True
```

Therefore, all environment variants use the same configuration schema while
providing values appropriate to their individual operating environments.
