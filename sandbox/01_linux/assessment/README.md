# Phase 01 Practical Assessment

This is the **one** assessment for Phase 01 — there is no separate quiz or
exam. It simulates a real engineering task rather than testing recall.

## Before You Start

This assessment integrates Lessons 03–12. Re-read the safety framing in
each of those lessons if you skipped ahead. Everything here happens inside
`sandbox/01_linux/workspace/` (or your own `/home/<user>` locations for
users/services/cron/SSH, as each lesson specified) — nothing here touches
`/etc`, `/mnt/c`, or any pre-existing system service or user account.

**No solution is provided for this assessment.** You are being evaluated on
your own design choices, evidence, and explanations — see
[`rubric.md`](rubric.md) for exactly how. This is the same **Evidence
Review** standard applied throughout every lesson: commands used, terminal
output, validation results, written explanation, troubleshooting notes,
and overall understanding — not a written test.

## Scenario

You're setting up your own machine for Data Engineering work, as if
onboarding onto a new team. Do the following, in your own way, using what
you learned in Lessons 03–12:

1. **User & permissions setup.** Create a dedicated non-root practice user
   for "pipeline work" and a shared practice directory with permissions
   that reflect a real access policy you design (e.g., a specific group
   can read/write, everyone else cannot). Justify your permission choices.

2. **Packages & services.** Install one small package your practice setup
   needs (your choice). Wrap a long-running dummy process (a simple loop
   script, as in Lesson 06) as a systemd service — or, if systemd isn't
   enabled on your WSL setup, write a clear conceptual walkthrough of what
   you would have configured and why.

3. **A real shell script.** Write a script (Lesson 10 style: validated
   arguments, `set -euo pipefail`, meaningful exit codes) that processes
   files in your shared practice directory and logs its own activity to a
   file it manages.

4. **Scheduling.** Schedule that script with cron, using absolute paths
   and explicit output redirection. Prove it actually ran on schedule, not
   just that it's registered.

5. **SSH.** Generate a dedicated practice SSH keypair and demonstrate
   working key-based authentication — against GitHub (client-only,
   zero server risk) is sufficient. You are **not required** to install or
   configure a local SSH server, and you must **not** modify
   `/etc/ssh/sshd_config` or disable password authentication as part of
   this assessment.

6. **Break something on purpose, then fix it.** Pick one piece of your
   setup (a permission, a cron path, a service config) and deliberately
   misconfigure it so it fails. Diagnose the failure using the
   troubleshooting skills from the relevant lesson, fix it, and document
   the whole process — this "incident report" is itself graded evidence,
   not a formality.

## Constraints (Safety)

- Everything lives under `sandbox/01_linux/workspace/` or your own
  practice user/service/cron entries — never a pre-existing system
  service, user, or config file.
- No `sudo apt remove` on anything you didn't install for this assessment.
- No `sshd_config` edits, no disabling password authentication.
- Clean up your practice user, service, and cron entry when you're
  completely done (keep evidence of them *before* cleanup — see below).

## Evidence Requirements

For **each** of the 6 steps above, record in
`notes/assessment_evidence.md` (use
[`../notes/evidence_template.md`](../notes/evidence_template.md) as the
format):
- The commands you actually ran, in order.
- Real terminal output (not paraphrased).
- A short explanation of what happened and why your design choice was
  correct for the scenario.
- Troubleshooting notes for step 6 (required) and for any other step where
  something didn't work the first time.

Points are awarded for evidence and understanding — **a completed
checklist with no evidence behind it earns no credit.** See
[`rubric.md`](rubric.md).

## When You're Done

- Confirm every cleanup step from each lesson's safety rules has been
  followed (practice user removed, service disabled/removed, cron entry
  removed).
- Fill in [`../reflection.md`](../reflection.md).
- Self-score using [`rubric.md`](rubric.md) before moving on to Phase 02
  and Checkpoint 1.
