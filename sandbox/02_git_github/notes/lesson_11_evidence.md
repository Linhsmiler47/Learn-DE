# Lesson 11 Evidence – Secret Management, Repository Hygiene & Maintenance

**Repository:** Learn-DE

**Lesson:** 11 – Secret Management, Repository Hygiene & Maintenance

**Completion Date:** 2026-07-19

---

# Guided Exercise

## Objective

Audit the repository for accidentally committed secrets, verify that secret-related files are ignored, review the repository security configuration, and document a secret-management incident or practice scenario.

---

## Secret History Audit

Checked whether a `.env` file had ever been committed:

```bash
git log --all --full-history -- .env
```

Output:

```text
<PASTE ACTUAL OUTPUT HERE>
```

Expected result:

```text
<NO OUTPUT>
```

No output means that a `.env` file has not appeared in the repository history.

---

## Private Key File Audit

Searched the repository for common private key filenames:

```bash
find . -iname "*.pem" -o -iname "id_rsa*" -o -iname "id_ed25519*" 2>/dev/null | grep -v "^\./\.git"
```

Output:

```text
<PASTE ACTUAL OUTPUT HERE>
```

Expected result:

```text
<NO OUTPUT>
```

No private key files were found outside the `.git` directory.

---

## Gitignore Verification

Checked whether `.gitignore` contains rules for secret-related files:

```bash
cat .gitignore | grep -A3 Secrets
```

Output:

```text
<PASTE ACTUAL .GITIGNORE OUTPUT HERE>
```

Verified that secret files such as `.env` are excluded from Git tracking.

If no matching section was found, record the real result:

```text
No section named "Secrets" was found in the current .gitignore file.
```

---

## Environment Variable Pattern

Created a disposable environment-variable example at:

```text
sandbox/02_git_github/workspace/env_pattern_demo/.env.example
```

File content:

```dotenv
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
API_KEY=your-api-key-here
```

This file demonstrates how required environment variables can be documented without storing real credentials.

The values are placeholders and are not real secrets.

---

## Repository Security Settings

Checked the repository configuration using:

```bash
gh api repos/Linhsmiler47/Learn-DE | grep -i "security\|visibility"
```

Output:

```text
<PASTE ACTUAL OUTPUT HERE>
```

Repository visibility:

```text
<PASTE public, private, OR internal HERE>
```

Checked GitHub:

```text
Settings → Code security and analysis
```

Current security settings:

```text
Dependency graph: <ENABLED OR DISABLED>
Dependabot alerts: <ENABLED OR DISABLED>
Dependabot security updates: <ENABLED OR DISABLED>
Secret scanning: <ENABLED OR DISABLED OR UNAVAILABLE>
Push protection: <ENABLED OR DISABLED OR UNAVAILABLE>
Private vulnerability reporting: <ENABLED OR DISABLED>
```

These values record the actual security configuration at the time the exercise was completed.

---

## Push Protection Incident

### Incident Status

```text
<CHOOSE ONE: Real incident occurred / No real incident has occurred>
```

### Real Incident

Use this section only if GitHub previously blocked a push containing a secret.

Secret type:

```text
<PASTE SECRET TYPE HERE>
```

GitHub response:

```text
<PASTE THE ACTUAL PUSH PROTECTION MESSAGE HERE>
```

Action taken:

```text
<DESCRIBE HOW THE SECRET WAS REMOVED OR REPLACED>
```

The secret was not pushed after GitHub detected it.

### Practice Scenario

Use this section if no real push-protection incident has occurred.

```text
No real push-protection incident has occurred in this repository yet.
Instead, I reviewed a deliberate practice scenario using a clearly fake
credential to understand how secret detection and remediation should work.
```

Example fake credential:

```text
FAKE_API_KEY=sk_test_this_is_not_real_1234567890
```

The value is clearly fake and was used only for local practice.

---

# Independent Exercise

## Objective

Commit a clearly fake secret on a temporary local branch, remove it from the branch history using interactive rebase, and confirm that the secret no longer appears anywhere in that branch's history.

The practice branch was never pushed.

---

## Safety Precautions

Only a fake value was used:

```text
FAKE_API_KEY=sk_test_this_is_not_real_1234567890
```

No real credential was used at any point.

The exercise was completed on a throwaway local branch.

---

## Temporary Branch

Created the temporary branch:

```text
<PASTE TEMPORARY BRANCH NAME HERE>
```

Example:

```text
practice/secret-cleanup
```

The branch was created from:

```text
main
```

The branch was not pushed to GitHub.

---

## Fake Secret File

Created a scratch file containing the fake secret.

File:

```text
<PASTE SCRATCH FILE PATH HERE>
```

Content:

```text
FAKE_API_KEY=sk_test_this_is_not_real_1234567890
```

Created a local commit containing this file.

Commit message:

```text
<PASTE ORIGINAL COMMIT MESSAGE HERE>
```

Initial history:

```bash
git log --oneline
```

Output:

```text
<PASTE INITIAL COMMIT HISTORY HERE>
```

---

## Secret Removal Process

Started an interactive rebase to edit or remove the commit containing the fake secret.

```bash
git rebase -i <BASE-COMMIT>
```

Chosen rebase action:

```text
<PASTE edit, drop, OR OTHER ACTION HERE>
```

### Method Used

```text
<DESCRIBE THE ACTUAL REMOVAL PROCESS HERE>
```

Example using `edit`:

```text
I marked the secret-containing commit as edit in the interactive rebase.
When Git stopped at that commit, I removed the fake secret from the file,
amended the commit, and continued the rebase.
```

