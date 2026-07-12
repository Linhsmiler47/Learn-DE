# Lesson 06 — Services & systemd

**Estimated effort:** Theory ~35 min · Guided practice ~30 min · Independent practice ~25 min

## Why This Matters

PostgreSQL, Docker, Airflow's webserver — most Data Engineering tools you'll
install from Phase 05 onward run as long-lived **services**, managed by
systemd. This is also the single biggest place WSL diverges from a normal
Ubuntu machine, so getting the mental model (and your own machine's
reality) straight here saves confusion in every later phase.

## Learning Objectives

- Explain what a service is and what systemd does.
- Check whether your own WSL setup has systemd enabled.
- Use `systemctl` to inspect, start, stop, enable, and disable a service.
- Write and register a minimal custom systemd service, safely.

## WSL Context — Read This Before Anything Else

**This is the single most important WSL caveat in Phase 01.**

On native Linux (and a full VM), systemd is always PID 1 and manages the
entire boot sequence — services marked "enabled" start automatically every
time the machine powers on. On WSL2, this is **not guaranteed**:

| Your situation | What to expect |
|---|---|
| `/etc/wsl.conf` has `[boot]` section with `systemd=true`, AND `ps -p 1 -o comm=` prints `systemd` | `systemctl` works exactly like native Ubuntu. Enabled services start automatically each time WSL starts (i.e., when you open your first terminal after a full WSL shutdown). |
| `ps -p 1 -o comm=` prints `init` or something else | `systemctl` commands will fail or do nothing meaningful. Treat this whole lesson's hands-on commands as **conceptual only** — read and understand them, but don't expect `systemctl start` to work. Enabling systemd requires editing `/etc/wsl.conf` and running `wsl --shutdown` from Windows PowerShell, which is outside the scope of a beginner exercise (it affects your whole WSL distro, not just this course) — treat it as an optional advanced step, not a requirement. |

**Check yours first:**

```bash
ps -p 1 -o comm=
cat /etc/wsl.conf 2>/dev/null || echo "(no wsl.conf — systemd likely not explicitly enabled)"
```

The reference machine this course was authored on has systemd enabled
(`/etc/wsl.conf` contains `[boot]\nsystemd=true`), so the examples below
show real, working output. If your check shows `init` instead, follow along
conceptually — Lessons 09, 11, and 12 will tell you the fallback commands
that work either way.

## Terminology

| Term | Definition |
|---|---|
| Service (unit) | A systemd-managed program with a defined start/stop/restart behavior, described by a `.service` file. |
| Unit file | The configuration file describing a service (or timer, socket, etc.) — e.g. `/usr/lib/systemd/system/cron.service`. |
| Enabled vs Active | "Enabled" means "start automatically at boot." "Active" means "running right now." A service can be enabled but not currently active, or active without being enabled. |
| Daemon | A program designed to run continuously in the background as a service (e.g., `cron`, `sshd`). |

## Mental Model

```
systemd (PID 1)
 ├── cron.service       [enabled, active]   <- starts at boot, running now
 ├── ssh.service        [not installed on this machine by default]
 ├── docker.service     [installed in Phase 05, enabled+active after that]
 └── your-custom.service [what you'll create in this lesson's exercise]
```

`systemctl status <service>` tells you both facts at once — whether it's
enabled (will start on boot) and active (running right now) — which is why
it's the single most useful command in this lesson.

## Theory

A service unit file is a small, declarative text file — this itself
previews Phase 04 (Configuration) and Phase 07 (Terraform)'s whole idea of
describing desired state instead of issuing one-off commands. A minimal
unit file looks like:

```ini
[Unit]
Description=My practice service

[Service]
ExecStart=/home/linhtran/Projects/Learn-DE/sandbox/01_linux/workspace/services_practice/loop.sh
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

- `[Unit]` — metadata and dependency ordering.
- `[Service]` — what to actually run, and how to handle it exiting/crashing.
- `[Install]` — how `enable` should wire it into the boot sequence.

## Command Syntax and Safety Notes

| Command | What it changes | Why elevated permission is required | Risk level | How to verify | How to undo |
|---|---|---|---|---|---|
| `systemctl status <service>` | Nothing — read-only | No `sudo` needed | None | — | — |
| `systemctl start <service>` | Starts the service right now (until stopped or reboot) | Yes — affects a system-wide daemon | **Low** for a practice service you wrote; **do not** start/stop unfamiliar system services as an exercise | `systemctl status <service>` shows `active (running)` | `sudo systemctl stop <service>` |
| `systemctl stop <service>` | Stops the service right now | Yes | Low, for your own practice service | `systemctl status` shows `inactive` | `sudo systemctl start <service>` |
| `systemctl enable <service>` | Registers the service to auto-start at boot (symlinks into a `.wants` directory) | Yes | Low for a practice service; **be cautious enabling anything you don't understand** — on native Linux this persists across every future reboot | `systemctl is-enabled <service>` | `sudo systemctl disable <service>` |
| `systemctl daemon-reload` | Tells systemd to re-read unit files after you edit one | Yes, editing unit files under `/etc/systemd/system/` requires root | None — this is just a refresh | Re-running `systemctl status` picks up the change | N/A, no state changed |

**Rule for this lesson**: only create/enable/start a systemd unit you wrote
yourself, in the practice location shown below. Never `stop`, `disable`, or
`start` a pre-existing system service (like `cron` or `chrony`) as a
learning exercise — read their status, don't change their state.

## Step-by-Step Example

```bash
# 1. Check systemd status (read-only, always safe)
$ systemctl status cron.service
● cron.service - Regular background program processing daemon
     Loaded: loaded (/usr/lib/systemd/system/cron.service; enabled; preset: enabled)
     Active: active (running) since Sun 2026-07-12 10:33:56 +07; 4h 55min ago
     ...

