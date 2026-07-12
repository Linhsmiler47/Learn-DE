# Guided Exercise — Lesson 12: Branching Strategies & Collaborative Workflows

## Steps

1. Review this learning path's actual branch history so far:
   ```bash
   cd ~/Projects/Learn-DE
   git log --graph --oneline --all
   git branch -a
   ```
2. Identify, in writing, which strategy (trunk-based / GitHub Flow / Git
   Flow) this history actually reflects — using your real branches
   (`docs/improve-root-readme`, `phase-02/gitattributes`, and any others
   still around) as evidence, not the lesson's hypothetical example.
3. Write a one-paragraph justification for why GitHub Flow fits this
   specific project (a solo learner, one continuously evolving repo, no
   need for parallel supported release versions).

## Evidence to Record

In `notes/lesson_12_evidence.md`: the real `git log --graph` output, your
identification of the strategy in use, and your justification paragraph.

## Validation

- Your identification should be checkable against the actual repo
  history — every real branch so far should have been short-lived,
  merged via PR, with no long-lived `develop`-style branch anywhere.

## When You're Done

Move to [`independent.md`](independent.md).
