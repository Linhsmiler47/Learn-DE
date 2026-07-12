# Guided Exercise — Lesson 05: Processes & Job Control

## Steps

1. ```bash
   sleep 300 &
   jobs
   ps aux | grep "sleep 300"
   ```
2. Note the PID from `ps`, then inspect it live:
   ```bash
   cat /proc/<PID>/cmdline | tr '\0' ' '; echo
   ```
3. Terminate it cleanly, then confirm:
   ```bash
   kill <PID>
   jobs
   ps aux | grep "sleep 300"
   ```
4. Repeat, but this time suspend and resume instead of killing:
   ```bash
   sleep 300
   # press Ctrl+Z
   jobs
   bg %1
   jobs
   kill %1
   ```

## Evidence to Record

In `notes/lesson_05_evidence.md`: every command and output above, including
the PID you found and used, and the `jobs` output at each stage (running,
stopped, backgrounded, terminated).

## Validation

- After the final `kill`, `ps aux | grep "sleep 300"` should show no
  matching process (aside from the `grep` command itself matching its own
  argument, which is expected and fine).

## When You're Done

Move to [`independent.md`](independent.md).
