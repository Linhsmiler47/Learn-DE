# Lesson 05 Evidence – Merge Conflicts

**Repository:** Learn-DE

**Lesson:** 05 – Merge Conflicts

**Completion Date:** 2026-07-19

---

# Guided Exercise

## Objective

Practice creating, identifying, resolving, and completing a merge conflict using two feature branches.

---

## Branch A

Created a feature branch from `main`.

```bash
git switch main
git switch -c practice/conflict-a
```

Created the scratch file.

```text
Version from branch A
```

Committed the change.

```bash
git add -f sandbox/02_git_github/CONFLICT_PRACTICE_SCRATCH.md
git commit -m "Practice: add scratch file, branch A version"
```

---

## Branch B

Returned to `main` and created another feature branch.

```bash
git switch main
git switch -c practice/conflict-b
```

Created the same file with different contents.

```text
Version from branch B
```

Committed the change.

```bash
git add -f sandbox/02_git_github/CONFLICT_PRACTICE_SCRATCH.md
git commit -m "Practice: add scratch file, branch B version"
```

---

## Merge Conflict

Merged `practice/conflict-b` into `practice/conflict-a`.

```bash
git switch practice/conflict-a
git merge practice/conflict-b
```

Git reported:

```text
CONFLICT (add/add): Merge conflict in sandbox/02_git_github/CONFLICT_PRACTICE_SCRATCH.md
Automatic merge failed; fix conflicts and then commit the result.
```

Conflict markers:

```text
<<<<<<< HEAD
Version from branch A
=======
Version from branch B
>>>>>>> practice/conflict-b
```

---

## Conflict Resolution

Resolved the conflict by preserving the information from both branches.

Final file:

```text
Conflict practice resolution

- Branch A proposed: Version from branch A
- Branch B proposed: Version from branch B
- Resolution: both versions were reviewed and preserved in this combined result.
```

Completed the merge.

```bash
git add -f sandbox/02_git_github/CONFLICT_PRACTICE_SCRATCH.md
git commit -m "Practice: resolve conflict in scratch file"
```

Verified:

```bash
git show HEAD:sandbox/02_git_github/CONFLICT_PRACTICE_SCRATCH.md
git log --graph --oneline --decorate
```

---

## Cleanup

Returned to `main`.

Deleted temporary branches.

```bash
git switch main
git branch -D practice/conflict-a
git branch -D practice/conflict-b
```

Verified that `main` remained unchanged.

---

# Independent Exercise

## Objective

Resolve a merge conflict by combining two valid changes instead of selecting only one version.

---

## Branch Alpha

Created branch.

```bash
git switch main
git switch -c practice/list-alpha
```

Created initial file.

```text
Learning Tasks

- Learn Linux
- Learn Git
```

Committed.

Added one new task.

```text
Learning Tasks

- Learn Linux
- Learn Git
- Practice branching
```

Committed again.

---

## Branch Beta

Created another branch from `main`.

```bash
git switch main
git switch -c practice/list-beta
```

Created the same initial file.

Added a different task.

```text
Learning Tasks

- Learn Linux
- Learn Git
- Practice merging
```

Committed.

---

## Merge Conflict

Merged Beta into Alpha.

```bash
git switch practice/list-alpha
git merge practice/list-beta
```

Git produced an add/add conflict.

Conflict markers:

```text
Learning Tasks

- Learn Linux
- Learn Git
<<<<<<< HEAD
- Practice branching
=======
- Practice merging
>>>>>>> practice/list-beta
```

---

## Resolution

Instead of choosing one version, combined both valid changes.

Final file:

```text
Learning Tasks

- Learn Linux
- Learn Git
- Practice branching
- Practice merging
```

Completed merge.

```bash
git add -f sandbox/02_git_github/MERGE_LIST.md
git commit -m "Practice: combine both learning tasks"
```

Verified merge commit.

```text
Merge: 5a2ed95 9a646ea
```

Confirmed history.

```bash
git log --graph --oneline --decorate
```

---

## Cleanup

Deleted temporary branches.

```bash
git switch main
git branch -D practice/list-alpha
git branch -D practice/list-beta
```

Confirmed that `main` still matched `origin/main`.

---

# What I Learned

* Merge conflicts occur when Git cannot automatically combine changes.
* Conflict markers identify the competing versions.
* Resolving a conflict requires editing the file manually.
* `git add` marks a conflicted file as resolved.
* A merge is completed only after creating a merge commit.
* The correct resolution is not always choosing one side; often the right solution is to preserve both changes.
* `git log --graph` helps visualize branch history and merge commits.

---

# Commands Practiced

```bash
git switch
git merge
git add
git commit
git status
git show
git log --graph --oneline --decorate
git branch -D
```
