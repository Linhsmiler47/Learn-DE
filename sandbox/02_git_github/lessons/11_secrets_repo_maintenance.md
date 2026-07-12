# Lesson 11 — Secret Management, Repository Hygiene & Maintenance

**Estimated effort:** Theory ~40 min · Guided practice ~30 min · Independent practice ~30 min

## Why This Matters

A secret committed to Git history doesn't stay hidden — clones, forks, and
cached copies can all carry it forward even after you "delete" the file.
This is the one Git mistake that isn't just inconvenient to fix; it can be
a real security incident. Checkpoint 4 onward, this repository will hold
real API keys and database credentials — the habits from this lesson are
what keep that safe.

## Learning Objectives

- Use `.env` / `.env.example` correctly so secrets never need to be committed in the first place.
- Understand GitHub Secret Scanning (detects after the fact) vs. Push Protection (blocks before the push lands).
- Remove a secret from history if it happens anyway.
- Understand why removing it from history is not the last step — rotation is.
- Perform a basic repository hygiene audit.

## Terminology

| Term | Definition |
|---|---|
| `.env` | A file holding real environment-variable values (including secrets) for local use — **never committed**. |
| `.env.example` | A committed template listing the *names* of required variables with placeholder values — documents what's needed without exposing anything. |
| GitHub Secret Scanning | Automatically scans pushed commits for patterns matching known secret formats (API keys, tokens) and alerts you if one is found. |
| GitHub Push Protection | Blocks a push *before* it completes if a recognized secret pattern is detected — proactive, not just reactive. |
| Credential rotation | Invalidating the exposed credential at its source (regenerating the API key/token) — the step that actually neutralizes an exposure. |

## Real Case Study: Document Your Own Incident

You mentioned experiencing a real GitHub push-protection incident on this
repository. This lesson is written to hold that case study, but the
specific details (what triggered it, whether it was a real secret or a
false positive, how it was resolved) live with you, not with me — I have
no visibility into what actually happened outside this conversation.

**When you work through this lesson**, replace this section with what
actually happened:

```markdown
### What triggered it
(what were you doing — pushing what, when)

### What Push Protection detected
(the secret pattern it flagged — never paste the actual secret value here,
even in evidence; describe the *type*, e.g. "a GitHub personal access
token pattern")

### Was it a real secret or a false positive?

### How it was resolved
(did you remove it before pushing, rotate a credential, or something else)

### What you'd do differently
```

This is more valuable *because* it's real — a genuine incident with your
own reasoning beats a hypothetical example every time.

## Theory: `.env` / `.env.example` Pattern

```
.env            <- real values, gitignored, never committed
.env.example    <- committed, documents what's needed:

    DATABASE_URL=postgresql://user:password@localhost:5432/dbname
    API_KEY=your-api-key-here
```

Anyone cloning the repo copies `.env.example` to `.env` and fills in real
values locally. Nobody needs to see anyone else's real credentials, and
nothing real ever needs to touch git history. This directly previews Phase
04 (Configuration), which formalizes this pattern for application config.

## Theory: Secret Scanning vs. Push Protection

- **Secret Scanning** runs *after* a push lands, checking commits already
  in the repository's history — it alerts you, but the secret is already
  in history by the time you're told.
- **Push Protection** runs *before* the push completes — if it recognizes
  a secret pattern in what you're about to push, it blocks the push
  outright, so the secret never lands in remote history at all. This is
  the stronger of the two, which is why it's worth confirming it's
  actually enabled on a repo (check **Settings → Code security and
  analysis** on GitHub — availability and defaults can differ for public
  vs. private repositories, so check your own repo's actual current
  settings rather than assuming).

## Theory: Why Rotation Is Non-Negotiable

Removing a secret from git history (rewriting commits, force-pushing the
clean version) does **not** guarantee nobody ever saw the old value —
anyone who cloned, forked, or fetched before the cleanup may still have
it, and GitHub's own caches can retain it briefly. The only step that
actually neutralizes an exposure is **rotating the credential at its
source**: regenerate the API key, reset the database password, revoke the
old token. History cleanup reduces future exposure; rotation eliminates
the risk from *past* exposure. Do both, in that priority order if a real
secret was ever pushed: rotate first (stops the bleeding immediately),
clean history second.

## Command Syntax and Safety Notes

