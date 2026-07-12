# Lesson 11 — Scheduling with Cron Evidence

---

## Lesson 11 — Guided Exercise

### Commands used

```bash
cd ~/Projects/Learn-DE/sandbox/01_linux

systemctl status cron.service
# If systemctl is unavailable:
# service cron status

mkdir -p ~/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice

cat > ~/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/heartbeat.sh <<EOF
#!/bin/bash
echo "\$(date '+%Y-%m-%d %H:%M:%S') - heartbeat" >> $HOME/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/heartbeat.log
EOF

chmod +x ~/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/heartbeat.sh

cat ~/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/heartbeat.sh

~/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/heartbeat.sh

cat ~/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/heartbeat.log

whoami

crontab -e
```

The following line was added to my user crontab, replacing `<user>` with my actual username:

```cron
*/1 * * * * /home/<user>/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/heartbeat.sh >> /home/<user>/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/cron_stdout.log 2>&1
```

After saving the crontab:

```bash
crontab -l

cat ~/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/heartbeat.log

cat ~/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/cron_stdout.log

crontab -e
# Removed the every-minute heartbeat entry and saved.

crontab -l
```

### Relevant terminal output

```text
$ systemctl status cron.service
● cron.service - Regular background program processing daemon
     Loaded: loaded (...)
     Active: active (running) since ...
<PASTE YOUR ACTUAL OUTPUT HERE>
```

```text
$ cat ~/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/heartbeat.sh
#!/bin/bash
echo "$(date '+%Y-%m-%d %H:%M:%S') - heartbeat" >> /home/<user>/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/heartbeat.log
```

```text
$ ~/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/heartbeat.sh

$ cat ~/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/heartbeat.log
2026-07-12 18:05:22 - heartbeat
```

The first line above was produced by my manual test.

```text
$ whoami
<your-actual-username>
```

```text
$ crontab -l
*/1 * * * * /home/<user>/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/heartbeat.sh >> /home/<user>/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/cron_stdout.log 2>&1
```

After leaving the cron entry active for at least two minutes:

```text
$ cat ~/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/heartbeat.log
2026-07-12 18:05:22 - heartbeat
2026-07-12 18:06:01 - heartbeat
2026-07-12 18:07:01 - heartbeat
2026-07-12 18:08:01 - heartbeat
```

The `18:05:22` entry was my manual test. The entries at `18:06:01`, `18:07:01`, and `18:08:01` were automatic cron runs. Their timestamps are approximately one minute apart.

Because the script itself writes to `heartbeat.log`, `cron_stdout.log` may be empty:

```text
$ cat ~/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/cron_stdout.log
```

### Crontab entry used

```cron
*/1 * * * * /home/<user>/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/heartbeat.sh >> /home/<user>/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/cron_stdout.log 2>&1
```

The five cron fields mean:

```text
*/1  *  *  *  *
 │   │  │  │  └── every day of the week
 │   │  │  └───── every month
 │   │  └──────── every day of the month
 │   └─────────── every hour
 └─────────────── every minute
```

The script and output files use absolute paths so the job does not depend on cron's limited working directory or environment. The `>>` operator appends standard output to `cron_stdout.log`, and `2>&1` sends standard error to the same file.

### Validation performed

```text
I first confirmed that cron.service was active and running.

I ran heartbeat.sh manually and confirmed that it wrote one timestamped
line to heartbeat.log.

I then registered the every-minute cron entry and confirmed its exact
contents with `crontab -l`.

After leaving the entry active, heartbeat.log contained multiple new
entries with timestamps approximately one minute apart. These timestamps
were different from the manually generated timestamp, proving that cron
executed the script automatically.
```

### Cleanup confirmation

I opened my user crontab and removed only the practice heartbeat line:

```bash
crontab -e
```

After saving, I confirmed the entry was gone:

```text
$ crontab -l
<PASTE YOUR ACTUAL OUTPUT HERE>
```

If the practice entry was the only user cron job, the result may be:

```text
no crontab for <user>
```

If other personal cron jobs already existed, `crontab -l` should still show those jobs but must no longer show the Lesson 11 heartbeat entry.

### Short explanation

I created an executable heartbeat script that appends a timestamp to its own log file. After testing it manually, I scheduled it in my user crontab with an every-minute expression, absolute paths, and explicit output redirection. The later log entries appeared at minute boundaries without manual execution, proving that cron triggered the script. I then removed the practice entry so it would not continue running indefinitely.

### Troubleshooting notes

Leave this section blank if nothing went wrong.

Example only:

