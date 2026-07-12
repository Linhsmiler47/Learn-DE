# Lesson 08 — Pull Requests & Code Review Workflow

**Estimated effort:** Theory ~30 min · Guided practice ~30 min · Independent practice ~25 min

## Why This Matters

A pull request is where "I wrote some code" becomes "this is reviewed,
discussed, and intentionally merged" — the actual unit of collaboration on
every professional engineering team, and the trigger for CI/CD (Phase 06).
Working solo doesn't make this optional to learn: even a solo PR against
your own repo builds the habit of re-reading your own diff as a reviewer
would, before it's permanent.

## Learning Objectives

- Open a PR with a description that actually helps a reviewer.
- Leave and respond to review comments — including on your own PR.
- Understand GitHub's three merge strategies and when each is appropriate.
- Configure basic branch protection and see it actually block something.

## Real Work for This Lesson

Your `docs/improve-root-readme` branch (cleaned up in Lesson 06, pushed in
Lesson 07) becomes a real PR here — merging it is the actual, lasting
outcome of this lesson, not a simulation.

## Terminology

| Term | Definition |
|---|---|
| Pull Request (PR) | A request to merge one branch into another, with a place for discussion, review, and CI results attached. |
| Merge commit | Preserves both branches' full history, joined by a two-parent commit. |
| Squash merge | Combines all of a PR's commits into one commit on the target branch — clean history, loses the PR's internal commit-by-commit story. |
| Rebase merge | Replays the PR's commits individually onto the target branch, no merge commit — keeps them separate but linear. |
| Branch protection | GitHub repo settings that require conditions (review, passing checks) before a branch can be merged into. |

## Theory: Choosing a Merge Strategy

| Strategy | Use when |
|---|---|
| Merge commit | You want to preserve exactly how the branch's work happened, including its own internal commit history — good for larger, multi-day features. |
| Squash merge | The PR's internal commits were exploratory/messy and only the final combined result matters to `main`'s history — good for small PRs like this lesson's README change. |
| Rebase merge | You want a fully linear history with no merge commits, but still want each of the PR's commits visible individually. |

There's no universally "correct" choice — Lesson 12 revisits this as part
of choosing a team-wide branching strategy. For this lesson's small,
already-cleaned-up PR, squash merge is a reasonable default.

## Command Syntax

| Command | Purpose |
|---|---|
| `gh pr create` | Open a PR from your current branch (interactive prompts, or flags for title/body) |
| `gh pr view` | Show the current branch's PR status |
| `gh pr view --web` | Open the PR in your browser |
| `gh pr merge` | Merge a PR (flags choose the strategy: `--squash`, `--merge`, `--rebase`) |
| `gh pr checks` | Show CI status on a PR (relevant again in Phase 06) |

## Step-by-Step Example

```bash
$ cd ~/Projects/Learn-DE
$ git switch docs/improve-root-readme
$ gh pr create --title "Add a real description to the root README" \
    --body "The root README was just a title. This adds a short, real description of what this repository is, matching CLAUDE.md's framing."

$ gh pr view
docs/improve-root-readme
Add a real description to the root README
...

# Leave a real review comment on your own diff (via web UI is easiest for this part):
$ gh pr view --web
```

In the browser: open the "Files changed" tab, leave a comment on the
actual line you changed (e.g., noting *why* you phrased the description
the way you did), then use "Review changes" → **Approve** (since it's your
own low-risk documentation change) or **Request changes** if you spot
something while reviewing your own diff — either is a legitimate, real
review outcome.

```bash
$ gh pr merge --squash --delete-branch
```

`--delete-branch` cleans up the now-merged branch automatically — one less
manual step, and it directly serves the "repo gets cleaner over time"
principle from the Repository Usage Policy.

## Branch Protection (a real, safe configuration change)

```bash
$ gh api repos/Linhsmiler47/Learn-DE/branches/main/protection \
    --method PUT \
    --field required_pull_request_reviews[required_approving_review_count]=0 \
    ... # (exact flags depend on current gh/API version — the web UI path is simpler for a first pass)
```

The web UI path is more reliable for a first attempt: repo **Settings →
Branches → Add branch protection rule** for `main`, requiring a PR before
merging. Then prove it: try `git push origin main` directly with a trivial
change and confirm GitHub rejects it.

## Guided Practice

See [`exercises/08_pull_requests_code_review/guided.md`](../exercises/08_pull_requests_code_review/guided.md).

## Common Mistakes

- Writing a PR description that just repeats the commit message instead of
  explaining context a reviewer wouldn't already have.
- Merging your own PR without actually reading the diff again first — the
  point of a PR is the re-read, not the button.
- Enabling branch protection then being unable to push your own
  small fixes directly — that's the protection working; go through a PR
  instead, even for yourself.

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| `gh pr create` fails with an auth error | `gh auth login` wasn't completed (Lesson 07) | Run `gh auth login` again |
| Direct push to `main` isn't actually blocked after adding protection | Rule wasn't saved, or you're an admin with "include administrators" unchecked | Check the branch protection rule's exact settings; admins can bypass unless explicitly included |
| Merge button is greyed out on GitHub | A required check/review hasn't been satisfied | That's branch protection working as configured — satisfy the requirement or adjust the rule |

## Knowledge Check

1. **What's the difference between a squash merge and a rebase merge?**
   *Answer: Squash combines all the PR's commits into one on the target branch; rebase merge replays them individually, still linear, without a merge commit.*
2. **Why review your own PR instead of just merging it?**
   *Answer: Re-reading the diff as a reviewer catches mistakes you didn't notice while writing it — the PR process, not just the code, is the safeguard.*
3. **What does branch protection requiring a PR actually prevent?**
   *Answer: Direct pushes to the protected branch — all changes must go through a reviewed pull request instead.*

## Completion Checklist

- [ ] You've opened, reviewed, and merged a real PR against `Learn-DE`.
- [ ] You've configured branch protection on `main` and confirmed it blocks a direct push.
- [ ] You can justify your merge strategy choice, not just default to one.

## Connects to Later Phases

Phase 06 (GitHub Actions/CI/CD) attaches automated checks directly to this
same PR mechanism — "required status checks" in branch protection is where
Phase 02 and Phase 06 fuse. Every checkpoint's real work from here forward
goes through a PR, not a direct push.

## Reference Materials

No source material exists in `ref roadmap/` for Git/GitHub — authored fresh.

## Next

Guided practice: [`exercises/08_pull_requests_code_review/guided.md`](../exercises/08_pull_requests_code_review/guided.md)
Independent exercise: [`exercises/08_pull_requests_code_review/independent.md`](../exercises/08_pull_requests_code_review/independent.md)
Next lesson: [09 — Issues, Milestones & Release Management](09_issues_releases.md)
