# Guided Exercise — Lesson 01: Linux & Ubuntu/WSL Mental Model

## Goal

Confirm, empirically, how your own machine is configured — don't take the
lesson's reference-machine examples on faith.

## Steps

1. Run each command below exactly as shown, in order:
   ```bash
   ps -p 1 -o comm=
   cat /etc/wsl.conf 2>/dev/null || echo "(no wsl.conf found)"
   cat /proc/version
   echo $HOME
   df -h $HOME | tail -1
   mount | grep /mnt/c
   ```
2. For each command, note the actual output you got.
3. Compare your `ps -p 1` result to the reference machine's (`systemd`).
   If yours differs, re-read Lesson 01's WSL Context table and identify
   which later lessons will behave differently for you.

## Evidence to Record

Using [`../../notes/evidence_template.md`](../../notes/evidence_template.md),
save `notes/lesson_01_evidence.md` with:
- The exact commands you ran and their real output.
- A one-paragraph explanation: is systemd enabled on your machine? What does that mean for Lessons 06, 09, 11, and 12?

## Validation

- Your `df -h $HOME` output should show a filesystem type consistent with
  WSL2's own virtual disk (not a `drvfs`/`9p` type mount, which would
  indicate your home directory is unexpectedly on the Windows side).

## When You're Done

Move to [`independent.md`](independent.md).
