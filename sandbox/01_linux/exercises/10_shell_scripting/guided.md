# Guided Exercise — Lesson 10: Basic Shell Scripting

## Steps

1. ```bash
   mkdir -p ~/Projects/Learn-DE/sandbox/01_linux/workspace/scripting_practice
   cd ~/Projects/Learn-DE/sandbox/01_linux/workspace/scripting_practice
   cat > greet.sh <<'EOF'
   #!/bin/bash
   set -euo pipefail

   NAME="${1:-}"
   if [ -z "$NAME" ]; then
     echo "Usage: $0 <name>" >&2
     exit 1
   fi

   echo "Hello, $NAME! Today is $(date +%A)."
   exit 0
   EOF
   chmod +x greet.sh
   ```
2. Test both the failure and success paths, checking the exit code each time:
   ```bash
   ./greet.sh
   echo "exit code: $?"
   ./greet.sh "Data Engineer"
   echo "exit code: $?"
   ```

## Evidence to Record

In `notes/lesson_10_evidence.md`: both runs' full output including the
printed exit codes, and an explanation of what `set -euo pipefail` is doing
in this specific script (even though this simple script may not visibly
demonstrate all three flags — explain what each would catch).

## Validation

- The no-argument run must exit with code `1`; the named run must exit with code `0`.

## When You're Done

Move to [`independent.md`](independent.md).