| Command | What it does | Risk level |
|---|---|---|
| `git rm --cached .env` | Stops tracking `.env` going forward (doesn't touch history) | **Low** — but doesn't fix past exposure if it was ever committed |
| `git log --all --full-history -- .env` | Check whether a file was ever committed, even if deleted later | Read-only, **none** |
| Interactive rebase to remove a secret (recent, unpushed commit) | Rewrites local history | **Low** if unpushed (Lesson 06's golden rule applies) |
| `git filter-repo` (or BFG Repo-Cleaner) | Rewrites **all** history to strip a file/pattern everywhere it ever appeared | **High** — rewrites shared history; requires everyone with a clone to re-clone; only do this after understanding the blast radius, and always rotate the credential regardless |

## Step-by-Step Example: Auditing This Repo's Hygiene

```bash
$ cd ~/Projects/Learn-DE
$ git log --all --full-history -- .env
(no output = .env was never committed — good)

$ cat .gitignore | grep -A1 "Secrets"
# Secrets
.env

$ git check-ignore -v sandbox/01_linux/workspace/some_test_file
.gitignore:27:sandbox/01_linux/workspace/*	sandbox/01_linux/workspace/some_test_file

$ find . -iname "*.pem" -o -iname "id_rsa*" -o -iname "id_ed25519*" 2>/dev/null | grep -v "^\./\.git"
(should be empty inside the repo — Phase 01's practice SSH keys live in ~/.ssh, outside this repo, which is correct)

$ git log --oneline --all | wc -l
(a sanity count — does this match what you expect?)

$ git branch --merged main
(lists branches already merged — safe to delete if stale)
```

## Guided Practice

See [`exercises/11_secrets_repo_maintenance/guided.md`](../exercises/11_secrets_repo_maintenance/guided.md).

## Common Mistakes

- Believing `git rm` (without `--cached` and without addressing history)
  removes a secret from the repo — it only removes it going forward.
- Cleaning history but skipping rotation — the exposure already happened;
  history cleanup alone doesn't undo that.
- Committing a real `.env` once "just to test," planning to remove it
  "later."
- Treating `.env.example` as optional — without it, nobody else (including
  future you) knows what variables are actually required.

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| GitHub blocks a push citing a detected secret | Push Protection working as intended | Remove the secret from the commit (amend if it's the last commit, interactive rebase if further back), then push again — and rotate the credential if it was ever real |
| A secret was already merged to `main` before you noticed | Detection happened after the fact (Secret Scanning) or wasn't enabled | Rotate the credential immediately, then decide whether history rewriting is worth the disruption to any other clones |
| Unsure whether something is a "real" secret or a placeholder | Ambiguous naming | When in doubt, treat it as real until proven otherwise — the cost of over-caution here is low |

## Knowledge Check

1. **What's the difference between Secret Scanning and Push Protection?**
   *Answer: Secret Scanning detects secrets already pushed to history; Push Protection blocks the push before the secret ever lands in remote history.*
2. **Why isn't removing a secret from git history sufficient on its own?**
   *Answer: Anyone who already cloned/fetched/forked before the cleanup may still have the old value — only rotating the credential at its source neutralizes the actual exposure.*
3. **What's the purpose of `.env.example`?**
   *Answer: Documents which environment variables are required, with placeholder values, without ever exposing real secrets — committed safely alongside a gitignored `.env`.*

## Completion Checklist

- [ ] You've documented your own real push-protection incident (or, if none occurred yet, a deliberate practice one on a temporary branch).
- [ ] You understand and can explain the rotation-then-cleanup priority.
- [ ] You've performed a real hygiene audit of `Learn-DE` (stale branches, `.gitignore` effectiveness, no stray secrets).
- [ ] You've written or reviewed a real `.env.example` pattern.

## Connects to Later Phases

Phase 04 (Configuration) formalizes `.env`/`.env.example` for application
config; Checkpoint 4 (API ingestion) is the first place a *real* credential
enters this repository's working set — everything here is what keeps that
safe.

## Reference Materials

No source material exists in `ref roadmap/` for Git secret management —
authored fresh.

## Next

Guided practice: [`exercises/11_secrets_repo_maintenance/guided.md`](../exercises/11_secrets_repo_maintenance/guided.md)
Independent exercise: [`exercises/11_secrets_repo_maintenance/independent.md`](../exercises/11_secrets_repo_maintenance/independent.md)
Next lesson: [12 — Branching Strategies & Collaborative Workflows](12_branching_strategies.md)
