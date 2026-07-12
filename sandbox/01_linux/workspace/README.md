# workspace/

Your safe, disposable practice area for Phase 01. Everything you create
while working through `lessons/` and `exercises/` happens here — sample
files, temporary directories, generated logs, scripts you write, exercise
outputs.

## Why this exists

Per Lesson 01: `/home/<user>/...` (which this repository already lives
under) is the correct side of the WSL filesystem split for Linux work —
real permissions, real speed, no `drvfs` emulation quirks. This folder is
where that principle becomes concrete: a dedicated, low-stakes place to
run commands that create, modify, or delete files, without any risk of
touching a system path or a file you actually care about.

## How lessons use this folder

Each lesson that involves creating files points here, typically into its
own subfolder, e.g.:

```
workspace/
├── fs_practice/            (Lesson 02)
├── permissions_practice/   (Lesson 03)
├── processes_practice/     (Lesson 05)
├── services_practice/      (Lesson 06)
├── env_practice/           (Lesson 08)
├── logs_practice/          (Lesson 09)
├── scripting_practice/     (Lesson 10)
└── cron_practice/          (Lesson 11)
```

You don't need to pre-create these — each lesson's guided exercise
includes the `mkdir -p` command that creates its own subfolder.

## What NOT to put here

- Anything that should persist as a graded artifact — evidence belongs in
  [`../notes/`](../notes/README.md), not here. This folder can be safely
  wiped and recreated at any time without losing your actual proof of work.
- Real credentials, private SSH keys used for anything beyond this
  course's practice exercises, or any `.env` file with real secrets.

## Version control

This folder's contents are runtime/practice artifacts, not learning
material — see the repository root [`.gitignore`](../../../.gitignore),
which excludes everything under `workspace/` except this README. If you
want to keep a specific file as evidence, copy the relevant output into
your `notes/` evidence file instead of relying on this folder being
preserved.
