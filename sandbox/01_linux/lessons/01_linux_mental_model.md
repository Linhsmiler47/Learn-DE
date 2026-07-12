# Lesson 01 — Linux & Ubuntu/WSL Mental Model

**Estimated effort:** Theory ~40 min · Guided practice ~20 min · Independent practice ~20 min

## Why This Matters

Every phase after this one assumes you can reason about *which* Linux you're
actually standing on. "Ubuntu" is not one thing — Ubuntu Server, an Ubuntu
VM, and Ubuntu-on-WSL behave differently in exactly the areas Data
Engineering tools care about most: services, scheduling, and networking. Get
this mental model wrong and you'll spend later phases debugging your
environment instead of the tool you're trying to learn.

## Learning Objectives

- Distinguish native Linux, Ubuntu Server, an Ubuntu VM, and Ubuntu on WSL.
- Explain why `/mnt/c` and `/home/<user>` behave differently, and know which
  one to use for Linux work.
- Check, on your own machine, whether systemd is running under WSL.
- Know which later lessons (services, cron, SSH, networking) need a WSL
  reality-check before you trust generic Linux instructions.

## Terminology

| Term | Definition |
|---|---|
| Kernel | The core program that talks to hardware and manages processes, memory, and files. Ubuntu's kernel and WSL2's kernel are both real Linux kernels — this is why WSL2 can run almost anything native Linux can. |
| Distribution (distro) | An OS built around the Linux kernel plus a package manager and userland tools. Ubuntu is a distribution. |
| WSL | Windows Subsystem for Linux — a Windows feature that runs a Linux distribution alongside Windows. |
| WSL1 vs WSL2 | WSL1 translates Linux syscalls to Windows syscalls (no real Linux kernel). WSL2 runs a real, lightweight Linux kernel inside a fast, managed virtual machine. **Assume WSL2** — it's the default since 2019 and is what this path targets. |
| `init` / PID 1 | The first process the kernel starts, responsible for starting everything else. On most modern Linux (including Ubuntu Server and, if enabled, WSL2) this is `systemd`. |
| `drvfs` | The WSL2 filesystem driver that mounts your Windows drives (e.g., `C:`) into Linux at `/mnt/c`. It's a translation layer, not a native Linux filesystem. |
| ext4 | The native Linux filesystem WSL2 uses for its own virtual disk — this is what backs `/home/<user>`. |

## Mental Model

```
                     Your Windows machine
                     ─────────────────────
                     │  Windows kernel    │
                     │  ┌──────────────┐  │
                     │  │  WSL2 VM     │  │   <- lightweight, managed VM,
                     │  │  ┌────────┐  │  │      real Linux kernel inside
                     │  │  │ Linux  │  │  │
                     │  │  │ kernel │  │  │
                     │  │  └────────┘  │  │
                     │  │  Ubuntu      │  │
                     │  │  userland    │  │
                     │  └──────────────┘  │
                     └─────────────────────┘

  Two filesystems visible from inside Ubuntu-on-WSL:

  /home/<user>/...   <- lives on WSL2's own virtual ext4 disk.
                        Real Linux permissions, real Linux speed.
                        THIS is where you do Linux work.

  /mnt/c/...         <- Windows' C: drive, exposed via drvfs.
                        Permission bits are emulated, not enforced the
                        Linux way. Much slower for many small files.
                        Use only when you need to touch a Windows file.
```

Compare that to the other environments you'll hear about:

| Environment | What it actually is | Own kernel? | Boots/services like a real machine? |
|---|---|---|---|
| Native Linux (bare metal) | Linux installed directly on hardware | Yes | Yes — full boot sequence, systemd manages everything from power-on |
| Ubuntu Server | Ubuntu, usually headless, on bare metal or as a VM | Yes | Yes |
| Ubuntu VM (e.g., VirtualBox, Hyper-V) | A full virtual machine running Ubuntu | Yes (virtualized) | Yes — behaves like a real machine because it *is* a full machine, just virtualized |
| **Ubuntu on WSL2 (your setup)** | A lightweight, Microsoft-managed VM running a real Linux kernel, tightly integrated with Windows | Yes (shared, minimal) | **Not by default** — WSL starts on demand when you open a terminal, not via a traditional boot sequence. Whether systemd runs at all depends on configuration (see below). |

