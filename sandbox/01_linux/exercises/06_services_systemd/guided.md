# Guided Exercise — Lesson 06: Services & systemd

## Prerequisite Check

Run `ps -p 1 -o comm=` first. If it prints `systemd`, follow the steps
below exactly. If it prints anything else, read through the steps
conceptually instead of running the `systemctl`/`sudo tee .../etc/systemd`
commands — record in your evidence that this section was conceptual-only
for your setup, and why.

## Safety Reminder

You are only ever starting/stopping/enabling a service **you wrote**.
Never stop, disable, or start a pre-existing system service as part of
this exercise.

## Steps

1. ```bash
   mkdir -p ~/Projects/Learn-DE/sandbox/01_linux/workspace/services_practice
   cat > ~/Projects/Learn-DE/sandbox/01_linux/workspace/services_practice/loop.sh <<'EOF'
   #!/bin/bash
   while true; do
     echo "practice service tick: $(date)"
     sleep 30
   done
   EOF
   chmod +x ~/Projects/Learn-DE/sandbox/01_linux/workspace/services_practice/loop.sh
   ```
2. Register the unit (replace `<user>` with your actual username in the path):
   ```bash
   sudo tee /etc/systemd/system/declab-practice.service > /dev/null <<'EOF'
   [Unit]
   Description=DE learning path practice service

   [Service]
   ExecStart=/home/<user>/Projects/Learn-DE/sandbox/01_linux/workspace/services_practice/loop.sh
   Restart=on-failure

   [Install]
   WantedBy=multi-user.target
   EOF
   sudo systemctl daemon-reload
   sudo systemctl start declab-practice.service
   systemctl status declab-practice.service
   ```
3. Confirm it's actually doing something:
   ```bash
   sleep 35
   systemctl status declab-practice.service   # should show it's still active
   ```
4. Clean up completely:
   ```bash
   sudo systemctl stop declab-practice.service
   sudo systemctl disable declab-practice.service
   sudo rm /etc/systemd/system/declab-practice.service
   sudo systemctl daemon-reload
   systemctl status declab-practice.service   # should now say "could not be found"
   ```

## Evidence to Record

In `notes/lesson_06_evidence.md`: every command and output, including the
final confirmation that the service was fully removed. If systemd wasn't
available on your setup, record your conceptual walkthrough instead and
explain what each step *would* have done.

## Validation

- `systemctl status declab-practice.service` must fail with "not found"
  after cleanup — leaving it registered is an incomplete exercise.

## When You're Done

Move to [`independent.md`](independent.md).
