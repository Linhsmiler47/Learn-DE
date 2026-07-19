# Lesson 04 Evidence — Configuration Architecture

## Working Directory

```text
~/Projects/Learn-DE/sandbox/04_configuration/workspace/architecture_practice
```

## Resolution Architecture

The application resolves configuration in the following order:

```text
Hardcoded defaults
        ↓
config/base.yaml
        ↓
Environment-specific YAML
        ↓
Environment variables
        ↓
CLI arguments
        ↓
Final schema validation
        ↓
Pipeline work
```

A layer later in the sequence has higher precedence than a layer earlier in
the sequence.

Therefore, the complete precedence order from highest to lowest is:

```text
CLI arguments
Environment variables
Environment-specific YAML
config/base.yaml
Hardcoded defaults
```

Validation is applied once, after all configuration layers have been
resolved.

---

# Configuration Files

## File: `config/base.yaml`

```yaml
database:
  host: base-db.internal
  port: 5432

pipeline:
  batch_size: 250

retry_policy:
  max_attempts: 3

logging:
  log_level: INFO
```

## File: `config/dev.yaml`

```yaml
database:
  host: localhost

pipeline:
  batch_size: 500

retry_policy:
  max_attempts: 1

logging:
  log_level: DEBUG
```

## File: `config/staging.yaml`

```yaml
database:
  host: staging-db.internal

pipeline:
  batch_size: 1000

retry_policy:
  max_attempts: 4

logging:
  log_level: INFO
```

## File: `config/prod.yaml`

```yaml
database:
  host: prod-db.internal

pipeline:
  batch_size: 2000

retry_policy:
  max_attempts: 5

logging:
  log_level: WARNING
```

---

# Configuration Resolver

## File: `resolve_config.py`

