# Phase 02 — Git & GitHub Commands Cheatsheet

A consolidated quick-reference across all 12 lessons. Lookup tool, not a
teaching document — see `lessons/` for explanations.

## Mental Model & Inspection (Lesson 01)

| Command | Purpose |
|---|---|
| `git log --oneline` | Compact commit history |
| `git log --graph --oneline --all` | Visualize all branches' history |
| `git show <commit>` | Full details of one commit |
| `git status` | Working dir / staging / last commit comparison |

## Repo Setup & Config (Lesson 02)

| Command | Purpose |
|---|---|
| `git init` | Create a new repo (never inside `Learn-DE` itself) |
| `git config --global <key> <value>` | User-wide setting |
| `git config --local <key> <value>` | This-repo-only setting |
| `git config --list --show-origin` | See every setting and which file set it |
| `git check-attr <attr> -- <path>` | Confirm a `.gitattributes` rule applies |

## Staging & Commits (Lesson 03)

| Command | Purpose |
|---|---|
| `git add <file>` | Stage a file |
| `git add -p` | Stage specific hunks interactively |
| `git diff` | Unstaged changes |
| `git diff --staged` | Staged changes (next commit's content) |
| `git commit -m "message"` | Commit staged changes |
| `git restore --staged <file>` | Unstage without losing changes |

## Branching (Lesson 04)

| Command | Purpose |
|---|---|
| `git branch` | List branches |
| `git switch -c <name>` | Create and switch to a new branch |
| `git switch <name>` | Switch branches |
| `git branch -d <name>` | Delete a merged branch (safe) |
| `git branch -D <name>` | Force-delete (only if you're sure) |

## Merging & Conflicts (Lesson 05)

| Command | Purpose |
|---|---|
| `git merge <branch>` | Merge a branch into the current one |
| `git merge --abort` | Cancel an in-progress conflicted merge |
| (conflict markers) | `<<<<<<<` / `=======` / `>>>>>>>` — read both sides before resolving |

## Rewriting History (Lesson 06 — unpushed/unshared commits only)

| Command | Purpose |
|---|---|
| `git commit --amend` | Replace the last commit |
| `git rebase -i <base>` | Reorder/squash/reword commits since `<base>` |
| `git rebase --continue` | After resolving a conflict mid-rebase |
| `git rebase --abort` | Cancel an in-progress rebase |

## Remotes & GitHub CLI (Lesson 07)

| Command | Purpose |
|---|---|
| `git remote -v` | List remotes |
| `git fetch` | Update remote-tracking refs only |
| `git pull` | Fetch + merge |
| `git push -u origin <branch>` | Push + set up tracking (first push) |
| `gh auth login` | Authenticate GitHub CLI |
| `gh repo view` | Show repo info (read-only) |

## Pull Requests (Lesson 08)

| Command | Purpose |
|---|---|
| `gh pr create` | Open a PR from the current branch |
| `gh pr view [--web]` | Check / open a PR |
| `gh pr merge --squash \| --merge \| --rebase --delete-branch` | Merge with a chosen strategy |

## Issues & Releases (Lesson 09)

| Command | Purpose |
|---|---|
| `gh issue create` | File an issue |
| `gh issue list` | List open issues |
| `git tag -a <name> -m "message"` | Annotated tag (for releases) |
| `gh release create <tag>` | Create a GitHub Release from a tag |
| `gh release delete <tag> -y` | Delete a release (safe — doesn't rewrite history) |

## Undoing Things (Lesson 10)

| Command | Purpose | Risk |
|---|---|---|
| `git reset --soft <commit>` | Move pointer, keep changes staged | Low |
| `git reset --mixed <commit>` | Move pointer, unstage but keep changes | Low |
| `git reset --hard <commit>` | Move pointer, discard changes | **High** |
| `git revert <commit>` | New commit undoing an old one | Low — safe on shared history |
| `git reflog` | Find "lost" commits | None (read-only) |

## Secrets & Hygiene (Lesson 11)

| Command | Purpose |
|---|---|
| `git log --all --full-history -- <file>` | Check if a file was ever committed, even if deleted later |
| `git rm --cached <file>` | Stop tracking a file going forward (doesn't clean history) |
| `git branch --merged main` | Find stale, safe-to-delete branches |

## Branching Strategy Reference (Lesson 12)

| Strategy | Shape |
|---|---|
| Trunk-based | Everyone commits to/near `main` constantly, tiny changes |
| GitHub Flow (this repo's strategy) | `main` always deployable, short-lived feature branches via PR |
| Git Flow | Long-lived `develop` + `release/`/`hotfix/` branches |
