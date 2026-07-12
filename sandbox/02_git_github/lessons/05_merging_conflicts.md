# Lesson 05 — Merging & Resolving Conflicts

**Estimated effort:** Theory ~30 min · Guided practice ~30 min · Independent practice ~25 min

## Why This Matters

Conflicts aren't a sign something went wrong — they're Git correctly
telling you it can't guess which of two real changes should win. Every
engineer eventually hits one; the skill is reading the markers and
resolving them by understanding both sides, not by panicking and picking
one blindly.

## Learning Objectives

- Distinguish a merge Git can do automatically from one that needs your judgment.
- Read conflict markers correctly.
- Resolve a conflict by understanding both changes, not guessing.
- Abort a merge safely if you get partway through and need to back out.

## A Note on Scope

This lesson's conflict is **deliberately engineered** on two temporary
practice branches created specifically for this exercise — per the
Repository Usage Policy, conflict practice happens on disposable branches,
never on `main` or the real `docs/improve-root-readme` thread from
Lessons 03–04. Both practice branches get deleted (not merged) once you're
done — nothing from this lesson lands in real history.

## Terminology

| Term | Definition |
|---|---|
| Conflict | A place where two branches changed the same lines (or one edited, one deleted) and Git can't auto-resolve. |
| Conflict markers | `<<<<<<<`, `=======`, `>>>>>>>` — delimit "your side" vs. "their side" in the file. |
| `git merge --abort` | Cancels an in-progress merge, restoring the pre-merge state exactly. |

## Mental Model

```
      main
       │
   ┌───┴───┐
   │       │
 branch-a  branch-b     <- both edited the same line differently
   │       │
   └───┬───┘
       │
  git merge branch-b (while on branch-a)
       │
       ▼
  CONFLICT: both sides touched the same line — Git stops and asks you
```

## Theory: Reading Conflict Markers

```text
<<<<<<< HEAD
This is the version on the branch you're currently on.
=======
This is the version from the branch you're merging in.
>>>>>>> branch-b
```

Resolving means editing this block into what the file *should* actually
say — which might be one side, the other, a combination, or something new
entirely — then removing all three marker lines and staging the result.
Blindly deleting one side without reading the other is how correct changes
get silently lost.

## Command Syntax and Safety Notes

| Command | What it does | Risk level |
|---|---|---|
| `git merge <branch>` | Merges `<branch>` into your current branch | **Low** on a practice branch; on `main`, still low if you actually intend the merge — the risk is in force-resolving conflicts carelessly, not in running `merge` itself |
| `git merge --abort` | Cancels an in-progress conflicted merge | **None** — fully restores pre-merge state |
| `git status` (mid-conflict) | Lists which files are conflicted | Read-only |

## Step-by-Step Example

```bash
$ cd ~/Projects/Learn-DE
$ git switch main
$ git switch -c practice/conflict-a
$ echo "Version from branch A" > sandbox/02_git_github/CONFLICT_PRACTICE_SCRATCH.md
$ git add sandbox/02_git_github/CONFLICT_PRACTICE_SCRATCH.md
$ git commit -m "Practice: add scratch file, branch A version"

$ git switch main
$ git switch -c practice/conflict-b
$ echo "Version from branch B" > sandbox/02_git_github/CONFLICT_PRACTICE_SCRATCH.md
$ git add sandbox/02_git_github/CONFLICT_PRACTICE_SCRATCH.md
$ git commit -m "Practice: add scratch file, branch B version"

$ git switch practice/conflict-a
$ git merge practice/conflict-b
Auto-merging sandbox/02_git_github/CONFLICT_PRACTICE_SCRATCH.md
CONFLICT (add/add): Merge conflict in sandbox/02_git_github/CONFLICT_PRACTICE_SCRATCH.md

$ cat sandbox/02_git_github/CONFLICT_PRACTICE_SCRATCH.md
<<<<<<< HEAD
Version from branch A
=======
Version from branch B
>>>>>>> practice/conflict-b

# Resolve by hand — decide what the file should actually say:
$ cat > sandbox/02_git_github/CONFLICT_PRACTICE_SCRATCH.md <<'EOF'
Resolved: combining both — this line proves I understood both sides.
EOF
$ git add sandbox/02_git_github/CONFLICT_PRACTICE_SCRATCH.md
$ git commit -m "Practice: resolve conflict in scratch file"

# Clean up — delete both practice branches, nothing merges to main:
$ git switch main
$ git branch -D practice/conflict-a practice/conflict-b
```

## Guided Practice

See [`exercises/05_merging_conflicts/guided.md`](../exercises/05_merging_conflicts/guided.md).

## Common Mistakes

- Resolving a conflict by deleting one side without reading it — you might
  be deleting a change that mattered.
- Forgetting to `git add` the resolved file before committing — the merge
  commit won't complete until Git sees the conflict as resolved.
- Not knowing `git merge --abort` exists, and trying to manually undo a
  conflicted merge by hand.

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| `git commit` refuses mid-conflict | Conflict markers still present, or file not staged | Resolve fully, remove all markers, `git add` the file, then commit |
| You're not sure your resolution is right | Understandable — conflicts require judgment | Re-read both original versions (`git show HEAD:<path>` and `git show <other-branch>:<path>`) before deciding |
| You want to start over | Merge is still in progress | `git merge --abort` restores the pre-merge state exactly |

## Knowledge Check

1. **What do the three conflict marker lines mean?**
   *Answer: `<<<<<<< HEAD` starts your current branch's version, `=======` separates the two sides, `>>>>>>> <branch>` ends the incoming branch's version.*
2. **What does `git merge --abort` do?**
   *Answer: Cancels the in-progress merge and restores the exact pre-merge state.*
3. **Why is blindly accepting "your side" or "their side" risky?**
   *Answer: You might discard a real, intended change from the other side without realizing it.*

## Completion Checklist

- [ ] You've created a real conflict on purpose and read the markers correctly.
- [ ] You resolved it by understanding both sides, not guessing.
- [ ] You've used `git merge --abort` at least once to confirm it works.
- [ ] Both practice branches are deleted; nothing from this lesson touched `main`.

## Connects to Later Phases

The Phase 02 practical assessment includes one real, controlled conflict
on the repository's actual work — this lesson is what makes that safe to
attempt for real.

## Reference Materials

No source material exists in `ref roadmap/` for Git — authored fresh.

## Next

Guided practice: [`exercises/05_merging_conflicts/guided.md`](../exercises/05_merging_conflicts/guided.md)
Independent exercise: [`exercises/05_merging_conflicts/independent.md`](../exercises/05_merging_conflicts/independent.md)
Next lesson: [06 — Rewriting History: Amend & Interactive Rebase](06_amend_interactive_rebase.md)
