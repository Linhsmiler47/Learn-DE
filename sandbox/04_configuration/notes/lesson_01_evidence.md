# Lesson 01 Evidence — Configuration File Formats

## Guided Exercise

### Working directory

```bash
~/Projects/Learn-DE/sandbox/04_configuration/workspace/formats_practice
```

---

## 1. YAML Configuration

### File: `pipeline_config.yaml`

```yaml
database:
  host: db.example.internal
  port: 5432
  name: analytics
  username: pipeline_user

api:
  endpoint: https://api.example.com/v1/events
  timeout_seconds: 30

batch_size: 1000

retry_policy:
  max_attempts: 3
  delay_seconds: 5
  backoff_multiplier: 2.0
```

### Validation command

```bash
python3 -c "import yaml; print(yaml.safe_load(open('pipeline_config.yaml')))"
```

### Validation output

```text
{'database': {'host': 'db.example.internal', 'port': 5432, 'name': 'analytics', 'username': 'pipeline_user'}, 'api': {'endpoint': 'https://api.example.com/v1/events', 'timeout_seconds': 30}, 'batch_size': 1000, 'retry_policy': {'max_attempts': 3, 'delay_seconds': 5, 'backoff_multiplier': 2.0}}
```

The YAML file parsed successfully.

---

## 2. JSON Configuration

### File: `pipeline_config.json`

```json
{
  "database": {
    "host": "db.example.internal",
    "port": 5432,
    "name": "analytics",
    "username": "pipeline_user"
  },
  "api": {
    "endpoint": "https://api.example.com/v1/events",
    "timeout_seconds": 30
  },
  "batch_size": 1000,
  "retry_policy": {
    "max_attempts": 3,
    "delay_seconds": 5,
    "backoff_multiplier": 2.0
  }
}
```

### Validation command

```bash
python3 -m json.tool pipeline_config.json
```

### Validation output

```json
{
    "database": {
        "host": "db.example.internal",
        "port": 5432,
        "name": "analytics",
        "username": "pipeline_user"
    },
    "api": {
        "endpoint": "https://api.example.com/v1/events",
        "timeout_seconds": 30
    },
    "batch_size": 1000,
    "retry_policy": {
        "max_attempts": 3,
        "delay_seconds": 5,
        "backoff_multiplier": 2.0
    }
}
```

The JSON file parsed successfully.

---

## 3. TOML Configuration

### File: `pipeline_config.toml`

```toml
batch_size = 1000

[database]
host = "db.example.internal"
port = 5432
name = "analytics"
username = "pipeline_user"

[api]
endpoint = "https://api.example.com/v1/events"
timeout_seconds = 30

[retry_policy]
max_attempts = 3
delay_seconds = 5
backoff_multiplier = 2.0
```

### Validation command

```bash
python3 -c "import tomllib; print(tomllib.load(open('pipeline_config.toml','rb')))"
```

### Validation output

```text
{'batch_size': 1000, 'database': {'host': 'db.example.internal', 'port': 5432, 'name': 'analytics', 'username': 'pipeline_user'}, 'api': {'endpoint': 'https://api.example.com/v1/events', 'timeout_seconds': 30}, 'retry_policy': {'max_attempts': 3, 'delay_seconds': 5, 'backoff_multiplier': 2.0}}
```

The TOML file parsed successfully.

---

## 4. Deliberate YAML Indentation Bug

To test YAML indentation rules, I deliberately changed the `database`
section to the following invalid structure:

```yaml
database:
  host: db.example.internal
 port: 5432
  name: analytics
  username: pipeline_user

api:
  endpoint: https://api.example.com/v1/events
  timeout_seconds: 30

batch_size: 1000

retry_policy:
  max_attempts: 3
  delay_seconds: 5
  backoff_multiplier: 2.0
```

The `port` line had only one leading space. It was therefore not aligned
with the other properties inside `database`.

### Command used to reproduce the error

```bash
python3 -c "import yaml; print(yaml.safe_load(open('pipeline_config.yaml')))"
```

### Error output

