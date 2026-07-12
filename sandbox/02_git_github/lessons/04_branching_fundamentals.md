# Lesson 04 — Branching Fundamentals & the HEAD Pointer

**Estimated effort:** Theory ~25 min · Guided practice ~25 min · Independent practice ~20 min

## Why This Matters

Every checkpoint, every phase's real-repo work, and every professional
workflow you'll ever join uses branches to isolate work in progress from
`main`. Branching being *cheap* (Lesson 01) is exactly why teams can have
dozens of people working in parallel without stepping on each other.

## Learning Objectives

- Create, switch to, and delete branches confidently.
- Explain what "diverged" means and see it in a real graph.
- Understand fast-forward vs. a "real" merge before Lesson 05 needs it.
- Know the difference between a branch that's safe to delete and one that isn't.

## Terminology

| Term | Definition |
|---|---|
| `git branch <name>` | Create a branch pointer at the current commit (doesn't switch to it). |
| `git switch <name>` / `git checkout <name>` | Move HEAD to point at a different branch. |
| `git switch -c <name>` | Create *and* switch in one step. |
| Diverged | Two branches whose histories have split — each has commits the other doesn't. |
| Fast-forward | A merge where the target branch hasn't diverged at all — Git just moves the pointer forward, no new commit needed. |

## Mental Model

```
Before:                          After git switch -c feature:

main -> C3                       main -> C3
                                  feature -> C3   (new pointer, same commit)
HEAD -> main                     HEAD -> feature  (you're "on" the new branch)

After one commit on feature:

main -> C3
feature -> C4 -> C3   (feature has moved; main hasn't)
HEAD -> feature
```

`main` and `feature` have now **diverged** as soon as either one gets a
commit the other doesn't have. This is the exact state Lesson 05 (merging)
picks up from.

## Theory: Fast-Forward vs. Real Merge

If `main` hasn't moved since `feature` branched off it, merging `feature`
back into `main` doesn't need a new commit at all — Git just slides
`main`'s pointer forward to `feature`'s commit. This is a **fast-forward
merge**. If `main` *has* moved (someone else merged something else in the
meantime), Git has to create a genuine merge commit with two parents. You
don't choose this — Git detects which situation you're in automatically —
but recognizing the difference in `git log --graph` matters for reading
history later.

## Command Syntax

| Command | Purpose |
|---|---|
| `git branch` | List local branches |
| `git branch <name>` | Create a branch (doesn't switch) |
| `git switch <name>` | Switch to an existing branch |
| `git switch -c <name>` | Create and switch |
| `git branch -d <name>` | Delete a branch **only if already merged** (safe) |
| `git branch -D <name>` | Force-delete a branch, merged or not (see Safety Notes) |

## Safety Notes

| Command | Risk level | Why |
|---|---|---|
| `git branch -d <name>` | **None** — Git refuses if the branch has unmerged commits | This is the safe default; use it |
| `git branch -D <name>` | **Medium** — deletes the branch pointer even if it has commits nothing else points to | Those commits become unreachable from any branch (recoverable via `reflog`, Lesson 10, but only for a limited time) — only force-delete a branch you're certain you don't need |

## Step-by-Step Example

```bash
$ cd ~/Projects/Learn-DE
$ git branch
* docs/improve-root-readme
  main

$ git log --graph --oneline --all
* <hash> (HEAD -> docs/improve-root-readme) Add a real description to the root README
* c87bebc (main, origin/main) Add Data Engineering learning instructions
* 9678afe Remove Zone.Identifier files and update gitignore
* f3f1329 Initial commit
```

Your `docs/improve-root-readme` branch has diverged from `main` by exactly
one commit — this is a fast-forward-mergeable state, since `main` hasn't
moved since you branched.

```bash
$ git switch main
$ git switch docs/improve-root-readme
```

Switching back and forth is instant and doesn't touch your working
directory's other files — only the ones that differ between the two
branches' snapshots change.

## Guided Practice

See [`exercises/04_branching_fundamentals/guided.md`](../exercises/04_branching_fundamentals/guided.md).

## Common Mistakes

- Forgetting which branch you're on before making changes — always check
  `git status` (it shows the current branch) or your shell prompt if
  configured to show it.
- Using `-D` reflexively instead of `-d`, deleting unmerged work by habit.
- Believing branch switching "copies" files — it doesn't; it changes what
  the working directory shows to match the target branch's snapshot.

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| `error: Your local changes ... would be overwritten by checkout` | Uncommitted changes conflict with the branch you're switching to | Commit or stash the changes first, then switch |
| `git branch -d` refuses to delete | The branch has commits not merged anywhere else | That's the safety check working — merge it first, or use `-D` only if you're sure |

## Knowledge Check

1. **What's the difference between `git branch <name>` and `git switch -c <name>`?**
   *Answer: `git branch` creates a branch without moving HEAD to it; `git switch -c` creates and switches in one step.*
2. **When does Git perform a fast-forward merge instead of creating a merge commit?**
   *Answer: When the target branch hasn't diverged — the branch being merged in is simply ahead, so the pointer can just move forward.*
3. **Why does `git branch -d` sometimes refuse to delete a branch?**
   *Answer: It's a safety check — it refuses if the branch has commits not reachable from anywhere else, to avoid silently losing work.*

## Completion Checklist

- [ ] You've created, switched between, and listed branches on the real repo.
- [ ] You can explain fast-forward vs. real merge before doing either in Lesson 05.
- [ ] You know why `-d` is safer than `-D`.

## Connects to Later Phases

Checkpoint branching (one branch per checkpoint, as the framework's
Repository Usage Policy establishes) and every future CI/CD trigger
(Phase 06) key off exactly this: branches as the unit of isolated,
reviewable work.

## Reference Materials

No source material exists in `ref roadmap/` for Git — authored fresh.

## Next

Guided practice: [`exercises/04_branching_fundamentals/guided.md`](../exercises/04_branching_fundamentals/guided.md)
Independent exercise: [`exercises/04_branching_fundamentals/independent.md`](../exercises/04_branching_fundamentals/independent.md)
Next lesson: [05 — Merging & Resolving Conflicts](05_merging_conflicts.md)