## Theory

**Why this distinction matters for you specifically**: this repository's
`CLAUDE.md` and requirements doc assume "Ubuntu/WSL" as one phrase, but a
lot of standard Ubuntu documentation silently assumes native Linux or a VM.
Three things behave differently on WSL2 and will bite you in later lessons
if you don't know it now:

1. **No traditional boot.** A real machine or VM boots once, runs
   systemd's full startup sequence, and services start automatically. WSL2
   starts a minimal environment the first time you open a shell (or run a
   `wsl` command from Windows) and can shut the whole VM down when idle.
   Anything that "starts on boot" on native Linux may need to be started by
   *you*, by hand, each session, on WSL — unless systemd is enabled and
   configured to auto-start it.

2. **systemd is optional, not guaranteed.** Since 2022, WSL2 *can* run
   systemd as PID 1, but only if `/etc/wsl.conf` explicitly enables it.
   Older setups, or distros you haven't configured, run a minimal init
   instead — and `systemctl` simply won't work.

3. **Two filesystems, two rule sets.** `/mnt/c` looks like a normal
   directory but is Windows' NTFS underneath, translated by `drvfs`.
   Permission and ownership changes there are unreliable and don't behave
   like real Linux permissions. `/home/<user>` is a real Linux filesystem —
   this is where Lessons 03+ (permissions, services, scripts) must happen.

## Check Your Own Machine

Run these (read-only, zero risk) commands and note the results — you'll
need them for later lessons:

```bash
# Is systemd running as PID 1?
ps -p 1 -o comm=

# What does /etc/wsl.conf say (if it exists)?
cat /etc/wsl.conf

# Confirm you're on WSL2's real Linux kernel
cat /proc/version

# Where is your home directory, and is it on the Linux side?
echo $HOME
df -h $HOME | tail -1

# Does /mnt/c exist and what filesystem type is it?
mount | grep /mnt/c
```

