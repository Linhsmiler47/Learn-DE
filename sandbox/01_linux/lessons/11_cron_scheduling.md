# Lesson 11 — Scheduling with Cron

**Estimated effort:** Theory ~25 min · Guided practice ~25 min · Independent practice ~20 min

## Why This Matters

Cron is the simplest possible answer to "run this on a schedule," and
Phase 17 (Airflow) is explicitly framed, in its own reference material, as
"beyond the cronjob." You need to feel cron's real limitations yourself
before "beyond it" means anything concrete.

## Learning Objectives

- Read and write crontab schedule expressions.
- Schedule a script to run periodically using your user crontab.
- Understand where cron job output goes by default, and how to capture it properly.
- Know what to check if a cron job "works when I run it manually but not on schedule."

## WSL Context

| Aspect | Behavior in WSL2 |
|---|---|
| The `cron` daemon itself | A normal Linux daemon — no WSL-specific quirks once it's running. |
| **Getting it running is the actual WSL issue.** | On native Linux, cron starts automatically at boot and just runs forever. WSL2 doesn't have a traditional boot sequence — if systemd is enabled (see Lesson 06 and Lesson 01's check), `cron.service` can be enabled and will start automatically each time WSL starts. **If systemd is not enabled**, nothing starts cron for you — you'd need to start it manually each WSL session (`sudo service cron start`), and it will not survive a full WSL shutdown/restart on its own. |
| Checking your situation | `systemctl status cron.service` (if systemd is enabled) or `service cron status` (works either way, using the older SysV-style wrapper) tell you whether it's currently running. |

**On the reference machine this course was authored on**, `systemctl status
cron.service` shows it `loaded (... enabled ...)` and `active (running)` —
systemd is enabled here, so cron behaves exactly like native Ubuntu. Check
your own machine before assuming the same.

## Terminology

| Term | Definition |
|---|---|
| Crontab | A per-user (or system-wide) file listing scheduled commands. |
| Cron expression | The 5-field `minute hour day month weekday` schedule syntax. |
| `crontab -e` | Edit your own user's crontab (opens an editor). |
| `crontab -l` | List your current crontab entries. |

## Mental Model

```
 ┌───────────── minute (0–59)
 │ ┌───────────── hour (0–23)
 │ │ ┌───────────── day of month (1–31)
 │ │ │ ┌───────────── month (1–12)
 │ │ │ │ ┌───────────── day of week (0–6, Sunday=0)
 │ │ │ │ │
 * * * * *  command-to-run

 Examples:
 0 2 * * *        -> every day at 2:00 AM
 */15 * * * *     -> every 15 minutes
 0 9 * * 1-5      -> 9:00 AM, Monday through Friday
```

## Theory

Cron jobs run in a **minimal environment** — not your interactive shell's
environment. This is the single most common cron confusion: a script that
"works fine when I run it myself" fails silently under cron because it
depended on a `PATH` entry, environment variable, or working directory that
only exists in your interactive shell (see Lesson 08). The fix is always
the same: make the script self-sufficient — use absolute paths, source
what it needs explicitly, and never assume an interactive `PATH`.

