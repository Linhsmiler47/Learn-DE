# Guided Exercise — Lesson 05: Capstone — Production-Style Configuration Architecture

## Goal

Produce and commit, for real, a reusable configuration convention for
`Learn-DE` — the same repository-wide home the framework already uses for
other reusable artifacts.

## Steps

1. ```bash
   cd ~/Projects/Learn-DE
   git switch -c phase-04/configuration-convention
   ```
2. Create `sandbox/_templates/CONFIGURATION_CONVENTION.md` (the same
   location pattern as `sandbox/_templates/PHASE_STRUCTURE.md`) containing,
   at minimum:
   - The documented config schema template (database, API, storage, batch
     size, retry policy, log level/format) from Lessons 01/04.
   - The documented precedence order from Lesson 02.
   - The documented dev/test/staging/prod/CI variant table from Lesson 03,
     with the explicit "what varies / what's fixed" statement.
   - A real `.env.example` matching the schema.
   - The dependency-management comparison note from Lesson 05, including
     which tool this repository will likely adopt in Phase 09 and why.
3. Commit with a clear, atomic message; push; open a real PR describing
   what this convention is for and which checkpoint will use it first
   (Checkpoint 4).
4. Review it yourself seriously — read it as if you were the Checkpoint 4
   you a few weeks from now, seeing it for the first time — then merge.

## Evidence to Record

In `notes/lesson_05_evidence.md`: the real PR URL and description, the
final convention document's content, and a short explanation of the
location choice (why `sandbox/_templates/` and not somewhere phase-04-specific).

## Validation

- The merged file must exist at `sandbox/_templates/CONFIGURATION_CONVENTION.md` on `main`.
- It must contain all five required pieces listed above — check each off explicitly.

## When You're Done

Move to [`independent.md`](independent.md).
