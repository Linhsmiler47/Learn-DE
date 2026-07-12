# Independent Exercise — Lesson 02: Filesystem Hierarchy & Navigation

## Goal

Organize a small "messy" dataset using only navigation and search commands.

## Task

Inside `workspace/fs_practice/messy/`, create 10 empty files yourself with
a mix of extensions and dates in their names, for example (you choose the
exact names): `report_2026_01.csv`, `report_2026_02.csv`, `notes.txt`,
`archive_old.log`, `data_backup.csv`, etc.

Then, using only `find` (and standard file-move commands), reorganize them
so that:
- All `.csv` files end up under `messy/csv/`
- All `.log` files end up under `messy/logs/`
- Everything else stays where it is

You decide the exact `find` invocation and how to move the matched files.

## Constraints

- Everything happens inside `workspace/fs_practice/messy/` — nothing
  outside this directory should be touched.

## Expected Behavior

After your reorganization, `find messy -name "*.csv"` should only return
paths under `messy/csv/`, and similarly for `.log` files under `messy/logs/`.

## Validation Commands

- `find workspace/fs_practice/messy -name "*.csv"`
- `find workspace/fs_practice/messy -name "*.log"`
- `tree workspace/fs_practice/messy` (if installed) or `ls -R` as a substitute

## Evidence to Submit

In `notes/lesson_02_evidence.md`: the commands you used to both create the
mess and clean it up, the final `find`/`tree` output proving the
reorganization worked, and a short explanation of your approach.

## Do Not

- Do not use a GUI file manager — the point is command-line fluency.
- Do not run any reorganization command against a directory outside `messy/`.