```python
import argparse
import os
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any

import yaml


CONFIG_DIRECTORY = Path(__file__).parent / "config"

ALLOWED_ENVIRONMENTS = {"dev", "staging", "prod"}
ALLOWED_LOG_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}

DEFAULT_CONFIG = {
    "database": {
        "host": "localhost",
        "port": 5432,
    },
    "pipeline": {
        "batch_size": 100,
    },
    "retry_policy": {
        "max_attempts": 2,
    },
    "logging": {
        "log_level": "DEBUG",
    },
}


class ConfigError(Exception):
    """Raised when configuration resolution or validation fails."""


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Resolve layered pipeline configuration."
    )

    parser.add_argument(
        "--environment",
        choices=sorted(ALLOWED_ENVIRONMENTS),
        help="Optional environment-specific configuration to load.",
    )

    parser.add_argument(
        "--database-host",
        help="Override database.host.",
    )

    parser.add_argument(
        "--database-port",
        type=int,
        help="Override database.port.",
    )

    parser.add_argument(
        "--batch-size",
        type=int,
        help="Override pipeline.batch_size.",
    )

    parser.add_argument(
        "--max-attempts",
        type=int,
        help="Override retry_policy.max_attempts.",
    )

    parser.add_argument(
        "--log-level",
        help="Override logging.log_level.",
    )

    parser.add_argument(
        "--show-layers",
        action="store_true",
        help="Print the configuration after each resolution layer.",
    )

    return parser.parse_args()


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise ConfigError(f"Configuration file does not exist: {path}")

    try:
        with path.open(encoding="utf-8") as file:
            data = yaml.safe_load(file)
    except yaml.YAMLError as exc:
        raise ConfigError(f"Invalid YAML in {path}: {exc}") from exc

    if data is None:
        return {}

    if not isinstance(data, dict):
        raise ConfigError(
            f"Configuration file must contain a YAML mapping: {path}"
        )

    return data


def deep_merge(
    original: dict[str, Any],
    override: dict[str, Any],
) -> dict[str, Any]:
    """
    Return a new dictionary where override values replace original values.

    Nested dictionaries are merged recursively.
    """
    result = deepcopy(original)

    for key, override_value in override.items():
        existing_value = result.get(key)

        if isinstance(existing_value, dict) and isinstance(
            override_value,
            dict,
        ):
            result[key] = deep_merge(existing_value, override_value)
        else:
            result[key] = deepcopy(override_value)

    return result


def set_nested_value(
    config: dict[str, Any],
    path: tuple[str, ...],
    value: Any,
) -> None:
    current = config

    for key in path[:-1]:
        if key not in current or not isinstance(current[key], dict):
            current[key] = {}

        current = current[key]

    current[path[-1]] = value


def parse_integer_environment_variable(name: str) -> int | None:
    raw_value = os.getenv(name)

    if raw_value is None:
        return None

    try:
        return int(raw_value)
    except ValueError as exc:
        raise ConfigError(
            f"Environment variable {name} must be an integer; "
            f"received {raw_value!r}"
        ) from exc


def apply_environment_variables(
    config: dict[str, Any],
) -> dict[str, Any]:
    result = deepcopy(config)

    environment_mappings = [
        (
            "PIPELINE_DATABASE_HOST",
            ("database", "host"),
            os.getenv("PIPELINE_DATABASE_HOST"),
        ),
        (
            "PIPELINE_DATABASE_PORT",
            ("database", "port"),
            parse_integer_environment_variable(
                "PIPELINE_DATABASE_PORT"
            ),
        ),
        (
            "PIPELINE_BATCH_SIZE",
            ("pipeline", "batch_size"),
            parse_integer_environment_variable(
                "PIPELINE_BATCH_SIZE"
            ),
        ),
        (
            "PIPELINE_MAX_ATTEMPTS",
            ("retry_policy", "max_attempts"),
            parse_integer_environment_variable(
                "PIPELINE_MAX_ATTEMPTS"
            ),
        ),
        (
            "PIPELINE_LOG_LEVEL",
            ("logging", "log_level"),
            os.getenv("PIPELINE_LOG_LEVEL"),
        ),
    ]

    for variable_name, config_path, value in environment_mappings:
        if value is not None:
            set_nested_value(result, config_path, value)

    return result


def apply_cli_arguments(
    config: dict[str, Any],
    arguments: argparse.Namespace,
) -> dict[str, Any]:
    result = deepcopy(config)

    cli_mappings = [
        (
            ("database", "host"),
            arguments.database_host,
        ),
        (
            ("database", "port"),
            arguments.database_port,
        ),
        (
            ("pipeline", "batch_size"),
            arguments.batch_size,
        ),
        (
            ("retry_policy", "max_attempts"),
            arguments.max_attempts,
        ),
        (
            ("logging", "log_level"),
            arguments.log_level,
        ),
    ]

    for config_path, value in cli_mappings:
        if value is not None:
            set_nested_value(result, config_path, value)

    return result


def require_key(
    config: dict[str, Any],
    path: tuple[str, ...],
) -> Any:
    value: Any = config

    for key in path:
        if not isinstance(value, dict) or key not in value:
            dotted_path = ".".join(path)
            raise ConfigError(
                f"Missing required configuration value: {dotted_path}"
            )

        value = value[key]

    return value


def validate_config(config: dict[str, Any]) -> None:
    """
    Validate the final resolved configuration exactly once.

    No individual resolution layer validates the complete configuration.
    """
    database_host = require_key(config, ("database", "host"))
    database_port = require_key(config, ("database", "port"))
    batch_size = require_key(config, ("pipeline", "batch_size"))
    max_attempts = require_key(
        config,
        ("retry_policy", "max_attempts"),
    )
    log_level = require_key(config, ("logging", "log_level"))

    if not isinstance(database_host, str) or not database_host.strip():
        raise ConfigError(
            "database.host must be a non-empty string"
        )

    if (
        not isinstance(database_port, int)
        or isinstance(database_port, bool)
    ):
        raise ConfigError("database.port must be an integer")

    if not 1 <= database_port <= 65535:
        raise ConfigError(
            "database.port must be between 1 and 65535"
        )

    if not isinstance(batch_size, int) or isinstance(batch_size, bool):
        raise ConfigError("pipeline.batch_size must be an integer")

    if batch_size <= 0:
        raise ConfigError(
            "pipeline.batch_size must be a positive integer"
        )

    if (
        not isinstance(max_attempts, int)
        or isinstance(max_attempts, bool)
    ):
        raise ConfigError(
            "retry_policy.max_attempts must be an integer"
        )

    if not 0 <= max_attempts <= 10:
        raise ConfigError(
            "retry_policy.max_attempts must be between 0 and 10; "
            f"received {max_attempts}"
        )

    if not isinstance(log_level, str):
        raise ConfigError("logging.log_level must be a string")

    normalized_log_level = log_level.upper()

    if normalized_log_level not in ALLOWED_LOG_LEVELS:
        allowed = ", ".join(sorted(ALLOWED_LOG_LEVELS))

        raise ConfigError(
            "logging.log_level must be one of "
            f"{allowed}; received {log_level!r}"
        )

    config["logging"]["log_level"] = normalized_log_level


def print_layer(name: str, config: dict[str, Any]) -> None:
    print(f"\n=== {name} ===")
    print(yaml.safe_dump(config, sort_keys=False).rstrip())


def resolve_config(
    arguments: argparse.Namespace,
) -> dict[str, Any]:
    # Layer 1: hardcoded defaults
    config = deepcopy(DEFAULT_CONFIG)

    if arguments.show_layers:
        print_layer("Layer 1: hardcoded defaults", config)

    # Layer 2: shared base file
    base_config = load_yaml(CONFIG_DIRECTORY / "base.yaml")
    config = deep_merge(config, base_config)

    if arguments.show_layers:
        print_layer("Layer 2: config/base.yaml", config)

    # Layer 3: environment-specific file
    if arguments.environment:
        environment_path = (
            CONFIG_DIRECTORY / f"{arguments.environment}.yaml"
        )
        environment_config = load_yaml(environment_path)
        config = deep_merge(config, environment_config)

        if arguments.show_layers:
            print_layer(
                f"Layer 3: config/{arguments.environment}.yaml",
                config,
            )
    elif arguments.show_layers:
        print("\n=== Layer 3: environment-specific file ===")
        print("Skipped: no --environment supplied")

    # Layer 4: environment variables
    config = apply_environment_variables(config)

    if arguments.show_layers:
        print_layer("Layer 4: environment variables", config)

    # Layer 5: CLI arguments
    config = apply_cli_arguments(config, arguments)

    if arguments.show_layers:
        print_layer("Layer 5: CLI arguments", config)

    # Validation occurs once, after all layers have been resolved.
    validate_config(config)

    return config


def run_pipeline(config: dict[str, Any]) -> None:
    """
    Represent pipeline work.

    This function must only run after configuration validation succeeds.
    """
    print("\nPipeline work started.")
    print(
        "Connecting to "
        f"{config['database']['host']}:"
        f"{config['database']['port']}"
    )
    print(
        f"Batch size: {config['pipeline']['batch_size']}"
    )
    print(
        "Retry attempts: "
        f"{config['retry_policy']['max_attempts']}"
    )
    print(
        f"Log level: {config['logging']['log_level']}"
    )


def main() -> int:
    arguments = parse_arguments()

    try:
        config = resolve_config(arguments)
    except ConfigError as exc:
        print(f"Configuration error: {exc}", file=sys.stderr)
        return 1

    print("\n=== Final validated configuration ===")
    print(yaml.safe_dump(config, sort_keys=False).rstrip())

    run_pipeline(config)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

---

# Guided Exercise Tests

## Test 1 — Hardcoded Defaults Followed by Base File

### Command

```bash
unset PIPELINE_DATABASE_HOST
unset PIPELINE_DATABASE_PORT
unset PIPELINE_BATCH_SIZE
unset PIPELINE_MAX_ATTEMPTS
unset PIPELINE_LOG_LEVEL

