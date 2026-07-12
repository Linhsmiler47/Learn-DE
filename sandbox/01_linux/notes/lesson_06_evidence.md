# Lesson 06 — Services & systemd Evidence

## Lesson 06 — Services & systemd: Guided

**Commands used** (paste the actual commands you ran, in order):

```bash
cd ~/Projects/Learn-DE/sandbox/01_linux/workspace

ps -p 1 -o comm=

mkdir -p services_practice

cat > services_practice/loop.sh <<'EOF'
#!/bin/bash
while true; do
  echo "practice service tick: $(date)"
  sleep 30
done
EOF

chmod +x services_practice/loop.sh

cat services_practice/loop.sh

ls -l services_practice/loop.sh

sudo tee /etc/systemd/system/declab-practice.service > /dev/null <<'EOF'
[Unit]
Description=DE learning path practice service

[Service]
ExecStart=/home/linhtran/Projects/Learn-DE/sandbox/01_linux/workspace/services_practice/loop.sh
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF

cat /etc/systemd/system/declab-practice.service

sudo systemctl daemon-reload

sudo systemctl start declab-practice.service

systemctl status declab-practice.service --no-pager

sleep 35

systemctl status declab-practice.service --no-pager

journalctl -u declab-practice.service --no-pager -n 10

sudo systemctl stop declab-practice.service

sudo systemctl disable declab-practice.service

sudo rm /etc/systemd/system/declab-practice.service

sudo systemctl daemon-reload

sudo systemctl reset-failed

systemctl status declab-practice.service --no-pager
```

**Relevant terminal output** (paste the actual output — not a paraphrase):

```text
Paste the actual output here.

Include:
- `systemd` from the prerequisite check
- The script contents and permissions
- The unit file contents
- The first active service status
- The active status after waiting 35 seconds
- The journal output showing service ticks
- The final “Unit declab-practice.service could not be found” message
```

**Validation performed** (which validation command(s) you ran, and what they showed):

```text
I ran `ps -p 1 -o comm=` and confirmed that PID 1 was `systemd`, so I performed the exercise hands-on. After starting `declab-practice.service`, I ran `systemctl status` and confirmed that the service was active and running.

I waited 35 seconds and checked the status again, confirming that the service remained active. I also used `journalctl` to verify that the script was producing timestamped service ticks. After stopping and removing the unit, the final status command reported that `declab-practice.service` could not be found, confirming complete cleanup.
```

**Short explanation** (2–4 sentences, in your own words: what did you do and why did it work?):

I created an executable Bash script that continuously printed a timestamp every 30 seconds. I registered the script as a custom systemd service, reloaded the systemd configuration, and started the service. I verified that it remained active and produced journal output, then stopped it and completely removed its unit file.

**Troubleshooting notes** (only if something went wrong — what broke, how you diagnosed it, how you fixed it; leave blank if nothing went wrong):

---

## Lesson 06 — Services & systemd: Independent

**Commands used** (paste the actual commands you ran, in order):

```bash
cd ~/Projects/Learn-DE/sandbox/01_linux/workspace

cat > services_practice/restart_test.sh <<'EOF'
#!/bin/bash

echo "restart test started: PID=$$ TIME=$(date)"
sleep 3
echo "restart test exiting with code 1: PID=$$ TIME=$(date)"
exit 1
EOF

chmod +x services_practice/restart_test.sh

cat services_practice/restart_test.sh

ls -l services_practice/restart_test.sh

sudo tee /etc/systemd/system/declab-restart-test.service > /dev/null <<'EOF'
[Unit]
Description=DE practice automatic restart test
StartLimitIntervalSec=60
StartLimitBurst=10

[Service]
ExecStart=/home/linhtran/Projects/Learn-DE/sandbox/01_linux/workspace/services_practice/restart_test.sh
Restart=on-failure
RestartSec=2

[Install]
WantedBy=multi-user.target
EOF

cat /etc/systemd/system/declab-restart-test.service

sudo systemctl daemon-reload

sudo systemctl start declab-restart-test.service

systemctl status declab-restart-test.service --no-pager

sleep 6

systemctl status declab-restart-test.service --no-pager

sleep 6

systemctl status declab-restart-test.service --no-pager

journalctl -u declab-restart-test.service --no-pager -n 30

sudo systemctl stop declab-restart-test.service

sudo systemctl disable declab-restart-test.service

sudo rm /etc/systemd/system/declab-restart-test.service

sudo systemctl daemon-reload

sudo systemctl reset-failed

systemctl status declab-restart-test.service --no-pager
```

**Script contents:**

```bash
#!/bin/bash

echo "restart test started: PID=$$ TIME=$(date)"
sleep 3
echo "restart test exiting with code 1: PID=$$ TIME=$(date)"
exit 1
```

**Unit file contents:**

```ini
[Unit]
Description=DE practice automatic restart test
StartLimitIntervalSec=60
StartLimitBurst=10

[Service]
ExecStart=/home/linhtran/Projects/Learn-DE/sandbox/01_linux/workspace/services_practice/restart_test.sh
Restart=on-failure
RestartSec=2

[Install]
WantedBy=multi-user.target
```

**Relevant terminal output** (paste the actual output — not a paraphrase):

```text
Paste the actual output here.

Include:
- The script contents
- The unit file contents
- Repeated `systemctl status` output
- Restart counter information
- Different Main PID values
- Journal entries showing multiple starts and non-zero exits
- The final “Unit declab-restart-test.service could not be found” message
```

**Validation performed** (which validation command(s) you ran, and what they showed):

```text
I repeatedly ran `systemctl status declab-restart-test.service` with delays between the checks. The service showed restart activity, and the Main PID changed between executions, proving that systemd created new processes after the previous processes exited with status 1.

I also used `journalctl -u declab-restart-test.service` and observed multiple start and exit messages with different PIDs. This demonstrated that `Restart=on-failure` automatically restarted the service after each non-zero exit. Finally, I stopped the service, removed its unit file, reloaded systemd, and confirmed that the unit could no longer be found.
```

**Short explanation** (2–4 sentences, in your own words: what did you do and why did it work?):

I created a script that waited three seconds and deliberately exited with status code 1. I configured a custom systemd unit with `Restart=on-failure` and a two-second restart delay. The changing PIDs, restart counter, and journal history proved that systemd repeatedly launched new processes after each failure. I then stopped and completely removed the practice service.

**Troubleshooting notes** (only if something went wrong — what broke, how you diagnosed it, how you fixed it; leave blank if nothing went wrong):

---
