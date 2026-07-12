# Guided Exercise — Lesson 11: Scheduling with Cron

## Safety Reminder

Only edit your own user crontab (`crontab -e`, no `sudo`). Remove the
practice entry when you're done — do not leave an every-minute job running
indefinitely.

## Steps

1. Confirm cron is actually running first:
   ```bash
   systemctl status cron.service   # or: service cron status
   ```
2. ```bash
   mkdir -p ~/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice
   cat > ~/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/heartbeat.sh <<EOF
   #!/bin/bash
   echo "\$(date '+%Y-%m-%d %H:%M:%S') - heartbeat" >> $HOME/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/heartbeat.log
   EOF
   chmod +x ~/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/heartbeat.sh
   ```
3. Test it manually before trusting cron with it:
   ```bash
   ~/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/heartbeat.sh
   cat ~/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/heartbeat.log
   ```
4. Schedule it every minute (fast feedback for learning only — not a
   real-world interval), using **absolute paths** and explicit output
   redirection:
   ```bash
   crontab -e
   # add (replace <user> with your username):
   # */1 * * * * /home/<user>/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/heartbeat.sh >> /home/<user>/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/cron_stdout.log 2>&1
   crontab -l
   ```
5. Wait 2–3 minutes, then check:
   ```bash
   cat ~/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/heartbeat.log
   ```
6. Clean up:
   ```bash
   crontab -e   # remove the line
   crontab -l   # confirm it's gone
   ```

## Evidence to Record

In `notes/lesson_11_evidence.md`: the crontab line you added, the
`heartbeat.log` contents showing at least 2 automatic runs (with
timestamps at least a minute apart, proving cron — not you — ran it), and
confirmation of cleanup.

## Validation

- `heartbeat.log` must contain lines with timestamps you did not generate
  by manually running the script — that's the proof cron actually
  triggered them.

## When You're Done

Move to [`independent.md`](independent.md).
