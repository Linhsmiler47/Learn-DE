# Lesson 07 — Package Management (APT)

**Estimated effort:** Theory ~20 min · Guided practice ~20 min · Independent practice ~15 min

## Why This Matters

Nearly every tool in this learning path — Docker, PostgreSQL, Terraform,
Airflow's system dependencies — gets onto your machine through `apt`. Knowing
how to install, inspect, update, and (carefully) remove packages is a
prerequisite for essentially every later phase.

## Learning Objectives

- Explain what a package manager does and why Ubuntu uses APT.
- Search, install, inspect, and remove packages safely.
- Understand the difference between `apt update` and `apt upgrade`.
- Know what happens on disk when a package is installed.

## WSL Context

| Aspect | Behavior in WSL2 |
|---|---|
| `apt` | Works exactly like native Ubuntu — this is one of the least WSL-affected topics in this phase. No special caveats. |

## Terminology

| Term | Definition |
|---|---|
| Package | A bundled, versioned unit of software plus its metadata (dependencies, install scripts). |
| Repository | A remote server hosting packages APT knows how to fetch from. |
| `apt` vs `dpkg` | `apt` is the high-level tool (resolves dependencies, talks to repositories); `dpkg` is the low-level tool that actually installs/removes `.deb` files. You'll use `apt` almost always. |
| Dependency | A package that another package requires in order to function. |

## Mental Model

```
apt update     -> refreshes APT's local list of "what's available" (talks to repos, no installs happen)
apt install X  -> resolves X's dependencies, downloads .deb files, hands them to dpkg to install
apt upgrade    -> installs newer versions of already-installed packages
apt remove X   -> uninstalls X, leaves its config files behind
apt purge X    -> uninstalls X AND its config files
apt autoremove -> removes packages that were installed only as dependencies and are no longer needed
```

## Theory

`apt update` does **not** install or upgrade anything — it only refreshes
APT's local index of what versions are available from your configured
repositories (listed in `/etc/apt/sources.list` and `/etc/apt/sources.list.d/`).
This is a common beginner confusion: running `apt update` and expecting
software to change. Nothing changes until you run `install` or `upgrade`.

## Command Syntax and Safety Notes

| Command | What it changes | Why elevated permission is required | Risk level | How to verify | How to undo |
|---|---|---|---|---|---|
| `apt update` | Refreshes the local package index only | Writes to `/var/lib/apt/` (system-owned) | None — no software changes | `apt list --upgradable` shows what's newer | N/A, nothing to undo |
| `apt install <pkg>` | Installs a new package and its dependencies | Writes to `/usr`, `/etc`, etc. | **Low** for a well-known small package (e.g., `tree`); read the "The following NEW packages will be installed" list before confirming | `dpkg -l <pkg>`, or just run the tool | `sudo apt remove <pkg>` |
| `apt remove <pkg>` | Uninstalls a package, keeps its config files | Same as install | **Medium** — removing a package something else depends on can break that other thing. Only remove packages *you* installed for practice. | `dpkg -l <pkg>` should show no longer installed | `sudo apt install <pkg>` again |
| `apt purge <pkg>` | Uninstalls a package AND its config files | Same as install | **Medium-High** — irreversible removal of configuration; only use on your own practice installs | `dpkg -l <pkg>` | Reinstall + reconfigure from scratch |

**Rule for this lesson**: only install/remove a small, inconsequential
package you chose specifically for practice (e.g., `tree`, `figlet`, `cowsay`)
— never remove a package you don't recognize, and never run `apt autoremove`
right after exploring, since it can remove dependencies other tools rely on
without you realizing it.

## Step-by-Step Example

```bash
$ sudo apt update
Hit:1 http://archive.ubuntu.com/ubuntu jammy InRelease
...
Reading package lists... Done

$ apt list --upgradable
(lists any installed packages with newer versions available)

$ sudo apt install tree
Reading package lists... Done
The following NEW packages will be installed:
  tree
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
...
Setting up tree (2.0.2-1) ...

$ dpkg -l | grep tree
ii  tree    2.0.2-1    amd64    displays an indented directory tree

$ tree -L 1 ~/Projects/Learn-DE
Learn-DE
├── CLAUDE.md
├── LEARNING_PATH.md
├── docs
├── ref roadmap
└── sandbox

# Clean up
$ sudo apt remove tree
```

## Guided Practice

See [`exercises/07_package_management/guided.md`](../exercises/07_package_management/guided.md).

## Common Mistakes

- Running `apt upgrade` (upgrades *everything*) when you meant to update
  one specific tool — prefer `apt install --only-upgrade <pkg>` when you
  only want one package touched.
- Piping `apt install` output through `grep` and missing the confirmation
  prompt, causing the shell to appear to "hang" (it's waiting for `y/n`).
- Removing a package without checking what depends on it first.

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| "Unable to locate package" | Package index is stale, or name is wrong | `sudo apt update` first, double-check the exact package name with `apt search <keyword>` |
| "Could not get lock /var/lib/dpkg/lock" | Another `apt`/`dpkg` process is running (or crashed mid-operation) | Wait for the other process to finish; only as a last resort research `sudo dpkg --configure -a` |
| Installed tool's command not found | Package installs a different binary name than expected | `dpkg -L <pkg>` lists every file the package installed, including the actual binary path |

## Knowledge Check

1. **What's the difference between `apt update` and `apt upgrade`?**
   *Answer: `update` refreshes the local index of available package versions; `upgrade` actually installs newer versions of already-installed packages. `update` alone changes no software.*
2. **What's the difference between `apt remove` and `apt purge`?**
   *Answer: `remove` uninstalls the package but leaves its configuration files; `purge` also deletes those config files.*
3. **How do you see exactly which files a package installed?**
   *Answer: `dpkg -L <package>`.*

## Completion Checklist

- [ ] You can explain the difference between `update`, `upgrade`, `install`, `remove`, and `purge`.
- [ ] You've installed a small practice package, verified it, used it, and removed it.
- [ ] You've located a package's installed files with `dpkg -L`.

## Reference Materials

- [How an application gets installed and executed in Ubuntu](../../../ref%20roadmap/My%20mentor/BUỔI%202/BÀI%20GIẢNG/HỆ%20ĐIỀU%20HÀNH/LINUX%20OS%20-%20UBUNTU/LESSON%202%20-%20UBUNTU%20-%20Cách%20mà%20một%20ứng%20dụng%20được%20cài%20đặt%20và%20thực%20thi%20trong%20Ubuntu.docx) — relevant context on install/execution, though not APT-specific.

## Next

Guided practice: [`exercises/07_package_management/guided.md`](../exercises/07_package_management/guided.md)
Independent exercise: [`exercises/07_package_management/independent.md`](../exercises/07_package_management/independent.md)
Next lesson: [08 — Environment Variables & Shell Configuration](08_environment_variables.md)
