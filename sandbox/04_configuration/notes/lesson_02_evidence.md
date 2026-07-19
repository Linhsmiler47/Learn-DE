# Lesson 02 Evidence — Application Configuration

## Working Directory

```text
~/Projects/Learn-DE/sandbox/04_configuration/workspace/config_loader_practice
```

---

# Guided Exercise

## 1. Environment Configuration

### File: `.env.example`

```dotenv
DATABASE_URL=postgresql://user:password@localhost:5432/pipeline_db
API_KEY=your-api-key-here
BATCH_SIZE=250
MAX_RETRIES=3
STORAGE_PATH=/tmp/pipeline-output
```

The example environment file was copied to `.env`:

```bash
cp .env.example .env
```

The environment variables were exported with:

```bash
set -a
source .env
set +a
```

---

## 2. Configuration Loader

### File: `load_config.py`

```python
import os
import sys
from dataclasses import dataclass
from pathlib import Path


class ConfigError(Exception):
    """Raised when application configuration is missing or invalid."""


@dataclass(frozen=True)
class Config:
    database_url: str
    api_key: str
    batch_size: int
    max_retries: int
    storage_path: str


def get_required_env(name: str) -> str:
    """
    Read a required environment variable.

    Raise ConfigError when the variable is missing or contains only
    whitespace.
    """
    value = os.getenv(name)

    if value is None or not value.strip():
        raise ConfigError(
            f"Missing required environment variable: {name}"
        )

    return value.strip()


def get_positive_integer(name: str, default: int) -> int:
    """
    Read an optional positive integer environment variable.

    Use the provided default when the variable is absent.
    """
    raw_value = os.getenv(name)

    if raw_value is None or not raw_value.strip():
        return default

    try:
        value = int(raw_value)
    except ValueError as exc:
        raise ConfigError(
            f"{name} must be an integer, received: {raw_value!r}"
        ) from exc

    if value <= 0:
        raise ConfigError(
            f"{name} must be greater than zero, received: {value}"
        )

    return value


def validate_storage_path(raw_path: str) -> str:
    """
    Require STORAGE_PATH to be an absolute filesystem path.
    """
    path = Path(raw_path)

    if not path.is_absolute():
        raise ConfigError(
            "Invalid STORAGE_PATH: expected an absolute path, "
            f"received: {raw_path!r}"
        )

    return str(path)


def load_config() -> Config:
    """
    Load and validate all application configuration.

    Required values:
    - DATABASE_URL
    - API_KEY
    - STORAGE_PATH

    Optional values with defaults:
    - BATCH_SIZE: defaults to 500
    - MAX_RETRIES: defaults to 3
    """
    database_url = get_required_env("DATABASE_URL")
    api_key = get_required_env("API_KEY")
    storage_path = validate_storage_path(
        get_required_env("STORAGE_PATH")
    )

    batch_size = get_positive_integer("BATCH_SIZE", default=500)
    max_retries = get_positive_integer("MAX_RETRIES", default=3)

    return Config(
        database_url=database_url,
        api_key=api_key,
        batch_size=batch_size,
        max_retries=max_retries,
        storage_path=storage_path,
    )


def main() -> int:
    try:
        config = load_config()
    except ConfigError as exc:
        print(f"Configuration error: {exc}", file=sys.stderr)
        return 1

    print("Configuration loaded successfully.")
    print(f"DATABASE_URL={config.database_url}")
    print(f"API_KEY={config.api_key}")
    print(f"BATCH_SIZE={config.batch_size}")
    print(f"MAX_RETRIES={config.max_retries}")
    print(f"STORAGE_PATH={config.storage_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

The loader uses a custom `ConfigError` exception for expected configuration
problems. The `main()` function catches that exception, prints one clear
error message, and returns exit status `1`. This avoids displaying a generic
Python traceback to the application user.

`DATABASE_URL`, `API_KEY`, and `STORAGE_PATH` are required.

`BATCH_SIZE` and `MAX_RETRIES` are optional. When they are absent, the
loader uses the following defaults:

```text
BATCH_SIZE=500
MAX_RETRIES=3
```

When supplied, both values must be positive integers.

---

## 3. Happy-Path Test

### Command

```bash
set -a
source .env
set +a
python3 load_config.py
```

### Output

```text
Configuration loaded successfully.
DATABASE_URL=postgresql://user:password@localhost:5432/pipeline_db
API_KEY=your-api-key-here
BATCH_SIZE=250
MAX_RETRIES=3
STORAGE_PATH=/tmp/pipeline-output
```

### Result

The loader successfully read all required values from the exported
environment. It also converted `BATCH_SIZE` and `MAX_RETRIES` from strings
into integers.

The process completed successfully with exit status `0`.

---

## 4. Fail-Fast Test for Missing `API_KEY`

### Commands

```bash
unset API_KEY
python3 load_config.py
echo "Exit code: $?"
```

### Output

```text
Configuration error: Missing required environment variable: API_KEY
Exit code: 1
```

### Result

The loader refused to continue because `API_KEY` was not available.

The error message named the missing variable explicitly:

```text
API_KEY
```

The program exited with status `1`, proving that the failure was reported
to the shell as an unsuccessful execution.

The application did not print a generic Python traceback.

After the test, the environment was restored with:

```bash
set -a
source .env
set +a
```

---

## 5. Environment-Variable Precedence Test

### Command

```bash
BATCH_SIZE=1000 python3 load_config.py
```

### Output

```text
Configuration loaded successfully.
DATABASE_URL=postgresql://user:password@localhost:5432/pipeline_db
API_KEY=your-api-key-here
BATCH_SIZE=1000
MAX_RETRIES=3
STORAGE_PATH=/tmp/pipeline-output
```

### Result

The `.env` file contained:

```text
BATCH_SIZE=250
```

However, the inline environment variable supplied to the command was:

```text
BATCH_SIZE=1000
```

The loader printed:

```text
BATCH_SIZE=1000
```

This demonstrates that the inline environment variable had higher
precedence than the previously exported `.env` value.

The override applied only to that command. The shell's original value
remained unchanged:

```bash
echo "$BATCH_SIZE"
```

```text
250
```

---

# Independent Exercise

## 6. New Required Configuration Value

The loader was extended with a new required value:

```text
STORAGE_PATH
```

`STORAGE_PATH` represents the directory path where the pipeline writes its
output.

The chosen validation rule was:

> `STORAGE_PATH` must be present, non-empty, and expressed as an absolute
> filesystem path.

For example, this value is valid:

```text
/tmp/pipeline-output
```

This value is invalid because it is relative:

```text
output/data
```

The relevant validation function is:

```python
def validate_storage_path(raw_path: str) -> str:
    """
    Require STORAGE_PATH to be an absolute filesystem path.
    """
    path = Path(raw_path)

    if not path.is_absolute():
        raise ConfigError(
            "Invalid STORAGE_PATH: expected an absolute path, "
            f"received: {raw_path!r}"
        )

    return str(path)
