# Lesson 07 — Remotes & Connecting to GitHub

**Estimated effort:** Theory ~30 min · Guided practice ~25 min · Independent practice ~20 min

## Why This Matters

`Learn-DE` is already connected to a real GitHub remote — this lesson
makes sure you understand *how*, not just that it works. Every checkpoint
from here forward pushes to GitHub; knowing what `fetch`, `pull`, and
tracking branches actually do prevents a whole category of "why didn't my
push show up" confusion later.

## Learning Objectives

- Understand `origin` as a name, not a special keyword, and what a remote actually is.
- Distinguish `fetch` (update your knowledge of the remote) from `pull` (fetch + merge).
- Understand tracking branches and why `git push` sometimes needs `-u`.
- Install and authenticate GitHub CLI (`gh`), and know when it's faster than the web UI.

## Terminology

| Term | Definition |
|---|---|
| Remote | A named reference to another copy of the repository, usually on a server — `origin` is just the conventional default name, not special syntax. |
| `fetch` | Downloads new commits/branches from a remote *without* touching your working branches. |
| `pull` | `fetch` followed by a `merge` (or rebase, if configured) into your current branch. |
| Tracking branch | A local branch configured to know which remote branch it corresponds to — this is what makes plain `git push`/`git pull` (no arguments) work. |

## Your Real Setup

```bash
$ git remote -v
origin  https://github.com/Linhsmiler47/Learn-DE.git (fetch)
origin  https://github.com/Linhsmiler47/Learn-DE.git (push)
```

This repo's remote uses **HTTPS**, not SSH — even though Phase 01 Lesson
12 set up an SSH keypair. Both are valid; this lesson covers both paths so
you can make an informed choice rather than assuming one:

| Approach | How auth works | When it's simpler |
|---|---|---|
| **HTTPS** (current setup) | A Personal Access Token or `gh auth login`'s stored credential | Simplest to set up from scratch; what `Learn-DE` already uses |
| **SSH** (Phase 01 Lesson 12's key) | The keypair you already generated | Nicer once set up — no token to manage — but requires the one-time key setup you already did |

You don't need to switch protocols to complete this phase — understanding
*why* the current HTTPS setup works is the actual objective.

## GitHub CLI (`gh`)

Not installed on this machine yet — install it like any other package
(Phase 01 Lesson 07):

```bash
$ sudo apt install gh
$ gh auth login
```

`gh auth login` walks you through browser-based authentication once, then
stores credentials so `gh` (and `git push`/`pull` over HTTPS) stop asking
you to authenticate every time.

**When `gh` beats the web UI**: repetitive or scriptable actions — checking
PR/issue status without a context switch away from the terminal, creating
a PR from the branch you're already on, and (later, in Phase 06) anything
that needs to run non-interactively in a script or pipeline. **When the
web UI beats `gh`**: actually reading a diff carefully or writing a
multi-paragraph review comment — screen space and formatting matter there.
You'll use both, deliberately, not one exclusively.

## Command Syntax

| Command | Purpose |
|---|---|
| `git remote -v` | List remotes and their URLs |
| `git fetch` | Download new commits/branches, don't merge |
| `git pull` | Fetch + merge into current branch |
| `git push` | Push current branch's new commits |
| `git push -u origin <branch>` | Push and set up tracking in one step (first push of a new branch) |
| `git clone <url>` | Copy a remote repository, with a remote named `origin` already configured |
| `gh auth login` | Authenticate `gh` (and HTTPS git operations) with GitHub |
| `gh repo view` | Show info about the current repo (read-only, safe) |
| `gh repo create` | Create a **new** GitHub repository — see the caution below |

## A Caution on `gh repo create`

Running this for real creates an actual new repository on GitHub — which
is exactly the "throwaway repo" the Repository Usage Policy asks you to
avoid by default. Understand its syntax and use case (you'll need it
someday, for a genuinely new project), but don't run it against creating a
real repo just for practice. If you want the hands-on rep, that's the
sanctioned exception case (isolated experimentation) — create one, confirm
it worked with `gh repo view`, then delete it with `gh repo delete` so it
doesn't linger.

## Step-by-Step Example

```bash
$ cd ~/Projects/Learn-DE
$ git remote -v
origin  https://github.com/Linhsmiler47/Learn-DE.git (fetch)
origin  https://github.com/Linhsmiler47/Learn-DE.git (push)

$ git fetch origin
$ git log origin/main --oneline -3
c87bebc (origin/main) Add Data Engineering learning instructions
...

$ gh auth login
# follow the browser prompts

$ gh repo view
Linhsmiler47/Learn-DE
...

$ git switch docs/improve-root-readme
$ git push -u origin docs/improve-root-readme
Enumerating objects...
...
branch 'docs/improve-root-readme' set up to track 'origin/docs/improve-root-readme'.
```

That last line is the tracking branch being established — from now on,
plain `git push`/`git pull` on this branch know where to go.

## Guided Practice

See [`exercises/07_remotes_github/guided.md`](../exercises/07_remotes_github/guided.md).

## Common Mistakes

- Confusing `fetch` and `pull` — `fetch` alone never changes your working
  files; `pull` does (it merges).
- Running plain `git push` on a brand-new branch and being confused by
  "no upstream branch" — that's what `-u` on the first push solves.
- Assuming SSH is required — HTTPS with a token/`gh auth login` is equally
  valid and is what this repo already uses.

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| `fatal: The current branch has no upstream branch` | First push of a new branch, no tracking set up yet | `git push -u origin <branch-name>` |
| `gh: command not found` | Not installed yet | `sudo apt install gh` |
| Push prompts for credentials repeatedly | No stored credential helper | `gh auth login` (also configures git's HTTPS credential storage) |

## Knowledge Check

1. **What's the difference between `git fetch` and `git pull`?**
   *Answer: `fetch` downloads remote changes without touching your working branches; `pull` fetches and then merges into your current branch.*
2. **What does `-u` do on `git push -u origin <branch>`?**
   *Answer: Sets up the tracking relationship so future plain `git push`/`pull` on that branch know which remote branch to use.*
3. **When is `gh` more efficient than the GitHub web UI?**
   *Answer: Repetitive/scriptable actions and staying in the terminal without a context switch — e.g., checking PR status or creating a PR from your current branch.*

## Completion Checklist

- [ ] You can explain this repo's actual remote configuration.
- [ ] You've installed and authenticated `gh`.
- [ ] You've pushed a real branch with `-u` and understand what tracking means.

## Connects to Later Phases

Phase 06 (CI/CD) triggers directly off pushes and PRs to this same remote;
Phase 06 also uses `gh` (or GitHub Actions' own equivalent mechanisms) for
scripted, non-interactive repository operations — this is the first time
you'll use the CLI that way, not the last.

## Reference Materials

No source material exists in `ref roadmap/` for Git/GitHub — authored fresh.

## Next

Guided practice: [`exercises/07_remotes_github/guided.md`](../exercises/07_remotes_github/guided.md)
Independent exercise: [`exercises/07_remotes_github/independent.md`](../exercises/07_remotes_github/independent.md)
Next lesson: [08 — Pull Requests & Code Review Workflow](08_pull_requests_code_review.md)
