# Phase Structure Standard

**This framework is stable (as of Phase 02's approval, 2026-07-12) — reuse
it; don't redesign it** unless explicitly requested. This is the canonical
folder structure and philosophy for every detailed phase module in
`sandbox/`. Phase 01 was refactored to match this standard; every phase
built from here forward (02–26) follows it from the start. Referenced by
[`../../LEARNING_PATH.md`](../../LEARNING_PATH.md).

## Lesson Count: 5-Core-Lesson Model (Default From Phase 04 Onward)

Phase 01 and Phase 02 were built with 10–12 smaller, single-topic lessons
each — that model is unchanged for those two and is not retrofitted.
**Phase 04 onward defaults to ~5 longer, combined-topic lessons instead**,
approved 2026-07-19. Each lesson covers what would have been 2–3 smaller
lessons, with the same internal structure (theory, mental model,
terminology, worked examples, safety notes, troubleshooting, knowledge
check, completion checklist) just at greater length per file. Use this
as the default for every new phase unless explicitly told otherwise.

## Folder Template

```
NN_phase_name/
├── README.md         Navigation only — objectives, lesson list, folder
│                     guide, scoring summary, links. Not the content itself.
├── lessons/          ~5 lessons (see above): theory, mental model,
│                     terminology, worked examples, safety notes,
│                     troubleshooting, knowledge check, completion checklist.
├── exercises/        One subfolder per lesson, each with:
│                       guided.md        (scaffolded, steps given)
│                       independent.md   (goal given, learner designs the solution)
├── assessment/       Exactly ONE practical assessment for the whole phase:
│                       README.md   (a real engineering scenario, not an exam)
│                       rubric.md   (100-point evidence-based scoring)
├── cheatsheet/        One consolidated command/concept quick-reference.
├── notes/             The learner's evidence log (graded) and free-form notes:
│                       README.md
│                       evidence_template.md
│                       lesson_NN_evidence.md   (one per lesson, learner-created)
├── workspace/          Disposable practice files only — never graded content:
│                       README.md   (the only tracked file; everything else
│                                    is gitignored — see root .gitignore)
└── reflection.md       Completed AFTER the practical assessment, not before.
```

## What Each Folder Is For (and isn't)

| Folder | Is for | Is not for |
|---|---|---|
| `README.md` | Orientation: what this phase covers, how it's organized, how it's scored, where to start | Teaching content — that belongs in `lessons/` |
| `lessons/` | The actual learning material | Exercises, evidence, or grading |
| `exercises/` | Tasks the learner does | Solutions — never write a solution to an independent exercise |
| `assessment/` | The one integrative, real-scenario practical test + its rubric | A second assessment, a quiz, or an exam |
| `cheatsheet/` | Fast lookup once concepts are already learned | Explanations — that's `lessons/` |
| `notes/` | The learner's own evidence and observations | Pre-written answers |
| `workspace/` | Throwaway practice artifacts | Anything that needs to survive being deleted and recreated |
| `reflection.md` | Retrospective after assessment | A restatement of the lesson content |

## Repository Usage

Every phase's exercises and assessment operate on the real `Learn-DE`
repository, not a throwaway one — see
[`../../LEARNING_PATH.md`](../../LEARNING_PATH.md#repository-usage-policy)
for the full policy. In brief, when authoring a phase's content:

- Default every exercise and the practical assessment to real,
  committed work on a dedicated feature branch — not a disposable repo.
  Only reach for an isolated throwaway repo when a lesson's concept
  genuinely requires it (call this out explicitly when it happens; it's
  the exception).
- `workspace/` is still exactly what it always was: disposable practice
  files, never committed, never long-term (see the folder table above).
  What changes under this policy is where the *real* exercise output
  goes — onto a feature branch in the actual repository, not left
  sitting in `workspace/` or invented in a scratch repo.
- Any exercise that teaches a destructive Git operation (interactive
  rebase, `reset`, cherry-pick, history rewriting, `filter-repo`,
  merge-conflict practice) must scope that operation to a **temporary
  practice branch** created for the exercise — never `main`, a long-lived
  learning branch, or a completed phase's branch, unless the lesson
  explicitly requires it there and names the risk first.
- The practical assessment should leave the repository better than it
  found it: organized commits, real Issues, real Releases, improved
  documentation — not synthetic work invented to hit a rubric category.

## No Quizzes, No Answer Keys

This framework does not use quizzes or separate answer-key files, and
none should be created for any phase unless explicitly requested. Recall
and understanding are demonstrated the same way real engineering work
demonstrates them — through an **Evidence Review** at the end of every
lesson, not a written test.

**Evidence Review** = for each lesson, the learner records in
`notes/lesson_NN_evidence.md`:
- Commands used
- Terminal output (real, not paraphrased)
- Validation results
- A written explanation, in the learner's own words
- Troubleshooting notes (when something went wrong)
- An honest note on overall understanding

This is what a phase reviewer (human or assistant) evaluates against —
never whether a completion checklist is checked. A checklist with no
evidence behind it earns no credit.

## One Assessment Per Phase

Each phase has exactly one practical assessment: a scenario that simulates
real engineering work (e.g., "set up a machine for pipeline work," "build
an ingestion job," "diagnose and fix a broken pipeline") and asks the
learner to apply most or all of the phase's lessons together. It is scored
with the same evidence-based rubric philosophy as every lesson — never an
academic-style test of recall.

## Default 100-Point Scoring Shape

Every phase's `assessment/rubric.md` starts from this shape and may adjust
category sizes slightly to fit the phase's content, but keeps the same
four categories and evidence-based grading:

| Category | Points |
|---|---|
| Guided exercises | 25 |
| Independent exercises | 30 |
| Practical assessment | 35 |
| Documentation and reflection | 10 |

**Completion criteria** (same for every phase):
- **80–100**: Pass — continue to the next phase.
- **70–79**: Review the weakest categories, redo only those, reassess.
- **Below 70**: Repeat the weakest lessons and exercises in full, then
  re-attempt the assessment.

## Learning Cycle

Per lesson: `Learn → Observe → Guided practice → Independent exercise → Validate → Debug → Evidence Review`

Per phase, once all lessons are done: `Practical assessment → Reflect`

## Architecture Practice

Where a phase involves building something (most do, from Checkpoint-linked
phases onward), architecture documentation still follows the templates in
[`architecture/system_architecture.md`](architecture/system_architecture.md)
and its neighboring files. This is independent of the phase structure
above; not every phase's exercises require a full architecture write-up,
but every checkpoint and the final project do (see `LEARNING_PATH.md`).