```

A missing value is detected first by `get_required_env()`.

A present but relative value is detected separately by
`validate_storage_path()`.

Therefore, the missing-value and invalid-value cases produce different
error messages.

---

## 7. Test Case 1 — Valid `STORAGE_PATH`

### Command

```bash
STORAGE_PATH=/tmp/pipeline-output python3 load_config.py
echo "Exit code: $?"
```

### Output

```text
Configuration loaded successfully.
DATABASE_URL=postgresql://user:password@localhost:5432/pipeline_db
API_KEY=your-api-key-here
BATCH_SIZE=250
MAX_RETRIES=3
STORAGE_PATH=/tmp/pipeline-output
Exit code: 0
```

### Result

The supplied storage path was present and absolute.

The configuration loaded successfully, and the process returned exit
status `0`.

---

## 8. Test Case 2 — Missing `STORAGE_PATH`

### Command

```bash
env -u STORAGE_PATH python3 load_config.py
echo "Exit code: $?"
```

### Output

```text
Configuration error: Missing required environment variable: STORAGE_PATH
Exit code: 1
```

### Result

The loader detected that `STORAGE_PATH` was missing.

The failure message clearly identified the missing variable:

```text
Missing required environment variable: STORAGE_PATH
```

The process returned exit status `1`.

---

## 9. Test Case 3 — Present but Invalid `STORAGE_PATH`

### Command

```bash
STORAGE_PATH=output/data python3 load_config.py
echo "Exit code: $?"
```

### Output

```text
Configuration error: Invalid STORAGE_PATH: expected an absolute path, received: 'output/data'
Exit code: 1
```

### Result

The value was present and non-empty, but it was rejected because
`output/data` is a relative path rather than an absolute path.

The failure message clearly explained the validation problem:

```text
Invalid STORAGE_PATH: expected an absolute path, received: 'output/data'
```

The process returned exit status `1`.

This test proves that the new validation catches a plausible-looking but
incorrect value, not only a missing or empty value.

---

## 10. Missing-versus-Invalid Comparison

The missing-value test produced:

```text
Configuration error: Missing required environment variable: STORAGE_PATH
```

The present-but-invalid test produced:

```text
Configuration error: Invalid STORAGE_PATH: expected an absolute path, received: 'output/data'
```

The messages are different because the failures represent different
configuration problems:

* The first value was not supplied at all.
* The second value was supplied but did not satisfy the absolute-path rule.

Both tests exited non-zero and failed before the application attempted to
perform pipeline work.

---

## 11. Final Validation Summary

The guided exercise demonstrated:

* Successful loading of required configuration.
* Default support for optional integer settings.
* Fail-fast behavior when `API_KEY` was missing.
* A clear error message without a Python traceback.
* A non-zero exit status for invalid configuration.
* Inline environment-variable precedence over an exported `.env` value.
* `BATCH_SIZE=1000` winning over `.env`'s `BATCH_SIZE=250`.

The independent exercise demonstrated:

* A new required `STORAGE_PATH` value.
* Validation beyond checking whether the value was empty.
* Successful loading with an absolute path.
* Fail-fast behavior when the value was missing.
* Fail-fast behavior when a relative path was supplied.
* Different messages for missing and invalid values.
* Exit status `0` for valid configuration.
* Exit status `1` for both invalid configurations.

All required Lesson 02 behaviors were demonstrated successfully.
