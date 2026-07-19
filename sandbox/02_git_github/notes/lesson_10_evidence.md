# Lesson 10 Evidence – Undoing Things Safely: Reset, Revert & Reflog

**Repository:** Learn-DE

**Lesson:** 10 – Undoing Things Safely: Reset, Revert & Reflog

**Completion Date:** 2026-07-19

---

# Guided Exercise

## Objective

Practice undoing Git changes safely by using:

* `git reset --hard`
* `git reflog`
* `git revert`

All work was completed on a temporary practice branch so that the `main` branch remained unchanged.

---

## Practice Branch

Created the temporary branch:

```text
practice/undo-demo
```

The branch was created from:

```text
main
```

---

## Practice Commit

Created the scratch file:

```text
sandbox/02_git_github/UNDO_PRACTICE_SCRATCH.md
```

Added the following content:

```text
bad change
```

Created the commit:

```text
Practice: a commit we'll undo
```

Initial commit information:

```text
<PASTE OUTPUT OF git log --oneline -1 HERE>
```

---

## Hard Reset

Removed the most recent commit using:

```bash
git reset --hard HEAD~1
```

Verified that the scratch file was removed:

```bash
ls sandbox/02_git_github/UNDO_PRACTICE_SCRATCH.md
```

Output:

```text
<PASTE THE FILE-NOT-FOUND OUTPUT HERE>
```

The commit was no longer referenced by the current branch, but it remained available through Git reflog.

---

## Reflog Search

Used the repository reflog to locate the removed commit:

```bash
git reflog
```

Relevant reflog output:

```text
<PASTE REFLOG OUTPUT SHOWING THE LOST COMMIT HERE>
```

The reflog showed the commit created before the hard reset.

Recovered commit hash:

```text
<PASTE RECOVERED COMMIT HASH HERE>
```

---

## Commit Recovery

Recovered the removed commit using:

```bash
git reset --hard <RECOVERED-COMMIT-HASH>
```

Verified the scratch file:

```bash
cat sandbox/02_git_github/UNDO_PRACTICE_SCRATCH.md
```

Output:

```text
bad change
```

This confirmed that the original commit was recovered through reflog rather than recreating the file manually.

---

## Revert

Practiced undoing the recovered commit without rewriting branch history.

```bash
git revert HEAD --no-edit
```

The revert created a new commit that reversed the original change.

Verified that the scratch file was removed again:

```bash
cat sandbox/02_git_github/UNDO_PRACTICE_SCRATCH.md
```

Output:

```text
<PASTE THE FILE-NOT-FOUND OUTPUT HERE>
```

---

## Resulting Commit History

Displayed the branch history:

```bash
git log --oneline
```

Output:

```text
<PASTE LOG SHOWING THE ORIGINAL COMMIT AND REVERT COMMIT HERE>
```

The history contained both:

1. The original practice commit.
2. A new revert commit that reversed it.

This demonstrated that `git revert` preserves history instead of deleting an existing commit.

---

## Guided Exercise Cleanup

Returned to the main branch:

```bash
git switch main
```

Deleted the temporary branch:

```bash
git branch -D practice/undo-demo
```

Confirmation:

```text
<PASTE BRANCH DELETION CONFIRMATION HERE>
```

Verified that the branch no longer existed:

```bash
git branch --list practice/undo-demo
```

Output:

```text
<NO OUTPUT>
```

Confirmed that the guided exercise did not modify the `main` branch.

---

# Independent Exercise

## Objective

Create three commits on a temporary branch, make the newest commits unreachable, locate the lost work through the repository reflog, and recover the correct content into a new branch.

The commit hashes were not recorded before the commits were made unreachable.

---

## Temporary Branch

Created a temporary branch for the independent exercise:

```text
<PASTE ORIGINAL TEMPORARY BRANCH NAME HERE>
```

Created three separate commits on this branch.

Commit descriptions:

```text
Commit 1: <PASTE DESCRIPTION HERE>
Commit 2: <PASTE DESCRIPTION HERE>
Commit 3: <PASTE DESCRIPTION HERE>
```

The commit hashes were intentionally not recorded before continuing.

---

## Making the Commits Unreachable

Moved the branch backward by two commits:

