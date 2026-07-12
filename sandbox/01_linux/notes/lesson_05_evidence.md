# Lesson 05 — Processes & Job Control Evidence

## Lesson 05 — Guided Exercise

**Commands used** (paste the actual commands you ran, in order):

```bash
cd ~/Projects/Learn-DE/sandbox/01_linux/workspace

sleep 300 &

jobs

ps aux | grep "sleep 300"

cat /proc/<GUIDED_PID>/cmdline | tr '\0' ' '; echo

kill <GUIDED_PID>

jobs

ps aux | grep "sleep 300"

sleep 300

# Pressed Ctrl+Z

jobs

bg %1

jobs

kill %1

jobs

ps aux | grep "sleep 300"
```

**Relevant terminal output** (paste the actual output — not a paraphrase):

```text
Paste the actual Guided Exercise terminal output here.

Include:
- The background job number and PID
- The output from `jobs`
- The output from `ps aux | grep "sleep 300"`
- The output from `/proc/114996/cmdline`
- The output after `kill`
- The `Stopped` status after pressing Ctrl+Z
- The `Running` status after using `bg`
- The final output proving that the process was terminated
```

**Validation performed** (which validation command(s) you ran, and what they showed):

```text
I used `jobs` to verify that the first `sleep 300` process was running as a background job. I then used `ps aux | grep "sleep 300"` to locate its PID and inspected `/proc/<GUIDED_PID>/cmdline` to confirm that the PID belonged to the correct `sleep 300` process.

After sending the default SIGTERM signal with `kill`, I used `jobs` and `ps` to confirm that the process had terminated. For the second process, I pressed Ctrl+Z and used `jobs` to confirm that it was stopped. I resumed it in the background using `bg %1`, verified that it was running, and then terminated it using `kill %1`.
```

**Short explanation** (2–4 sentences, in your own words: what did you do and why did it work?):

I started a `sleep 300` process in the background and inspected it using `jobs`, `ps`, and its `/proc` command-line information. I terminated the first process using its PID. I then started another `sleep 300` process in the foreground, suspended it with Ctrl+Z, resumed it in the background with `bg`, and terminated it using its shell job number.

**Troubleshooting notes** (only if something went wrong — what broke, how you diagnosed it, how you fixed it; leave blank if nothing went wrong):

---

## Lesson 05 — Independent Exercise

**Commands used** (paste the actual commands you ran, in order):

```bash
cd ~/Projects/Learn-DE/sandbox/01_linux/workspace

mkdir -p processes_practice

nano processes_practice/timestamp_loop.sh

chmod 700 processes_practice/timestamp_loop.sh

cat processes_practice/timestamp_loop.sh

./processes_practice/timestamp_loop.sh \
  > processes_practice/timestamp_loop.log 2>&1 &

pgrep -af timestamp_loop.sh

ps aux | grep "[t]imestamp_loop.sh"

cat /proc/116608/cmdline | tr '\0' ' '; echo

kill 116608

pgrep -af timestamp_loop.sh

ps aux | grep "[t]imestamp_loop.sh"

kill -9 116608
```

**Script contents:**

```bash
#!/usr/bin/env bash

while true; do
    date
    sleep 3
done
```

**Relevant terminal output** (paste the actual output — not a paraphrase):

```text
Paste your earlier output from these commands here:

cat processes_practice/timestamp_loop.sh

pgrep -af timestamp_loop.sh

ps aux | grep "[t]imestamp_loop.sh"

cat /proc/116608/cmdline | tr '\0' ' '; echo

kill 116608
```

Final validation output:

```text
linhtran@DESKTOP-FSMTJKA:~/Projects/Learn-DE/sandbox/01_linux/workspace$ pgrep -af timestamp_loop.sh

linhtran@DESKTOP-FSMTJKA:~/Projects/Learn-DE/sandbox/01_linux/workspace$ ps aux | grep "[t]imestamp_loop.sh"

linhtran@DESKTOP-FSMTJKA:~/Projects/Learn-DE/sandbox/01_linux/workspace$ kill -9 116608
bash: kill: (116608) - No such process
```

**Validation performed** (which validation command(s) you ran, and what they showed):

```text
I located the process by running `pgrep -af timestamp_loop.sh` instead of reusing the PID displayed when the background process was launched. I also used `ps aux | grep "[t]imestamp_loop.sh"` and inspected `/proc/116608/cmdline` to confirm that PID 116608 belonged to my `timestamp_loop.sh` script.

I first sent the default SIGTERM signal using `kill 116608`. Afterward, both `pgrep -af timestamp_loop.sh` and `ps aux | grep "[t]imestamp_loop.sh"` returned no output, confirming that the script was no longer running. Therefore, SIGTERM successfully stopped the process and escalation to SIGKILL was not necessary.
```

**Short explanation** (2–4 sentences, in your own words: what did you do and why did it work?):

I created a Bash script that ran continuously and printed a timestamp every three seconds. I started it in the background, then located it by its script name rather than reusing the PID displayed at launch. After confirming the process command line, I sent SIGTERM using a plain `kill` command. The process disappeared from both `pgrep` and `ps`, proving that SIGTERM was sufficient.

**Troubleshooting notes** (only if something went wrong — what broke, how you diagnosed it, how you fixed it; leave blank if nothing went wrong):

After the plain `kill` command, both `pgrep -af timestamp_loop.sh` and `ps aux | grep "[t]imestamp_loop.sh"` returned no output, showing that the process had already stopped. I unnecessarily tried `kill -9 116608` afterward, but Bash returned `No such process` because PID 116608 no longer existed. This confirmed that the original SIGTERM signal was sufficient and escalation to SIGKILL was not needed.

---
