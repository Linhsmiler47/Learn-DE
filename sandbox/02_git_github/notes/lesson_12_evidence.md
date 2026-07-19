# Lesson 12 Evidence – Branching Strategies & Collaborative Workflows

**Repository:** Learn-DE

**Lesson:** 12 – Branching Strategies & Collaborative Workflows

**Completion Date:** 2026-07-19

---

# Guided Exercise

## Objective

Review the real branch and commit history of the repository, identify the branching strategy currently in use, and explain why that strategy fits this project.

---

## Repository History

Reviewed the complete repository history using:

```bash
git log --graph --oneline --all
```

Output:

```text
<PASTE ACTUAL git log --graph --oneline --all OUTPUT HERE>
```

The graph showed the commits and merged branches created during the previous Git and GitHub lessons.

---

## Repository Branches

Reviewed all local and remote branches using:

```bash
git branch -a
```

Output:

```text
<PASTE ACTUAL git branch -a OUTPUT HERE>
```

Branches used during the project included:

```text
docs/improve-root-readme
phase-02/gitattributes
fix/wording-lesson-doc
```

Some of these branches may no longer appear because they were deleted after their Pull Requests were merged.

---

## Branching Strategy Identification

The repository history most closely reflects:

```text
GitHub Flow
```

The workflow used throughout the repository followed this pattern:

1. Begin from the stable `main` branch.
2. Create a short-lived branch for one specific change.
3. Commit the work on that branch.
4. Push the branch to GitHub.
5. Open a Pull Request.
6. Review and merge the Pull Request into `main`.
7. Delete the completed branch.

Examples include:

```text
docs/improve-root-readme
```

This branch was created for a focused README documentation improvement.

```text
phase-02/gitattributes
```

This branch was created for the repository-wide `.gitattributes` configuration.

```text
fix/wording-lesson-doc
```

This branch was created for a small documentation wording change.

Each branch represented a specific piece of work and was intended to be merged back into `main` through a Pull Request.

---

## Why This Is Not Git Flow

The repository does not use Git Flow because it does not contain long-lived branches such as:

```text
develop
release/*
hotfix/*
```

There is no separate integration branch between feature branches and `main`.

Changes are merged directly into `main` through Pull Requests after they are reviewed.

The project also does not maintain several supported production release versions at the same time.

---

## Why This Is Not Trunk-Based Development

The repository is not using strict trunk-based development because changes are normally completed on named feature or documentation branches before being merged.

Branches such as:

```text
docs/improve-root-readme
phase-02/gitattributes
fix/wording-lesson-doc
```

were used instead of committing every change directly to `main`.

Although the branches were short-lived, the workflow still relied on Pull Requests and separate branches for each unit of work.

---

## GitHub Flow Justification

GitHub Flow fits this project because it is a solo learning repository with one continuously evolving main branch. Each lesson produces a small, focused change that can be developed on a short-lived branch, reviewed through a Pull Request, and merged directly into `main`. The project does not require a permanent `develop` branch, scheduled release branches, or support for several production versions at the same time. GitHub Flow therefore provides enough structure to practice professional collaboration habits while keeping the workflow simple and easy to manage.

---

## Guided Exercise Validation

The repository history supports the GitHub Flow identification because:

* Work was completed on short-lived branches.
* Each branch focused on one specific change.
* Changes were merged through Pull Requests.
* Completed branches were deleted.
* `main` remained the central branch.
* No long-lived `develop` branch was used.
* No permanent release or hotfix branch structure was used.

The actual repository history therefore matches GitHub Flow more closely than Git Flow or strict trunk-based development.

---

# Independent Exercise

## Objective

Design two hypothetical software-development scenarios where a branching strategy other than GitHub Flow would be more appropriate.

The scenarios must be different from the current Learn-DE repository and from each other.

---

# Scenario 1 – Git Flow

## Scenario

A team of twelve developers maintains a business application that publishes a major release every three months. Customers may remain on the previous major version for up to one year, so the team must continue issuing critical fixes for both the current and previous release. Development for the next release continues while release testing and maintenance work occur at the same time.

---

## Recommended Strategy

```text
Git Flow
```

---

## Property Driving the Choice

The main property driving this choice is:

```text
Multiple release lines must be developed and supported in parallel.
```

The team needs separate areas for:

* Ongoing development for the next release
* Stabilization of the upcoming release
* Emergency fixes for the production release
* Maintenance of an older supported version

A long-lived `develop` branch would collect work intended for the next release.