```bash
git reset --hard HEAD~2
```

Switched away from the temporary branch:

```bash
git switch main
```

Deleted the temporary branch pointer:

```bash
git branch -D <TEMPORARY-BRANCH-NAME>
```

At this point, no branch pointed to the most recent lost commit.

---

## Branch Containment Before Recovery

Checked whether any branch contained the lost commit:

```bash
git branch --contains <RECOVERED-HASH>
```

Output before recovery:

```text
<PASTE OUTPUT HERE>
```

Expected result:

```text
<NO BRANCHES LISTED>
```

This confirmed that the commit was not reachable from an existing branch.

---

## Reflog Investigation

Searched the full local reflog:

```bash
git reflog
```

Relevant reflog output:

```text
<PASTE REFLOG SEARCH OUTPUT HERE>
```

Search process:

```text
<DESCRIBE HOW YOU IDENTIFIED THE CORRECT COMMIT>
```

Example description:

```text
I looked for the entries created before the hard reset and branch deletion.
I inspected possible commit hashes with git show until I found the commit
containing the expected third change.
```

Dead ends or incorrect candidates:

```text
<DESCRIBE ANY WRONG COMMITS CHECKED, OR WRITE "None">
```

---

## Verifying the Lost Commit

Inspected the possible lost commit:

```bash
git show <RECOVERED-HASH>
```

Relevant output:

```text
<PASTE OUTPUT SHOWING THE EXPECTED CONTENT HERE>
```

Recovered commit hash:

```text
<PASTE RECOVERED COMMIT HASH HERE>
```

The displayed content matched the third commit created before the branch was deleted.

---

## Recovery Branch

Created a new branch pointing to the recovered commit:

```bash
git switch -c recovery/lesson-10 <RECOVERED-HASH>
```

Recovery branch:

```text
recovery/lesson-10
```

---

## Recovery Validation

Verified the recovered files:

```bash
<PASTE COMMAND USED TO DISPLAY THE RECOVERED CONTENT>
```

Output:

```text
<PASTE RECOVERED CONTENT HERE>
```

Verified the recovered commit:

```bash
git log --oneline -3
```

Output:

```text
<PASTE RECOVERED BRANCH LOG HERE>
```

The recovered content matched the content of the original third commit.

---

## Branch Containment After Recovery

Checked which branch contained the recovered commit:

```bash
git branch --contains <RECOVERED-HASH>
```

Output after recovery:

```text
* recovery/lesson-10
```

This confirmed that the previously unreachable commit was reachable again through the recovery branch.

---

## Independent Exercise Cleanup

Returned to the main branch:

```bash
git switch main
```

Deleted the recovery branch:

```bash
git branch -D recovery/lesson-10
```

Confirmation:

```text
<PASTE BRANCH DELETION CONFIRMATION HERE>
```

Verified that the temporary branches had been removed:

```bash
git branch
```

Output:

```text
<PASTE FINAL BRANCH LIST HERE>
```

Confirmed that no exercise files or commits were added to `main`.

---

# Reset, Revert and Reflog Comparison

## Git Reset

```text
git reset --hard
```

Moves the current branch pointer to another commit and updates both the working tree and staging area.

It can make commits appear lost if no branch or tag still points to them.

---

## Git Revert

```text
git revert
```

Creates a new commit that reverses the changes introduced by an earlier commit.

It preserves the existing commit history and is safer for commits that have already been shared.

---

## Git Reflog

```text
git reflog
```

Records recent movements of local references such as branch updates, resets, checkouts, commits, and rebases.

It can be used to locate commits that are no longer reachable from a branch.

---

# What I Learned

* `git reset --hard` changes branch history and can remove working-tree changes.
* A commit removed by reset may still be recoverable through reflog.
* Reflog records local reference movements even when a branch no longer points to a commit.
* `git show` can be used to inspect a candidate commit before recovering it.
* `git branch --contains` shows whether a commit is reachable from a branch.
* Creating a branch at a lost commit makes that commit reachable again.
* `git revert` creates a new inverse commit and preserves existing history.
* Temporary branches provide a safe environment for practicing destructive Git operations.
* Destructive commands should be tested away from important branches such as `main`.