python3 resolve_config.py --show-layers
```

### Relevant Output

```text
=== Layer 1: hardcoded defaults ===
database:
  host: localhost
  port: 5432
pipeline:
  batch_size: 100
retry_policy:
  max_attempts: 2
logging:
  log_level: DEBUG

=== Layer 2: config/base.yaml ===
database:
  host: base-db.internal
  port: 5432
pipeline:
  batch_size: 250
retry_policy:
  max_attempts: 3
logging:
  log_level: INFO

=== Layer 3: environment-specific file ===
Skipped: no --environment supplied
```

The `batch_size` value changed from the hardcoded default of `100` to the
base-file value of `250`.

The final value was:

```text
Batch size: 250
```

---

## Test 2 — Environment-Specific File Override

### Command

```bash
python3 resolve_config.py \
  --environment dev \
  --show-layers
```

### Relevant Output

```text
=== Layer 1: hardcoded defaults ===
pipeline:
  batch_size: 100

=== Layer 2: config/base.yaml ===
pipeline:
  batch_size: 250

=== Layer 3: config/dev.yaml ===
pipeline:
  batch_size: 500
```

The development environment file replaced the base value:

```text
100 → 250 → 500
```

The final pipeline output included:

```text
Pipeline work started.
Connecting to localhost:5432
Batch size: 500
Retry attempts: 1
Log level: DEBUG
```

---

## Test 3 — Environment-Variable Override

### Command

```bash
PIPELINE_BATCH_SIZE=750 \
python3 resolve_config.py \
  --environment dev \
  --show-layers