By default, cron emails job output to the user (if mail is configured,
which it usually isn't in a fresh WSL setup) or silently discards it. **Always
redirect output explicitly** so you have something to debug with.

## Command Syntax and Safety Notes

| Command | What it changes | Why elevated permission is required | Risk level | How to verify | How to undo |
|---|---|---|---|---|---|
| `crontab -e` | Edits **your own** user's schedule (`/var/spool/cron/crontabs/<you>`) | No `sudo` needed for your own crontab | **Low** — only affects your own scheduled jobs | `crontab -l` | Remove/comment out the line in `crontab -e` |
| `crontab -l` | Nothing — read-only | No | None | — | — |
| `sudo service cron start` | Starts the cron daemon for the system | Yes — it's a system-wide daemon | **Low** — starting a stopped daemon is safe | `service cron status` | `sudo service cron stop` |

**Rule for this lesson**: only ever edit your **own** user crontab
(`crontab -e`, no `sudo`). Never edit `/etc/crontab` or another user's
crontab as a beginner exercise — user crontabs are sufficient for
everything here and cannot affect other users or system-wide jobs.

## Step-by-Step Example

```bash
# Check cron is actually running first
$ systemctl status cron.service   # or: service cron status

# Prepare a practice script (absolute paths only — no assumptions about PATH)
$ mkdir -p ~/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice
$ cat > ~/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/heartbeat.sh <<'EOF'
#!/bin/bash
echo "$(date '+%Y-%m-%d %H:%M:%S') - heartbeat" >> /home/linhtran/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/heartbeat.log
EOF
$ chmod +x ~/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/heartbeat.sh

# Test it manually first — always do this before trusting cron with it
$ ~/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/heartbeat.sh
$ cat ~/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/heartbeat.log
2026-07-12 16:00:01 - heartbeat

# Schedule it every minute (for fast feedback while learning — not a real-world interval)
$ crontab -e
# add this line, with output explicitly redirected:
*/1 * * * * /home/linhtran/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/heartbeat.sh >> /home/linhtran/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/cron_stdout.log 2>&1

$ crontab -l
*/1 * * * * /home/linhtran/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/heartbeat.sh >> ...

# Wait ~2 minutes, then check
$ tail -f ~/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/heartbeat.log

# Clean up when done practicing
$ crontab -e   # delete the line
$ crontab -l   # confirm it's gone
```

## Guided Practice

See [`exercises/11_cron_scheduling/guided.md`](../exercises/11_cron_scheduling/guided.md).

## Common Mistakes

- Scheduling a script that references a relative path or relies on your
  interactive shell's `PATH`/environment variables — works manually, fails
  under cron.
- Not redirecting stdout/stderr, then having no way to debug why a job
  "didn't seem to run."
- Forgetting that WSL might not have cron running at all if systemd isn't
  enabled — checking `crontab -l` shows the job is *scheduled*, but that
  doesn't mean anything is running it.
- Leaving a `*/1 * * * *` (every-minute) test job in your crontab after
  you're done practicing.

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| Job never runs, but `crontab -l` shows it | cron daemon isn't running | `systemctl status cron.service` or `service cron status`; start it if systemd is enabled, or note this as a WSL limitation for your setup |
| Job runs manually but fails under cron | Missing absolute paths / relied on interactive-only environment variables | Rewrite the script to use full paths everywhere and avoid assuming any `PATH` beyond the absolute basics |
| No log output at all, even the log file's missing | Script itself never ran, or output wasn't redirected | Add `>> logfile 2>&1` explicitly to the crontab line |

## Knowledge Check

1. **What are the five fields in a cron expression, in order?**
   *Answer: minute, hour, day of month, month, day of week.*
2. **Why does a script that "works when I run it manually" sometimes fail under cron?**
   *Answer: Cron runs jobs in a minimal environment, not your interactive shell's environment — scripts relying on interactive `PATH`/env vars or relative paths can fail silently.*
3. **What's the WSL-specific risk with relying on cron for a real schedule?**
   *Answer: Unless systemd is enabled (and cron.service enabled within it), nothing restarts cron automatically when WSL restarts — it may not be running at all without you noticing.*

## Completion Checklist

- [ ] You verified cron is actually running before scheduling anything.
- [ ] You scheduled a script using only absolute paths, with output explicitly redirected.
- [ ] You confirmed the job ran by checking its log/output, not just by trusting `crontab -l`.
- [ ] You removed the practice cron entry when done.

## Reference Materials

- [Cron scheduler in Ubuntu](../../../ref%20roadmap/My%20mentor/BUỔI%202/BÀI%20GIẢNG/HỆ%20ĐIỀU%20HÀNH/LINUX%20OS%20-%20UBUNTU/LESSON%202%20-%20UBUNTU%20-%20Scheduler%20trong%20UBUNTU.docx)
- [Running a script with crontab on Ubuntu](../../../ref%20roadmap/My%20mentor/BUỔI%203/BÀI%20GIẢNG/SCHEDULER/SCHEDULER%20OF%20OS/LESSON%203%20-%20RUN%20SCRIPT%20WITH%20CRONTAB%20-%20UBUNTU.docx)

## Next

Guided practice: [`exercises/11_cron_scheduling/guided.md`](../exercises/11_cron_scheduling/guided.md)
Independent exercise: [`exercises/11_cron_scheduling/independent.md`](../exercises/11_cron_scheduling/independent.md)
Next lesson: [12 — SSH & Basic Networking Commands](12_ssh_networking.md)
