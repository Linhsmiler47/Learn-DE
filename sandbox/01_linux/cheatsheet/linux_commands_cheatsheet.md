# Phase 01 — Linux Commands Cheatsheet

A consolidated quick-reference across all 12 lessons. This is a lookup
tool, not a teaching document — see `lessons/` for explanations.

## Navigation & Filesystem (Lesson 02)

| Command | Purpose |
|---|---|
| `pwd` | Print working directory |
| `cd <path>` / `cd -` / `cd ~` | Change directory / previous dir / home |
| `ls -la` | List all, long format |
| `find <path> -name "<pattern>" -type f` | Search for files |
| `tree -L <n>` | Visual directory tree, depth-limited |
| `df -h` | Mounted filesystems and space |
| `du -sh <path>` | Size of a directory |

## Permissions & Ownership (Lesson 03)

| Command | Purpose |
|---|---|
| `ls -l` | Show permission string |
| `chmod <octal> <file>` | Set permissions (e.g., `chmod 644`) |
| `chmod u+x <file>` | Symbolic form (add execute for owner) |
| `chown <user>:<group> <file>` | Change ownership (`sudo` needed) |
| `umask` | Show default permission mask for new files |

## Users, Groups, sudo (Lesson 04)

| Command | Purpose |
|---|---|
| `id [user]` | Show UID/GID/groups |
| `whoami` | Current user |
| `sudo <cmd>` | Run one command as root |
| `sudo useradd -m <name>` | Create user with home dir |
| `sudo usermod -aG <group> <name>` | Add user to group |
| `sudo userdel -r <name>` | Delete user + home dir |
| `getent passwd <name>` / `groups <name>` | Inspect user / group membership |

## Processes & Jobs (Lesson 05)

| Command | Purpose |
|---|---|
| `ps aux` | List all processes |
| `top` / `htop` | Live process view |
| `kill <pid>` | Send SIGTERM |
| `kill -9 <pid>` | Send SIGKILL (last resort) |
| `pkill -f <pattern>` | Kill by command-line match |
| `command &` | Run in background |
| `jobs` / `fg` / `bg` | Manage shell jobs |
| `Ctrl+Z` / `Ctrl+C` | Suspend / interrupt foreground process |

## Services & systemd (Lesson 06 — requires systemd enabled on WSL)

| Command | Purpose |
|---|---|
| `ps -p 1 -o comm=` | Check if systemd is PID 1 |
| `systemctl status <service>` | Enabled? Active? |
| `sudo systemctl start/stop <service>` | Start/stop now |
| `sudo systemctl enable/disable <service>` | Auto-start at boot, yes/no |
| `sudo systemctl daemon-reload` | Reload unit files after editing |

## Package Management (Lesson 07)

| Command | Purpose |
|---|---|
| `sudo apt update` | Refresh package index (no installs) |
| `sudo apt upgrade` | Upgrade installed packages |
| `sudo apt install <pkg>` | Install |
| `sudo apt remove <pkg>` | Uninstall, keep config |
| `sudo apt purge <pkg>` | Uninstall + config |
| `dpkg -l \| grep <pkg>` | Check install status |
| `dpkg -L <pkg>` | List files a package installed |
| `apt show <pkg>` | Package metadata/dependencies |

## Environment Variables (Lesson 08)

| Command | Purpose |
|---|---|
| `echo $VAR` | Print a variable |
| `export VAR=value` | Set + make inheritable by subprocesses |
| `env` / `printenv` | List all environment variables |
| `echo $PATH` | Show command search path |
| `which <cmd>` | Which `PATH` entry provides a command |
| `source ~/.bashrc` | Reload shell config after editing |

## Logs (Lesson 09)

| Command | Purpose |
|---|---|
| `tail -f <file>` | Follow a log file live |
| `less <file>` | Page through a file |
| `journalctl -u <service>` | Service logs (systemd only) |
| `journalctl -f` | Follow the journal live (systemd only) |
| `grep -i "<pattern>" <file>` | Search a log |

## Shell Scripting (Lesson 10)

| Construct | Purpose |
|---|---|
| `#!/bin/bash` | Shebang |
| `set -euo pipefail` | Fail fast on error/unset var/pipe failure |
| `"$1"`, `"$2"`, ... | Positional arguments (always quote) |
| `if [ -z "$VAR" ]; then ... fi` | Conditional |
| `for x in list; do ... done` | Loop |
| `chmod +x script.sh && ./script.sh` | Make executable and run |
| `echo $?` | Exit code of last command |

## Cron (Lesson 11)

```
* * * * *  command
│ │ │ │ │
│ │ │ │ └── day of week (0-6, Sun=0)
│ │ │ └──── month (1-12)
│ │ └────── day of month (1-31)
│ └──────── hour (0-23)
└────────── minute (0-59)
```

| Command | Purpose |
|---|---|
| `crontab -e` | Edit your own crontab |
| `crontab -l` | List your own crontab |
| `systemctl status cron.service` / `service cron status` | Is cron running? |

## SSH & Networking (Lesson 12)

| Command | Purpose |
|---|---|
| `ssh-keygen -t ed25519 -f <path>` | Generate a new keypair |
| `ssh-keygen -l -f <path>.pub` | Show a public key's fingerprint |
| `ssh -T -i <key> git@github.com` | Test key-based auth against GitHub |
| `ip addr` | Show interfaces/IPs |
| `ping -c 4 <host>` | Test reachability |
| `curl -I <url>` | HTTP headers only |
| `ss -tulpn` | Listening ports + owning process |
| `dig +short <domain>` | DNS lookup |

**Never** in this cheatsheet or this course: disabling SSH password auth,
editing `/etc/ssh/sshd_config`, or running any command against `/etc`,
`/usr`, or `/var` outside of what a lesson explicitly instructs.
