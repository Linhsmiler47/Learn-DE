# Lesson 08 — Environment Variables & Shell Configuration Evidence

## Lesson 08 — Guided Exercise

**Commands used**

```bash
echo $MY_VAR

MY_VAR=hello

echo $MY_VAR

bash -c 'echo $MY_VAR'

export MY_VAR=hello

bash -c 'echo $MY_VAR'

echo $PATH

which python3

env | grep WSL

echo 'export DECLAB_PRACTICE_VAR=hello' >> ~/.bashrc

source ~/.bashrc

echo $DECLAB_PRACTICE_VAR

# Removed the line from ~/.bashrc using nano

source ~/.bashrc

echo $DECLAB_PRACTICE_VAR
```

**Relevant terminal output**

```text
Paste your actual terminal output here.
```

**Validation performed**

I first demonstrated that a normal shell variable is available only in the current shell. After exporting it, a child shell inherited the variable successfully. I then added a practice variable to `.bashrc`, reloaded the configuration, confirmed that it was available, removed the line again, and verified that the variable disappeared after re-sourcing the file.

**Short explanation**

A shell variable exists only in the current shell until it is exported. The `export` command makes the variable part of the environment so child processes inherit it. Variables added to `.bashrc` are recreated whenever Bash loads that configuration file.

**Troubleshooting notes**

---

## Lesson 08 — Independent Exercise

**Script contents**

```bash
#!/usr/bin/env bash

NAME="${NAME:-Developer}"
LEVEL="${LEVEL:-INFO}"
TARGET="${TARGET:-./}"

echo "Hello, $NAME!"
echo "Log level: $LEVEL"
echo "Target directory: $TARGET"
```

**Commands used**

```bash
mkdir -p env_practice

nano env_practice/env_demo.sh

chmod +x env_practice/env_demo.sh

./env_practice/env_demo.sh

NAME=linhtran LEVEL=DEBUG ./env_practice/env_demo.sh

NAME=linhtran LEVEL=ERROR TARGET=/tmp ./env_practice/env_demo.sh
```

**Relevant terminal output**

```text
Paste the output from all three executions here.
```

**Validation performed**

I executed the script without any environment variables and confirmed that all default values defined with `${VAR:-default}` were used. I then ran the script again with two variables set inline and finally with all variables set inline, confirming that the script changed its behavior without modifying the script itself.

**Short explanation**

The script reads its configuration entirely from environment variables. Each variable uses the `${VAR:-default}` pattern so that a sensible default value is used whenever the variable is not provided. This keeps the script configurable without hardcoding environment-specific values.

**Troubleshooting notes**

---
