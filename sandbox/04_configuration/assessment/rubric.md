# Phase 04 Scoring Rubric (100 points)

Every category is graded on **evidence in `notes/`**, not on checked
boxes. No quiz — see [`README.md`](README.md) for the one practical
assessment.

## Guided Exercises — 25 points

5 lessons × 5 points each, scored 0–5:

- **5**: Real commands/config, real output, matches the stated Validation
  criterion, at least a one-sentence explanation.
- **3**: Present but thin — validation not explicitly confirmed, or explanation missing.
- **0**: No evidence, or a checklist with no real output behind it.

## Independent Exercises — 30 points

5 lessons × 6 points each, scored 0–6:

- **6**: Goal fully met, own design choices, real validation output, constraints respected.
- **3**: Goal partially met, or thin on explanation/validation.
- **0**: Not attempted, or no evidence submitted.

## Practical Assessment — 35 points

| Category | Points | What's evaluated |
|---|---|---|
| Format choice + justification | 4 | A real, reasoned choice tied to where that format actually shows up in this learning path |
| Real `.env.example` | 5 | Matches Checkpoint 4's real anticipated needs, no real secrets |
| Multi-environment variants | 8 | Identical schema across dev/test/staging/prod/ci, genuinely differing values, correct secrets-handling story per environment |
| Layered, validated config loader | 10 | Actually runs; demonstrates all four layers overriding correctly; fail-fast validation actually rejects a bad value |
| Logging as configuration | 4 | Present as ordinary validated config values, scoped correctly (no scope creep into observability) |
| Dependency-management note | 4 | Real, findable reference from Checkpoint 4's README back to the capstone's recorded decision |

## Documentation and Reflection — 10 points

| Item | Points |
|---|---|
| `notes/` populated with real evidence for at least 4 of 5 lessons | 5 |
| `reflection.md` thoughtfully completed (specific, not generic) | 5 |

## Completion Criteria

| Score | Outcome |
|---|---|
| **80–100** | Pass — continue to the next phase in your Progress Tracking plan. |
| **70–79** | Review the weakest categories, redo only those, reassess. |
| **Below 70** | Repeat the weakest lessons and exercises in full, then re-attempt the assessment. |

## Self-Scoring Worksheet

```
Guided exercises:            __ / 25
Independent exercises:       __ / 30
Practical assessment:        __ / 35
Documentation & reflection:  __ / 10
                              -------
TOTAL:                       __ / 100
```
