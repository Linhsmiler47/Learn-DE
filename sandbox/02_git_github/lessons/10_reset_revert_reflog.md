# Lesson 10 — Undoing Things Safely: Reset, Revert & Reflog

**Estimated effort:** Theory ~30 min · Guided practice ~25 min · Independent practice ~20 min

## Why This Matters

Everyone eventually needs to undo something in Git — a bad commit, a
premature push, an experiment gone wrong. Knowing which of `reset`,
`revert`, and `reflog` is the right tool for a given situation is the
difference between a two-minute fix and a panicked, lost afternoon.

## Learning Objectives

- Distinguish `reset --soft`, `--mixed`, and `--hard`, and know which changes history vs. just moves the pointer.
- Know when `revert` is the right choice instead of `reset` (hint: anything already shared).
- Use `reflog` to recover a commit that no longer seems reachable from any branch.

## A Note on Scope

Every exercise in this lesson happens on **temporary practice branches**,
per the Repository Usage Policy — `reset --hard` and history rewriting
never touch `main` or the real `docs/improve-root-readme`/`gitattributes`
threads.

## Terminology

| Term | Definition |
|---|---|
| `git reset --soft <commit>` | Moves the branch pointer to `<commit>`; keeps all changes staged. |
| `git reset --mixed <commit>` (default) | Moves the pointer; unstages changes but keeps them in the working directory. |
| `git reset --hard <commit>` | Moves the pointer; **discards** all changes in staging and working directory. |
| `git revert <commit>` | Creates a **new** commit that undoes `<commit>`'s changes — history isn't rewritten, just added to. |
| `git reflog` | A local log of every place HEAD has pointed, including commits no branch currently references. |

## Mental Model

```
reset --soft/--mixed/--hard   <- moves the pointer backward, optionally discarding work
                                  (rewrites what the branch points to)

revert                        <- adds a NEW commit that cancels a previous one
                                  (history keeps growing forward, nothing is erased)

reflog                        <- your safety net: even after a --hard reset or a
                                  rebase, the old commits usually still exist,
                                  unreferenced, until git eventually garbage-collects them
```

## Theory: Reset vs. Revert — the Decision That Matters

**If the commit is only on your local, unshared branch**: `reset` is fine
— you're allowed to rewrite what nobody else has seen. **If the commit is
already pushed and shared** (on `main`, or a branch someone else pulled):
use `revert` instead — it adds a new, honest "undo" commit rather than
rewriting history other people may have already built on. This is the
same golden rule from Lesson 06, applied to undoing instead of cleaning up.

## Command Syntax and Safety Notes

| Command | What it changes | Risk level | How to undo |
|---|---|---|---|
| `git reset --soft <commit>` | Branch pointer only | **Low** — nothing is lost, just unstaged/staged differently | Reset forward again, or the changes are still in staging |
| `git reset --mixed <commit>` | Branch pointer + unstages | **Low** — changes remain in the working directory | Re-add and commit if needed |
| `git reset --hard <commit>` | Branch pointer + discards all uncommitted/unstaged work | **High** — uncommitted work is genuinely gone; committed work is usually recoverable via `reflog` for a while | `git reflog` to find the commit you reset away from, then `git reset --hard <that-hash>` |
| `git revert <commit>` | Adds a new commit undoing the change | **Low** — never rewrites existing history | `git revert` the revert, if needed |
| `git reflog` | Nothing — read-only | **None** | — |

## Step-by-Step Example

```bash
$ cd ~/Projects/Learn-DE
$ git switch main
$ git switch -c practice/undo-demo
$ echo "bad change" >> sandbox/02_git_github/UNDO_PRACTICE_SCRATCH.md
$ git add sandbox/02_git_github/UNDO_PRACTICE_SCRATCH.md
$ git commit -m "Practice: a commit we'll undo"
$ git log --oneline -1
<hash> Practice: a commit we'll undo

# Scenario A: reset --hard, then recover with reflog
$ git reset --hard HEAD~1
HEAD is now at <previous-hash> ...
$ ls sandbox/02_git_github/UNDO_PRACTICE_SCRATCH.md
ls: cannot access ...: No such file or directory   # gone, as expected

$ git reflog
<current-hash> HEAD@{0}: reset: moving to HEAD~1
<hash> HEAD@{1}: commit: Practice: a commit we'll undo   # <- still here!

$ git reset --hard <hash>
$ cat sandbox/02_git_github/UNDO_PRACTICE_SCRATCH.md
bad change   # recovered

# Scenario B: revert instead, as you would on a shared branch
$ git revert HEAD --no-edit
$ cat sandbox/02_git_github/UNDO_PRACTICE_SCRATCH.md
cat: ...: No such file or directory   # undone, but via a NEW commit
$ git log --oneline
<hash2> Revert "Practice: a commit we'll undo"
<hash>  Practice: a commit we'll undo
...

# Clean up — this was practice, delete the branch entirely
$ git switch main
$ git branch -D practice/undo-demo
```

## Guided Practice

See [`exercises/10_reset_revert_reflog/guided.md`](../exercises/10_reset_revert_reflog/guided.md).

## Common Mistakes

- Using `reset --hard` on a branch with uncommitted work you actually
  wanted to keep — always check `git status` first.
- Using `reset` on a commit that's already pushed/shared, instead of `revert`.
- Not knowing `reflog` exists, and assuming a "lost" commit is gone forever.

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| `reset --hard` deleted work you wanted | Didn't check `git status`/commit first | If it was committed, `git reflog` almost always finds it; if it was never committed, it's genuinely gone — this is why "commit early, commit often" matters |
| `revert` causes a conflict | The reverted commit's changes overlap with later changes | Same conflict-resolution process as Lesson 05 — resolve, then `git revert --continue` |
| `reflog` entry you need has "disappeared" | Reflog entries expire eventually (default ~90 days for unreachable commits) | This is why `reflog` is a safety net for recent mistakes, not permanent storage |

## Knowledge Check

1. **What's the difference between `reset --mixed` and `reset --hard`?**
   *Answer: `--mixed` unstages changes but keeps them in the working directory; `--hard` discards them entirely.*
2. **Why is `revert` safer than `reset` for a commit that's already been pushed and shared?**
   *Answer: `revert` adds a new commit undoing the change without rewriting existing history that others may have already pulled; `reset` rewrites what the branch points to.*
3. **What does `git reflog` show that `git log` doesn't?**
   *Answer: Every place HEAD has pointed locally, including commits no longer referenced by any branch — recoverable, at least for a while.*

## Completion Checklist

- [ ] You've used all three `reset` modes and can explain the difference.
- [ ] You've recovered a "lost" commit using `reflog`.
- [ ] You've used `revert` and explained why it's the right choice for shared history.
- [ ] The practice branch is deleted; nothing touched `main`.

## Connects to Later Phases

Every checkpoint's "break something on purpose, then fix it" exercises
(starting with Phase 01's practical assessment, and continuing in Phase
02's own assessment) rely on exactly this recovery toolkit.

## Reference Materials

No source material exists in `ref roadmap/` for Git — authored fresh.

## Next

Guided practice: [`exercises/10_reset_revert_reflog/guided.md`](../exercises/10_reset_revert_reflog/guided.md)
Independent exercise: [`exercises/10_reset_revert_reflog/independent.md`](../exercises/10_reset_revert_reflog/independent.md)
Next lesson: [11 — Secret Management, Repository Hygiene & Maintenance](11_secrets_repo_maintenance.md)
