# Lesson 04 — Users, Groups & Privilege Escalation

**Estimated effort:** Theory ~30 min · Guided practice ~25 min · Independent practice ~25 min

## Why This Matters

Almost everything from here on (installing packages, running services,
configuring Docker) requires understanding *why* a command needs elevated
privilege and what that privilege actually does. Blindly typing `sudo` in
front of anything that fails is how systems get broken; understanding it is
how you avoid that.

## Learning Objectives

- Explain the difference between a regular user and root.
- Read `/etc/passwd` and `/etc/group` to understand what a user/group is.
- Use `sudo` deliberately, understanding exactly what it grants.
- Create a practice user and group safely, and know how to remove them.

## WSL Context

| Aspect | Behavior in WSL2 |
|---|---|
| Users/groups | Fully normal Linux user/group system, isolated from your Windows account. Your WSL username is often different from your Windows username. |
| `sudo` | Works normally. Your WSL user is typically already in the `sudo` group by default (the user created during WSL setup). |
| Root | WSL does have a real root user; `sudo` and `su` both work as on native Linux. |

## Terminology

| Term | Definition |
|---|---|
| User | An account identified by a UID (user ID); UID 0 is always root. |
| Group | A named collection of users, identified by a GID; used to share permissions among multiple users. |
| root | The Linux superuser — bypasses almost all permission checks. |
| `sudo` | "Substitute user, do" — runs a single command as another user (root by default), if you're authorized. |
| `su` | "Switch user" — starts a new shell as another user. |
| `/etc/passwd` | The file listing all user accounts (no passwords stored here despite the name — that's `/etc/shadow`). |
| `/etc/group` | The file listing all groups and their members. |

## Mental Model

```
root (UID 0)
 │
 │  sudo (temporary, command-scoped elevation, logged, requires your password)
 │
your user (UID 1000, e.g. "linhtran")
 ├── primary group: linhtran (UID 1000's own group)
 └── supplementary groups: sudo, adm, cdrom, dip, plugdev, users, ...
        (each supplementary group grants specific extra permissions,
         e.g. "sudo" group members may use the sudo command at all,
         "docker" group — added later in Phase 05 — lets you run docker
         without sudo)
```

`sudo` does **not** log you in as root permanently — it elevates a single
command, then you're back to your normal user. This is safer and more
auditable than `su`, which starts a whole root shell.

## Theory

Why does installing a package (Lesson 07) need `sudo` but editing a file in
your own home directory doesn't? Because `apt` writes to `/usr`, `/etc`,
and other system-owned locations that your regular user doesn't have write
access to — by design, so that one compromised user account can't rewrite
system binaries. `sudo` is the deliberate, logged exception path for when
you (a human who's supposed to have this power) need to cross that boundary.

## Command Syntax and Safety Notes

| Command | What it changes | Why elevated permission is required | Risk level | How to verify | How to undo |
|---|---|---|---|---|---|
| `sudo <command>` | Runs one command as root | It runs as root by definition — that's what `sudo` means | Depends entirely on `<command>` — `sudo ls` is harmless, `sudo rm -rf /` is catastrophic. **Always read the command before pressing enter.** | Check the command's own output/effect | N/A — undo depends on what the command did |
| `useradd -m <name>` | Creates a new user account and home directory | Modifying `/etc/passwd`/`/etc/shadow` requires root | **Low**, if it's a throwaway practice user | `id <name>`, `getent passwd <name>` | `sudo userdel -r <name>` (see below) |
| `usermod -aG <group> <name>` | Adds a user to a supplementary group | Modifying `/etc/group` requires root | **Low** for a practice user; be careful adding **yourself** to a group — some (like `sudo`) grant real elevated power | `groups <name>` | `sudo gpasswd -d <name> <group>` (removes from that one group) |
| `userdel -r <name>` | Deletes a user and their home directory | Same reason as `useradd` | **Medium** — irreversible; only ever run on a practice user you created yourself, never on your own account | `id <name>` should now fail | N/A — recreate the user if needed |

**Rule for this lesson**: only ever create/delete a dedicated **practice**
user (e.g., `declab`), never modify your own primary account's group
memberships as an exercise, and never delete your own user.

## Step-by-Step Example

```bash
$ whoami
linhtran
$ id
uid=1000(linhtran) gid=1000(linhtran) groups=1000(linhtran),27(sudo),...

$ sudo useradd -m declab
[sudo] password for linhtran:
$ id declab
uid=1001(declab) gid=1001(declab) groups=1001(declab)

$ getent passwd declab
declab:x:1001:1001::/home/declab:/bin/sh

$ sudo usermod -aG users declab
$ groups declab
declab : declab users

# Clean up when you're done practicing:
$ sudo userdel -r declab
$ id declab
id: 'declab': no such user
```

## Guided Practice

See [`exercises/04_users_groups_sudo/guided.md`](../exercises/04_users_groups_sudo/guided.md).

## Common Mistakes

- Running `sudo` on a whole pipeline (`sudo command1 | command2`) when only
  `command1` needed elevation — only the piped command runs as root, which
  often isn't what you intended.
- Adding yourself to unfamiliar groups "just to see what happens" — some
  grant real power (e.g., `docker` group membership is root-equivalent).
- Forgetting `-r` on `userdel`, leaving an orphaned home directory behind.

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| `sudo: command not found` after adding yourself to a new group | Group membership changes require a new shell/login session to take effect | Log out and back in, or run `newgrp <group>` |
| "user 'declab' is currently used by process" on `userdel` | A shell or process is still running as that user | Exit any shell you opened as that user first |
| `useradd: command not found` | Rare, but some minimal WSL images trim admin tools | `sudo apt install passwd` (provides `useradd`/`userdel` on Debian-based systems) |

## Knowledge Check

1. **What's the difference between `sudo` and `su`?**
   *Answer: `sudo` elevates a single command and returns you to your normal user; `su` starts a new shell session as another user (root by default) until you exit it.*
2. **Why does WSL's default user usually already have `sudo` access?**
   *Answer: The first user created during WSL distro setup is automatically added to the `sudo` group.*
3. **What does `-r` do on `userdel`?**
   *Answer: Also removes the user's home directory (without it, the account is deleted but its home directory is left behind).*

## Completion Checklist

- [ ] You can explain what `sudo` actually does (and doesn't do).
- [ ] You've created and removed a practice user without touching your own account.
- [ ] You can read `/etc/passwd` and `/etc/group` entries.
- [ ] You've verified every change with `id`/`getent`/`groups` before and after.

## Reference Materials

- No direct source in `ref roadmap/` — authored fresh. The closest related
  material is [Ubuntu server administration commands](../../../ref%20roadmap/My%20mentor/BUỔI%202/BÀI%20GIẢNG/HỆ%20ĐIỀU%20HÀNH/LINUX%20OS%20-%20UBUNTU/LESSON%202%20-%20UBUNTU%20-%20Cac_lenh_quan_tri_server_Ubuntu.docx), which touches admin commands generally.

## Next

Guided practice: [`exercises/04_users_groups_sudo/guided.md`](../exercises/04_users_groups_sudo/guided.md)
Independent exercise: [`exercises/04_users_groups_sudo/independent.md`](../exercises/04_users_groups_sudo/independent.md)
Next lesson: [05 — Processes & Job Control](05_processes_job_control.md)