Example commands:

```bash
git rebase -i HEAD~2
```

```bash
nano <SCRATCH-FILE>
```

```bash
git add <SCRATCH-FILE>
git commit --amend --no-edit
git rebase --continue
```

Record only the commands and method actually used.

---

## Cleaned History

Displayed the rewritten branch history:

```bash
git log --oneline
```

Output:

```text
<PASTE CLEANED COMMIT HISTORY HERE>
```

The commit history no longer contained a commit introducing the fake secret.

---

## Secret History Validation

Searched all visible Git history for the fake variable name:

```bash
git log --all -p | grep -i "FAKE_API_KEY"
```

Output:

```text
<PASTE ACTUAL OUTPUT HERE>
```

Expected result:

```text
<NO OUTPUT>
```

No output confirmed that the fake secret did not appear in the reachable repository history after cleanup.

---

## Additional File Validation

Checked the current branch files:

```bash
grep -Rni "FAKE_API_KEY" . \
  --exclude-dir=.git
```

Output:

```text
<PASTE ACTUAL OUTPUT HERE>
```

Expected result:

```text
<NO OUTPUT>
```

This confirmed that the fake secret was also absent from the current working tree.

---

## Branch Cleanup

Returned to the main branch:

```bash
git switch main
```

Deleted the temporary branch:

```bash
git branch -D <TEMPORARY-BRANCH-NAME>
```

Confirmation:

```text
<PASTE BRANCH DELETION OUTPUT HERE>
```

Verified that the branch no longer existed:

```bash
git branch --list <TEMPORARY-BRANCH-NAME>
```

Output:

```text
<NO OUTPUT>
```

The practice branch was never pushed.

---

# Already Pushed Scenario

## Scenario

Assume the following fake secret had already been pushed and merged:

```text
FAKE_API_KEY=sk_test_this_is_not_real_1234567890
```

Removing the value from the latest version of a file would not be enough because the credential would still exist in Git history.

---

## Step 1 – Rotate or Revoke the Secret

The first action would be to revoke or rotate the exposed credential immediately.

For an API key, this would involve:

1. Disabling the exposed key through the service provider.
2. Creating a replacement key.
3. Updating the application or deployment environment with the new key.
4. Confirming that the old key can no longer be used.

Rotation must happen before repository cleanup because rewriting Git history does not prevent someone from using a credential they already copied.

---

## Step 2 – Remove the Secret From the Current Files

Remove the exposed value from the repository files.

Replace the real secret with an environment variable reference or placeholder.

Example:

```dotenv
API_KEY=your-api-key-here
```

Ensure the real `.env` file is covered by `.gitignore`.

---

## Step 3 – Clean the Repository History

Use an appropriate history-rewriting tool, such as:

```text
git filter-repo
```

or GitHub-supported secret-removal procedures.

The rewrite would remove the secret from all affected commits, branches, and tags.

Because history rewriting changes commit hashes, all collaborators would need clear instructions before continuing work.

---

## Step 4 – Force Push the Cleaned History

After validating the rewritten repository, force push the affected branches and tags.

This action would only be performed after:

* Coordinating with collaborators
* Creating a backup
* Confirming that the credential had already been revoked
* Verifying that the rewritten history no longer contained the secret

---

## Step 5 – Notify Collaborators

Collaborators would need to stop using old local clones.

They should either clone the repository again or carefully reset their local branches to the cleaned remote history.

Old clones could accidentally reintroduce the secret-containing commits.

---

## Step 6 – Review Logs and Access

Review the service provider's access logs for suspicious use of the exposed credential.

Record:

* When the credential was exposed
* When it was revoked
* Which repositories or branches were affected
* Whether unauthorized access occurred
* What preventive controls were added afterward

---

## Step 7 – Improve Prevention

After resolving the incident, enable or strengthen:

* GitHub secret scanning
* Push protection
* `.gitignore` rules
* Pre-commit secret scanning
* Environment-variable documentation
* Credential rotation procedures
* Least-privilege access

---

# Rotation First, Cleanup Second

The correct priority is:

```text
1. Revoke or rotate the exposed credential.
2. Remove it from the current repository files.
3. Rewrite the Git history.
4. Coordinate with collaborators.
5. Review logs and strengthen prevention.
```

Repository cleanup cannot make an exposed credential safe again.

A credential must always be treated as compromised once it has been committed and pushed.

---

# Repository Hygiene Review

## Tracked Files

Reviewed the repository for files that should not be committed, including:

```text
.env
*.pem
id_rsa
id_ed25519
credentials files
temporary files
build output
editor configuration files
```

Findings:

```text
<PASTE ACTUAL FINDINGS HERE>
```

---

## Disposable Workspace

The `.env.example` demonstration remained inside:

```text
sandbox/02_git_github/workspace/env_pattern_demo
```

This location is intended for disposable lesson practice.

No real secrets were stored in the example.

---

# What I Learned

* Secrets should never be stored directly in tracked repository files.
* `.env.example` documents required variables without exposing real values.
* `.gitignore` prevents new files from being tracked but does not remove files already present in Git history.
* A secret remains exposed even after it is deleted from the latest version of a file.
* Interactive rebase can remove sensitive content from unpushed local history.
* History should be inspected with `git log -p`, not only by checking the current working tree.
* A practice branch containing a fake secret must never be pushed.
* If a real secret is pushed, revocation or rotation is more urgent than Git history cleanup.
* Push protection can prevent recognized credentials from reaching a remote repository.
* Repository hygiene includes secret scanning, dependency security, ignored files, and regular maintenance.
