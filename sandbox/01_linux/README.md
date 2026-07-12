# Phase 01 — Linux and Development Environment

This phase is a full guided learning module, not just a syllabus. If
you're starting fresh, go straight to
[`lessons/01_linux_mental_model.md`](lessons/01_linux_mental_model.md) —
the rest of this README is the map, not the content itself.

## Learning Objectives

- Navigate and administer an Ubuntu/WSL system confidently from the shell,
  knowing precisely where WSL behaves differently from native Linux.
- Understand the Linux filesystem hierarchy, permissions, users, and groups.
- Manage processes, services, packages, environment variables, and logs.
- Write basic shell scripts, schedule them with cron, and use SSH safely.

## Prerequisites

- None — this is the entry point of the whole learning path.

## How This Module Is Organized

```
01_linux/
├── README.md            <- you are here — navigation only, not content
├── lessons/              12 lessons, each a complete guided unit (theory,
│                         mental model, WSL notes, worked examples, safety
│                         notes, troubleshooting, knowledge checks)
├── exercises/            guided.md + independent.md per lesson
├── assessment/           the ONE practical assessment for this phase + rubric
├── cheatsheet/           one consolidated command quick-reference
├── notes/                your evidence log + free-form notes (graded)
├── workspace/            your safe practice sandbox (ungraded, disposable)
└── reflection.md         phase-level reflection, completed after the assessment
```

This phase follows the repository-wide phase structure standard — see
[`../_templates/PHASE_STRUCTURE.md`](../_templates/PHASE_STRUCTURE.md).
There are no quizzes or answer keys in this framework: understanding is
demonstrated through an **Evidence Review** at the end of every lesson —
your own commands, terminal output, validation results, explanations, and
troubleshooting notes, captured in `notes/` — not a written test.

## Lesson Sequence

| # | Lesson | Est. effort (theory/guided/independent) |
|---|---|---|
| 01 | [Linux & Ubuntu/WSL Mental Model](lessons/01_linux_mental_model.md) | 40 / 20 / 20 min |
| 02 | [Filesystem Hierarchy & Navigation](lessons/02_filesystem_hierarchy.md) | 30 / 25 / 25 min |
| 03 | [File & Directory Permissions, Ownership](lessons/03_permissions_ownership.md) | 35 / 30 / 25 min |
| 04 | [Users, Groups & Privilege Escalation](lessons/04_users_groups_sudo.md) | 30 / 25 / 25 min |
| 05 | [Processes & Job Control](lessons/05_processes_job_control.md) | 30 / 25 / 20 min |
| 06 | [Services & systemd](lessons/06_services_systemd.md) | 35 / 30 / 25 min |
| 07 | [Package Management (APT)](lessons/07_package_management.md) | 20 / 20 / 15 min |
| 08 | [Environment Variables & Shell Configuration](lessons/08_environment_variables.md) | 25 / 20 / 20 min |
| 09 | [Logs & Monitoring](lessons/09_logs_monitoring.md) | 25 / 25 / 20 min |
| 10 | [Basic Shell Scripting](lessons/10_shell_scripting.md) | 35 / 30 / 30 min |
| 11 | [Scheduling with Cron](lessons/11_cron_scheduling.md) | 25 / 25 / 20 min |
| 12 | [SSH & Basic Networking Commands](lessons/12_ssh_networking.md) | 40 / 30 / 20 min |

Total estimated effort: roughly 12–16 hours across theory, guided, and
independent practice, plus the practical assessment. Pace yourself — this
is a foundation phase, not a race.

## Your Environment Matters: WSL-Awareness Runs Throughout

This module assumes Ubuntu-on-WSL2 as the primary environment (per
`CLAUDE.md`). Lesson 01 opens with a full comparison of native Linux,
Ubuntu Server, an Ubuntu VM, and Ubuntu on WSL — including the
`/mnt/c` vs `/home/<user>` filesystem split — and every later lesson
touching systemd, services, cron, SSH, networking, or permissions
explicitly states whether it works normally in WSL, needs systemd enabled,
behaves differently, or is conceptual-only on your setup. Check your own
machine in Lesson 01 before assuming any example output matches yours.

## Safety Model

- All hands-on file/permission/process/script/log work happens in
  [`workspace/`](workspace/README.md) — never in a system directory.
- Every risky command category (`sudo`, `chmod`, `chown`, `useradd`,
  `usermod`, `systemctl`, package removal, cron, SSH) is documented in its
  lesson with: what it changes, why elevation is needed, its risk level,
  how to verify the result, and how to undo it.
- SSH is taught safely: keys, `known_hosts`, `authorized_keys`, and
  key-based auth are all required; disabling password authentication and
  editing `/etc/ssh/sshd_config` are **optional advanced challenges only**,
  never a required step, with the lock-yourself-out risk explained before
  any server-side configuration is shown.
- Nothing in `workspace/` is version-controlled except its own README —
  see the root [`.gitignore`](../../.gitignore).

## The Learning Cycle (per lesson)

`Learn → Observe → Guided practice → Independent exercise → Validate → Debug → Evidence Review`
— then, at the phase level, once all 12 lessons are done:
`Practical assessment → Reflect`.

**Evidence Review** is what ends every lesson in this framework — there is
no quiz. It means writing up, in `notes/lesson_NN_evidence.md` (template:
[`notes/evidence_template.md`](notes/evidence_template.md)): the commands
you used, the real terminal output you got, your validation results, a
written explanation in your own words, any troubleshooting notes, and
whether you genuinely understand the concept — not whether a checkbox is
ticked.

## Assessment and Scoring

100 points total — see [`assessment/rubric.md`](assessment/rubric.md) for
the full breakdown. There is **one** practical assessment for this phase
(no separate exam), simulating a real engineering scenario. Scoring is
evidence-based throughout: what's actually in your `notes/` evidence
files, not which checkboxes are ticked.

| Category | Points |
|---|---|
| Guided exercises | 25 |
| Independent exercises | 30 |
| Practical assessment | 35 |
| Documentation and reflection | 10 |

**80–100**: pass, continue. **70–79**: review weak categories, reassess.
**Below 70**: repeat the weakest lessons and exercises.

## Reference Materials (`ref roadmap/`, read-only)

Each lesson links its own specific reference material inline. Direct
source exists for the filesystem, permissions (partial), logs, cron, and
key-value/env-var lessons; Git, systemd/services, package management
concepts, shell scripting, users/groups, and SSH are authored fresh (no
direct `ref roadmap/` source) — each lesson states this explicitly rather
than fabricating a link.

## When You're Done

Complete [`reflection.md`](reflection.md), self-score against
[`assessment/rubric.md`](assessment/rubric.md), then continue to
[Phase 02 — Git and GitHub](../02_git_github/README.md) and
[Checkpoint 1](../checkpoints/checkpoint_01_linux_git/README.md).
