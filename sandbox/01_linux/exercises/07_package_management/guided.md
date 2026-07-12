# Guided Exercise — Lesson 07: Package Management (APT)

## Steps

1. ```bash
   sudo apt update
   apt list --upgradable | head -5
   ```
2. ```bash
   sudo apt install tree
   dpkg -l | grep tree
   dpkg -L tree | head -10
   ```
3. Use it, then remove it:
   ```bash
   tree -L 1 ~/Projects/Learn-DE
   sudo apt remove tree
   dpkg -l | grep tree   # should show it's no longer installed ("un" state)
   ```

## Evidence to Record

In `notes/lesson_07_evidence.md`: the install confirmation prompt output,
`dpkg -L tree` file listing, the `tree` command's own output, and the
removal confirmation.

## Validation

- `dpkg -l | grep tree` after removal should show status `un` (or the
  package should be entirely absent), not `ii`.

## When You're Done

Move to [`independent.md`](independent.md).
