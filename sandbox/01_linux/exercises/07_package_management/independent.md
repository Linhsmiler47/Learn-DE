# Independent Exercise — Lesson 07: Package Management (APT)

## Goal

Investigate a package's dependencies *before* installing it, then confirm
what actually got installed.

## Task

Pick a small, unfamiliar-to-you package (not `tree` — something else, e.g.
`figlet`, `cowsay`, `ncdu`, or another small CLI tool). Before installing
it, use APT to find out what it depends on. Then install it, verify what
actually landed on disk, use it once, and remove it — including checking
whether `apt` considers any leftover packages safe to auto-remove
afterward (without blindly running `autoremove`).

## Constraints

- Choose a package you've never installed before, so the "investigate
  first" step is genuine.
- Do not run `apt autoremove` without first inspecting what it proposes to
  remove.

## Expected Behavior

You should be able to state, before installing, what (if anything) your
chosen package depends on, and after installing, exactly which files it put
on disk.

## Validation Commands

- `apt show <package>` (metadata, including dependencies) — run this *before* installing
- `dpkg -L <package>` (files installed) — run *after*
- `apt autoremove --dry-run` (shows what *would* be removed, without doing it)

## Evidence to Submit

In `notes/lesson_07_evidence.md`: the pre-install `apt show` output, the
post-install `dpkg -L` output, proof you used the tool once, the removal
command, and the `--dry-run` output you checked before deciding whether to
actually run `autoremove`.

## Do Not

- Do not run `apt autoremove` (without `--dry-run` first) as part of this exercise.
- Do not install anything requiring configuration beyond a simple CLI tool.
