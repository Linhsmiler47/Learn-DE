# Independent Exercise — Lesson 02: Repository Setup, Configuration, `.gitignore` & `.gitattributes`

## Goal

Audit and improve the real repo's `.gitignore` — it already exists and
works, but prove that to yourself rather than assuming it.

## Task

Review the current root `.gitignore`. For at least three of its rules,
design and run your own real test proving the rule actually works (create
a matching file, confirm `git status` doesn't show it as untracked-and-
suggested, then remove your test file). If you find a gap — something this
repository's real structure could produce that isn't covered — propose and
add a real rule for it on your `phase-02/gitattributes` branch (or a new
small branch if you prefer to keep concerns separate).

## Constraints

- Test files must be cleaned up after proving each rule — don't leave
  scratch test files lying around uncommitted or committed.
- Any real `.gitignore` improvement should be a genuine gap, not an
  invented one — check the actual rules against the actual repo structure.

## Expected Behavior

For each rule you test, you can show a before/after `git status` proving
the rule either does or doesn't catch a specific real example.

## Validation Commands

- `git status` (before and after creating each test file)
- `git check-ignore -v <test-file>` (shows exactly which rule matched, if any)

## Evidence to Submit

In `notes/lesson_02_evidence.md`: which three rules you tested, the exact
test file you used for each, the `git status`/`git check-ignore` proof,
and (if applicable) the gap you found and the rule you added to close it.

## Do Not

- Do not leave test artifacts uncommitted and untracked in the real repo
  when you're done — clean up after each test.
