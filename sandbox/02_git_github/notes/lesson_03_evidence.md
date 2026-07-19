# Lesson 03 Evidence — Staging, Committing & Commit Hygiene

## Guided Exercise

### Commands Used

```bash
cd ~/Projects/Learn-DE

git switch -c docs/improve-root-readme

cat README.md

# Edited README.md to add a real repository description

git status
git diff

git add README.md
git diff --staged

git commit -m "Add a real description to the root README"

# Edited README.md again to point to LEARNING_PATH.md

git status
git diff

git add README.md
git diff --staged

git commit -m "Point the root README at LEARNING_PATH.md"

git log --oneline -2
```

---

### README After First Edit

```markdown
# Learn-DE

Learn-DE is a hands-on repository for learning Data Engineering through practical exercises and real Git workflows.
It contains lessons, guided exercises, independent exercises, and notes covering Linux, Git, and other core Data Engineering topics.
```

---

### `git status` Before First Commit

```text
On branch docs/improve-root-readme

Changes not staged for commit:
        modified: README.md

Untracked files:
        sandbox/02_git_github/notes/lesson_01_evidence.md
        sandbox/02_git_github/notes/lesson_02_evidence.md
```

---

### `git diff` Before First Commit

```diff
diff --git a/README.md b/README.md
@@
 # Learn-DE

+Learn-DE is a hands-on repository for learning Data Engineering through practical exercises and real Git workflows.
+It contains lessons, guided exercises, independent exercises, and notes covering Linux, Git, and other core Data Engineering topics.
```

---

### `git diff --staged` Before First Commit

```diff
diff --git a/README.md b/README.md
@@
 # Learn-DE

+Learn-DE is a hands-on repository for learning Data Engineering through practical exercises and real Git workflows.
+It contains lessons, guided exercises, independent exercises, and notes covering Linux, Git, and other core Data Engineering topics.
```

---

### README After Second Edit

```markdown
See `LEARNING_PATH.md` for the complete learning roadmap.
```

---

### `git status` Before Second Commit

```text
On branch docs/improve-root-readme

Changes not staged for commit:
        modified: README.md
```

---

### `git diff` Before Second Commit

```diff
diff --git a/README.md b/README.md
@@
 See `LEARNING_PATH.md` for the complete learning roadmap.
```

---

### `git diff --staged` Before Second Commit

```diff
diff --git a/README.md b/README.md
@@
 See `LEARNING_PATH.md` for the complete learning roadmap.
```

---

### Guided Exercise Validation

```bash
git log --oneline -2
```

Output:

```text
df2629f (HEAD -> docs/improve-root-readme) Point the root README at LEARNING_PATH.md
fba6fff Add a real description to the root README
```

---

# Independent Exercise — Splitting Mixed Changes with `git add -p`

## Goal

Practice splitting unrelated edits into separate atomic commits using `git add -p`.

---

## Two Unrelated Changes

### Edit 1

Changed the wording of the repository description.

```diff
-Learn-DE is a hands-on repository for learning Data Engineering through practical exercises and real Git workflows.
+Learn-DE is practical learning repository for learning Data Engineering through practical exercises and real Git workflows.
```

### Edit 2

Added a contribution note at the end of the README.

```markdown
Contributions and suggestions are welcome.
```

---

## Commands Used

```bash
git diff

git add -p README.md

git diff --staged

git commit -m "Improve repository description wording"

git add -p README.md

git diff --staged

git commit -m "Add contribution note to README"

git show HEAD
git show HEAD~1

git log --oneline -2
```

---

## `git add -p` Session

```text
(1/1) Stage this hunk [y,n,q,a,d,s,e,p,P,?]? s

Split into 2 hunks.

(1/2) Stage this hunk [y,n,q,a,d,k,K,j,J,g,/,e,p,P,?]? y

(2/2) Stage this hunk [y,n,q,a,d,k,K,j,J,g,/,e,p,P,?]? n
```

Second staging session:

```text
(1/1) Stage this hunk [y,n,q,a,d,s,e,p,P,?]? y
```

---

## First Commit Diff

```bash
git show HEAD~1
```

Output:

```diff
commit 9904953f648511ceda871f480c4c5df199e7bfaf

Author: Linh Tran

    Improve repository description wording

diff --git a/README.md b/README.md
@@
-Learn-DE is a hands-on repository for learning Data Engineering through practical exercises and real Git workflows.
+Learn-DE is practical learning repository for learning Data Engineering through practical exercises and real Git workflows.
```

This commit contains only the wording improvement.

---

## Second Commit Diff

```bash
git show HEAD
```

Output:

```diff
commit 9489021680230014d1972a6ca1fd7890d8c8f9a6

Author: Linh Tran

    Add contribution note to README

diff --git a/README.md b/README.md
@@
+Contributions and suggestions are welcome.
```

This commit contains only the contribution note.

---

## Independent Exercise Validation

```bash
git log --oneline -2
```

Output:

```text
9489021 (HEAD -> docs/improve-root-readme) Add contribution note to README
9904953 Improve repository description wording
```

### Conclusion

The two unrelated edits were made before any commit and then successfully separated into two atomic commits using `git add -p`. Each commit contains exactly one logical change, demonstrating proper staging and commit hygiene.
