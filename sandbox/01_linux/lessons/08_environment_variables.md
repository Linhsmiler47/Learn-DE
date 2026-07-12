# Lesson 08 — Environment Variables & Shell Configuration

**Estimated effort:** Theory ~25 min · Guided practice ~20 min · Independent practice ~20 min

## Why This Matters

Phase 04 (Configuration) and every checkpoint from Checkpoint 2 onward
depend on environment variables to keep secrets and settings out of code.
This lesson is where that pattern starts — and it's also where "key-value
storage" from the reference material (app config, not just shell config)
lives conceptually.

## Learning Objectives

- Explain what an environment variable is and how it differs from a shell variable.
- Read, set, export, and persist environment variables correctly.
- Understand `PATH` and how the shell finds commands.
- Know where shell configuration lives (`.bashrc`, `.profile`) and when each runs.

## WSL Context

| Aspect | Behavior in WSL2 |
|---|---|
| Environment variables | Work exactly like native Linux. |
| WSL-specific variables | WSL adds a few of its own, e.g. `WSL_DISTRO_NAME`, `WSL_INTEROP` — visible with `env \| grep WSL`. These aren't required knowledge, just good to recognize so they don't look like a mystery. |
| `WSLENV` | An optional, advanced mechanism for sharing specific environment variables between Windows and WSL processes. Not needed for this course — mentioned only so you know it exists if you see it elsewhere. |

## Terminology

| Term | Definition |
|---|---|
| Shell variable | A variable that exists only in your current shell session (e.g., set with `x=5`). |
| Environment variable | A variable exported so that any process your shell starts *inherits* it (set with `export X=5`). |
| `PATH` | An environment variable listing directories the shell searches, in order, when you type a command name. |
| `.bashrc` | Runs for every new *interactive* non-login shell (e.g., each new terminal tab). |
| `.profile` / `.bash_profile` | Runs once for *login* shells. |

## Mental Model

```
Shell variable (x=5)
   │  visible only in this shell
   │
   export x           <- promotes it
   ▼
Environment variable  (now inherited by any command/process this shell starts)
   │
   child process (e.g., python script)
   ▼
os.environ["x"]  in that child process — sees the value
```

`PATH` is just an environment variable containing a colon-separated list:

```
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```

When you type `ls`, the shell checks each of these directories, in order,
for a file named `ls`, and runs the first match.

## Theory

The reference material's "key-value storage" concept for Ubuntu maps
directly onto this lesson: a Linux application's configuration is very
often just environment variables (or a `.env`-style key-value file it
reads at startup) — not a registry (that's Windows) and not a fixed system
API. This is exactly the pattern Phase 04 formalizes for application
configuration, and Phase 09 (Python) will read these values with
`os.environ`.

## Command Syntax

| Command | Purpose | Notes |
|---|---|---|
| `echo $VAR` | Print a variable's value | Empty output means it's unset |
| `export VAR=value` | Set and export an environment variable for this session | Lost when the shell closes unless persisted (see below) |
| `env` / `printenv` | List all current environment variables | `env \| grep NAME` to find one |
| `unset VAR` | Remove a variable | — |
| `which <command>` | Show which `PATH` entry provides a command | — |
| `echo $PATH` | Show your current `PATH` | Read left to right |

**Persisting a variable** across sessions means adding an `export` line to
`~/.bashrc` (for interactive shells) and reloading it with `source ~/.bashrc`.

## Step-by-Step Example

```bash
$ echo $MY_VAR
                      # (empty — not set yet)

$ MY_VAR=hello
$ echo $MY_VAR
hello

$ bash -c 'echo $MY_VAR'
                      # (empty! a plain shell variable isn't inherited)

$ export MY_VAR=hello
$ bash -c 'echo $MY_VAR'
hello                 # now it IS inherited by the child shell

$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

$ which python3
/usr/bin/python3

# Check what WSL itself added to your environment:
$ env | grep WSL
WSL_DISTRO_NAME=Ubuntu
WSL_INTEROP=/run/WSL/442_interop

# Make it permanent (edit ~/.bashrc, don't just append blindly — open it in
# an editor and add the line deliberately):
$ echo 'export MY_VAR=hello' >> ~/.bashrc
$ source ~/.bashrc
$ echo $MY_VAR
hello
```

## Guided Practice

See [`exercises/08_environment_variables/guided.md`](../exercises/08_environment_variables/guided.md).

## Common Mistakes

- Setting a variable without `export` and being confused why a script or
  subprocess doesn't see it.
- Editing `PATH` incorrectly (e.g., `PATH=/some/dir` instead of
  `PATH=/some/dir:$PATH`) — this replaces the entire `PATH`, breaking every
  standard command until you fix it or open a new shell.
- Forgetting to `source ~/.bashrc` after editing it, then wondering why the
  change "didn't work."

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| Variable is empty in a script but set in your shell | It was set but not exported | Use `export VAR=value` |
| "command not found" for something you just installed | Its install directory isn't in `PATH` | Check with `echo $PATH`, add the directory following the safe append pattern above |
| Accidentally broke `PATH` in the current shell | Overwrote it instead of appending | Open a **new** terminal (the broken `PATH` only affects the current shell unless you also broke `.bashrc` permanently) |

## Knowledge Check

1. **What's the difference between a shell variable and an environment variable?**
   *Answer: A shell variable exists only in the current shell; an environment variable (created with `export`) is inherited by any child process the shell starts.*
2. **What does `PATH` actually contain, and how is it used?**
   *Answer: A colon-separated list of directories; the shell searches them in order to find the executable matching a typed command name.*
3. **What's the safe way to add a directory to `PATH` without breaking existing commands?**
   *Answer: `export PATH=/new/dir:$PATH` (prepend/append to the existing value, never overwrite it outright).*

## Completion Checklist

- [ ] You can explain the difference between a shell variable and an environment variable and demonstrate it.
- [ ] You've safely added and then removed a persisted variable in `.bashrc`.
- [ ] You can explain what `PATH` is and locate a command's source directory with `which`.

## Reference Materials

- [How applications and the system store key-value config on Ubuntu](../../../ref%20roadmap/My%20mentor/BUỔI%202/BÀI%20GIẢNG/HỆ%20ĐIỀU%20HÀNH/LINUX%20OS%20-%20UBUNTU/LESSON%202%20-%20UBUNTU%20-%20Cách%20lưu%20trữ%20key-value%20của%20ứng%20dụng%20và%20hệ%20thống%20trên%20Ubuntu.docx) — directly relevant; this lesson formalizes that concept.

## Next

Guided practice: [`exercises/08_environment_variables/guided.md`](../exercises/08_environment_variables/guided.md)
Independent exercise: [`exercises/08_environment_variables/independent.md`](../exercises/08_environment_variables/independent.md)
Next lesson: [09 — Logs & Monitoring](09_logs_monitoring.md)
