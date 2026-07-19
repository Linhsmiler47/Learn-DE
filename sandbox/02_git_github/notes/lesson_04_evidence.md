# Lesson 04 Evidence — Branching Fundamentals & the HEAD Pointer

## Guided Exercise

### Step 1 — Inspect Existing Branches and Commit Graph

Commands:

```bash
cd ~/Projects/Learn-DE
git branch
git --no-pager log --graph --oneline --all
```

Output:

```text
  docs/improve-root-readme
* main
  phase-02/gitattributes
  practice/branch-mechanics
  practice/git-add-p

* 9489021 (practice/branch-mechanics, docs/improve-root-readme) Add contribution note to README
* 9904953 Improve repository description wording
* df2629f Point the root README at LEARNING_PATH.md
* fba6fff Add a real description to the root README
| * 7e029c2 (phase-02/gitattributes) Add .gitattributes for line-ending normalization and binary data files
|/
* e881578 (HEAD -> main, origin/main, practice/git-add-p) Add learning path on 07-13
* c87bebc Add Data Engineering learning instructions
* 9678afe Remove Zone.Identifier files and update gitignore
* f3f1329 Initial commit
```

At this point, `HEAD` pointed to `main`, and `main` pointed to commit `e881578`.

The branch `docs/improve-root-readme` pointed to commit `9489021`, which was four commits ahead of `main`.

The branch `phase-02/gitattributes` pointed to its own independent commit, `7e029c2`.

---

### Step 2 — Compare `main` and `docs/improve-root-readme`

Commands:

```bash
git --no-pager log main..docs/improve-root-readme --oneline
git --no-pager log docs/improve-root-readme..main --oneline
```

Output:

```text
9489021 Add contribution note to README
9904953 Improve repository description wording
df2629f Point the root README at LEARNING_PATH.md
fba6fff Add a real description to the root README
```

The second command produced no output:

```text
```

Explanation:

```text
git log main..docs/improve-root-readme --oneline
```

shows commits that are reachable from `docs/improve-root-readme` but not reachable from `main`.

In this repository, it displayed the four Lesson 03 commits because the documentation branch had moved ahead while `main` had remained at commit `e881578`.

The reverse command:

```text
git log docs/improve-root-readme..main --oneline
```

shows commits reachable from `main` but not from `docs/improve-root-readme`.

It produced no output because `main` had not received any new commits after the two branches separated.

---

### Step 3 — Switch Branches and Compare `README.md`

Commands:

```bash
git switch main
cat README.md

git switch docs/improve-root-readme
cat README.md
```

Output on `main`:

```text
Already on 'main'
Your branch is up to date with 'origin/main'.

# Learn-DE
```

Output on `docs/improve-root-readme`:

```text
Switched to branch 'docs/improve-root-readme'

# Learn-DE

Learn-DE is practical learning repository for learning Data Engineering through practical exercises and real Git workflows.
It contains lessons, guided exercises, independent exercises, and notes covering Linux, Git, and other core Data Engineering topics.

See `LEARNING_PATH.md` for the complete learning roadmap.

Contributions and suggestions are welcome.
```

This demonstrated that switching branches updates the working tree to match the commit referenced by the selected branch.

The changes from Lesson 03 were visible on `docs/improve-root-readme` but not on `main`.

---

### Step 4 — Practice Branch Creation and Deletion

A branch named `practice/branch-mechanics` already existed from an earlier attempt and pointed to commit `9489021`.

Attempting to recreate and delete it produced:

```text
fatal: a branch named 'practice/branch-mechanics' already exists
```

and:

```text
error: the branch 'practice/branch-mechanics' is not fully merged
hint: If you are sure you want to delete it, run 'git branch -D practice/branch-mechanics'
```

The existing branch did not contain unique work because the same commit was still referenced by `docs/improve-root-readme`, so it was safely removed:

```bash
git switch main
git branch -D practice/branch-mechanics
```

Output:

```text
Already on 'main'
Your branch is up to date with 'origin/main'.
Deleted branch practice/branch-mechanics (was 9489021).
```

The branch was then recreated correctly from `main`:

```bash
git switch -c practice/branch-mechanics
git branch
```

Output:

```text
Switched to a new branch 'practice/branch-mechanics'

  docs/improve-root-readme
  main
  phase-02/gitattributes
* practice/branch-mechanics
  practice/git-add-p
```

The branch was switched away from and deleted normally:

```bash
git switch main
git branch -d practice/branch-mechanics
```

Output:

```text
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
Deleted branch practice/branch-mechanics (was e881578).
```

