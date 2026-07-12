# Guided Exercise — Lesson 09: Issues, Milestones & Release Management

## Steps

1. File a real, actionable issue:
   ```bash
   cd ~/Projects/Learn-DE
   gh issue create \
       --title "Fill in real evidence for Phase 01 Lessons 06, 07, 08, and 12" \
       --body "Per the Phase 01 bare-minimum review in LEARNING_PATH.md's Progress Tracking: these lessons have correct command design but placeholder/unfilled evidence. Revisit when returning to Phase 01."
   gh issue list
   ```
2. Practice the release mechanism safely (create and then delete):
   ```bash
   git switch main
   git pull
   git tag -a v0.0.1-practice -m "Practice tag — not a real milestone"
   git push origin v0.0.1-practice
   gh release create v0.0.1-practice --title "Practice release" \
       --notes "Practicing the release mechanism — will be deleted after this lesson."
   gh release view v0.0.1-practice
   ```
3. Clean up the practice release/tag:
   ```bash
   gh release delete v0.0.1-practice -y
   git push origin --delete v0.0.1-practice
   git tag -d v0.0.1-practice
   ```

## Evidence to Record

In `notes/lesson_09_evidence.md`: the real issue's URL and content, the
practice release's creation and view output, and confirmation of its
deletion (tag no longer exists locally or on the remote).

## Validation

- `gh issue list` should show your real issue.
- `git tag` (after cleanup) should not list `v0.0.1-practice`.
- `git ls-remote --tags origin` should not list it either.

## When You're Done

Move to [`independent.md`](independent.md).
