# Guided Exercise — Lesson 02: Filesystem Hierarchy & Navigation

## Goal

Practice navigation and search commands inside your safe practice workspace.

## Steps

1. Create your workspace structure (if you haven't already — see
   [`../../workspace/README.md`](../../workspace/README.md)):
   ```bash
   mkdir -p ~/Projects/Learn-DE/sandbox/01_linux/workspace/fs_practice/{data,scripts,logs}
   cd ~/Projects/Learn-DE/sandbox/01_linux/workspace/fs_practice
   ```
2. Create a few sample files:
   ```bash
   touch data/sample1.csv data/sample2.csv scripts/run.sh logs/app.log
   ```
3. Practice each of these and observe the output:
   ```bash
   pwd
   ls -la
   ls -la data/
   find . -name "*.csv"
   find . -type f -mtime -1
   du -sh .
   df -h .
   ```
4. If `tree` is installed (Lesson 07 covers installing it — skip if not yet installed):
   ```bash
   tree -L 2
   ```

## Evidence to Record

In `notes/lesson_02_evidence.md`: the commands above, their actual output,
and a short explanation of what `find . -type f -mtime -1` is actually
checking for.

## Validation

- `find . -name "*.csv"` should list exactly `data/sample1.csv` and `data/sample2.csv`.
- `df -h .` should show the filesystem is your WSL2 Linux disk, not `/mnt/c`.

## When You're Done

Move to [`independent.md`](independent.md).