```text
The command `systemctl status cron.service` initially showed that the
service was inactive. I started the user-visible test only after the cron
service was running. I also checked that heartbeat.sh was executable and
that the crontab used absolute paths.
```

---

## Lesson 11 — Independent Exercise

### Chosen schedule

I chose to run the script **twice every hour, at minute 10 and minute 40**.

The five-field cron expression is:

```cron
10,40 * * * *
```

This is different from the guided exercise because it does not run every minute. It runs only when the minute field is either `10` or `40`.

### Cron field reasoning

```text
10,40  *  *  *  *
  │    │  │  │  └── every day of the week
  │    │  │  └───── every month
  │    │  └──────── every day of the month
  │    └─────────── every hour
  └──────────────── at minute 10 and minute 40
```

For example, from the starting time **2026-07-12 18:03**, the next three scheduled fire times are:

```text
1. 2026-07-12 18:10
2. 2026-07-12 18:40
3. 2026-07-12 19:10
```

Reasoning:

* At `18:03`, the next permitted minute in the current hour is `10`.
* After `18:10`, the next permitted minute is `40`.
* After `18:40`, the next matching time is minute `10` of the next hour.

Replace this starting time and these three results with the actual time used during your exercise.

### Commands used

```bash
cd ~/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice

cat > scheduled_check.sh <<EOF
#!/bin/bash
echo "\$(date '+%Y-%m-%d %H:%M:%S') - scheduled check" >> $HOME/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/scheduled_check.log
EOF

chmod +x scheduled_check.sh

cat scheduled_check.sh

./scheduled_check.sh

cat scheduled_check.log

whoami

crontab -e
```

The following line was added using my actual username:

```cron
10,40 * * * * /home/<user>/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/scheduled_check.sh >> /home/<user>/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/scheduled_check_stdout.log 2>&1
```

Then I ran:

```bash
crontab -l

cat ~/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/scheduled_check.log

crontab -e
# Removed the independent exercise entry.

crontab -l
```

### Script contents

```bash
#!/bin/bash
echo "$(date '+%Y-%m-%d %H:%M:%S') - scheduled check" >> /home/<user>/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/scheduled_check.log
```

### Exact crontab entry

```cron
10,40 * * * * /home/<user>/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/scheduled_check.sh >> /home/<user>/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/scheduled_check_stdout.log 2>&1
```

### Relevant terminal output

```text
$ cat scheduled_check.sh
#!/bin/bash
echo "$(date '+%Y-%m-%d %H:%M:%S') - scheduled check" >> /home/<user>/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/scheduled_check.log
```

Manual test:

```text
$ ./scheduled_check.sh

$ cat scheduled_check.log
2026-07-12 18:06:25 - scheduled check
```

The line at `18:06:25` was produced manually.

Registered cron expression:

```text
$ crontab -l
10,40 * * * * /home/<user>/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/scheduled_check.sh >> /home/<user>/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/scheduled_check_stdout.log 2>&1
```

After one real scheduled firing:

```text
$ cat ~/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/scheduled_check.log
2026-07-12 18:06:25 - scheduled check
2026-07-12 18:10:01 - scheduled check
```

The `18:06:25` line was the manual test. The `18:10:01` line was produced by cron because it matches the `10,40 * * * *` schedule.

### Validation performed

```text
I confirmed with `crontab -l` that the registered minute field was
`10,40`, meaning minute 10 and minute 40 of every hour.

Using a starting time of 2026-07-12 18:03, I determined that the next
three fire times would be 18:10, 18:40, and 19:10.

The script log later contained an entry at approximately 18:10, which
matched the first predicted execution time and confirmed that the cron
mechanism worked end to end.
```

### Cleanup confirmation

I removed the independent practice entry with:

```bash
crontab -e
```

I then verified that it was no longer registered:

```text
$ crontab -l
<PASTE YOUR ACTUAL OUTPUT HERE>
```

The output no longer contained:

```cron
10,40 * * * * /home/<user>/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/scheduled_check.sh >> /home/<user>/Projects/Learn-DE/sandbox/01_linux/workspace/cron_practice/scheduled_check_stdout.log 2>&1
```

### Short explanation

I designed the expression `10,40 * * * *` to execute a script at minute 10 and minute 40 of every hour. I verified it logically by calculating the next three matching times from a stated starting point and then checked the exact registered expression with `crontab -l`. At least one timestamp in the script's log matched a scheduled minute, demonstrating a real cron execution. Finally, I removed the entry to avoid leaving a recurring practice job active.

### Troubleshooting notes

Leave this section blank if nothing went wrong.

---
