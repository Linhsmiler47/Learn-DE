# Independent Exercise — Lesson 04: Users, Groups & Privilege Escalation

## Goal

Set up a shared-access scenario between two practice users, without giving
either of them `sudo`.

## Task

Create two practice users (choose your own names, e.g. `declab_a` and
`declab_b`) and a new group (e.g. `declab_team`). Configure things so that:
- Both users are members of `declab_team`.
- A directory exists (e.g., `/home/declab_a/shared/`, or another location
  you choose) that both users could read and write to, based on group
  ownership and permissions (combining this with Lesson 03's knowledge).
- Neither practice user is added to the `sudo` group.

You decide the exact sequence of `useradd`, `groupadd`, `usermod`, `chown`,
and `chmod` commands.

## Constraints

- Only ever elevate with `sudo` for the specific administrative commands
  that require it (creating users/groups, changing ownership) — don't
  add either practice user to `sudo`.
- Clean up both users and the group when you're done.

## Expected Behavior

Both practice users should, in principle, be able to read/write the shared
directory based on group permissions alone (you don't need to actually log
in as them — verifying with `ls -l`, `groups`, and permission math is
sufficient evidence).

## Validation Commands

- `groups declab_a`, `groups declab_b` — both should list `declab_team`.
- `ls -ld <shared_directory>` — group ownership and permission bits should
  support your intended access.
- `id declab_a` — confirm `sudo` is absent from the group list.

## Evidence to Submit

In `notes/lesson_04_evidence.md`: your full command sequence, the
verification output, and an explanation of why the permission bits you
chose actually grant the access you intended (tie back to Lesson 03).
Include cleanup commands and their confirmation.

## Do Not

- Do not add either practice user to the `sudo` group.
- Do not leave the practice users/group in place after the exercise.
