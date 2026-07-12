# Lesson 09 — Logs & Monitoring

**Estimated effort:** Theory ~25 min · Guided practice ~25 min · Independent practice ~20 min

## Why This Matters

When a pipeline fails at 2am in a later phase, logs are the only evidence
you'll have. Knowing where logs live and how to read them live (not just
after the fact) is a direct prerequisite for the "Debug" step in every
lesson's — and every checkpoint's — learning cycle.

## Learning Objectives

- Locate and read plain-file logs under `/var/log`.
- Use `journalctl` to query systemd's structured logs (when available).
- Follow a log in real time and filter it usefully.
- Know which approach to use depending on whether your WSL has systemd enabled.

## WSL Context

| Aspect | Behavior in WSL2 |
|---|---|
| `/var/log/*.log` files | Always work, systemd or not — these are just plain text files. |
| `journalctl` | **Requires systemd to be running as PID 1.** If your `ps -p 1 -o comm=` (Lesson 01) showed `systemd`, this works fully, including `journalctl -u <service>` and `journalctl -f`. If it showed something else, `journalctl` will error — fall back to reading `/var/log/` files directly and use `tail -f` instead of `journalctl -f`. |

Both paths are taught below so this lesson works either way.

## Terminology

| Term | Definition |
|---|---|
| Log rotation | The practice of archiving/compressing old logs and starting fresh ones, so logs don't grow forever. |
| `journalctl` | The command-line tool for querying systemd's structured journal. |
| Journal | systemd's centralized, binary log store (as opposed to plain text files in `/var/log`). |
| Following a log | Watching new lines appear in real time (`tail -f` or `journalctl -f`). |

## Mental Model

```
                          Two log worlds, pick based on Lesson 01's check:

  systemd enabled                          systemd NOT enabled (or plain files)
  ────────────────                         ──────────────────────────────────
  journalctl                               /var/log/syslog
  journalctl -u <service>                  /var/log/<app>/<app>.log
  journalctl -f  (follow)                  tail -f /var/log/<app>/<app>.log
  journalctl --since "1 hour ago"          grep + timestamps in the file itself
```

Many services write to **both** — systemd captures their stdout/stderr into
the journal even while the application also writes its own log file. Don't
be surprised to find the same information in two places.

## Theory

`/var/log` is the traditional, universal location — plain text files,
readable with any text tool, and the fallback that always works regardless
of your init system. `journalctl` is systemd's newer, richer alternative:
structured, filterable by service/time/priority, and it also captures
output from services that don't write their own log files at all. Both
matter because you'll meet both across different tools in later phases
(some write only to their own log file, some rely entirely on the journal).

## Command Syntax

| Command | Purpose | Common flags |
|---|---|---|
| `tail -f <file>` | Follow a log file in real time | `-n 50` (start with last 50 lines) |
| `less <file>` | Page through a (possibly large) log file | `/pattern` to search, `G` to jump to end |
| `grep <pattern> <file>` | Search a log file | `-i` (case-insensitive), `-n` (line numbers) |
| `journalctl` | Query the systemd journal (if enabled) | `-u <service>`, `-f` (follow), `--since "10 min ago"`, `-p err` (priority filter) |
| `journalctl -b` | Logs since last boot | Meaningful on native Linux; on WSL, "boot" means since WSL last fully restarted |

## Step-by-Step Example

**If systemd is enabled (check with `ps -p 1 -o comm=` from Lesson 01):**

```bash
$ journalctl -u cron.service --since "1 hour ago"
Jul 12 15:17:01 DESKTOP-FSMTJKA CRON[89110]: pam_unix(cron:session): session opened for user root
Jul 12 15:17:01 DESKTOP-FSMTJKA CRON[89110]: (root) CMD (cd / && run-parts --report /etc/cron.hourly)
...

$ journalctl -u cron.service -f
(stays open, showing new lines as they appear — Ctrl+C to stop)
```

**Either way (always works):**