```text
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/usr/lib/python3/dist-packages/yaml/__init__.py", line 125, in safe_load
    return load(stream, SafeLoader)
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/yaml/__init__.py", line 81, in load
    return loader.get_single_data()
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/yaml/constructor.py", line 49, in get_single_data
    node = self.get_single_node()
           ^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/yaml/composer.py", line 36, in get_single_node
    document = self.compose_document()
               ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/yaml/composer.py", line 55, in compose_document
    node = self.compose_node(None, None)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/yaml/composer.py", line 84, in compose_node
    node = self.compose_mapping_node(anchor)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/yaml/composer.py", line 127, in compose_mapping_node
    while not self.check_event(MappingEndEvent):
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/yaml/parser.py", line 98, in check_event
    self.current_event = self.state()
                         ^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/yaml/parser.py", line 438, in parse_block_mapping_key
    raise ParserError("while parsing a block mapping", self.marks[-1],
yaml.parser.ParserError: while parsing a block mapping
  in "pipeline_config.yaml", line 1, column 1
expected <block end>, but found '<block mapping start>'
  in "pipeline_config.yaml", line 3, column 2
```

> Note: File paths and some traceback line numbers can differ depending on
> the Python and PyYAML versions installed. The important part of the error
> is that YAML expected the current mapping block to end but encountered a
> new mapping at the incorrect indentation level.

---

## 5. YAML Bug Fix

I fixed the error by adding one more leading space before `port`, making it
aligned with the other fields inside `database`.

### Incorrect YAML

```yaml
database:
  host: db.example.internal
 port: 5432
```

### Corrected YAML

```yaml
database:
  host: db.example.internal
  port: 5432
```

### Full corrected file

```yaml
database:
  host: db.example.internal
  port: 5432
  name: analytics
  username: pipeline_user

api:
  endpoint: https://api.example.com/v1/events
  timeout_seconds: 30

batch_size: 1000

retry_policy:
  max_attempts: 3
  delay_seconds: 5
  backoff_multiplier: 2.0
```

### Validation after the fix

```bash
python3 -c "import yaml; print(yaml.safe_load(open('pipeline_config.yaml')))"
```

### Output after the fix

```text
{'database': {'host': 'db.example.internal', 'port': 5432, 'name': 'analytics', 'username': 'pipeline_user'}, 'api': {'endpoint': 'https://api.example.com/v1/events', 'timeout_seconds': 30}, 'batch_size': 1000, 'retry_policy': {'max_attempts': 3, 'delay_seconds': 5, 'backoff_multiplier': 2.0}}
```

The YAML file parsed successfully after the indentation was corrected.

---

## 6. Comparing the Parsed YAML, JSON, and TOML Data

### File: `compare_configs.py`

```python
import json
import tomllib

import yaml


with open("pipeline_config.yaml", encoding="utf-8") as file:
    yaml_config = yaml.safe_load(file)

with open("pipeline_config.json", encoding="utf-8") as file:
    json_config = json.load(file)

with open("pipeline_config.toml", "rb") as file:
    toml_config = tomllib.load(file)


print("YAML:")
print(yaml_config)

print("\nJSON:")
print(json_config)

print("\nTOML:")
print(toml_config)

print("\nYAML == JSON:", yaml_config == json_config)
print("JSON == TOML:", json_config == toml_config)
print("All configs are identical:", yaml_config == json_config == toml_config)

assert yaml_config == json_config == toml_config

print("\nValidation passed: all three files contain identical data.")
```

### Comparison command

```bash
python3 compare_configs.py
```

### Comparison output