# 2. Write a tiny practice script and a unit file (in your workspace)
$ mkdir -p ~/Projects/Learn-DE/sandbox/01_linux/workspace/services_practice
$ cat > ~/Projects/Learn-DE/sandbox/01_linux/workspace/services_practice/loop.sh <<'EOF'
#!/bin/bash
while true; do
  echo "practice service tick: $(date)"
  sleep 30
done
EOF
$ chmod +x ~/Projects/Learn-DE/sandbox/01_linux/workspace/services_practice/loop.sh

# 3. Register the unit (requires sudo — writes to /etc/systemd/system/)
$ sudo tee /etc/systemd/system/declab-practice.service > /dev/null <<'EOF'
[Unit]
Description=DE learning path practice service

[Service]
ExecStart=/home/linhtran/Projects/Learn-DE/sandbox/01_linux/workspace/services_practice/loop.sh
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF

$ sudo systemctl daemon-reload
$ sudo systemctl start declab-practice.service
$ systemctl status declab-practice.service
● declab-practice.service - DE learning path practice service
     Active: active (running) ...

# 4. Clean up when done practicing
$ sudo systemctl stop declab-practice.service
$ sudo systemctl disable declab-practice.service
$ sudo rm /etc/systemd/system/declab-practice.service
$ sudo systemctl daemon-reload
```

## Guided Practice

See [`exercises/06_services_systemd/guided.md`](../exercises/06_services_systemd/guided.md).

## Common Mistakes

- Forgetting `daemon-reload` after editing a unit file — systemd won't see
  your changes until you tell it to re-read them.
- Enabling a practice service and forgetting to disable/remove it — it'll
  keep starting every time you open WSL.
- Assuming `systemctl` will work at all without checking PID 1 first (see
  the WSL Context box above) — save yourself the confusion.

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| `systemctl: command not found` or `System has not been booted with systemd` | systemd is not PID 1 on your WSL setup | Confirmed by `ps -p 1 -o comm=` showing something other than `systemd`. Treat this lesson's hands-on parts as conceptual; see the WSL Context box. |
| Unit file changes don't seem to apply | Forgot `systemctl daemon-reload` | Run it, then retry |
| `Failed to start ...: Unit not found` | Typo in service name, or file not in `/etc/systemd/system/` | Check exact filename with `systemctl list-unit-files \| grep declab` |

## Knowledge Check

1. **What's the difference between "enabled" and "active" for a service?**
   *Answer: Enabled means it will start automatically at boot; active means it's running right now. A service can be one without the other.*
2. **What command must you run after editing a unit file, before your change takes effect?**
   *Answer: `sudo systemctl daemon-reload`.*
3. **Why might `systemctl` not work at all on some WSL setups?**
   *Answer: systemd must be PID 1 and explicitly enabled via `/etc/wsl.conf`; older or unconfigured WSL setups use a minimal init instead, where `systemctl` has nothing to talk to.*

## Completion Checklist

- [ ] You've checked whether your own WSL has systemd enabled and noted the result.
- [ ] You can read a `systemctl status` output and state whether the service is enabled and/or active.
- [ ] You've written and registered a minimal custom service, started it, verified it, then fully cleaned it up (stopped, disabled, unit file removed).
- [ ] You never modified a pre-existing system service's state.

## Reference Materials

- No direct source in `ref roadmap/` teaches systemd/services as a concept —
  authored fresh. Tangentially related: [How an app gets installed and executed in Ubuntu](../../../ref%20roadmap/My%20mentor/BUỔI%202/BÀI%20GIẢNG/HỆ%20ĐIỀU%20HÀNH/LINUX%20OS%20-%20UBUNTU/LESSON%202%20-%20UBUNTU%20-%20Cách%20mà%20một%20ứng%20dụng%20được%20cài%20đặt%20và%20thực%20thi%20trong%20Ubuntu.docx).

## Next

Guided practice: [`exercises/06_services_systemd/guided.md`](../exercises/06_services_systemd/guided.md)
Independent exercise: [`exercises/06_services_systemd/independent.md`](../exercises/06_services_systemd/independent.md)
Next lesson: [07 — Package Management (APT)](07_package_management.md)
