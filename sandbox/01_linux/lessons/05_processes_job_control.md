# Lesson 05 — Processes & Job Control

**Estimated effort:** Theory ~30 min · Guided practice ~25 min · Independent practice ~20 min

## Why This Matters

Every service, script, and pipeline you'll ever run (Airflow workers, Spark
jobs, a stuck Docker container) is, underneath, just a process. When
something hangs or misbehaves in later phases, "find the process, inspect
it, signal it" is the actual debugging skill — not magic, just this lesson.

## Learning Objectives

- Explain what a process is and how it relates to `/proc`.
- Use `ps`, `top`/`htop` to inspect running processes.
- Send signals with `kill`, understanding what different signals mean.
- Run processes in the foreground/background and manage shell jobs.

## WSL Context

| Aspect | Behavior in WSL2 |
|---|---|
| Process management (`ps`, `kill`, jobs) | Fully normal — this is standard Linux kernel behavior, unaffected by WSL's lack of traditional boot. |
| Visibility | You only see processes running *inside this WSL VM*, not Windows processes (and vice versa) — they're separate process trees. |

## Terminology

| Term | Definition |
|---|---|
| Process | A running instance of a program, identified by a PID (process ID). |
| Parent/child process | Every process (except PID 1) has a parent that started it. |
| Signal | A message sent to a process (e.g., "please terminate," "please stop"). |
| Foreground process | Occupies your terminal; you can't type another command until it finishes (or you background/stop it). |
| Background process | Runs without occupying your terminal (`command &`). |
| Zombie process | A finished process whose exit status hasn't been collected by its parent yet — harmless in small numbers, a sign of a bug if it accumulates. |

## Mental Model

```
PID 1 (systemd, on this WSL setup)
 ├── PID 138  cron
 ├── PID 512  bash (your shell)
 │     └── PID 890  sleep 100   <- a foreground job you started
 └── PID 640  some-other-service
```

Every process has exactly one parent, forming a tree rooted at PID 1. When
a parent dies, its children are "re-parented" (usually to PID 1) rather
than vanishing.

## Theory

`/proc/<pid>/` is a live, kernel-generated view of a running process — its
command line (`/proc/<pid>/cmdline`), environment (`/proc/<pid>/environ`),
open files, and more. Tools like `ps` and `top` are, fundamentally, just
convenient formatters over what's already in `/proc`.

**Signals** are how you communicate with a running process without direct
access to its code:

| Signal | Number | Meaning |
|---|---|---|
| `SIGTERM` | 15 | "Please terminate" (default for `kill`) — the process can catch this and clean up first |
| `SIGKILL` | 9 | "Terminate immediately" — cannot be caught or ignored; the kernel just removes the process |
| `SIGINT` | 2 | What Ctrl+C sends — "interrupt" |
| `SIGSTOP`/`SIGCONT` | 19/18 | Pause/resume a process |

Always try `SIGTERM` (plain `kill <pid>`) before `SIGKILL` (`kill -9 <pid>`)
— `SIGKILL` gives the process no chance to clean up (e.g., close files
safely, flush a log).

## Command Syntax

| Command | Purpose | Common flags |
|---|---|---|
| `ps aux` | List all running processes | `aux` = all users, all processes, detailed |
| `top` / `htop` | Live, updating process view | `htop` is friendlier but not always preinstalled |
| `kill <pid>` | Send a signal (default `SIGTERM`) | `-9` for `SIGKILL`, `-l` to list all signal names |
| `pkill <name>` | Kill by process name instead of PID | `-f` matches full command line |
| `jobs` | List background/stopped jobs in this shell | — |
| `command &` | Run `command` in the background | — |
| `fg` / `bg` | Bring a job to foreground / resume in background | `fg %1` (job number 1) |
| `Ctrl+Z` | Suspend the current foreground process | (keyboard shortcut, not a command) |

## Step-by-Step Example

```bash
$ sleep 300 &
[1] 12345
$ jobs
[1]+  Running                 sleep 300 &

$ ps aux | grep sleep
linhtran   12345  0.0  0.0   2600   512 pts/0    S    10:00   0:00 sleep 300

$ cat /proc/12345/cmdline | tr '\0' ' '
sleep 300

$ kill 12345
$ jobs
[1]+  Terminated              sleep 300

# If a process ignores SIGTERM (rare, but happens):
$ kill -9 12345   # SIGKILL, last resort
```

## Guided Practice

See [`exercises/05_processes_job_control/guided.md`](../exercises/05_processes_job_control/guided.md).

## Common Mistakes

- Reaching for `kill -9` immediately instead of a plain `kill` first — this
  skips the process's chance to shut down cleanly and can leave things
  (like lock files) in a bad state.
- Confusing a job number (`%1`, shown by `jobs`) with a PID (shown by `ps`)
  — `kill %1` and `kill 12345` are both valid but mean different things.
- Forgetting `&` and then being "stuck" in a foreground process — remember
  `Ctrl+Z` then `bg` gets you unstuck without killing it.

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| `kill <pid>` does nothing | Process is ignoring `SIGTERM`, or you have the wrong PID | Confirm with `ps -p <pid>`, then try `kill -9 <pid>` as a last resort |
| Terminal "stuck" after running a command | It's a foreground process still running (or waiting for input) | `Ctrl+Z` to suspend, then `bg` to background it, or `Ctrl+C` to stop it |
| `ps aux` shows a process you don't recognize | Could be a leftover background job from an earlier session | Check its command line (`ps -p <pid> -o cmd=`) before killing anything |

## Knowledge Check

1. **What's the difference between `SIGTERM` and `SIGKILL`?**
   *Answer: `SIGTERM` asks a process to terminate and can be caught for cleanup; `SIGKILL` terminates it immediately with no chance to clean up.*
2. **How do you run a command in the background from the start?**
   *Answer: Append `&` to the command.*
3. **What does `/proc/<pid>/` represent?**
   *Answer: A live, kernel-generated view of that specific process's state (command line, environment, open files, etc.).*

## Completion Checklist

- [ ] You can list running processes and identify one by name or PID.
- [ ] You've started a background job, checked it with `jobs`, and terminated it with plain `kill`.
- [ ] You can explain when `kill -9` is appropriate versus a plain `kill`.

## Reference Materials

- [How an application gets installed and executed in Ubuntu](../../../ref%20roadmap/My%20mentor/BUỔI%202/BÀI%20GIẢNG/HỆ%20ĐIỀU%20HÀNH/LINUX%20OS%20-%20UBUNTU/LESSON%202%20-%20UBUNTU%20-%20Cách%20mà%20một%20ứng%20dụng%20được%20cài%20đặt%20và%20thực%20thi%20trong%20Ubuntu.docx) (context for how a process comes to exist)

## Next

Guided practice: [`exercises/05_processes_job_control/guided.md`](../exercises/05_processes_job_control/guided.md)
Independent exercise: [`exercises/05_processes_job_control/independent.md`](../exercises/05_processes_job_control/independent.md)
Next lesson: [06 — Services & systemd](06_services_systemd.md)
