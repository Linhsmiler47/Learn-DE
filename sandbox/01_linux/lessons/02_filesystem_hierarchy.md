# Lesson 02 — Filesystem Hierarchy & Navigation

**Estimated effort:** Theory ~30 min · Guided practice ~25 min · Independent practice ~25 min

## Why This Matters

Every tool you install from Phase 05 onward puts files somewhere specific
and expects you to find them: configs in `/etc`, logs in `/var/log`,
binaries in `/usr/bin`, your own projects under `/home/<user>`. If the
hierarchy is a mystery, every later "where did that config go?" moment
turns into guesswork instead of a two-second `cd`.

## Learning Objectives

- Navigate the Linux filesystem confidently using absolute and relative paths.
- Explain what each major top-level directory is for.
- Use `ls`, `cd`, `pwd`, `find`, and `tree` to explore and locate files.
- Know, concretely, why this course's exercises live under `/home/<user>` and not `/mnt/c`.

## WSL Context

| Aspect | Behavior in WSL2 |
|---|---|
| `/home/<user>` | Real Linux (ext4) filesystem on WSL2's own virtual disk. Full Linux semantics: permissions, symlinks, case sensitivity, all normal. **Use this for everything in this course.** |
| `/mnt/c`, `/mnt/d`, etc. | Your Windows drives, mounted via `drvfs`. Case-insensitive-ish, permission bits emulated, slower for many small files (each access round-trips through the translation layer). Fine for reading a Windows file when you need to; avoid for course exercises. |
| Everything else (`/etc`, `/var`, `/usr`, ...) | Normal Linux paths inside the WSL2 VM, same as any Ubuntu install. |

This repository lives at `/home/<user>/Projects/Learn-DE` — already on the
correct (fast, fully-Linux) side. Good default; no action needed.

## Terminology

| Term | Definition |
|---|---|
| Absolute path | A path starting from `/`, e.g. `/home/linhtran/Projects`. Always means the same location regardless of where you currently are. |
| Relative path | A path interpreted from your current directory, e.g. `../sandbox`. |
| Working directory | The directory your shell is currently "in" — shown by `pwd`. |
| Symlink | A file that points to another file/directory (like a shortcut). |
| Hidden file | Any file/directory whose name starts with `.` (e.g. `.bashrc`) — not shown by default `ls`. |

## Mental Model

```
/                      <- root: everything starts here
├── home/<user>/       <- your personal files (this course lives here)
├── etc/               <- system-wide configuration files
├── var/                <- variable data: logs (var/log), spool, cache
│   └── log/
├── usr/                <- installed software, libraries, most binaries
│   ├── bin/
│   └── lib/
├── bin/, sbin/          <- essential system binaries (often symlinked into /usr on Ubuntu)
├── opt/                 <- optional/third-party software, self-contained installs
├── tmp/                 <- temporary files, cleared on reboot
├── dev/                 <- device files (hardware interfaces as files)
├── proc/, sys/          <- virtual filesystems exposing kernel/process info (not real files on disk)
└── mnt/, media/         <- mount points for other filesystems (this is where /mnt/c lives on WSL)
```

The rule of thumb: **configuration lives in `/etc`, logs live in `/var/log`,
software lives in `/usr` or `/opt`, and your own stuff lives in `/home`.**
You'll see this exact split reused constantly from Phase 05 onward.

## Theory

Linux has one unified tree — there's no "C: drive" concept. Everything,
including other physical drives or the Windows filesystem (on WSL), gets
*mounted* somewhere inside this one tree. `df -h` shows you what's mounted
where.

`/proc` and `/sys` deserve a special mention: they look like normal
directories full of files, but they're generated on the fly by the kernel
to expose live information (e.g., `/proc/<pid>/` describes a running
process — this is how tools like `ps` get their data). You'll use `/proc`
directly in Lesson 05.

## Command Syntax

| Command | Purpose | Common flags |
|---|---|---|
| `pwd` | Print working directory | — |
| `cd <path>` | Change directory | `cd -` (previous dir), `cd ~` (home) |
| `ls <path>` | List directory contents | `-l` (long/detailed), `-a` (include hidden), `-h` (human-readable sizes) |
| `find <path> -name <pattern>` | Search for files | `-type f` (files only), `-type d` (dirs only), `-mtime -1` (modified in last day) |
| `tree <path>` | Visual directory tree | `-L <n>` (limit depth) — may need `sudo apt install tree` |
| `df -h` | Show mounted filesystems and space usage | `-h` human-readable |
| `du -sh <path>` | Show size of a directory | `-s` (summary), `-h` human-readable |

