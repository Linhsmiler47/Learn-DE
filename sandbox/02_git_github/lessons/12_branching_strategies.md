# Lesson 12 — Branching Strategies & Collaborative Workflows

**Estimated effort:** Theory ~25 min · Guided practice ~20 min · Independent practice ~20 min

## Why This Matters

Every command from Lessons 01–11 is a tool; this lesson is about choosing
*when* to use which tool, consistently, as a team (even a team of one).
The Repository Usage Policy already committed this learning path to
"feature branch per unit of work, `main` stays stable" — this lesson makes
sure you understand that as a deliberate choice among alternatives, not an
arbitrary rule.

## Learning Objectives

- Compare trunk-based development, GitHub Flow, and Git Flow.
- Explain the trade-offs each makes, not just its steps.
- Choose a strategy appropriate to solo work vs. a team, and justify it.
- Recognize which strategy this learning path has been using all along.

## Terminology

| Term | Definition |
|---|---|
| Trunk-based development | Everyone commits to (or merges very frequently into) one main branch; feature branches, if used, are very short-lived. |
| GitHub Flow | `main` is always deployable; all work happens on feature branches merged via PR; no long-lived branches beyond `main`. |
| Git Flow | Long-lived `develop` and `main` branches, plus `feature/`, `release/`, and `hotfix/` branches with defined merge rules between them. |

## Theory: The Three Strategies

**Trunk-based development** optimizes for integration speed — changes are
small and merged constantly, minimizing how long any branch diverges from
`main`. It demands strong automated testing (Phase 06) since there's
little isolation to catch problems before they reach `main`.

**GitHub Flow** (what this learning path has been using since Lesson 03)
optimizes for simplicity: one long-lived branch (`main`), everything else
is a short-lived feature branch merged via reviewed PR. No `develop`
branch, no release branches — deploy from `main` whenever it's in a good
state.

**Git Flow** optimizes for **release management** in contexts with
scheduled, versioned releases and the need to patch older versions in
production simultaneously with developing new features — at the cost of
real complexity (more branch types, more merge rules to remember). It's
common in shipped-software contexts (versioned libraries, installed
applications with a support window); it's usually more process than a
small team or solo project needs.

| Strategy | Best for | Cost |
|---|---|---|
| Trunk-based | Fast-moving teams with strong CI/CD | Requires excellent automated testing to be safe |
| GitHub Flow | Most small-to-medium teams, continuously deployed projects | Less structure for managing multiple simultaneous release versions |
| Git Flow | Versioned software with long-supported releases | Real overhead — more branches, more rules, easy to do inconsistently |

## Why This Path Uses GitHub Flow

Simple, deployable-at-any-time `main`, short-lived feature branches per
phase/checkpoint, PR-based review even solo — exactly GitHub Flow, and
exactly what Lessons 03–08 already had you doing on the real repository.
This isn't a coincidence: it's the right-sized choice for a solo learner
building one continuously-evolving repository, without the overhead Git
Flow would add for no real benefit here.

## Step-by-Step Example: Diagramming the Same Feature Three Ways

Take a hypothetical feature: "add a data quality check to Checkpoint 5."

```
Trunk-based:
main: ---A---B(small commit 1)---C(small commit 2)---D(small commit 3)---
      (each commit tiny, merged/committed to main within hours)

GitHub Flow (this path's actual approach):
main:              A -------------------------- E (merge)
                     \                          /
feature/dq-check:     B --- C --- D (PR opened, reviewed, merged)

Git Flow:
main:     ---A------------------------------F(release merge)---
develop:      \--B---C---D---E(feature merged to develop)--/
feature/dq:        \--B---C---D--/
```

## Guided Practice

See [`exercises/12_branching_strategies/guided.md`](../exercises/12_branching_strategies/guided.md).

## Common Mistakes

- Adopting Git Flow's full ceremony for a solo/small project "because it's
  the proper way" — it's proper for its specific problem, not universally.
- Trunk-based development without the CI safety net it requires — this is
  how broken code reaches `main` constantly.
- Not picking a strategy at all, and ending up with an inconsistent mix of
  direct-to-main commits and occasional feature branches.

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| Team members disagree on when to branch vs. commit directly | No agreed strategy | Pick one explicitly (this lesson's comparison table), document it, revisit if it's not working |
| Long-lived feature branches keep producing painful merge conflicts | Trying to do trunk-based-style fast integration on GitHub-Flow-style long branches | Either merge more frequently (smaller PRs) or accept longer-lived branches need more deliberate conflict management |

## Knowledge Check

1. **What does GitHub Flow assume is always true about `main`?**
   *Answer: That it's always in a deployable/good state — all work happens on branches merged in via reviewed PR, never committed directly.*
2. **What extra branch types does Git Flow add beyond `main` and feature branches?**
   *Answer: A long-lived `develop` branch, plus `release/` and `hotfix/` branches with defined rules for merging between them.*
3. **Why does trunk-based development demand strong automated testing?**
   *Answer: With minimal branch isolation and constant merging to `main`, there's little else standing between a bad change and production.*

## Completion Checklist

- [ ] You can compare all three strategies' trade-offs, not just recite their steps.
- [ ] You can explain why this learning path uses GitHub Flow specifically.
- [ ] You could justify a strategy choice for a hypothetical team scenario different from your own.

## Connects to Later Phases

Phase 06 (CI/CD) is what makes trunk-based development *safe* when it's
the right choice — you now understand why that pairing matters. Every
checkpoint and future phase continues this same GitHub Flow pattern
already established.

## Reference Materials

No source material exists in `ref roadmap/` for Git branching strategies —
authored fresh.

## Next

Guided practice: [`exercises/12_branching_strategies/guided.md`](../exercises/12_branching_strategies/guided.md)
Independent exercise: [`exercises/12_branching_strategies/independent.md`](../exercises/12_branching_strategies/independent.md)
Next: [`../assessment/README.md`](../assessment/README.md) — the Phase 02 practical assessment.
