# Lesson 03 — File & Directory Permissions, Ownership

**Estimated effort:** Theory ~35 min · Guided practice ~30 min · Independent practice ~25 min

## Why This Matters

Nearly every "permission denied" error you'll hit from Docker volumes
(Phase 05) to Airflow log directories (Phase 17) to SSH keys (Lesson 12)
traces back to this lesson. Understanding permissions precisely — not just
"chmod 777 it and move on" — is what separates debugging in five minutes
from debugging for an hour.

## Learning Objectives

- Read and interpret `ls -l` permission strings.
- Understand the owner/group/other model and read/write/execute bits.
- Safely change permissions and ownership using a dedicated practice directory.
- Know why `chmod`/`chown` behave unreliably on `/mnt/c`.

## WSL Context

| Aspect | Behavior in WSL2 |
|---|---|
| `chmod`/`chown` on `/home/<user>` | Fully normal — real Linux permission enforcement. |
| `chmod`/`chown` on `/mnt/c` | **Unreliable.** `drvfs` emulates a fixed permission model; `chmod` may appear to succeed but not actually restrict access the way it would on ext4. **Do all permission exercises under `/home/<user>` (this course's `workspace/`).** |

## Terminology

| Term | Definition |
|---|---|
| Owner | The user who owns the file (usually whoever created it). |
| Group | A named set of users; a file has exactly one owning group. |
| Other | Everyone else (not owner, not in the owning group). |
| Mode | The permission bits, expressible as symbols (`rwx`) or octal digits (`755`). |
| `r`, `w`, `x` | Read, write, execute. On a directory, `x` means "can enter/traverse it," not "can execute it." |
| umask | A mask that determines the *default* permissions of newly created files. |

## Mental Model

```
-rwxr-xr--  1 linhtran linhtran   220 Jul 12 10:00 deploy.sh
│└┬┘└┬┘└┬┘
│ │  │  └─ other: r-- (read only)
│ │  └──── group: r-x (read + execute)
│ └─────── owner: rwx (read + write + execute)
└───────── file type: - (regular file), d (directory), l (symlink)
```

Octal shorthand: r=4, w=2, x=1, summed per group.
`rwx r-x r--` = `7 5 4` = `chmod 754`.

## Theory

Permissions are checked **in order: owner, then group, then other** — the
first matching category wins. If you own a file but it's `chmod 077`
(nothing for owner, full for group/other), *you* are locked out and only
other users can access it. This surprises people constantly — permissions
are not additive across categories.

For directories, the three bits mean something slightly different:
- `r` on a directory: can list its contents (`ls`).
- `w` on a directory: can create/delete files inside it.
- `x` on a directory: can `cd` into it or access files inside by exact path,
  even without `r`.

## Command Syntax and Safety Notes

| Command | What it changes | Why elevated permission is required | Risk level | How to verify | How to undo |
|---|---|---|---|---|---|
| `chmod <mode> <file>` | The read/write/execute bits on a file/directory | **No `sudo` needed if you own the file.** `sudo` only required to change a file you don't own. | **Low**, if scoped to your own practice files. **High** if run on system paths (`/etc`, `/usr`) — never do that here. | `ls -l <file>` before and after | Re-run `chmod` with the original mode (write it down before changing anything!) |
| `chown <user>:<group> <file>` | The owner and/or group of a file | Yes, `sudo` required to change ownership to another user | **Low** on your own practice files; **do not** run on system files | `ls -l <file>` before and after | `sudo chown <original_user>:<original_group> <file>` |

**Rule for this entire course**: only ever run `chmod`/`chown` inside
`sandbox/01_linux/workspace/` (or another dedicated practice directory).
Never target `/etc`, `/usr`, `/var`, or any path you didn't create yourself.

## Step-by-Step Example

All of this happens inside your practice workspace — see
[Environment Setup](../workspace/README.md) if you haven't created it yet.

```bash
$ cd ~/Projects/Learn-DE/sandbox/01_linux/workspace
$ mkdir -p permissions_practice && cd permissions_practice
$ echo "hello" > notes.txt
$ ls -l notes.txt
-rw-r--r-- 1 linhtran linhtran 6 Jul 12 10:00 notes.txt

$ chmod 600 notes.txt      # owner: read/write only, nobody else can read
$ ls -l notes.txt
-rw------- 1 linhtran linhtran 6 Jul 12 10:00 notes.txt

$ chmod u+x notes.txt      # add execute for owner (symbolic form)
$ ls -l notes.txt
-rwx------ 1 linhtran linhtran 6 Jul 12 10:00 notes.txt

$ chmod 644 notes.txt      # back to a normal, safe default
$ ls -l notes.txt
-rw-r--r-- 1 linhtran linhtran 6 Jul 12 10:00 notes.txt
```

## Guided Practice

See [`exercises/03_permissions_ownership/guided.md`](../exercises/03_permissions_ownership/guided.md).

## Common Mistakes

- `chmod 777` as a reflex "fix" for permission errors — it works by removing
  all protection, which defeats the point and is a real security smell even
  in a learning environment.
- Forgetting that `x` on a *directory* means "traversable," not "executable,"
  and being confused why a directory needs `+x` to be `cd`-able.
- Running `chmod`/`chown` recursively (`-R`) without first checking what's
  inside the directory — it's easy to affect files you didn't mean to touch.

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| "Permission denied" opening your own file | Owner bits don't include the needed permission | `ls -l` to check, then `chmod` to add the specific bit needed (avoid `777`) |
| `chmod` "succeeds" but access still behaves oddly | You're on `/mnt/c`, where bits are emulated | Move the file to `/home/<user>` (your `workspace/`) and repeat |
| `chown` fails with "Operation not permitted" | Trying to change ownership without `sudo` | Only use `sudo chown` on files you understand and own the *effect* of changing — never on system paths |

## Knowledge Check

1. **What does `chmod 640 file` set?**
   *Answer: Owner: read+write (6), group: read (4), other: nothing (0).*
2. **Why might `chmod` appear to "not work" on a file under `/mnt/c`?**
   *Answer: `/mnt/c` uses drvfs, which emulates Linux permission bits over Windows NTFS rather than enforcing them natively.*
3. **Do you need `sudo` to `chmod` a file you own?**
   *Answer: No — `sudo` is only needed to change permissions/ownership on files you don't own.*

## Completion Checklist

- [ ] You can read any `ls -l` permission string correctly.
- [ ] You've changed a file's permissions using both octal and symbolic notation, and verified the change with `ls -l`.
- [ ] You've practiced only inside `workspace/`, never on a system path.
- [ ] You can explain, in your own words, why `/mnt/c` permission changes are unreliable.

## Reference Materials

- [Ubuntu basic commands](../../../ref%20roadmap/My%20mentor/BUỔI%202/BÀI%20GIẢNG/HỆ%20ĐIỀU%20HÀNH/LINUX%20OS%20-%20UBUNTU/LESSON%202%20-%20UBUNTU%20-%20Cac_lenh_can_ban_Ubuntu.docx) (touches permissions briefly)
- No dedicated permissions lesson exists in `ref roadmap/` — most of this lesson is authored fresh.

## Next

Guided practice: [`exercises/03_permissions_ownership/guided.md`](../exercises/03_permissions_ownership/guided.md)
Independent exercise: [`exercises/03_permissions_ownership/independent.md`](../exercises/03_permissions_ownership/independent.md)
Next lesson: [04 — Users, Groups & Privilege Escalation](04_users_groups_sudo.md)