Release branches could be created when a version enters stabilization:

```text
release/2.0
```

Production hotfixes could be handled independently:

```text
hotfix/1.9.1
```

This structure would allow developers to continue building the next version without mixing unfinished work into a release that is already being tested.

---

## Why Not GitHub Flow

GitHub Flow would be less suitable because merging every completed branch directly into `main` would make it difficult to separate:

* Work intended for the next quarterly release
* Fixes intended for the current production release
* Fixes required for an older supported release

The team needs explicit release boundaries and parallel maintenance branches.

---

## Why Not Trunk-Based Development

Trunk-based development would require the team to integrate most work continuously into one shared branch.

That approach could still work with advanced feature flags and release automation, but the scenario assumes that several released versions must remain independently supported.

Maintaining separate release lines would still be necessary, reducing the simplicity normally provided by trunk-based development.

---

## Cost of Git Flow

Git Flow would introduce more branch management and coordination overhead.

Developers would need to ensure that important fixes were merged into the correct combination of:

```text
main
develop
release/*
hotfix/*
```

The larger number of long-lived branches could also create merge conflicts and make it harder to determine which version contains a particular fix.

---

# Scenario 2 – Trunk-Based Development

## Scenario

A team of forty developers operates a cloud-based service that is deployed to production many times each day. The project has comprehensive automated tests, mandatory continuous integration checks, feature flags, automated rollback, and strong monitoring. The service has only one production version because every customer uses the same hosted platform.

---

## Recommended Strategy

```text
Trunk-based development
```

---

## Property Driving the Choice

The main property driving this choice is:

```text
High testing maturity and a very frequent deployment cadence.
```

The team needs changes to integrate continuously so that developers do not maintain large branches that drift away from the shared codebase.

Developers would either commit directly to the trunk through protected checks or use branches that exist for only a few hours.

Incomplete features would remain disabled through feature flags until they were ready for users.

This approach would support:

* Frequent integration
* Small code changes
* Fast automated validation
* Rapid production deployments
* Reduced long-running merge conflicts

---

## Why Not GitHub Flow

GitHub Flow could support this team, but traditional multi-day feature branches and separate Pull Request cycles for every change could slow down a deployment process that runs many times per day.

The team benefits from extremely small changes being integrated almost immediately into the shared trunk.

Pull Requests could still exist, but branches would need to be very short-lived and the overall workflow would be closer to trunk-based development than conventional GitHub Flow.

---

## Why Not Git Flow

Git Flow would be unsuitable because its long-lived `develop` and release branches would delay integration.

The service does not maintain several supported production versions, and it does not need quarterly release stabilization branches.

The additional branch structure would conflict with the goal of deploying small, tested changes continuously.

---

## Cost of Trunk-Based Development

Trunk-based development requires substantial engineering discipline and infrastructure.

The team must maintain:

* Reliable automated tests
* Fast continuous integration pipelines
* Effective feature flags
* Strong code review practices
* Automated rollback procedures
* Production monitoring

A broken change can affect the shared trunk quickly, so weak test coverage or slow validation would create a serious risk for the entire team.

---

# Strategy Comparison

## Learn-DE Repository

```text
Strategy: GitHub Flow
Driving property: A solo learner using one evolving main branch and short-lived task branches.
Main cost: Pull Requests add some process overhead for very small changes.
```

---

## Quarterly Business Application

```text
Strategy: Git Flow
Driving property: Multiple release versions and release activities must be supported in parallel.
Main cost: More long-lived branches and greater merge-management complexity.
```

---

## Continuously Deployed Cloud Service

```text
Strategy: Trunk-based development
Driving property: Mature automation and multiple production deployments per day.
Main cost: Requires strong testing, feature flags, monitoring, and disciplined integration.
```

---

# What I Learned

* A branching strategy should be chosen based on the project's actual release and collaboration requirements.
* GitHub Flow works well when one stable branch receives changes through short-lived branches and Pull Requests.
* Git Flow can be useful when teams must prepare future releases while maintaining several supported versions.
* Trunk-based development works best when teams integrate frequently and have mature automated testing and deployment systems.
* Git Flow introduces additional branch-management overhead.
* Trunk-based development requires reliable automation and engineering discipline.
* No branching strategy is automatically best for every project.
* Team size alone does not determine the correct strategy.
* Release cadence, support requirements, testing maturity, and deployment practices are more important factors.
* The repository's real branch history should support any claim about the strategy being used.
