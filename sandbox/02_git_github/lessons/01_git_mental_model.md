# Lesson 01 — Git's Mental Model: Enough to Reason About Merge, Rebase, and Reset

**Estimated effort:** Theory ~25 min · Guided practice ~15 min · Independent practice ~15 min

## Why This Matters

Every Data Engineering pipeline you'll build from Phase 09 onward lives in
a repository. When a merge does something unexpected, when a rebase
"loses" a commit, or when `reset` doesn't do what you thought — the only
way to debug that with confidence is knowing what Git actually is
underneath the commands. This lesson is deliberately short: just enough
mental model to make Lessons 04–10 make sense, not a Git-internals course.

## Learning Objectives

- Explain a commit as a snapshot made of pointers, not a diff.
- Explain HEAD as a pointer to a branch, which is itself a pointer to a commit.
- Explain a branch as "just a movable label," not a container.
- Read `git log --graph` and know what you're looking at.

## Terminology

| Term | Definition |
|---|---|
| Commit | A snapshot of the whole repository at a point in time, plus a pointer to its parent commit(s). |
| Branch | A movable pointer to a single commit — nothing more. Creating a branch is instant because it's just writing one pointer. |
| HEAD | A pointer to "where you currently are" — normally pointing at a branch, which points at a commit. |
| Detached HEAD | HEAD pointing directly at a commit instead of a branch — you're "not on a branch." Not dangerous, just easy to lose track of. |
| Working directory | The actual files on disk, as you see them in your editor. |
| Staging area (index) | The place changes go when you `git add` them — a draft of the next commit. |

## Mental Model

```
commit C3 (HEAD -> main)
   │
   ▼
commit C2
   │
   ▼
commit C1  (no parent — the first commit)
```

`main` is a pointer at `C3`. `HEAD` is a pointer at `main`. When you make a
new commit, Git creates `C4` pointing back at `C3`, then moves `main`'s
pointer to `C4`. Nothing about `C1`, `C2`, or `C3` changes — they're
permanent snapshots. This is the one idea that makes everything else in
this phase make sense:

- **A merge** creates a new commit with *two* parents, joining two lines of pointers.
- **A rebase** creates *new* commits that replay old changes onto a different parent, then moves the branch pointer — the old commits still exist for a while (that's what `reflog`, in Lesson 10, recovers from).
- **A reset** just moves a branch pointer (and optionally the staging area/working directory) to point somewhere else — it doesn't "delete" commits, it just stops pointing at them.

You do not need to know how Git stores this on disk (SHA hashing,
compression, object files) to use any of this correctly. That's real, but
it's implementation detail — this lesson stops at the pointer model on
purpose.

## Theory

Three states, same content, different "readiness":

```
Working Directory  --git add-->  Staging Area  --git commit-->  Repository (a new commit)
   (your files)                  (the draft)                     (permanent snapshot)
```

`git status` is, fundamentally, a report comparing these three states to
each other. Once you can read `git status` as "here's what differs between
these three places," the rest of Git's day-to-day commands stop feeling
like memorized incantations.

## Command Syntax

| Command | Purpose |
|---|---|
| `git log --oneline` | One line per commit, newest first |
| `git log --graph --oneline --all` | Same, but drawn as a graph across all branches |
| `git show <commit>` | Show exactly what a commit changed |
| `git status` | Compare working directory / staging area / last commit |

## Step-by-Step Example

This repo (`Learn-DE`) already has real history — use it directly:

```bash
$ cd ~/Projects/Learn-DE
$ git log --oneline
c87bebc Add Data Engineering learning instructions
9678afe Remove Zone.Identifier files and update gitignore
f3f1329 Initial commit

$ git log --graph --oneline --all
* c87bebc (HEAD -> main, origin/main) Add Data Engineering learning instructions
* 9678afe Remove Zone.Identifier files and update gitignore
* f3f1329 Initial commit

$ git show --stat c87bebc
commit c87bebc...
Author: Linh Tran <linhsmiler47@gmail.com>
...
```

Notice `(HEAD -> main, origin/main)` on the first line — that's the mental
model made visible: `HEAD` points at `main`, `main` and `origin/main`
currently point at the same commit, and that commit points back at the one
before it.

## Guided Practice

See [`exercises/01_git_mental_model/guided.md`](../exercises/01_git_mental_model/guided.md).

## Common Mistakes

- Thinking a commit stores a "diff" — it stores a full snapshot (Git is
  efficient about this internally, but conceptually, think snapshot).
- Thinking a branch is a copy of files — it's one pointer, nothing is
  duplicated.
- Panicking in detached HEAD state — it's recoverable (Lesson 10), not
  broken.

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| `git log --graph` shows branches you didn't expect | `--all` shows every branch/remote-tracking ref, not just your current one | Drop `--all` to see only your current branch's history |
| "You are in 'detached HEAD' state" | You checked out a commit directly instead of a branch | Not an error — `git switch -c <new-branch-name>` if you want to keep working from here |

## Knowledge Check

1. **What does creating a new branch actually do, mechanically?**
   *Answer: Writes one new pointer at the current commit — no files are copied or duplicated.*
2. **What's the difference between HEAD and `main`?**
   *Answer: `main` points at a commit; HEAD normally points at `main` (or whichever branch you're on) — HEAD is "where you are," the branch is "what commit that resolves to."*
3. **Does a commit change if you create a new branch pointing at it?**
   *Answer: No — commits are permanent snapshots; only pointers (branches, HEAD) move.*

## Completion Checklist

- [ ] You can read a `git log --graph --oneline --all` output and explain what each symbol represents.
- [ ] You can explain, without notes, why creating a branch is instant.
- [ ] You're not afraid of detached HEAD state.

## Connects to Later Phases

Every checkpoint from here forward assumes this pointer model: Docker
Compose files, Terraform modules, and every pipeline script get committed,
branched, merged, and occasionally reset — using exactly this model, just
applied to different file types.

## Reference Materials

No source material exists in `ref roadmap/` for Git — authored fresh, as
noted in `LEARNING_PATH.md`'s Scope Notes.

## Next

Guided practice: [`exercises/01_git_mental_model/guided.md`](../exercises/01_git_mental_model/guided.md)
Independent exercise: [`exercises/01_git_mental_model/independent.md`](../exercises/01_git_mental_model/independent.md)
Next lesson: [02 — Repository Setup, Configuration, `.gitignore` & `.gitattributes`](02_repo_setup_configuration.md)
