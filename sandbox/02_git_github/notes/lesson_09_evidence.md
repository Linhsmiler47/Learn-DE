# Lesson 09 Evidence – Issues & Releases

**Repository:** Learn-DE

**Lesson:** 09 – Issues & Releases

**Completion Date:** 2026-07-19

---

# Guided Exercise

## Objective

Practice creating GitHub Issues, creating Releases from Git tags, and managing repository releases.

---

## GitHub Issue

Created a GitHub Issue using GitHub CLI.

Example command:

```bash
gh issue create
```

Verified the issue was successfully created.

---

## Git Tag

Created a practice Git tag.

```bash
git tag v0.0.1-practice
```

Pushed the tag.

```bash
git push origin v0.0.1-practice
```

---

## GitHub Release

Created a GitHub Release from the practice tag.

Verified the Release on GitHub.

Deleted the Release and removed the practice tag after completing the exercise.

---

# Independent Exercise

## Objective

Complete a real GitHub workflow using Issues, branches, Pull Requests, and Releases.

---

## Branch

Created a working branch.

```text
fix/wording-lesson-doc
```

---

## Documentation Change

Updated the guided exercise heading.

Changed:

```text
## Steps
```

to:

```text
## Steps to do
```

File modified:

```text
sandbox/02_git_github/exercises/09_issues_releases/guided.md
```

---

## Commit

Commit message:

```text
Clarify Lesson 09 guided exercise heading
```

---

## Pull Request

Created a Pull Request for the documentation update.

PR Title:

```text
Clarify Lesson 09 guided exercise heading
```

Merge strategy:

```text
Squash and merge
```

The Pull Request was merged successfully.

---

## Validation

Updated the local repository.

```bash
git switch main
git pull --ff-only
```

Verified that the merged changes were present on the `main` branch.

---

## Issue Verification

Checked GitHub Issues.

```bash
gh issue list --state closed
```

Result:

```text
no issues match your search in Linhsmiler47/Learn-DE
```

The Pull Request was merged successfully.

However, no GitHub Issue was automatically closed because the merged Pull Request was not linked to an existing Issue using a closing keyword.

---

# What I Learned

- GitHub Issues are used to track planned work.
- Git tags identify specific repository versions.
- GitHub Releases are created from Git tags.
- Pull Requests provide a structured workflow for merging changes.
- Squash merge keeps the commit history clean.
- Linking a Pull Request with `Fixes #<issue>` automatically closes the related Issue after the PR is merged.

---

# Commands Practiced

```bash
gh issue create
gh issue list
gh issue view
git tag
git push origin <tag>
gh release create
gh release delete
git tag -d
git push --delete origin <tag>
git switch
git add
git commit
git push
gh pr create
gh pr view
gh pr merge --squash --delete-branch
git pull --ff-only
```