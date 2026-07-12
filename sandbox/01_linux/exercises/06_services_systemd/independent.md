# Independent Exercise — Lesson 06: Services & systemd

## Goal

Prove that systemd's `Restart=on-failure` actually works, not just that you
can copy the directive into a unit file.

## Task

Using your own systemd knowledge (or conceptual understanding, if your WSL
doesn't have systemd enabled), design a practice service whose script
deliberately **exits** after a short time (unlike Lesson 06's infinite
loop) with a non-zero exit code, configured with `Restart=on-failure`.
Start it, then demonstrate that systemd actually restarts it automatically
after each exit — don't just state that it should.

If systemd isn't available on your setup, instead write a one-page
conceptual explanation: given the unit file you'd write, trace through
exactly what systemd would do on each restart, including what limits
(`StartLimitIntervalSec`, `StartLimitBurst`) would eventually stop it from
restarting forever.

## Constraints

- Use a distinctly named unit (not `declab-practice.service` again — pick
  a new name so you don't collide with Lesson 06's cleanup).
- Fully stop, disable, and remove the unit file when finished.

## Expected Behavior

If hands-on: `systemctl status` should show a restart count greater than
zero, and successive checks should show the process's PID changing each
time (proof it's a new process, not the same one still running).

## Validation Commands

- `systemctl status <your-service>` (repeated a few times, a few seconds apart)
- `journalctl -u <your-service>` (if available) to see the restart history

## Evidence to Submit

In `notes/lesson_06_evidence.md`: your unit file contents, the script's
exit behavior, and either (a) real `systemctl status`/`journalctl` output
showing multiple restarts with changing PIDs, or (b) your conceptual
walkthrough if systemd wasn't available.

## Do Not

- Do not leave the practice unit registered after this exercise.
- Do not apply `Restart=on-failure` experiments to any pre-existing service.
