# Lesson 07 — Package Management (APT) Evidence

## Lesson 07 — Package Management: Guided

**Commands used** (paste the actual commands you ran, in order):

```bash
cd ~/Projects/Learn-DE/sandbox/01_linux/workspace

sudo apt update

apt list --upgradable 2>/dev/null | head -5

sudo apt install tree

dpkg -l | grep -E '^ii[[:space:]]+tree[[:space:]]'

dpkg -L tree | head -10

tree -L 1 ~/Projects/Learn-DE

sudo apt remove tree

dpkg -l | grep -E '^[a-z]{2}[[:space:]]+tree[[:space:]]' \
  || echo "tree package is absent from dpkg -l"
```

**Relevant terminal output** (paste the actual output — not a paraphrase):

```text
Paste the actual terminal output here.

Include:
- The final output from `sudo apt update`
- The first five lines from the upgradable-package check
- The `tree` installation output, including the confirmation prompt
- The `ii` package status after installation
- The first ten lines from `dpkg -L tree`
- The output produced by the `tree` command
- The package-removal output
- The final package-status check
```

**Validation performed** (which validation command(s) you ran, and what they showed):

```text
I used `dpkg -l` after installation and confirmed that `tree` had the `ii` status, meaning that the package was installed. I used `dpkg -L tree` to inspect files installed by the package and ran `tree -L 1 ~/Projects/Learn-DE` to confirm that the command worked.

After running `sudo apt remove tree`, I checked the package status again. The package no longer had the `ii` installed status, confirming that it had been removed.
```

**Short explanation** (2–4 sentences, in your own words: what did you do and why did it work?):

I updated APT's package information and installed the `tree` command-line package. I verified the installation using `dpkg`, inspected files belonging to the package, and used `tree` to display the top level of my project directory. Finally, I removed the package and confirmed that it was no longer installed.

**Troubleshooting notes** (only if something went wrong — what broke, how you diagnosed it, how you fixed it; leave blank if nothing went wrong):

---

## Lesson 07 — Package Management: Independent

**Chosen package:** `figlet`

**Commands used** (paste the actual commands you ran, in order):

```bash
cd ~/Projects/Learn-DE/sandbox/01_linux/workspace

apt show figlet

dpkg -l | grep -E '^[a-z]{2}[[:space:]]+figlet[[:space:]]' \
  || echo "figlet is not currently listed as installed"

sudo apt install figlet

dpkg -l | grep -E '^ii[[:space:]]+figlet[[:space:]]'

dpkg -L figlet

figlet "Lesson 07"

sudo apt remove figlet

dpkg -l | grep -E '^[a-z]{2}[[:space:]]+figlet[[:space:]]' \
  || echo "figlet package is absent from dpkg -l"

sudo apt autoremove --dry-run
```

**Relevant terminal output** (paste the actual output — not a paraphrase):

```text
Paste the actual terminal output here.

Include:
- The complete relevant `apt show figlet` metadata, especially `Depends`
- The pre-install package-status check
- The installation output and confirmation prompt
- The `ii` package status after installation
- The output from `dpkg -L figlet`
- The ASCII-art output from `figlet "Lesson 07"`
- The package-removal output
- The final package-status check
- The complete relevant output from `sudo apt autoremove --dry-run`
```

**Validation performed** (which validation command(s) you ran, and what they showed):

```text
Before installing `figlet`, I ran `apt show figlet` and inspected its dependency information. After installation, I used `dpkg -l` to confirm that the package had the `ii` installed status and used `dpkg -L figlet` to inspect the files installed on disk.

I ran `figlet "Lesson 07"` and confirmed that the tool generated ASCII-art text. After removing the package, I verified that it no longer had the `ii` installed status. Finally, I ran `sudo apt autoremove --dry-run` to inspect what APT would consider safe to remove without actually removing anything.
```

**Short explanation** (2–4 sentences, in your own words: what did you do and why did it work?):

Before installing `figlet`, I inspected its package metadata and dependency information using `apt show`. I then installed it, verified its package status, inspected the files it placed on disk, and used the command once. After removing it, I checked the package status and performed an autoremove dry run so I could review any proposed cleanup without changing the system.

**Dependency conclusion:**

`figlet` depends on: **replace this text with the actual value shown on the `Depends:` line in your `apt show figlet` output.**

**Autoremove conclusion:**

**Replace this text with what your actual dry-run showed.** State whether APT proposed removing any packages and confirm that no packages were removed because the command used `--dry-run`.

**Troubleshooting notes** (only if something went wrong — what broke, how you diagnosed it, how you fixed it; leave blank if nothing went wrong):

---