```

### Relevant Output

```text
=== Layer 3: config/dev.yaml ===
pipeline:
  batch_size: 500

=== Layer 4: environment variables ===
pipeline:
  batch_size: 750
```

The environment variable had higher precedence than the development YAML
file:

```text
100 → 250 → 500 → 750
```

The final pipeline output included:

```text
Batch size: 750
```

---

## Test 4 — CLI Override

### Command

```bash
PIPELINE_BATCH_SIZE=750 \
python3 resolve_config.py \
  --environment dev \
  --batch-size 1000 \
  --show-layers
```

### Relevant Output

```text
=== Layer 3: config/dev.yaml ===
pipeline:
  batch_size: 500

=== Layer 4: environment variables ===
pipeline:
  batch_size: 750

=== Layer 5: CLI arguments ===
pipeline:
  batch_size: 1000
```

The complete resolution sequence was:

```text
Hardcoded default: 100
Base YAML:         250
Development YAML:  500
Environment var:   750
CLI argument:      1000
```

The final value was:

```text
Batch size: 1000
```

This confirms that CLI arguments have the highest precedence.

---

# Invalid Log-Level Validation

## Command

```bash
python3 resolve_config.py \
  --environment dev \
  --log-level VERBOSE

echo "Exit code: $?"
```

## Output

```text
Configuration error: logging.log_level must be one of DEBUG, ERROR, INFO, WARNING; received 'VERBOSE'
Exit code: 1
```

The output did not contain:

```text
Pipeline work started.
```

Therefore, the invalid configuration was rejected before pipeline work
began.

---

# Independent Exercise

## Additional Business-Logic Constraint

The resolver requires:

```text
0 <= retry_policy.max_attempts <= 10
```

The validation code is:

```python
if (
    not isinstance(max_attempts, int)
    or isinstance(max_attempts, bool)
):
    raise ConfigError(
        "retry_policy.max_attempts must be an integer"
    )

if not 0 <= max_attempts <= 10:
    raise ConfigError(
        "retry_policy.max_attempts must be between 0 and 10; "
        f"received {max_attempts}"
    )
