# Lesson 10 — Basic Shell Scripting

**Estimated effort:** Theory ~35 min · Guided practice ~30 min · Independent practice ~30 min

## Why This Matters

Cron jobs (Lesson 11), custom systemd services (Lesson 06), and countless
small automation tasks in every later phase are just shell scripts. This is
where you stop typing commands one at a time and start automating them.

## Learning Objectives

- Write a bash script with variables, conditionals, loops, and functions.
- Accept and validate command-line arguments.
- Use exit codes correctly so other tools (cron, systemd, CI) can detect failure.
- Make a script executable and run it safely from your practice workspace.

## WSL Context

| Aspect | Behavior in WSL2 |
|---|---|
| Shell scripting | Fully normal — no WSL-specific behavior. |
| Line endings | One real gotcha: if you ever create or edit a script from the Windows side (e.g., Notepad, or a file under `/mnt/c`), it may get Windows-style line endings (`\r\n`), which breaks bash with a cryptic `bad interpreter` error. Always create/edit scripts from within WSL (e.g., using an editor connected to the Linux filesystem) and keep them under `/home/<user>`. |

## Terminology

| Term | Definition |
|---|---|
| Shebang | The `#!/bin/bash` first line telling the OS which interpreter to run the script with. |
| Exit code | A number (0–255) a script/command returns on finish; `0` means success, anything else means some kind of failure. |
| Positional parameter | `$1`, `$2`, etc. — the arguments passed to a script. |
| Conditional | An `if`/`elif`/`else` block controlling flow based on a test. |

## Mental Model

```
#!/bin/bash          <- shebang: "run this with bash"
set -euo pipefail     <- fail fast: stop on error, unset variable, or pipe failure

INPUT_DIR="$1"         <- positional parameter
if [ -z "$INPUT_DIR" ]; then
  echo "Usage: $0 <directory>" >&2
  exit 1                <- non-zero exit code signals failure to whatever called this script
fi

for file in "$INPUT_DIR"/*.txt; do
  echo "Processing $file"
done

exit 0                  <- explicit success
```

## Theory

`set -euo pipefail` at the top of a script is a strong default worth
memorizing:
- `-e`: exit immediately if any command fails (non-zero exit).
- `-u`: treat using an unset variable as an error (catches typos like `$INPTU_DIR`).
- `-o pipefail`: a pipeline (`cmd1 | cmd2`) fails if *any* stage fails, not just the last one.

Without these, bash's default behavior is to keep going after errors —
which is exactly how a data pipeline script silently produces wrong results
instead of failing loudly. This single line previews the "idempotency and
fail loudly, not silently" theme that runs through Phase 12 (ETL) and every
checkpoint afterward.

## Command Syntax

| Construct | Purpose | Example |
|---|---|---|
| `VAR="value"` | Variable assignment (no spaces around `=`) | `NAME="pipeline"` |
| `"$VAR"` | Variable reference (always quote to handle spaces safely) | `echo "$NAME"` |
| `if [ condition ]; then ... fi` | Conditional | `if [ -f "$FILE" ]; then ...` |
| `for x in list; do ... done` | Loop over a list | `for f in *.txt; do ...` |
| `function_name() { ... }` | Function definition | `log() { echo "[$(date)] $1"; }` |
| `$?` | Exit code of the last command | `echo $?` |
| `chmod +x script.sh` | Make a script executable | — |
| `./script.sh arg1` | Run it | — |

## Step-by-Step Example

```bash
$ mkdir -p ~/Projects/Learn-DE/sandbox/01_linux/workspace/scripting_practice
$ cd ~/Projects/Learn-DE/sandbox/01_linux/workspace/scripting_practice

$ cat > greet.sh <<'EOF'
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

$ chmod +x greet.sh
$ ./greet.sh
Usage: ./greet.sh <name>
$ echo $?
1

$ ./greet.sh "Data Engineer"
Hello, Data Engineer! Today is Sunday.
$ echo $?
0
```

## Guided Practice

See [`exercises/10_shell_scripting/guided.md`](../exercises/10_shell_scripting/guided.md).

## Common Mistakes

- Forgetting to quote variables (`$FILE` instead of `"$FILE"`) — breaks on
  filenames with spaces.
- Not setting `set -euo pipefail`, so a failed command partway through the
  script is silently ignored and the script "succeeds" anyway.
- Editing a script from the Windows side and getting `\r\n` line endings,
  producing `bad interpreter: /bin/bash^M: no such file or directory`.
- Forgetting `chmod +x` and then being confused by "Permission denied."

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| `bad interpreter: /bin/bash^M` | Windows-style line endings in the script | Run `sed -i 's/\r$//' script.sh`, or recreate the file entirely from within WSL |
| `Permission denied` running `./script.sh` | Script isn't executable | `chmod +x script.sh` |
| Script "works" but produces wrong output silently | Missing `set -euo pipefail`, an error was swallowed | Add it, re-run, and read the actual error that surfaces |

## Knowledge Check

1. **What does `set -euo pipefail` actually change?**
   *Answer: `-e` exits on any command failure, `-u` errors on unset variables, `-o pipefail` makes a pipeline fail if any stage fails, not just the last.*
2. **What does an exit code of `0` mean, and why does it matter for automation?**
   *Answer: Success. Tools like cron, systemd, and CI use the exit code to decide whether to treat a run as failed and whether to retry/alert.*
3. **Why should scripts always be created/edited from within WSL, not from `/mnt/c`?**
   *Answer: Editing from the Windows side risks Windows-style line endings (`\r\n`), which breaks the shebang interpreter line on Linux.*

## Completion Checklist

- [ ] You've written a script with a shebang, `set -euo pipefail`, at least one conditional, and one loop.
- [ ] Your script validates its arguments and exits non-zero on bad input.
- [ ] You've verified both the success and failure exit codes with `echo $?`.

## Reference Materials

- No direct source in `ref roadmap/` teaches shell scripting as a topic —
  authored fresh. Related later material: [Custom scheduler built in Python](../../../ref%20roadmap/My%20mentor/BUỔI%203/BÀI%20GIẢNG/SCHEDULER/CODE%20TOOL%20SCHEDULER%20CUSTOM%20BASIC/LESSON%203%20-%20CUSTOM%20SCHEDULER%20BẰNG%20PYTHON%20CODE.docx) (Python, not bash, but similar automation mindset — Phase 09 territory).

## Next

Guided practice: [`exercises/10_shell_scripting/guided.md`](../exercises/10_shell_scripting/guided.md)
Independent exercise: [`exercises/10_shell_scripting/independent.md`](../exercises/10_shell_scripting/independent.md)
Next lesson: [11 — Scheduling with Cron](11_cron_scheduling.md)