**Reference example** (from the machine this course was authored on — your
output may differ, and that's the point of checking):

```
$ ps -p 1 -o comm=
systemd
$ cat /etc/wsl.conf
[boot]
systemd=true

[user]
default=linhtran
```

This machine has systemd **enabled**. If yours prints `init` instead of
`systemd`, or `/etc/wsl.conf` has no `[boot] systemd=true` line, later
lessons on services/cron/SSH will behave differently for you — each of
those lessons tells you exactly what changes.

## WSL Behavior Reference (used throughout Phase 01)

| Topic | Works normally in WSL? | Needs systemd? | Notes |
|---|---|---|---|
| Filesystem navigation, file ops | Yes, on `/home/<user>` | No | Avoid `/mnt/c` for permission-sensitive exercises |
| Permissions (`chmod`/`chown`) | Yes, on `/home/<user>` | No | Unreliable/emulated on `/mnt/c` — see Lesson 03 |
| Users & groups, `sudo` | Yes | No | WSL has its own Linux user namespace, separate from your Windows account |
| Processes (`ps`, `kill`, jobs) | Yes | No | You'll only see processes inside this WSL VM, not Windows processes |
| Services (`systemctl`) | **Only if systemd is enabled** | Yes | See Lesson 06 for the check and the fallback if it's not enabled |
| Package management (`apt`) | Yes | No | Works exactly like native Ubuntu |
| Environment variables | Yes | No | WSL adds a few extra variables (e.g., `WSL_DISTRO_NAME`) you'll notice in Lesson 08 |
| Logs (`journalctl`) | **Only if systemd is enabled** | Yes | Falls back to plain files under `/var/log` otherwise — see Lesson 09 |
| Shell scripting | Yes | No | Fully normal |
| Cron | **Depends on systemd being enabled AND the cron service being started** | Effectively yes, in practice | See Lesson 11 — cron itself doesn't require systemd, but WSL's lack of auto-boot means *something* has to start the cron daemon each session |
| SSH client (`ssh`) | Yes | No | Fully normal, used constantly (e.g., GitHub) |
| SSH server (`sshd`) | Usually not installed by default; startable manually or via systemd if enabled | Effectively yes, in practice | See Lesson 12 |
| Networking (`ip`, `ping`, `ss`) | Mostly yes | No | WSL2 networks through a virtual switch; inbound connections from your LAN need extra configuration not covered here — treat as conceptual for anything beyond localhost |

You will see this table's rows referenced again, in more depth, inside
Lessons 03, 06, 09, 11, and 12.

## Guided Practice

See [`exercises/01_linux_mental_model/guided.md`](../exercises/01_linux_mental_model/guided.md).
You'll run the "Check Your Own Machine" commands above, plus a couple more,
and record the results in your own words.

## Common Mistakes

- Assuming a tutorial written for "Ubuntu" automatically applies unchanged
  to WSL — always ask "does this rely on a boot sequence, systemd, or
  inbound networking?" before trusting it blindly.
- Doing permission/ownership exercises inside `/mnt/c` and being confused
  when `chmod` doesn't seem to do anything.
- Confusing your Windows username with your WSL Linux username — they are
  often different and unrelated.

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| `ps -p 1 -o comm=` prints `init` not `systemd` | systemd not enabled for this distro | See Lesson 06 for how to check/enable it — not required for this lesson |
| `cat /etc/wsl.conf` says "No such file or directory" | No custom WSL config has been set yet | Normal — it means you're on WSL defaults; not an error |
| `/mnt/c` doesn't exist | Not running under WSL, or drive mounting disabled | If you're in a container/VM instead of WSL, some WSL-specific notes won't apply to you — that's fine, treat them as conceptual |

## Knowledge Check

1. **What is the practical difference between an Ubuntu VM and Ubuntu on WSL2, given that both run a real Linux kernel?**
   *Answer: A VM boots and behaves like an independent machine with a full boot sequence; WSL2 is a managed, lightweight VM that Windows starts on demand and does not go through a traditional boot sequence, so nothing "starts on boot" unless explicitly configured.*
2. **Why shouldn't you do permission exercises under `/mnt/c`?**
   *Answer: `/mnt/c` is Windows' NTFS filesystem exposed through a translation layer (`drvfs`); Linux permission bits are emulated there, not enforced the same way as on a real Linux filesystem, so `chmod`/`chown` results are unreliable.*
3. **How do you check whether systemd is PID 1 on your system?**
   *Answer: `ps -p 1 -o comm=` — it prints `systemd` or `init` (or another init program).*
4. **Where should your Data Engineering project files live for Linux exercises to behave predictably?**
   *Answer: Under `/home/<user>/...` (the WSL2 native ext4 filesystem), not under `/mnt/c`.*

## Completion Checklist

- [ ] You can name the difference between native Linux, Ubuntu Server, an Ubuntu VM, and Ubuntu on WSL2.
- [ ] You've run the "Check Your Own Machine" commands and recorded your own results.
- [ ] You know whether your own WSL has systemd enabled.
- [ ] You understand why `/home/<user>` is preferred over `/mnt/c` for this course's exercises.

## Reference Materials

- No direct source in `ref roadmap/` covers WSL specifically — this lesson
  is authored fresh for your environment.
- Supplementary/optional: [Computer architecture lecture (Vietnamese)](../../../ref%20roadmap/My%20mentor/BUỔI%201/LESSON%201%20-%20TÂM%20PHÁP%20IT%20-%20Bài%20giảng%20_Kiến%20trúc%20máy%20tính.pdf) — general OS/hardware background, not WSL-specific.

## Next

Guided practice: [`exercises/01_linux_mental_model/guided.md`](../exercises/01_linux_mental_model/guided.md)
Independent exercise: [`exercises/01_linux_mental_model/independent.md`](../exercises/01_linux_mental_model/independent.md)
Next lesson: [02 — Filesystem Hierarchy & Navigation](02_filesystem_hierarchy.md)
