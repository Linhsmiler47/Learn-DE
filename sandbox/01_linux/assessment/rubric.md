# Phase 01 Scoring Rubric (100 points)

Every category below is graded on **evidence in `notes/`**, not on checked
boxes. A lesson's completion checklist being fully checked with no
supporting evidence file earns **0** for that lesson's contribution — the
checklist is a personal tracking aid, not proof of work.

There is no separate quiz or exam. Understanding is demonstrated the same
way real engineering work demonstrates it: through commands, real output,
validation, explanation, and how you handled things going wrong. Each
lesson's own **Evidence Review** (commands used, terminal output,
validation results, written explanation, troubleshooting notes, and
overall understanding — see the lesson's Knowledge Check and Completion
Checklist sections) is what this rubric scores against, not a written test.

## Guided Exercises — 25 points

12 lessons × ~2 points each (24), + 1 point for consistently running the
"Validation" step specified in each `guided.md` and recording its actual
output (not just the primary steps).

Per-lesson guided exercise scoring (0–2):
- **2**: Evidence file shows every step's real command + output, matches
  the stated Validation criterion, and includes at least a one-sentence
  explanation of what happened.
- **1**: Most steps present with output, but validation criterion not
  explicitly confirmed, or explanation missing/thin.
- **0**: No evidence file, or evidence is a checklist with no actual
  command output.

## Independent Exercises — 30 points

12 lessons × ~2.5 points each, scored on the same 0–2 pattern as guided
exercises but weighted higher because independent exercises require your
own design choices, not just following steps.

Per-lesson independent exercise scoring (0–2.5):
- **2.5**: Goal fully met, own design choices explained (not copied from
  the guided exercise), validation commands run with real output,
  constraints respected (workspace-only, no destructive commands).
- **1.5**: Goal partially met, or evidence is present but thin on
  explanation/validation.
- **0**: Not attempted, or no evidence submitted.

## Practical Assessment — 35 points

This is the **one** assessment for this phase — a single, integrated,
real-engineering scenario (see [`README.md`](README.md)), not an exam.
Scored on evidence of what actually happened, not on a checklist.

| Category | Points | What's evaluated |
|---|---|---|
| User & permissions setup | 7 | Correct, justified permission scheme; practice user created/cleaned up properly |
| Package & service configuration | 7 | Package installed and verified; service (or conceptual walkthrough) correctly designed |
| Shell script correctness & quality | 7 | Argument validation, `set -euo pipefail`, meaningful exit codes, real file processing logic |
| Cron scheduling correctness | 6 | Correct absolute-path scheduling, explicit output redirection, proof of at least one real automatic firing |
| Logging & troubleshooting evidence | 4 | Script's own log output, plus a genuine, well-documented "break it, diagnose it, fix it" incident report |
| SSH configuration & safety compliance | 4 | Working key-based auth demonstrated; **zero points if `sshd_config` was modified or password auth was disabled** — this is a hard constraint, not a style preference |

## Documentation and Reflection — 10 points

| Item | Points |
|---|---|
| `notes/` populated with real evidence (commands, output, explanation, troubleshooting) for at least 10 of 12 lessons | 5 |
| `reflection.md` thoughtfully completed (specific, not generic answers) | 5 |

## Completion Criteria

| Score | Outcome |
|---|---|
| **80–100** | Pass — proceed to Phase 02 and Checkpoint 1. |
| **70–79** | Review the specific categories above that scored weakest. Redo only those lessons' independent exercises, then re-attempt just the practical assessment categories tied to those lessons — not the whole phase. |
| **Below 70** | Identify which lessons have the most 0-scores across guided/independent exercises. Repeat those lessons and exercises in full, then re-attempt the practical assessment. |

## Self-Scoring Worksheet

Copy this into `notes/phase01_score.md` and fill in your own totals:

```
Guided exercises:            __ / 25
Independent exercises:       __ / 30
Practical assessment:        __ / 35
Documentation & reflection:  __ / 10
                              -------
TOTAL:                       __ / 100
```
