
## Lesson 02 — Filesystem Hierarchy & Navigation: Independent

**Commands used** (paste the actual commands you ran, in order):

```bash
cd ~/Projects/Learn-DE
mkdir -p workspace/fs_practice/messy
cd workspace/fs_practice/messy

touch report_2026_01.csv
touch report_2026_02.csv
touch sales_2025_12.csv
touch data_backup.csv
touch application_2026_01.log
touch archive_old.log
touch error_2026_02.log
touch notes.txt
touch README.md
touch todo_2026_03.txt

ls -l

mkdir csv logs

find . -maxdepth 1 -type f -name "*.csv" -exec mv -t csv {} +
find . -maxdepth 1 -type f -name "*.log" -exec mv -t logs {} +

cd ~/Projects/Learn-DE

find workspace/fs_practice/messy -name "*.csv"
find workspace/fs_practice/messy -name "*.log"
tree workspace/fs_practice/messy
```

**Relevant terminal output** (paste the actual output — not a paraphrase):

```text

```

**Validation performed** (which validation command(s) you ran, and what they showed):

```text
I ran find workspace/fs_practice/messy -name "*.csv" and confirmed that every CSV file was under the messy/csv directory.

I ran find workspace/fs_practice/messy -name "*.log" and confirmed that every log file was under the messy/logs directory.

I also ran tree workspace/fs_practice/messy to verify that the TXT and Markdown files remained directly inside messy.
```

**Short explanation** (2–4 sentences, in your own words: what did you do and why did it work?):

I created ten empty files with a mixture of CSV, log, text, and Markdown extensions. I used `find` with `-maxdepth 1` to locate only CSV and log files directly inside the `messy` directory, then moved them into the appropriate subdirectories. The other file types were not matched by either command, so they remained in their original location.

**Troubleshooting notes** (only if something went wrong — what broke, how you diagnosed it, how you fixed it; leave blank if nothing went wrong):

---
