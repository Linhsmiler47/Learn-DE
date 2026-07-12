# Guided Exercise — Lesson 09: Logs & Monitoring

## Steps

1. Check which logging path applies to you (from Lesson 01/06's systemd check):
   ```bash
   ps -p 1 -o comm=
   ```
2. If `systemd`:
   ```bash
   journalctl -u cron.service --since "1 hour ago" | tail -10
   ```
   If not `systemd`, skip to step 3 directly.
3. Always-available path:
   ```bash
   sudo tail -n 20 /var/log/syslog
   grep -i "error" /var/log/syslog | tail -5
   ```
4. Practice log, entirely your own (no `sudo` needed):
   ```bash
   mkdir -p ~/Projects/Learn-DE/sandbox/01_linux/workspace/logs_practice
   for i in 1 2 3; do echo "$(date) - practice log line $i" >> ~/Projects/Learn-DE/sandbox/01_linux/workspace/logs_practice/app.log; done
   tail -n 5 ~/Projects/Learn-DE/sandbox/01_linux/workspace/logs_practice/app.log
   ```
5. Open a second terminal and follow the log live while appending more
   lines from the first:
   ```bash
   # terminal A:
   tail -f ~/Projects/Learn-DE/sandbox/01_linux/workspace/logs_practice/app.log
   # terminal B:
   echo "$(date) - a live line" >> ~/Projects/Learn-DE/sandbox/01_linux/workspace/logs_practice/app.log
   ```

## Evidence to Record

In `notes/lesson_09_evidence.md`: all command output, and specifically a
screenshot-in-text (paste the terminal output) proving you saw a new line
appear live in `tail -f` after appending it from the other terminal.

## Validation

- The `tail -f` terminal must show the new line appearing without you
  restarting the command.

## When You're Done

Move to [`independent.md`](independent.md).
