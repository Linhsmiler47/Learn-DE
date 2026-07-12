# Phase 02 — Git and GitHub

This phase is a full guided learning module. If you're starting fresh, go
straight to [`lessons/01_git_mental_model.md`](lessons/01_git_mental_model.md)
— the rest of this README is the map, not the content itself.

This phase follows the repository-wide phase structure standard — see
[`../_templates/PHASE_STRUCTURE.md`](../_templates/PHASE_STRUCTURE.md).
No quizzes, no answer keys. Understanding is demonstrated through an
**Evidence Review** at the end of every lesson, captured in `notes/`.

## Learning Objectives

- Understand Git's pointer model (commits, branches, HEAD) well enough to
  reason about merge, rebase, and reset — not memorize commands.
- Work confidently with staging, commits, branches, merges, and conflicts.
- Rewrite your own unshared history safely with amend and interactive rebase.
- Use GitHub (and GitHub CLI) for remotes, pull requests, code review,
  issues, and releases.
- Manage secrets safely and keep a repository healthy over time.

## Prerequisites

- Phase 01 (shell comfort). No `ref roadmap/` material exists for Git —
  every lesson is authored fresh, as documented in `LEARNING_PATH.md`.

## How This Module Is Organized

```
02_git_github/
├── README.md            <- you are here — navigation only
├── lessons/              12 lessons: theory, mental model, terminology,
│                         worked examples on the REAL repository, safety
│                         notes, troubleshooting, knowledge checks
├── exercises/            guided.md + independent.md per lesson
├── assessment/           the ONE practical assessment for this phase + rubric
├── cheatsheet/            one consolidated command quick-reference
├── notes/                 your evidence log + free-form notes (graded)
├── workspace/             disposable scratch space (rarely needed — see below)
└── reflection.md          completed after the assessment
```

## This Phase Uses the Real `Learn-DE` Repository

Per the Repository Usage Policy in `LEARNING_PATH.md`, almost nothing in
this phase happens in a throwaway repo. Instead:

- **Real, lasting work** (a `.gitattributes` file, a real README
  description, real PRs, real Issues, a real Release) happens on real
  feature branches in `Learn-DE` itself — two small real threads run
  through Lessons 02→08 and 03→04→06→07→08.
- **Destructive practice** (conflicts, rebase reordering, reset/reflog
  recovery) happens on **temporary branches** created specifically for
  that exercise and deleted afterward — never merged, never touching `main`.
- `workspace/` is used only for the rare case of truly disposable files
  (like Lesson 02's one-time `git init` demo) — most lessons don't need it
  at all.

## Lesson Sequence

| # | Lesson | Est. effort (theory/guided/independent) |
|---|---|---|
| 01 | [Git's Mental Model](lessons/01_git_mental_model.md) | 25 / 15 / 15 min |
| 02 | [Repository Setup, Configuration, `.gitignore` & `.gitattributes`](lessons/02_repo_setup_configuration.md) | 25 / 25 / 20 min |
| 03 | [Staging, Committing & Commit Hygiene](lessons/03_staging_commit_hygiene.md) | 25 / 25 / 20 min |
| 04 | [Branching Fundamentals & the HEAD Pointer](lessons/04_branching_fundamentals.md) | 25 / 25 / 20 min |
| 05 | [Merging & Resolving Conflicts](lessons/05_merging_conflicts.md) | 30 / 30 / 25 min |
| 06 | [Rewriting History: Amend & Interactive Rebase](lessons/06_amend_interactive_rebase.md) | 35 / 30 / 30 min |
| 07 | [Remotes & Connecting to GitHub](lessons/07_remotes_github.md) | 30 / 25 / 20 min |
| 08 | [Pull Requests & Code Review Workflow](lessons/08_pull_requests_code_review.md) | 30 / 30 / 25 min |
| 09 | [Issues, Milestones & Release Management](lessons/09_issues_releases.md) | 30 / 25 / 20 min |
| 10 | [Undoing Things Safely: Reset, Revert & Reflog](lessons/10_reset_revert_reflog.md) | 30 / 25 / 20 min |
| 11 | [Secret Management, Repository Hygiene & Maintenance](lessons/11_secrets_repo_maintenance.md) | 40 / 30 / 30 min |
| 12 | [Branching Strategies & Collaborative Workflows](lessons/12_branching_strategies.md) | 25 / 20 / 20 min |

Total estimated effort: roughly **14–18 hours** across theory, guided, and
independent practice, plus the practical assessment.

## The Learning Cycle (per lesson)

`Learn → Observe → Guided practice → Independent exercise → Validate → Debug → Evidence Review`
— then, at the phase level: `Practical assessment → Reflect`.

## Assessment and Scoring

100 points total — see [`assessment/rubric.md`](assessment/rubric.md).
One practical assessment (no exam): bring the real, currently-uncommitted
Phase 01 + framework backlog under proper version control, end to end —
branching, commit hygiene, rebase, PR + review, a real controlled
conflict, issues + labels, a release, secret management, and repository
maintenance. See [`assessment/README.md`](assessment/README.md).

| Category | Points |
|---|---|
| Guided exercises | 25 |
| Independent exercises | 30 |
| Practical assessment | 35 |
| Documentation and reflection | 10 |

**80–100**: pass, continue. **70–79**: review weak categories, reassess.
**Below 70**: repeat the weakest lessons and exercises.

## Reference Materials (`ref roadmap/`, read-only)

No source material exists in `ref roadmap/` for Git or GitHub — every
lesson in this phase is authored fresh, as already documented in
`LEARNING_PATH.md`'s Scope Notes.

## When You're Done

Complete [`reflection.md`](reflection.md), self-score against
[`assessment/rubric.md`](assessment/rubric.md), then continue per your
Progress Tracking plan in `LEARNING_PATH.md` (Phase 03 remains **Skipped
Temporarily** until after Phase 07; Phase 04 is next in your actual order).