```text
YAML:
{'database': {'host': 'db.example.internal', 'port': 5432, 'name': 'analytics', 'username': 'pipeline_user'}, 'api': {'endpoint': 'https://api.example.com/v1/events', 'timeout_seconds': 30}, 'batch_size': 1000, 'retry_policy': {'max_attempts': 3, 'delay_seconds': 5, 'backoff_multiplier': 2.0}}

JSON:
{'database': {'host': 'db.example.internal', 'port': 5432, 'name': 'analytics', 'username': 'pipeline_user'}, 'api': {'endpoint': 'https://api.example.com/v1/events', 'timeout_seconds': 30}, 'batch_size': 1000, 'retry_policy': {'max_attempts': 3, 'delay_seconds': 5, 'backoff_multiplier': 2.0}}

TOML:
{'batch_size': 1000, 'database': {'host': 'db.example.internal', 'port': 5432, 'name': 'analytics', 'username': 'pipeline_user'}, 'api': {'endpoint': 'https://api.example.com/v1/events', 'timeout_seconds': 30}, 'retry_policy': {'max_attempts': 3, 'delay_seconds': 5, 'backoff_multiplier': 2.0}}

YAML == JSON: True
JSON == TOML: True
All configs are identical: True

Validation passed: all three files contain identical data.
```

Although TOML printed `batch_size` first, dictionary key order did not
affect equality. All three files contained the same keys, nested structures,
values, and data types.

---

# Independent Exercise

## 7. More Complex Pipeline Structure

For the independent exercise, I extended the configuration to contain two
API data sources.

The two API sources have different:

* Names
* Endpoints
* Timeout values
* Maximum retry attempts
* Retry delays
* Backoff multipliers

The intended logical structure is:

```python
{
    "batch_size": 1000,
    "database": {
        "host": "db.example.internal",
        "port": 5432,
        "name": "analytics",
        "username": "pipeline_user"
    },
    "data_sources": {
        "primary": {
            "endpoint": "https://api.example.com/v1/events",
            "timeout_seconds": 30,
            "retry_policy": {
                "max_attempts": 3,
                "delay_seconds": 5,
                "backoff_multiplier": 2.0
            }
        },
        "secondary": {
            "endpoint": "https://backup-api.example.net/v2/metrics",
            "timeout_seconds": 45,
            "retry_policy": {
                "max_attempts": 5,
                "delay_seconds": 10,
                "backoff_multiplier": 1.5
            }
        }
    }
}
```

---

## 8. INI Configuration

### File: `pipeline_config.ini`

```ini
[pipeline]
batch_size = 1000

[database]
host = db.example.internal
port = 5432
name = analytics
username = pipeline_user

[api_primary]
endpoint = https://api.example.com/v1/events
timeout_seconds = 30
retry_max_attempts = 3
retry_delay_seconds = 5
retry_backoff_multiplier = 2.0

[api_secondary]
endpoint = https://backup-api.example.net/v2/metrics
timeout_seconds = 45
retry_max_attempts = 5
retry_delay_seconds = 10
retry_backoff_multiplier = 1.5
```

### Manual inspection

The INI file contains four sections:

```text
[pipeline]
[database]
[api_primary]
[api_secondary]
```

The primary and secondary APIs are represented by separate, specially named
sections.

The primary API contains:

```text
endpoint = https://api.example.com/v1/events
timeout_seconds = 30
retry_max_attempts = 3
retry_delay_seconds = 5
retry_backoff_multiplier = 2.0
```

The secondary API contains:

```text
endpoint = https://backup-api.example.net/v2/metrics
timeout_seconds = 45
retry_max_attempts = 5
retry_delay_seconds = 10
retry_backoff_multiplier = 1.5
```

The values are genuinely different, so the two API sources can be
distinguished clearly.

---

## 9. XML Configuration

### File: `pipeline_config.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<pipeline_config>
  <pipeline>
    <batch_size>1000</batch_size>
  </pipeline>

  <database>
    <host>db.example.internal</host>
    <port>5432</port>
    <name>analytics</name>
    <username>pipeline_user</username>
  </database>

  <data_sources>
    <api name="primary">
      <endpoint>https://api.example.com/v1/events</endpoint>
      <timeout_seconds>30</timeout_seconds>
      <retry_policy>
        <max_attempts>3</max_attempts>
        <delay_seconds>5</delay_seconds>
        <backoff_multiplier>2.0</backoff_multiplier>
      </retry_policy>
    </api>

    <api name="secondary">
      <endpoint>https://backup-api.example.net/v2/metrics</endpoint>
      <timeout_seconds>45</timeout_seconds>
      <retry_policy>
        <max_attempts>5</max_attempts>
        <delay_seconds>10</delay_seconds>
        <backoff_multiplier>1.5</backoff_multiplier>
      </retry_policy>
    </api>
  </data_sources>