```

This is a business-rule and range validation, not merely a required-key or
type check.

A retry count greater than 10 could make a failed pipeline wait excessively
and repeatedly call an unavailable external service.

A retry count of zero is allowed because CI or fail-fast workflows may need
to surface the first failure immediately.

---

## Out-of-Range Test

### Command

```bash
python3 resolve_config.py \
  --environment dev \
  --max-attempts 11

echo "Exit code: $?"
```

### Output

```text
Configuration error: retry_policy.max_attempts must be between 0 and 10; received 11
Exit code: 1
```

The pipeline did not begin work.

---

## Valid Upper-Boundary Test

### Command

```bash
python3 resolve_config.py \
  --environment dev \
  --max-attempts 10

echo "Exit code: $?"
```

### Output

```text
=== Final validated configuration ===
database:
  host: localhost
  port: 5432
pipeline:
  batch_size: 500
retry_policy:
  max_attempts: 10
logging:
  log_level: DEBUG

Pipeline work started.
Connecting to localhost:5432
Batch size: 500
Retry attempts: 10
Log level: DEBUG
Exit code: 0
```

The exact upper boundary of `10` was accepted successfully.

---

# Architecture Anti-Pattern Avoided

## Selected Anti-Pattern: Per-Layer Validation

Per-layer validation means validating each source separately while the
configuration is still incomplete.

For example, a poor architecture might:

1. Validate hardcoded defaults.
2. Validate `base.yaml`.
3. Validate `dev.yaml`.
4. Validate environment variables.
5. Validate CLI arguments.

That design is problematic because environment files and CLI arguments are
normally partial overrides.

For example, `config/dev.yaml` does not need to repeat every required key.
It can contain only values that differ:

```yaml
database:
  host: localhost

pipeline:
  batch_size: 500
```

Validating this partial dictionary as a complete configuration would
incorrectly report missing keys such as `database.port` or
`logging.log_level`.

The implementation in `resolve_config.py` structurally prevents per-layer
validation.

The `resolve_config()` function first applies all five layers:

```python
config = deepcopy(DEFAULT_CONFIG)
config = deep_merge(config, base_config)
config = deep_merge(config, environment_config)
config = apply_environment_variables(config)
config = apply_cli_arguments(config, arguments)
```

Only after these operations are complete does it call:

```python
validate_config(config)
```

No call to `validate_config()` appears inside:

```text
load_yaml()
deep_merge()
apply_environment_variables()
apply_cli_arguments()
```

Those functions only load or apply configuration values. They do not try to
validate an incomplete configuration as though it were final.

The application then returns the validated result:

```python
validate_config(config)
return config
```

In `main()`, pipeline work is invoked only after `resolve_config()` returns
successfully:

```python
config = resolve_config(arguments)
run_pipeline(config)
```

When validation raises `ConfigError`, execution moves to the exception
handler:

```python
except ConfigError as exc:
    print(f"Configuration error: {exc}", file=sys.stderr)
    return 1
```

Therefore, `run_pipeline()` is never called when the final configuration is
invalid.

This is not merely a convention documented in comments. The order of
function calls in `resolve_config()` and `main()` structurally enforces the
architecture:

```text
Resolve every layer
        ↓
Validate final configuration once
        ↓
Run pipeline only after success
```

---

# Final Validation Summary

The implementation demonstrated all five configuration layers:

```text
Hardcoded defaults
config/base.yaml
Environment-specific YAML
Environment variables
CLI arguments
```

The `batch_size` value changed through the complete sequence:

```text
100 → 250 → 500 → 750 → 1000
```

This proves that the resolution order operates correctly.

The invalid logging level:

```text
VERBOSE
```

was rejected with a clear error message and exit status `1`.

The independent retry rule rejected:

```text
max_attempts = 11
```

while accepting the upper boundary:

```text
max_attempts = 10
```

The architecture avoids per-layer validation by resolving all configuration
sources first and calling `validate_config()` exactly once before any
pipeline work executes.