## Step-by-Step Example

```bash
$ pwd
/home/linhtran

$ cd Projects/Learn-DE
$ pwd
/home/linhtran/Projects/Learn-DE

$ ls -la
total 32
drwxr-xr-x  5 linhtran linhtran 4096 Jul 12 13:55 .
drwxr-xr-x  3 linhtran linhtran 4096 Jul  5 15:07 ..
-rw-r--r--  1 linhtran linhtran  172 Jul 12 11:37 .gitignore
-rw-r--r--  1 linhtran linhtran  937 Jul 12 13:56 CLAUDE.md
drwxr-xr-x  2 linhtran linhtran 4096 Jul 12 09:28 docs
drwxr-xr-x  4 linhtran linhtran 4096 Jul 12 09:28 ref roadmap
drwxr-xr-x  7 linhtran linhtran 4096 Jul 12 14:03 sandbox

$ find sandbox -maxdepth 1 -type d
sandbox
sandbox/01_linux
sandbox/02_git_github
...

$ df -h /home/linhtran /mnt/c
Filesystem      Size  Used Avail Use% Mounted on
/dev/sdc        251G   12G  227G   6% /
C:\             476G  210G  266G  45% /mnt/c
```

Notice `/home/linhtran` and `/mnt/c` are **different filesystems** — that's
the WSL split from Lesson 01, made visible.

## Guided Practice

See [`exercises/02_filesystem_hierarchy/guided.md`](../exercises/02_filesystem_hierarchy/guided.md).

## Common Mistakes

- Using `find /` for a search — scans the entire tree including `/proc` and
  `/mnt/c`, which is slow and noisy. Scope your searches (`find ~/Projects ...`).
- Forgetting `-a` on `ls` and concluding a hidden config file "doesn't exist."
- Confusing `~` (home directory) with `/` (root) — `~` is a shortcut for
  `/home/<user>`, not the top of the tree.

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| `cd` says "No such file or directory" | Typo, or path is relative when you meant absolute | Use tab-completion; double-check with `pwd` first |
| `find` runs forever | Searching from `/` or `/mnt/c` with a huge tree | Scope the search path, add `-maxdepth` |
| `tree: command not found` | Not installed by default on Ubuntu | `sudo apt install tree` (see Lesson 07 before running this) |

## Knowledge Check

1. **What's the difference between `/home/<user>` and `/mnt/c` on this course's WSL setup?**
   *Answer: `/home/<user>` is a native Linux (ext4) filesystem on WSL2's own disk; `/mnt/c` is the Windows C: drive exposed through a translation layer, with emulated permissions and slower small-file access.*
2. **Where would you expect to find a service's log files?**
   *Answer: `/var/log/`.*
3. **What does `cd -` do?**
   *Answer: Returns you to the previous working directory.*

## Completion Checklist

- [ ] You can navigate to any directory using both absolute and relative paths.
- [ ] You can explain what `/etc`, `/var/log`, `/usr`, `/opt`, and `/home` are each for.
- [ ] You've confirmed, on your own machine, that `/home/<user>` and `/mnt/c` are different filesystems.

## Reference Materials

- [Ubuntu filesystem architecture](../../../ref%20roadmap/My%20mentor/BUỔI%202/BÀI%20GIẢNG/HỆ%20ĐIỀU%20HÀNH/LINUX%20OS%20-%20UBUNTU/LESSON%202%20-%20UBUNTU%20-%20Kien_truc_thu_muc_Ubuntu.docx)
- [Ubuntu basic commands](../../../ref%20roadmap/My%20mentor/BUỔI%202/BÀI%20GIẢNG/HỆ%20ĐIỀU%20HÀNH/LINUX%20OS%20-%20UBUNTU/LESSON%202%20-%20UBUNTU%20-%20Cac_lenh_can_ban_Ubuntu.docx)

## Next

Guided practice: [`exercises/02_filesystem_hierarchy/guided.md`](../exercises/02_filesystem_hierarchy/guided.md)
Independent exercise: [`exercises/02_filesystem_hierarchy/independent.md`](../exercises/02_filesystem_hierarchy/independent.md)
Next lesson: [03 — File & Directory Permissions, Ownership](03_permissions_ownership.md)