```bash
$ ls /var/log
alternatives.log  apt/  auth.log  dpkg.log  syslog  ...

$ sudo tail -n 20 /var/log/syslog
Jul 12 15:17:01 DESKTOP-FSMTJKA CRON[89110]: ...

$ sudo tail -f /var/log/syslog
(stays open, showing new lines as they appear — Ctrl+C to stop)

$ grep -i "error" /var/log/syslog | tail -5
```

**Practice log (your own, no `sudo` needed):**

```bash
$ mkdir -p ~/Projects/Learn-DE/sandbox/01_linux/workspace/logs_practice
$ for i in 1 2 3; do echo "$(date) - practice log line $i" >> ~/Projects/Learn-DE/sandbox/01_linux/workspace/logs_practice/app.log; done
$ tail -f ~/Projects/Learn-DE/sandbox/01_linux/workspace/logs_practice/app.log
```

## Guided Practice

See [`exercises/09_logs_monitoring/guided.md`](../exercises/09_logs_monitoring/guided.md).

## Common Mistakes

- Assuming `journalctl` will work without checking Lesson 01's systemd
  status first, then concluding logging is "broken" on WSL.
- Using `cat` on a huge log file instead of `less` or `tail` — floods your
  terminal instead of letting you navigate it.
- Forgetting `sudo` when reading logs owned by root (e.g., `/var/log/syslog`
  is often root-readable only, or restricted to the `adm` group).

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| `journalctl` says "Failed to determine timestamps" or `No journal files were found` | systemd isn't managing the journal on your setup | Confirmed by Lesson 01's `ps -p 1` check; use `/var/log` files instead |
| `tail: cannot open '/var/log/syslog': Permission denied` | The file is restricted to root/`adm` group | Use `sudo tail ...`, or check if you're in the `adm` group (`groups`) |
| Log file doesn't exist for an app you expect to have one | The app might log only to the journal, or hasn't started yet | Check `journalctl -u <service>` if systemd is enabled, otherwise check the app's own documentation for its log path |

## Knowledge Check

1. **When would `journalctl -f` fail to work at all?**
   *Answer: When systemd is not running as PID 1 on your WSL setup (no journal is being maintained).*
2. **What's the always-available fallback for following a log in real time?**
   *Answer: `tail -f <logfile>` on a plain-text log under `/var/log` or an application's own log path.*
3. **Why might the same event show up in both `/var/log` and `journalctl`?**
   *Answer: systemd captures a service's stdout/stderr into the journal even if the application also writes its own separate log file.*

## Completion Checklist

- [ ] You know, concretely, whether `journalctl` works on your machine.
- [ ] You can read a log file with `tail`/`less`/`grep` regardless of systemd status.
- [ ] You've followed a log in real time and seen new lines appear as they're written.

## Reference Materials

- [Ubuntu log monitoring commands](../../../ref%20roadmap/My%20mentor/BUỔI%202/BÀI%20GIẢNG/HỆ%20ĐIỀU%20HÀNH/LINUX%20OS%20-%20UBUNTU/LESSON%202%20-%20UBUNTU%20-%20Cac%20lenh%20ve%20monitor%20log%20trong%20Ubuntu.docx)
- [Monitoring the logs of an arbitrary application on Ubuntu](../../../ref%20roadmap/My%20mentor/BUỔI%202/BÀI%20GIẢNG/HỆ%20ĐIỀU%20HÀNH/LINUX%20OS%20-%20UBUNTU/LESSON%202%20-%20UBUNTU%20-%20Theo%20dõi%20log%20của%201%20ứng%20dụng%20bất%20kỳ%20trên%20ubuntu.docx)

## Next

Guided practice: [`exercises/09_logs_monitoring/guided.md`](../exercises/09_logs_monitoring/guided.md)
Independent exercise: [`exercises/09_logs_monitoring/independent.md`](../exercises/09_logs_monitoring/independent.md)
Next lesson: [10 — Basic Shell Scripting](10_shell_scripting.md)
