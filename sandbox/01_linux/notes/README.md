# notes/

Your personal, free-form space for this phase. Nothing here is
pre-written for you to fill in mechanically — it exists so your evidence,
confusions, and "aha" moments have somewhere to live that isn't lost at
the end of a terminal session.

## What goes here

- **Evidence files** (required for scoring): `lesson_NN_evidence.md` for
  each lesson's guided and independent exercises, plus
  `assessment_evidence.md` for the practical assessment. Use
  [`evidence_template.md`](evidence_template.md) as the format — commands
  used, real terminal output, a short explanation, and troubleshooting
  notes when something went wrong.
- **Your own running notes**: anything you want to remember — a command
  you keep forgetting, a mental model that finally clicked, a question to
  ask later.
- **`phase01_score.md`**: your self-scored rubric worksheet (template in
  [`../assessment/rubric.md`](../assessment/rubric.md)).

## What doesn't go here

- Generated runtime artifacts (logs, temp files, scripts you're actively
  testing) — those belong in [`../workspace/`](../workspace/README.md).
  Keep the distinction: `notes/` is what you *write about* your work;
  `workspace/` is where the work itself happens.
- Anything containing a real secret, credential, or private key — evidence
  files may reference a key's *fingerprint* or *public* contents, never a
  private key.

## Why evidence matters here

Scoring (see [`../assessment/rubric.md`](../assessment/rubric.md)) is
based on what's actually in these files — real commands and real output —
not on whether a lesson's completion checklist got checked. An empty
`notes/` folder with every checklist ticked scores zero on every exercise
category; a messy `notes/` folder full of real attempts, including failed
ones with troubleshooting notes, scores well.
