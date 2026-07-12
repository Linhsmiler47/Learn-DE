# Guided Exercise — Lesson 04: Users, Groups & Privilege Escalation

## Safety Reminder

You will create and delete a **dedicated practice user** (`declab`). Never
modify your own account's group memberships or delete your own user as
part of this exercise.

## Steps

1. ```bash
   id                       # note your own UID/groups first
   sudo useradd -m declab
   id declab
   getent passwd declab
   ```
2. ```bash
   sudo usermod -aG users declab
   groups declab
   ```
3. Clean up:
   ```bash
   sudo userdel -r declab
   id declab   # should now fail — that's expected and correct
   ```

## Evidence to Record

In `notes/lesson_04_evidence.md`: every command and its output, including
the final `id declab` failure message proving cleanup succeeded.

## Validation

- `id declab` must fail with "no such user" after cleanup — if it doesn't,
  you haven't fully removed the practice account.

## When You're Done

Move to [`independent.md`](independent.md).