Final branch list:

```bash
git branch
```

Output:

```text
  docs/improve-root-readme
* main
  phase-02/gitattributes
  practice/git-add-p
```

This time, normal deletion with `-d` succeeded because `practice/branch-mechanics` had no unique commit and pointed to the same commit as `main`.

---

## Guided Exercise Conclusion

The guided exercise demonstrated that:

* Branches are movable references to commits.
* `HEAD` identifies the currently checked-out branch.
* Switching branches changes the working tree to match the selected branch.
* Range notation such as `main..branch` compares commits reachable from one reference but not another.
* A branch with no unique commits can be safely removed with `git branch -d`.

---

# Independent Exercise

## Goal

Create two independent branches from `main`, add one throwaway commit to each branch, compare the real Git graph with a self-created pointer diagram, and delete both branches without merging.

The two branches used were:

```text
practice/pointer-alpha
practice/pointer-beta
```

The throwaway commits were:

```text
ced2aee Add alpha pointer practice file
4c317c6 Add beta pointer practice file
```

---

## Stage 1 — Before Either Practice Branch Existed

Command:

```bash
git switch main
git --no-pager log --graph --oneline --all --decorate
```

Relevant output:

```text
* 9489021 (docs/improve-root-readme) Add contribution note to README
* 9904953 Improve repository description wording
* df2629f Point the root README at LEARNING_PATH.md
* fba6fff Add a real description to the root README
| * 7e029c2 (phase-02/gitattributes) Add .gitattributes for line-ending normalization and binary data files
|/
* e881578 (HEAD -> main, origin/main, practice/git-add-p) Add learning path on 07-13
* c87bebc Add Data Engineering learning instructions
* 9678afe Remove Zone.Identifier files and update gitignore
* f3f1329 Initial commit
```

Pointer diagram:

```text
HEAD
  |
  v
main
  |
  v
e881578
```

At this stage, `HEAD` pointed to `main`, and `main` pointed to commit `e881578`.

Neither practice branch existed yet.

---

## Stage 2 — After Creating Branch A

Commands:

```bash
git switch -c practice/pointer-alpha
git --no-pager log --graph --oneline --all --decorate
```

Relevant output:

```text
* e881578 (HEAD -> practice/pointer-alpha, origin/main, practice/git-add-p, main) Add learning path on 07-13
```

Pointer diagram:

```text
HEAD
  |
  v
practice/pointer-alpha
  |
  +------> e881578
             ^
             |
            main
```

Both `main` and `practice/pointer-alpha` pointed to the same commit.

`HEAD` pointed to `practice/pointer-alpha`, indicating that it was the currently checked-out branch.

---

## Stage 3 — After Committing on Branch A

Commands:

```bash
mkdir -p sandbox/02_git_github/workspace/lesson04-alpha

echo "Branch alpha practice file" \
  > sandbox/02_git_github/workspace/lesson04-alpha/alpha.txt

git add -f sandbox/02_git_github/workspace/lesson04-alpha/alpha.txt
git commit -m "Add alpha pointer practice file"

git --no-pager log --graph --oneline --all --decorate
```

Commit output:

```text
[practice/pointer-alpha ced2aee] Add alpha pointer practice file
 1 file changed, 1 insertion(+)
 create mode 100644 sandbox/02_git_github/workspace/lesson04-alpha/alpha.txt
```

Relevant graph:

```text
* ced2aee (HEAD -> practice/pointer-alpha) Add alpha pointer practice file
|
* e881578 (origin/main, practice/git-add-p, main) Add learning path on 07-13
```

Pointer diagram:

```text
HEAD
  |
  v
practice/pointer-alpha
  |
  v
ced2aee
  |
  v
e881578
  ^
  |
 main
```

The commit moved `practice/pointer-alpha` forward from `e881578` to `ced2aee`.

`main` remained unchanged at `e881578`.

---

## Stage 4 — After Creating Branch B from `main`

Commands:

```bash
git switch main
git switch -c practice/pointer-beta

git --no-pager log --graph --oneline --all --decorate
```

Relevant graph:

```text
* ced2aee (practice/pointer-alpha) Add alpha pointer practice file
|
* e881578 (HEAD -> practice/pointer-beta, origin/main, practice/git-add-p, main) Add learning path on 07-13
```

Pointer diagram:

```text
practice/pointer-alpha
          |
          v
       ced2aee
          |
          v
       e881578
       ^     ^
       |     |
     main   practice/pointer-beta
               ^
               |
              HEAD
```

