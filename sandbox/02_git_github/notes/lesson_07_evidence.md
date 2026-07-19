# Lesson 07 Evidence – Remotes & Connecting to GitHub

**Repository:** Learn-DE

**Lesson:** 07 – Remotes & Connecting to GitHub

**Completion Date:** 2026-07-19

---

# Guided Exercise

## Objective

Practice working with Git remotes, connecting a local repository to GitHub, authenticating with GitHub CLI, and publishing a feature branch.

---

## Verify Remote Configuration

Checked configured remotes.

```bash
git remote -v
```

Example output:

```text
origin  https://github.com/Linhsmiler47/Learn-DE.git (fetch)
origin  https://github.com/Linhsmiler47/Learn-DE.git (push)
```

Updated remote-tracking references.

```bash
git fetch origin
```

Verified the latest commits on the remote main branch.

```bash
git log origin/main --oneline -3
```

Example:

```text
e881578 Add learning path on 07-13
c87bebc Add Data Engineering learning instructions
9678afe Remove Zone.Identifier files and update gitignore
```

---

## GitHub CLI Authentication

Verified GitHub CLI.

```bash
gh auth status
```

Confirmed repository.

```bash
gh repo view
```

Repository:

```text
Linhsmiler47/Learn-DE
```

---

## Publish Feature Branch

Switched to the cleaned feature branch.

```bash
git switch docs/improve-root-readme
```

Published the branch.

```bash
git push -u origin docs/improve-root-readme
```

Git configured upstream tracking.

Example output:

```text
branch 'docs/improve-root-readme' set up to track 'origin/docs/improve-root-readme'
```

---

## Validation

Verified branch tracking.

```bash
git branch -vv
```

Confirmed:

```text
docs/improve-root-readme [origin/docs/improve-root-readme]
```

---

# Independent Exercise

## Objective

Demonstrate the difference between `git fetch` and `git pull`.

---

## Setup

Instead of editing GitHub through the web interface, used a second local clone to simulate another developer.

Created another clone.

```bash
git clone https://github.com/Linhsmiler47/Learn-DE.git Learn-DE-second
```

Checked out the same feature branch.

```bash
git switch docs/improve-root-readme
```

Created a new commit.

```text
Add remote fetch and pull practice note
```

Pushed the commit.

Later created another commit.

```text
Add second remote-only practice note
```

Pushed again.

---

## Fetch

Back in the original repository:

```bash
git fetch origin
```

Observed:

- Remote-tracking branch updated.
- Local branch remained unchanged until pull.

Evidence collected:

```bash
git log origin/docs/improve-root-readme --oneline
git log docs/improve-root-readme --oneline
```

At this stage:

- `origin/docs/improve-root-readme` pointed to the newest remote commit.
- `docs/improve-root-readme` still pointed to the previous local commit.
- The working tree was unchanged.

This demonstrated that **`git fetch` only updates local knowledge of the remote and does not modify the checked-out branch.**

---

## Pull

Integrated the remote changes.

```bash
git pull
```

Verified:

```bash
git log origin/docs/improve-root-readme --oneline -3
git log docs/improve-root-readme --oneline -3
git status
```

Output:

```text
=== REMOTE AFTER PULL ===

2f4bcbd Add second remote-only practice note
9fb49fe Add remote fetch and pull practice note
55798a3 Add contribution note to README

=== LOCAL AFTER PULL ===

2f4bcbd Add second remote-only practice note
9fb49fe Add remote fetch and pull practice note
55798a3 Add contribution note to README
```

`git status` reported:

```text
Your branch is up to date with 'origin/docs/improve-root-readme'.
```

README also contained both newly added lines:

```text
Remote fetch/pull practice.
Second remote-only practice update.
```

---

## Cleanup

Removed the temporary clone.

```bash
rm -rf ~/Projects/Learn-DE-second
```

The feature branch `docs/improve-root-readme` was intentionally kept because it will be used in Lesson 08.

---

# What I Learned

- A remote stores another copy of the repository.
- `origin` is the default remote created by cloning.
- `git fetch` downloads new commits and updates remote-tracking branches without modifying the current branch.
- `git pull` performs a fetch followed by integrating the fetched changes into the current branch.
- Upstream tracking allows simple commands such as `git pull` and `git push` without explicitly specifying the remote and branch.
- GitHub CLI simplifies authentication and repository management from the terminal.

---

# Commands Practiced

```bash
git remote -v
git fetch
git log
git switch
git push -u
git branch -vv
git pull
gh auth status
gh repo view
```