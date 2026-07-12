# Guided Exercise — Lesson 03: File & Directory Permissions, Ownership

## Safety Reminder

Everything in this exercise happens inside
`workspace/permissions_practice/`. Never target `/etc`, `/usr`, `/var`, or
any file you didn't create.

## Steps

1. ```bash
   mkdir -p ~/Projects/Learn-DE/sandbox/01_linux/workspace/permissions_practice
   cd ~/Projects/Learn-DE/sandbox/01_linux/workspace/permissions_practice
   echo "hello" > notes.txt
   ls -l notes.txt
   ```
2. Change permissions and observe each result:
   ```bash
   chmod 600 notes.txt ; ls -l notes.txt
   chmod u+x notes.txt ; ls -l notes.txt
   chmod 644 notes.txt ; ls -l notes.txt
   ```
3. Try to read the file as a permission level that would deny you, to see
   the actual error (don't use `sudo` to bypass it — the point is to see
   the denial):
   ```bash
   chmod 000 notes.txt
   cat notes.txt
   chmod 644 notes.txt   # restore before moving on
   ```

## Evidence to Record

In `notes/lesson_03_evidence.md`: every command and its output, plus the
exact error message you got from `cat notes.txt` when permissions were `000`.

## Validation

- After the final `chmod 644`, `ls -l notes.txt` must show `-rw-r--r--`.

## When You're Done

Move to [`independent.md`](independent.md).
