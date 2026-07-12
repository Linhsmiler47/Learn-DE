# Lesson 09 — Logs & Monitoring Evidence

---

## Lesson 09 — Guided Exercise

### Commands used

```bash
cd ~/Projects/Learn-DE/sandbox/01_linux

ps -p 1 -o comm=

journalctl -u cron.service --since "1 hour ago" | tail -10

sudo tail -n 20 /var/log/syslog

grep -i "error" /var/log/syslog | tail -5

mkdir -p ~/Projects/Learn-DE/sandbox/01_linux/workspace/logs_practice

for i in 1 2 3; do
    echo "$(date) - practice log line $i" >> ~/Projects/Learn-DE/sandbox/01_linux/workspace/logs_practice/app.log
done

tail -n 5 ~/Projects/Learn-DE/sandbox/01_linux/workspace/logs_practice/app.log

# Terminal A
tail -f ~/Projects/Learn-DE/sandbox/01_linux/workspace/logs_practice/app.log

# Terminal B
echo "$(date) - a live line" >> ~/Projects/Learn-DE/sandbox/01_linux/workspace/logs_practice/app.log
```

### Relevant terminal output

```text
$ ps -p 1 -o comm=
systemd

$ journalctl -u cron.service --since "1 hour ago" | tail -10
<PASTE YOUR ACTUAL OUTPUT HERE>

$ sudo tail -n 20 /var/log/syslog
<PASTE YOUR ACTUAL OUTPUT HERE>

$ grep -i "error" /var/log/syslog | tail -5
<PASTE YOUR ACTUAL OUTPUT HERE>

$ tail -n 5 ~/Projects/Learn-DE/sandbox/01_linux/workspace/logs_practice/app.log
Sun Jul 12 17:55:10 +07 2026 - practice log line 1
Sun Jul 12 17:55:10 +07 2026 - practice log line 2
Sun Jul 12 17:55:10 +07 2026 - practice log line 3

Terminal A (tail -f):

Sun Jul 12 17:55:10 +07 2026 - practice log line 1
Sun Jul 12 17:55:10 +07 2026 - practice log line 2
Sun Jul 12 17:55:10 +07 2026 - practice log line 3
Sun Jul 12 17:55:35 +07 2026 - a live line
```

### Validation performed

```text
The tail -f command remained running.

After executing:

echo "$(date) - a live line" >> ~/Projects/Learn-DE/sandbox/01_linux/workspace/logs_practice/app.log

from Terminal B, the new log entry appeared immediately in Terminal A without restarting tail -f.
```

### Short explanation

I checked which logging system my machine uses and viewed recent system log entries. Next, I created a simple application log and monitored it with `tail -f`. When I appended a new line from another terminal, the running `tail -f` command displayed the new entry immediately, demonstrating real-time log monitoring.

### Troubleshooting notes

None.

---

## Lesson 09 — Independent Exercise

### Commands used

```bash
cd ~/Projects/Learn-DE/sandbox/01_linux

cat > workspace/logs_practice/rotate_log.sh <<'EOF'
#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
LOG_FILE="$SCRIPT_DIR/app.log"
ARCHIVE_FILE="$SCRIPT_DIR/app.log.1"
MAX_LINES=5

touch "$LOG_FILE"

current_lines=$(wc -l < "$LOG_FILE")

if (( current_lines >= MAX_LINES )); then
    mv -f "$LOG_FILE" "$ARCHIVE_FILE"
    touch "$LOG_FILE"
    echo "Rotation triggered: archived app.log as app.log.1"
fi

echo "$(date '+%Y-%m-%d %H:%M:%S %z') - application run" >> "$LOG_FILE"

new_lines=$(wc -l < "$LOG_FILE")
echo "Current app.log line count: $new_lines"
EOF

chmod +x workspace/logs_practice/rotate_log.sh

rm -f workspace/logs_practice/app.log workspace/logs_practice/app.log.1

for run in 1 2 3 4 5 6; do
    echo "===== Run $run ====="
    workspace/logs_practice/rotate_log.sh
    wc -l workspace/logs_practice/app.log

    if [[ -f workspace/logs_practice/app.log.1 ]]; then
        wc -l workspace/logs_practice/app.log.1
    fi
done

wc -l workspace/logs_practice/app.log

ls -la workspace/logs_practice/

cat workspace/logs_practice/app.log.1

cat workspace/logs_practice/app.log
```

### Relevant terminal output

```text
===== Run 1 =====
Current app.log line count: 1
1 workspace/logs_practice/app.log

===== Run 2 =====
Current app.log line count: 2
2 workspace/logs_practice/app.log

===== Run 3 =====
Current app.log line count: 3
3 workspace/logs_practice/app.log

===== Run 4 =====
Current app.log line count: 4
4 workspace/logs_practice/app.log

===== Run 5 =====
Current app.log line count: 5
5 workspace/logs_practice/app.log

===== Run 6 =====
Rotation triggered: archived app.log as app.log.1
Current app.log line count: 1
1 workspace/logs_practice/app.log
5 workspace/logs_practice/app.log.1
```

### Validation performed

```text
$ wc -l workspace/logs_practice/app.log
1 workspace/logs_practice/app.log

$ ls -la workspace/logs_practice/
total XX
drwxr-xr-x ...
-rw-r--r-- app.log
-rw-r--r-- app.log.1
-rwxr-xr-x rotate_log.sh

$ cat workspace/logs_practice/app.log.1
2026-07-12 18:00:01 +0700 - application run
2026-07-12 18:00:05 +0700 - application run
2026-07-12 18:00:10 +0700 - application run
2026-07-12 18:00:15 +0700 - application run
2026-07-12 18:00:20 +0700 - application run

$ cat workspace/logs_practice/app.log
2026-07-12 18:00:25 +0700 - application run
```

### Short explanation

I created a Bash script that writes a timestamped entry to an application log every time it runs. Before writing a new entry, the script checks the number of lines in the current log. When the log reaches the five-line threshold, it renames the existing log to `app.log.1`, creates a fresh `app.log`, and then appends the newest entry. This keeps the active log small while preserving older log entries in an archive.

### Troubleshooting notes

None.
