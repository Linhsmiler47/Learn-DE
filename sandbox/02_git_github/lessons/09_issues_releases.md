# Lesson 09 — Issues, Milestones & Release Management

**Estimated effort:** Theory ~30 min · Guided practice ~25 min · Independent practice ~20 min

## Why This Matters

Issues are how work gets tracked and prioritized before it's code; releases
are how finished work gets communicated to whoever depends on it — even if
"whoever" is just future you, checking what state a project was in three
months ago. Both are real project-management tools you'll rely on for
every Data Engineering checkpoint from here forward.

## Learning Objectives

- File a real, actionable GitHub Issue — not a placeholder.
- Link an issue to the commit/PR that resolves it, and close it automatically.
- Understand semantic versioning well enough to tag a release correctly.
- Write release notes that actually help a reader.

## Terminology

| Term | Definition |
|---|---|
| Issue | A tracked unit of work, bug, or discussion on GitHub, independent of any specific branch or commit. |
| Closing keyword | Words like `Fixes #12` or `Closes #12` in a commit message or PR description that auto-close the referenced issue on merge. |
| Tag | A named pointer at a specific commit, typically used to mark releases (unlike a branch, a tag doesn't move). |
| Semantic versioning (semver) | `MAJOR.MINOR.PATCH` — increment MAJOR for breaking changes, MINOR for new backward-compatible features, PATCH for fixes. |
| GitHub Release | A tag plus release notes, shown in a dedicated, browsable place on the repo. |

## Real Work for This Lesson

You have real, pending work to track. Based on the Phase 01 evidence
review (in `LEARNING_PATH.md`'s Progress Tracking), file at least one real
issue for something genuinely unfinished — e.g., "Fill in real evidence
for Phase 01 Lessons 06, 07, 08, 12" or "Complete Phase 01's practical
assessment." This has actual lasting value, unlike a placeholder issue
invented just for practice.

## Command Syntax

| Command | Purpose |
|---|---|
| `gh issue create` | File a new issue (interactive, or with `--title`/`--body`) |
| `gh issue list` | List open issues |
| `gh issue close <number>` | Close an issue manually |
| `git tag <name>` | Create a lightweight tag at the current commit |
| `git tag -a <name> -m "message"` | Create an annotated tag (preferred for releases — carries its own message/metadata) |
| `gh release create <tag>` | Create a GitHub Release from a tag, with notes |
| `gh release delete <tag>` | Delete a release (safe — see below) |

## Step-by-Step Example

**Filing a real issue:**

```bash
$ gh issue create \
    --title "Fill in real evidence for Phase 01 Lessons 06, 07, 08, and 12" \
    --body "Per the Phase 01 bare-minimum review in LEARNING_PATH.md's Progress Tracking: these lessons have correct command design but placeholder/unfilled evidence. Revisit when returning to Phase 01."
```

**Linking a future commit to this issue** (do this whenever you actually
resolve it): include `Fixes #<issue-number>` in that commit's message or
PR description — GitHub closes the issue automatically when the commit
lands on the default branch.

**Practicing a release (safe to create and delete — tags/releases aren't
history rewriting):**

```bash
$ git switch main
$ git pull
$ git tag -a v0.0.1-practice -m "Practice tag — not a real milestone"
$ git push origin v0.0.1-practice
$ gh release create v0.0.1-practice --title "Practice release" \
    --notes "Practicing the release mechanism — will be deleted after this lesson."

# Confirm it exists, then clean up:
$ gh release view v0.0.1-practice
$ gh release delete v0.0.1-practice -y
$ git push origin --delete v0.0.1-practice
$ git tag -d v0.0.1-practice
```

Deleting a tag/release doesn't rewrite any commit history — it just
removes a reference, which is why this is safe to practice for real and
clean up, unlike the destructive operations in Lessons 05/06/10.

## Guided Practice

See [`exercises/09_issues_releases/guided.md`](../exercises/09_issues_releases/guided.md).

## Common Mistakes

- Filing vague issues ("fix stuff") — the same commit-hygiene discipline
  from Lesson 03 applies to issues.
- Forgetting the closing keyword, so a merged fix doesn't auto-close its issue.
- Confusing a lightweight tag (`git tag <name>`) with an annotated tag
  (`git tag -a`) — annotated tags carry a message and are the right choice
  for releases.
- Bumping MAJOR/MINOR/PATCH inconsistently with what actually changed.

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| Issue didn't auto-close after merge | Missing or misspelled closing keyword, or it wasn't on the default branch yet | Check the exact keyword syntax (`Fixes #12`, not `Fixed #12` unless your convention supports both) |
| `gh release create` fails, tag not found | Tag wasn't pushed yet | `git push origin <tag>` first |
| Confused about which version number to bump | Unsure if a change is breaking | When in doubt for a learning-path project, PATCH is usually safe; save MAJOR for changes that would break someone depending on this repo's structure |

## Knowledge Check

1. **What's the difference between a tag and a branch?**
   *Answer: A tag is a fixed pointer at one commit — it doesn't move; a branch is a movable pointer that advances with new commits.*
2. **What does `Fixes #12` in a commit message do?**
   *Answer: Automatically closes issue #12 on GitHub when that commit lands on the repository's default branch.*
3. **Why is deleting a practice release/tag safe, unlike rebase or reset?**
   *Answer: It only removes a reference (the tag) — it doesn't rewrite or discard any commit history.*

## Completion Checklist

- [ ] You've filed at least one real, actionable issue.
- [ ] You've practiced creating and cleanly deleting a release/tag.
- [ ] You can explain semantic versioning well enough to choose a version number correctly.

## Connects to Later Phases

The Phase 02 practical assessment's release step uses exactly this
mechanism to mark real phase completion milestones. Phase 06 (CI/CD) will
later automate release creation from a pipeline using the same `gh
release create` command you just ran by hand.

## Reference Materials

No source material exists in `ref roadmap/` for Git/GitHub — authored fresh.

## Next

Guided practice: [`exercises/09_issues_releases/guided.md`](../exercises/09_issues_releases/guided.md)
Independent exercise: [`exercises/09_issues_releases/independent.md`](../exercises/09_issues_releases/independent.md)
Next lesson: [10 — Undoing Things Safely: Reset, Revert & Reflog](10_reset_revert_reflog.md)
