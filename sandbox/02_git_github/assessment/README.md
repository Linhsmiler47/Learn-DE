# Phase 02 Practical Assessment

This is the **one** assessment for Phase 02 — there is no separate quiz or
exam. It uses the real `Learn-DE` repository to do real, lasting work: by
the end, Phase 01's currently-uncommitted content is properly organized
and merged into `main`, real Issues track what's genuinely next, and a
real Release marks the milestone.

## Before You Start

Confirm the starting state (it should look like this, or close to it):

```bash
cd ~/Projects/Learn-DE
git status
```

At the time this assessment was written, `git status` shows `LEARNING_PATH.md`
and `sandbox/` as untracked, and `.gitignore` as modified — this is Phase
01's real, finished-but-uncommitted work, plus the framework refactor and
this Phase 02 module itself. That backlog is the raw material for this
assessment. If your `git status` looks different by the time you reach
this assessment (e.g., some of it is already committed from earlier lesson
practice), that's fine — organize whatever remains.

**No solution is provided.** You are being evaluated on your own branch
design, commit organization, and real decisions — see [`rubric.md`](rubric.md).

## Scenario

Bring this real backlog of work under proper version-control discipline,
end to end, exactly as a professional engineer would when finally
committing a large chunk of finished-but-uncommitted work.

### 1. Branching

Create a feature branch for this work (e.g., `phase-01-content` or
similar) rather than committing any of it directly to `main`.

### 2. Commit hygiene

Split the addition into logical, atomic commits. Don't do this as one
giant commit. Reasonable groupings (adjust based on what's actually still
uncommitted when you get here):
- The framework docs (`LEARNING_PATH.md`, `sandbox/_templates/`, `sandbox/README.md`)
- Phase 01's lessons and exercises
- Phase 01's assessment, cheatsheet, notes scaffolding, and workspace README
- Phase 02's own module (this one)
- The `.gitignore` changes, with a message explaining why

### 3. Interactive rebase

Before opening the PR, clean up this branch's commit sequence — reorder,
squash, or reword anything that doesn't read as an intentional, clean
story.

### 4. Pull request + review

Push the branch, open a real PR, write a real description (this is a
large PR — summarize what it adds and why, the way you'd want a
reviewer to be oriented), review it yourself seriously, and merge with a
deliberately chosen strategy (Lesson 08/12).

### 5. Controlled merge conflict

Before merging step 4's PR, create one additional small branch that also
touches a shared file the big PR touches (e.g., a different section of
`LEARNING_PATH.md`, or `.gitignore`). Merge the big PR first, then resolve
the real conflict this second branch now has against the updated `main` —
by understanding both sides (Lesson 05), not guessing.

### 6. Issues, labels, and project organization

File real Issues for what's genuinely next (e.g., "Design Phase 03 module
once resumed," "Fill in Phase 01 Lessons 06/07/08/12 real evidence,"
"Design Phase 04 curriculum"). Create and apply a real label taxonomy
(e.g., `phase-content`, `revisit`, `framework`) — not just default GitHub
labels used arbitrarily.

### 7. Release

Tag and cut a real GitHub Release (e.g., `v0.1.0`) marking genuine
completion of the Phase 01 + framework + Phase 02 content milestone, with
real release notes summarizing what shipped.

### 8. Secret management

Audit the real repository per Lesson 11: confirm `workspace/` directories
are correctly ignored across both phases, confirm no stray secrets exist
anywhere in the new content, and write up your real (or practiced)
push-protection case study if you haven't already in Lesson 11.

### 9. Repository maintenance

Finish with a clean `git status`, a readable `git log --graph --oneline`,
no leftover practice branches, and branch protection on `main` still
correctly configured (Lesson 08).

## Constraints (Safety)

- No force-push to `main`.
- No rewriting already-merged history.
- The controlled conflict in step 5 touches only small, non-destructive
  sections of real files — never deletes real content.
- No real credential is ever pasted into any evidence file — only the
  *pattern* of what happened, per Lesson 11.

## Evidence Requirements

For **each** of the 9 steps above, record in `notes/assessment_evidence.md`
(use [`../notes/evidence_template.md`](../notes/evidence_template.md)):
- The commands you actually ran, in order.
- Real terminal output (not paraphrased).
- For GitHub web actions (PR, Issues, Release): the real URL and the real
  text you wrote.
- A short explanation of each decision (branch grouping, merge strategy,
  label taxonomy) and why it was correct for this real scenario.
- Troubleshooting notes for step 5 (required) and anywhere else something
  didn't work the first time.

Points are awarded for evidence and understanding — **a completed
checklist with no evidence behind it earns no credit.** See
[`rubric.md`](rubric.md).

## When You're Done

- Confirm `git status` on `main` is clean and `git log --graph --oneline`
  reads as an intentional story.
- Fill in [`../reflection.md`](../reflection.md).
- Self-score using [`rubric.md`](rubric.md) before moving on to Phase 03
  (or wherever your Progress Tracking plan takes you next).