</pipeline_config>
```

### Manual inspection

The XML file has one root element:

```xml
<pipeline_config>
```

The two sources are placed inside the same parent element:

```xml
<data_sources>
```

Both sources use the repeated `<api>` element. They are distinguished by
their `name` attributes:

```xml
<api name="primary">
```

```xml
<api name="secondary">
```

Each API has its own nested retry policy:

```xml
<retry_policy>
  <max_attempts>...</max_attempts>
  <delay_seconds>...</delay_seconds>
  <backoff_multiplier>...</backoff_multiplier>
</retry_policy>
```

This structure corresponds directly to two similarly shaped API objects.

---

## 10. INI and XML Comparison

INI was simple to read and convenient for basic key-value settings.
However, it did not naturally support nested data or repeated objects.

To represent two API sources in INI, I had to create two manually named
sections:

```ini
[api_primary]
[api_secondary]
```

I also had to flatten the nested retry policy. Instead of representing a
retry-policy object directly, I created keys such as:

```ini
retry_max_attempts
retry_delay_seconds
retry_backoff_multiplier
```

This naming convention works for a small configuration, but it becomes
harder to maintain when more nested settings or more API sources are added.

Another limitation is that Python's `configparser` generally reads INI
values as strings. The application must explicitly convert numeric fields
using methods such as `getint()` and `getfloat()`.

XML handled the two-source structure more naturally. Both sources could use
the same repeated `<api>` tag, and each source could contain a nested
`<retry_policy>` element. This preserved the hierarchy of the intended data
more clearly than INI.

However, XML was much more verbose. It required opening and closing tags for
every value, which made the configuration longer and visually heavier than
INI, YAML, JSON, or TOML.

For this two-source pipeline:

* INI was shorter and easier to edit for simple values.
* INI required flattened keys and specially named sections.
* XML represented repeated and nested structures more accurately.
* XML was more verbose and required more syntax.
* Both formats were able to represent the same real configuration, but XML
  matched the intended logical structure more directly.

---

## 11. Optional Programmatic Validation of INI and XML

Although the exercise required manual inspection, I also wrote a Python
script to parse both files and convert them into the same normalized
dictionary structure.

### File: `inspect_ini_xml.py`

```python
import configparser
import pprint
import xml.etree.ElementTree as ET


def load_ini(path):
    parser = configparser.ConfigParser()
    loaded_files = parser.read(path, encoding="utf-8")

    if not loaded_files:
        raise FileNotFoundError(f"Could not read INI file: {path}")

    return {
        "batch_size": parser.getint("pipeline", "batch_size"),
        "database": {
            "host": parser.get("database", "host"),
            "port": parser.getint("database", "port"),
            "name": parser.get("database", "name"),
            "username": parser.get("database", "username"),
        },
        "data_sources": {
            "primary": {
                "endpoint": parser.get("api_primary", "endpoint"),
                "timeout_seconds": parser.getint(
                    "api_primary",
                    "timeout_seconds",
                ),
                "retry_policy": {
                    "max_attempts": parser.getint(
                        "api_primary",
                        "retry_max_attempts",
                    ),
                    "delay_seconds": parser.getint(
                        "api_primary",
                        "retry_delay_seconds",
                    ),
                    "backoff_multiplier": parser.getfloat(
                        "api_primary",
                        "retry_backoff_multiplier",
                    ),
                },
            },
            "secondary": {
                "endpoint": parser.get("api_secondary", "endpoint"),
                "timeout_seconds": parser.getint(
                    "api_secondary",
                    "timeout_seconds",
                ),
                "retry_policy": {
                    "max_attempts": parser.getint(
                        "api_secondary",
                        "retry_max_attempts",
                    ),
                    "delay_seconds": parser.getint(
                        "api_secondary",
                        "retry_delay_seconds",
                    ),
                    "backoff_multiplier": parser.getfloat(
                        "api_secondary",
                        "retry_backoff_multiplier",
                    ),
                },
            },
        },
    }


