# Lesson 03 — Staging, Committing & Commit Hygiene

**Estimated effort:** Theory ~25 min · Guided practice ~25 min · Independent practice ~20 min

## Why This Matters

A commit history is documentation — for you in six months, and for anyone
reviewing your Data Engineering pipeline changes later. "fix stuff" tells a
reviewer (or future you) nothing. Atomic, well-described commits are what
make `git log`, `git bisect`, and code review actually useful instead of
archaeology.

## Learning Objectives

- Use `git add`, `git status`, and `git diff`/`git diff --staged` to know exactly what's about to be committed.
- Write commit messages that explain *why*, not just *what*.
- Make atomic commits — each one a single logical change.
- Use `git add -p` to split unrelated changes into separate commits.

## A Note on Scope

This lesson's real-repo practice is intentionally **small**: you'll improve
the root `README.md`, which is currently just a title. The much larger job
of properly committing all of Phase 01's and the framework's currently
untracked work is reserved for the **Phase 02 practical assessment** —
don't do that larger job piecemeal here. This lesson's small branch will
resurface again in Lessons 04, 06, 07, and 08.

## Terminology

| Term | Definition |
|---|---|
| Staging area / index | The draft of your next commit — what `git add` populates. |
| Atomic commit | A commit containing exactly one logical change — easy to review, easy to revert alone. |
| `git add -p` | Interactively stage *parts* of a file's changes, not the whole file at once. |

## Mental Model

```
git diff              <- working directory vs. staging area (unstaged changes)
git diff --staged     <- staging area vs. last commit (what commit would contain right now)
git commit            <- staging area becomes a new permanent commit
```

If `git diff` and `git diff --staged` are both empty, there's nothing to
commit — `git status` is just summarizing this same comparison.

## Theory: What Makes a Commit Message Good

A commit message has two parts: a short summary line (what changed,
imperative mood: "Add," not "Added" or "Adding") and, when the *why* isn't
obvious, a blank line followed by a longer explanation. "Fix bug" fails
this; "Fix off-by-one error in date range filter causing the last day to
be excluded" passes it. The test: could someone reading only the message,
with no other context, understand why this commit exists?

## Command Syntax

| Command | Purpose |
|---|---|
| `git add <file>` | Stage a specific file |
| `git add -p` | Interactively stage specific hunks within a file |
| `git status` | Summarize working directory vs. staging vs. last commit |
| `git diff` | Show unstaged changes |
| `git diff --staged` | Show staged changes (what the next commit would contain) |
| `git commit -m "message"` | Commit staged changes |
| `git commit --amend` | See Lesson 06 — modifies the *last* commit only |

## Step-by-Step Example

```bash
$ cd ~/Projects/Learn-DE
$ git switch -c docs/improve-root-readme

$ cat README.md
# Learn-DE

$ cat > README.md <<'EOF'
# Learn-DE

Personal Data Engineering learning repository: an architecture-first path
from Linux fundamentals through Data Engineering to cloud deployment.
EOF

$ git diff
diff --git a/README.md b/README.md
...
+Personal Data Engineering learning repository: an architecture-first path
+from Linux fundamentals through Data Engineering to cloud deployment.

$ git add README.md
$ git diff --staged
(same content, now shown as staged)

$ git commit -m "Add a real description to the root README"
```

## Guided Practice

See [`exercises/03_staging_commit_hygiene/guided.md`](../exercises/03_staging_commit_hygiene/guided.md)
— you'll extend this same branch with a second, deliberately separate
commit, then in the independent exercise practice splitting mixed changes
apart with `git add -p`.

## Common Mistakes

- `git add .` out of habit, without checking `git status`/`git diff` first
  — easy way to accidentally stage something you didn't mean to (a stray
  temp file, a half-finished edit elsewhere).
- Commit messages like "wip," "asdf," "fix," with no other context.
- Cramming two unrelated changes into one commit, making it impossible to
  revert one without the other.

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| `git commit` opens an editor unexpectedly | No `-m` flag given | Either provide `-m "message"` or write the message in the editor and save/exit |
| Staged a file you didn't mean to | Used `git add .` broadly | `git restore --staged <file>` to unstage (doesn't touch the working directory content) |
| `git diff` shows nothing but you know you changed a file | The change is already staged | Use `git diff --staged` instead |

## Knowledge Check

1. **What's the difference between `git diff` and `git diff --staged`?**
   *Answer: `git diff` shows unstaged changes (working dir vs. staging area); `git diff --staged` shows what's staged (staging area vs. last commit).*
2. **What makes a commit "atomic"?**
   *Answer: It contains exactly one logical change, reviewable and revertible on its own.*
3. **How do you unstage a file without losing your changes?**
   *Answer: `git restore --staged <file>`.*

## Completion Checklist

- [ ] You can explain what `git status` is comparing.
- [ ] You've made at least two atomic, well-messaged commits on a real branch.
- [ ] You've used `git add -p` at least once to split a change.

## Connects to Later Phases

Every checkpoint's grading (from Checkpoint 1 onward) looks at your commit
history as evidence of process, not just the final diff. Good commit
hygiene here is what makes that evidence legible later.

## Reference Materials

No source material exists in `ref roadmap/` for Git — authored fresh.

## Next

Guided practice: [`exercises/03_staging_commit_hygiene/guided.md`](../exercises/03_staging_commit_hygiene/guided.md)
Independent exercise: [`exercises/03_staging_commit_hygiene/independent.md`](../exercises/03_staging_commit_hygiene/independent.md)
Next lesson: [04 — Branching Fundamentals & the HEAD Pointer](04_branching_fundamentals.md)
