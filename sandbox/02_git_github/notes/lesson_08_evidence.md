# Lesson 08 Evidence – Pull Requests & Code Review Workflow

**Repository:** Learn-DE

**Lesson:** 08 – Pull Requests & Code Review Workflow

**Completion Date:** 2026-07-19

---

# Guided Exercise

## Objective

Create a real Pull Request, review the proposed changes, merge through GitHub, and verify the result on the main branch.

---

## Pull Request

Created a Pull Request from:

```text
docs/improve-root-readme
```

into:

```text
main
```

PR URL:

```text
<PASTE YOUR PR URL HERE>
```

---

## PR Title

```text
Add a real description to the root README
```

---

## PR Description

```text
The root README was just a title. This adds a short, real description of the repository, links to the learning roadmap, and adds contribution guidance.
```

---

## Review

Reviewed the changes through GitHub's **Files changed** page.

Review comment:

```text
<PASTE YOUR REAL REVIEW COMMENT HERE>
```

Example:

```text
The learning roadmap link is placed near the repository description so new contributors can quickly find the recommended learning sequence.
```

Because I am the repository owner and only contributor, GitHub does not allow me to approve my own Pull Request. I completed the review by leaving a real review comment before merging.

---

## Merge Strategy

Merged using:

```text
Squash and merge
```

Reason:

- This feature represented one logical change.
- The branch contained multiple development commits.
- Squashing kept the `main` history clean and easy to read.

Merge confirmation:

```text
<OPTIONAL: paste merge confirmation message>
```

---

## Validation

Updated the local repository.

```bash
git switch main
git pull --ff-only
```

Verified the latest commits.

```bash
git log --oneline -3
```

Output:

```text
<PASTE OUTPUT HERE>
```

Verified README.

```bash
cat README.md
```

Final README:

```text
<PASTE FINAL README CONTENT HERE>
```

Confirmed that the new repository description now exists on `main`.

---

# Independent Exercise

## Objective

Repeat the complete Pull Request workflow for the `.gitattributes` branch and configure branch protection.

---

## Pull Request

Branch:

```text
phase-02/gitattributes
```

PR URL:

```text
<PASTE SECOND PR URL HERE>
```

---

## PR Description

```text
This PR adds a repository-wide .gitattributes file to normalize text line endings and identify common binary data files so Git handles them consistently across operating systems.
```

---

## Branch Protection

Repository visibility:

```text
Public
```

Configured a branch ruleset protecting:

```text
main
```

Rules enabled:

- Require a pull request before merging

GitHub Ruleset status:

```text
Active
```

---

## Direct Push Test

Created a trivial local commit on `main`.

Attempted:

```bash
git push origin main
```

GitHub response:

```text
<PASTE THE ACTUAL REJECTED PUSH ERROR MESSAGE HERE>
```

This confirmed that direct pushes to `main` were blocked by branch protection.

Reset the temporary local commit.

```bash
git reset --hard origin/main
```

---

## Review

Reviewed the Pull Request through GitHub.

Review comment:

```text
<PASTE YOUR REAL REVIEW COMMENT HERE>
```

---

## Merge Strategy

Chosen strategy:

```text
Squash and merge
```

Justification:

The `.gitattributes` branch introduced one repository configuration change. Squashing combined the implementation history into one clean commit while preserving a concise history on `main`.

---

## Validation

Updated the local repository.

```bash
git switch main
git pull --ff-only
```

Verified history.

```bash
git log --oneline -5
```

Output:

```text
<PASTE OUTPUT HERE>
```

Verified the `.gitattributes` file.

```bash
cat .gitattributes
```

Confirmed that `.gitattributes` is now present on `main`.

---

# What I Learned

- A Pull Request provides a structured workflow for reviewing code before merging.
- GitHub allows inline review comments to explain implementation decisions.
- Squash merge is useful when multiple development commits represent one logical change.
- Branch protection prevents direct changes to important branches.
- Requiring Pull Requests encourages review and maintains a cleaner project history.
- GitHub CLI simplifies creating and managing Pull Requests from the terminal.

---

# Commands Practiced

```bash
gh pr create
gh pr view
gh pr diff
gh pr merge --squash --delete-branch
git switch
git pull --ff-only
git log
git push
git reset --hard
```