# Lesson 06 — Rewriting History: Amend & Interactive Rebase

**Estimated effort:** Theory ~35 min · Guided practice ~30 min · Independent practice ~30 min

## Why This Matters

Real work is messy while you're doing it — typo fixes, "oops forgot this"
commits, a message that seemed clear until you reread it. Professional
repos don't show that mess in `main`'s history; they show a clean story.
Amend and interactive rebase are how you turn your real, messy process
into that clean story — *before* anyone else sees it.

## Learning Objectives

- Use `commit --amend` to fix the most recent commit only.
- Use interactive rebase to reorder, squash, and reword commits.
- State and justify the golden rule: never rebase commits that are already shared/pushed and someone else might have built on.
- Recognize when rebase is the wrong tool (Lesson 12 covers this further).

## A Note on Scope

You'll clean up the real `docs/improve-root-readme` branch from Lessons
03–04 — it's still unpushed and unmerged, so it's entirely safe to rewrite.
This is exactly the situation where rebase is appropriate: **your own
commits, not yet shared with anyone**.

## Terminology

| Term | Definition |
|---|---|
| `git commit --amend` | Replaces the *most recent* commit with a new one (new content and/or message) — everything before it is untouched. |
| Interactive rebase | `git rebase -i <base>` — opens an editable list of commits since `<base>`, letting you reorder, squash, reword, or drop them. |
| Squash | Combine two or more commits into one. |
| Reword | Change a commit's message without changing its content. |

## Mental Model

Rebase doesn't edit old commits in place — it **creates new commits** with
the requested changes and moves the branch pointer to the last new one.
The old commits still exist for a while, unreferenced by any branch — this
is exactly what `reflog` (Lesson 10) can recover if a rebase goes wrong.

```
Before:  main -> C3
         docs/improve-root-readme -> C5 -> C4 -> C3
                                     (typo fix)  (original)

After squashing C5 into C4:

         docs/improve-root-readme -> C4' -> C3
                                     (C4' is a NEW commit combining C4+C5;
                                      C4 and C5 still exist, just unreferenced)
```

## Theory: The Golden Rule of Rebase

**Never rebase commits that other people (or another clone of the repo)
might already have.** Rebase rewrites commit history — if someone already
pulled the old commits and you rewrite them, their history and yours now
disagree, and reconciling that is painful. The rule in practice: rebase
freely on branches only you are using and haven't pushed yet (or have
pushed but know for certain nobody else has pulled); once a branch is
genuinely shared, use `merge` to bring in new changes instead.

## Command Syntax and Safety Notes

| Command | What it does | Risk level |
|---|---|---|
| `git commit --amend` | Replaces the last commit | **Low** if unpushed; **higher** if already pushed and shared — anyone who pulled the old version now has diverged history |
| `git rebase -i <base>` | Rewrites commits since `<base>` | **Low** on your own unpushed branch; **do not** use on `main` or a branch others are actively using |
| `git rebase --abort` | Cancels an in-progress rebase | **None** — restores pre-rebase state |

## Step-by-Step Example

```bash
$ cd ~/Projects/Learn-DE
$ git switch docs/improve-root-readme
$ git log --oneline
<hash2> Add a real description to the root README
c87bebc (main, origin/main) Add Data Engineering learning instructions
...

# Simulate the real mess: a follow-up typo fix
$ sed -i 's/an architecture-first/an architecture‑first/' README.md   # (example edit)
$ git add README.md
$ git commit -m "typo"

$ git log --oneline
<hash3> typo
<hash2> Add a real description to the root README
c87bebc (main, origin/main) Add Data Engineering learning instructions

# Clean it up: squash "typo" into the previous commit, reword it
$ git rebase -i c87bebc
```

In the editor that opens:

```text
pick <hash2> Add a real description to the root README
squash <hash3> typo
```

Save and close. Git then opens a second editor to combine the messages —
edit it down to one clean message, e.g. "Add a real description to the
root README." Save and close again.

```bash
$ git log --oneline
<hash2-new> Add a real description to the root README
c87bebc (main, origin/main) Add Data Engineering learning instructions
```

One clean commit, ready for Lesson 07–08's push and PR.

## Guided Practice

See [`exercises/06_amend_interactive_rebase/guided.md`](../exercises/06_amend_interactive_rebase/guided.md).

## Common Mistakes

- Rebasing a branch that's already been pushed and pulled by someone
  else (or by you, on another machine) without realizing the history now
  diverges.
- Panicking mid-rebase on a conflict — the same conflict-resolution
  skills from Lesson 05 apply; resolve, `git add`, then `git rebase
  --continue`.
- Confusing `--amend` (last commit only) with rebase (a range of commits).

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| Rebase stops with a conflict | Same as a merge conflict, just mid-replay | Resolve the file, `git add` it, then `git rebase --continue` |
| You want to cancel entirely | Changed your mind mid-rebase | `git rebase --abort` |
| Pushing after a rebase is rejected | The remote has the old (pre-rebase) commits; histories diverged | Since this is your own unpushed/not-yet-shared branch, `git push --force-with-lease` is appropriate here — never on `main` |

## Knowledge Check

1. **What's the golden rule of rebase?**
   *Answer: Never rebase commits that others might already have — only rewrite history that's still entirely yours and unshared.*
2. **Does `git rebase -i` edit old commits, or create new ones?**
   *Answer: It creates new commits with the requested changes and moves the branch pointer; the old commits become unreferenced, not edited in place.*
3. **What's the difference in scope between `--amend` and interactive rebase?**
   *Answer: `--amend` only touches the single most recent commit; interactive rebase can reorder/squash/reword any range of commits since a chosen base.*

## Completion Checklist

- [ ] You've used `--amend` to fix a commit.
- [ ] You've used interactive rebase to squash and reword commits on a real, unpushed branch.
- [ ] You can state the golden rule of rebase without looking it up.

## Connects to Later Phases

The Phase 02 practical assessment's rebase step, and every future PR you
open across this entire learning path, uses exactly this "clean up before
you ask someone to review it" discipline.

## Reference Materials

No source material exists in `ref roadmap/` for Git — authored fresh.

## Next

Guided practice: [`exercises/06_amend_interactive_rebase/guided.md`](../exercises/06_amend_interactive_rebase/guided.md)
Independent exercise: [`exercises/06_amend_interactive_rebase/independent.md`](../exercises/06_amend_interactive_rebase/independent.md)
Next lesson: [07 — Remotes & Connecting to GitHub](07_remotes_github.md)