def required_text(parent, path):
    value = parent.findtext(path)

    if value is None:
        raise ValueError(f"Missing required XML element: {path}")

    return value


def load_xml(path):
    root = ET.parse(path).getroot()
    sources = {}

    for api_element in root.findall("./data_sources/api"):
        source_name = api_element.attrib.get("name")

        if not source_name:
            raise ValueError("An API element is missing its name attribute")

        sources[source_name] = {
            "endpoint": required_text(api_element, "endpoint"),
            "timeout_seconds": int(
                required_text(api_element, "timeout_seconds")
            ),
            "retry_policy": {
                "max_attempts": int(
                    required_text(
                        api_element,
                        "./retry_policy/max_attempts",
                    )
                ),
                "delay_seconds": int(
                    required_text(
                        api_element,
                        "./retry_policy/delay_seconds",
                    )
                ),
                "backoff_multiplier": float(
                    required_text(
                        api_element,
                        "./retry_policy/backoff_multiplier",
                    )
                ),
            },
        }

    return {
        "batch_size": int(
            required_text(root, "./pipeline/batch_size")
        ),
        "database": {
            "host": required_text(root, "./database/host"),
            "port": int(
                required_text(root, "./database/port")
            ),
            "name": required_text(root, "./database/name"),
            "username": required_text(root, "./database/username"),
        },
        "data_sources": sources,
    }


ini_config = load_ini("pipeline_config.ini")
xml_config = load_xml("pipeline_config.xml")

print("Parsed INI:")
pprint.pp(ini_config)

print("\nParsed XML:")
pprint.pp(xml_config)

print("\nINI == XML:", ini_config == xml_config)

assert ini_config == xml_config

print("Validation passed: INI and XML represent identical data.")
```

### Validation command

```bash
python3 inspect_ini_xml.py
```

### Validation output

```text
Parsed INI:
{'batch_size': 1000,
 'database': {'host': 'db.example.internal',
              'port': 5432,
              'name': 'analytics',
              'username': 'pipeline_user'},
 'data_sources': {'primary': {'endpoint': 'https://api.example.com/v1/events',
                              'timeout_seconds': 30,
                              'retry_policy': {'max_attempts': 3,
                                               'delay_seconds': 5,
                                               'backoff_multiplier': 2.0}},
                  'secondary': {'endpoint': 'https://backup-api.example.net/v2/metrics',
                                'timeout_seconds': 45,
                                'retry_policy': {'max_attempts': 5,
                                                 'delay_seconds': 10,
                                                 'backoff_multiplier': 1.5}}}}

Parsed XML:
{'batch_size': 1000,
 'database': {'host': 'db.example.internal',
              'port': 5432,
              'name': 'analytics',
              'username': 'pipeline_user'},
 'data_sources': {'primary': {'endpoint': 'https://api.example.com/v1/events',
                              'timeout_seconds': 30,
                              'retry_policy': {'max_attempts': 3,
                                               'delay_seconds': 5,
                                               'backoff_multiplier': 2.0}},
                  'secondary': {'endpoint': 'https://backup-api.example.net/v2/metrics',
                                'timeout_seconds': 45,
                                'retry_policy': {'max_attempts': 5,
                                                 'delay_seconds': 10,
                                                 'backoff_multiplier': 1.5}}}}

INI == XML: True
Validation passed: INI and XML represent identical data.
```

---

## 12. Final Validation Summary

The guided exercise produced three configuration files:

```text
pipeline_config.yaml
pipeline_config.json
pipeline_config.toml
```

All three files:

* Parsed without errors after the YAML indentation fix.
* Contained the same database connection settings.
* Contained the same API endpoint and timeout.
* Contained the same batch size.
* Contained the same retry-policy values.
* Produced equal Python dictionaries.

The comparison result was:

```text
All configs are identical: True
```

The independent exercise produced:

```text
pipeline_config.ini
pipeline_config.xml
```

Both files represented:

* The same database connection.
* The same batch size.
* A primary API source.
* A secondary API source.
* A distinct retry policy for each API source.

The normalized comparison result was:

```text
INI == XML: True
```

Therefore, all configuration files met the requirements of Lesson 01.