Branch B was created from `main`, not from branch A.

Therefore, `practice/pointer-beta` pointed to `e881578`, while `practice/pointer-alpha` remained at `ced2aee`.

The file committed on branch A was not present on branch B.

---

## Stage 5 — After Committing on Branch B

Commands:

```bash
mkdir -p sandbox/02_git_github/workspace/lesson04-beta

echo "Branch beta practice file" \
  > sandbox/02_git_github/workspace/lesson04-beta/beta.txt

git add -f sandbox/02_git_github/workspace/lesson04-beta/beta.txt
git commit -m "Add beta pointer practice file"

git --no-pager log --graph --oneline --all --decorate
```

Commit output:

```text
[practice/pointer-beta 4c317c6] Add beta pointer practice file
 1 file changed, 1 insertion(+)
 create mode 100644 sandbox/02_git_github/workspace/lesson04-beta/beta.txt
```

Pointer diagram:

```text
practice/pointer-alpha          practice/pointer-beta
          |                               |
          v                               v
       ced2aee                          4c317c6
           \                             /
            \                           /
             +-------- e881578 --------+
                         ^
                         |
                        main

HEAD -> practice/pointer-beta
```

A history-oriented version of the same diagram:

```text
             ced2aee  alpha commit
            /        practice/pointer-alpha
e881578 ----
            \
             4c317c6  beta commit
                      practice/pointer-beta
                      HEAD
```

Both commits had the same parent, `e881578`.

Neither commit changed the `main` pointer.

Branch A did not move when branch B received a commit, and branch B did not contain branch A's commit.

---

## Independent Branch Validation

Commands:

```bash
git --no-pager log main..practice/pointer-alpha --oneline
git --no-pager log main..practice/pointer-beta --oneline
```

Output:

```text
ced2aee (practice/pointer-alpha) Add alpha pointer practice file
```

```text
4c317c6 (HEAD -> practice/pointer-beta) Add beta pointer practice file
```

This confirmed that each branch had exactly one commit that was not reachable from `main`.

It also confirmed that the branches had independent histories after starting from the same commit.

---

## Initial Mismatch and Correction

During the first attempt, the directory:

```text
sandbox/02_git_github/workspace/lesson04
```

was created and committed only on branch A.

After switching back to `main` and creating branch B, the directory was no longer present in the working tree.

The attempt to create `beta.txt` inside that directory failed:

```text
bash: sandbox/02_git_github/workspace/lesson04/beta.txt: No such file or directory
```

Git also reported:

```text
fatal: pathspec 'sandbox/02_git_github/workspace/lesson04/beta.txt' did not match any files
```

The initial diagram assumed the directory would still be available after switching branches. The actual result showed that this assumption was incorrect.

The directory belonged to branch A's commit. Since branch B was created from `main`, branch B did not contain branch A's committed file or directory.

The exercise was repeated using separate directories:

```text
sandbox/02_git_github/workspace/lesson04-alpha
sandbox/02_git_github/workspace/lesson04-beta
```

This mismatch helped demonstrate the pointer model more clearly: creating branch B from `main` gave branch B the repository state stored at `main`, not the state stored at branch A.

---

## Cleanup

The two branches were throwaway branches and were not merged.

Commands:

```bash
git switch main
git branch -D practice/pointer-alpha
git branch -D practice/pointer-beta

git branch
git status
```

Because both branches contained unmerged commits, forced deletion with `-D` was used intentionally.

Expected deletion output:

```text
Deleted branch practice/pointer-alpha (was ced2aee).
Deleted branch practice/pointer-beta (was 4c317c6).
```

Final branch list:

```text
  docs/improve-root-readme
* main
  phase-02/gitattributes
  practice/git-add-p
```

Final status:

```text
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
        sandbox/02_git_github/notes/lesson_01_evidence.md
        sandbox/02_git_github/notes/lesson_02_evidence.md
        sandbox/02_git_github/notes/lesson_03_evidence.md

nothing added to commit but untracked files present
```

---

## Independent Exercise Conclusion

This exercise demonstrated that branches are independent movable pointers.

Both practice branches started at the same commit:

```text
e881578
```

After one commit on each branch:

```text
practice/pointer-alpha -> ced2aee
practice/pointer-beta  -> 4c317c6
main                   -> e881578
```

The commit on branch A did not move branch B or `main`.

The commit on branch B did not move branch A or `main`.

`HEAD` followed whichever branch was currently checked out, and a new commit advanced only that branch's pointer.

Deleting the branch pointers did not merge their commits into `main`.
