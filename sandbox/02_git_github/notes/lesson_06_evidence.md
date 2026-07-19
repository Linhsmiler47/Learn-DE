# Lesson 06 Evidence – Rewriting History: Amend & Interactive Rebase

**Repository:** Learn-DE

**Lesson:** 06 – Rewriting History: Amend & Interactive Rebase

**Completion Date:** 2026-07-19

---

# Guided Exercise

## Objective

Practice rewriting local Git history using Interactive Rebase by removing a small follow-up "typo" commit and creating a cleaner commit history.

---

## Initial Branch

Worked on the existing feature branch:

```bash
git switch docs/improve-root-readme
```

Verified current history:

```bash
git log --oneline
```

History before cleanup:

```text
f904e3c typo
9489021 Add contribution note to README
9904953 Improve repository description wording
df2629f Point the root README at LEARNING_PATH.md
fba6fff Add a real description to the root README
```

The extra `typo` commit represented a realistic follow-up fix that should have been part of an earlier commit.

---

## Interactive Rebase

Started an interactive rebase from the branch base:

```bash
git rebase -i e881578
```

Rebase todo list:

```text
pick fba6fff Add a real description to the root README
pick df2629f Point the root README at LEARNING_PATH.md
pick 9904953 Improve repository description wording
squash f904e3c typo
pick 9489021 Add contribution note to README
```

During the rebase I encountered merge conflicts because later commits modified the same sections of `README.md`.

Conflict resolution required:

- editing `README.md`
- staging the resolved file
- continuing the rebase

using:

```bash
git add README.md
git rebase --continue
```

Git replayed each commit until the rebase completed successfully.

---

## Final History

Verified the rewritten history:

```bash
git log --oneline
```

Result:

```text
55798a3 Add contribution note to README
9904953 Improve repository description wording
df2629f Point the root README at LEARNING_PATH.md
fba6fff Add a real description to the root README
```

The temporary `typo` commit no longer appeared in history.

---

## What I Learned

- Interactive rebase rewrites commit history.
- `squash` combines one commit into the commit immediately above it.
- Rewriting history changes commit hashes.
- Interactive rebase may stop for merge conflicts that must be resolved manually.
- History should be cleaned before pushing a feature branch.

---

# Independent Exercise

## Objective

Practice reordering commits using Interactive Rebase and understand how changing commit order can introduce conflicts.

---

## Temporary Branch

Created a throwaway practice branch:

```bash
git switch main
git switch -c practice/rebase-order
```

---

## Original Commit Sequence

Created three commits.

Commit 1

```text
Create rebase practice file
```

File:

```text
Rebase Practice

Status: draft
```

Commit 2

```text
Change status to review
```

Changed:

```text
Status: draft
```

to

```text
Status: review
```

Commit 3

```text
Add owner field
```

Resulting file:

```text
Rebase Practice

Owner: Linh
Status: review
```

Original history:

```text
Add owner field
Change status to review
Create rebase practice file
```

---

## Reordering Commits

Started Interactive Rebase:

```bash
git rebase -i main
```

Changed the todo list from:

```text
pick Create rebase practice file
pick Change status to review
pick Add owner field
```

to:

```text
pick Create rebase practice file
pick Add owner field
pick Change status to review
```

This reordered the commits from:

```
1 → 2 → 3
```

to:

```
1 → 3 → 2
```

---

## Conflict

Git stopped with a merge conflict because the reordered commit expected the file to already contain:

```text
Status: review
```

while the current file still contained:

```text
Status: draft
```

Conflict markers appeared in:

```text
sandbox/02_git_github/REBASE_ORDER.md
```

---

## Conflict Resolution

Resolved the first conflict by preserving only the change introduced by the reordered commit.

Intermediate file:

```text
Rebase Practice

Owner: Linh
Status: draft
```

Completed that commit.

The final commit then changed:

```text
Status: draft
```

to

```text
Status: review
```

Final file:

```text
Rebase Practice

Owner: Linh
Status: review
```

Completed the rebase with:

```bash
git add sandbox/02_git_github/REBASE_ORDER.md
git rebase --continue
```

---

## Final Verification

Verified history:

```bash
git log --oneline
```

Verified commit contents:

```bash
git show HEAD
git show HEAD~1
git show HEAD~2
```

Confirmed that the final history reflected the reordered sequence while preserving the correct file contents.

---

## Cleanup

Returned to `main`.

Deleted the temporary practice branch.

```bash
git switch main
git branch -D practice/rebase-order
```

---

# What I Learned

- Interactive rebase can reorder commits as well as squash them.
- Reordering commits can introduce real merge conflicts.
- Commit dependencies matter.
- Conflicts during rebase are resolved exactly like merge conflicts:
  - edit files
  - `git add`
  - `git rebase --continue`
- A successful rebase preserves the intended final state while producing a cleaner and more logical history.

---

# Commands Practiced

```bash
git rebase -i
git rebase --continue
git add
git log --oneline
git show
git status
git switch
git branch -D
```