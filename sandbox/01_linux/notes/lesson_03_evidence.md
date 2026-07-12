## Lesson 03 — File & Directory Permissions, Ownership: Independent

**Commands used** (paste the actual commands you ran, in order):

```bash
pwd

mkdir -p permissions_practice/scenario

touch permissions_practice/scenario/private_notes.txt
touch permissions_practice/scenario/team_readme.txt
touch permissions_practice/scenario/public_info.txt

chmod 600 permissions_practice/scenario/private_notes.txt
chmod 640 permissions_practice/scenario/team_readme.txt
chmod 644 permissions_practice/scenario/public_info.txt

ls -l permissions_practice/scenario/

stat -c "%a %n" permissions_practice/scenario/*
```

**Relevant terminal output** (paste the actual output — not a paraphrase):

```text

linhtran@DESKTOP-FSMTJKA:~/Projects/Learn-DE$ cd ~/Projects/Learn-DE/sandbox/01_linux/workspace/
linhtran@DESKTOP-FSMTJKA:~/Projects/Learn-DE/sandbox/01_linux/workspace$ mkdir -p permissions_practice/scenario

touch permissions_practice/scenario/private_notes.txt
touch permissions_practice/scenario/team_readme.txt
touch permissions_practice/scenario/public_info.txt
linhtran@DESKTOP-FSMTJKA:~/Projects/Learn-DE/sandbox/01_linux/workspace$ chmod 600 permissions_practice/scenario/private_notes.txt

chmod 640 permissions_practice/scenario/team_readme.txt

chmod 644 permissions_practice/scenario/public_info.txt
linhtran@DESKTOP-FSMTJKA:~/Projects/Learn-DE/sandbox/01_linux/workspace$ ls -l permissions_practice/scenario/
total 0
-rw------- 1 linhtran linhtran 0 Jul 12 17:03 private_notes.txt
-rw-r--r-- 1 linhtran linhtran 0 Jul 12 17:03 public_info.txt
-rw-r----- 1 linhtran linhtran 0 Jul 12 17:03 team_readme.txt
linhtran@DESKTOP-FSMTJKA:~/Projects/Learn-DE/sandbox/01_linux/workspace$ stat -c "%a %n" permissions_practice/scenario/*
600 permissions_practice/scenario/private_notes.txt
644 permissions_practice/scenario/public_info.txt
640 permissions_practice/scenario/team_readme.txt
```

**Validation performed** (which validation command(s) you ran, and what they showed):

```text
I ran `ls -l permissions_practice/scenario/` to verify the symbolic permission strings for all three files. The output showed that `private_notes.txt` had `-rw-------`, `team_readme.txt` had `-rw-r-----`, and `public_info.txt` had `-rw-r--r--`.

I also ran `stat -c "%a %n" permissions_practice/scenario/*` to verify the octal permission modes. It confirmed that the files had modes `600`, `640`, and `644`.
```

**Short explanation** (2–4 sentences, in your own words: what did you do and why did it work?):

I created three text files inside `permissions_practice/scenario/` and assigned permissions based on the required access for the owner, group, and others. I used mode `600` for the private file, `640` for the team-readable file, and `644` for the publicly readable file. I did not add execute permission because these are regular text files.

**One-sentence justification per file:**

* `private_notes.txt`: Mode `600` gives the owner read and write permissions while giving no permissions to the group or others.
* `team_readme.txt`: Mode `640` gives the owner read and write permissions, gives the group read permission, and gives no permissions to others.
* `public_info.txt`: Mode `644` gives the owner read and write permissions while allowing both the group and others to read the file.

**Troubleshooting notes** (only if something went wrong — what broke, how you diagnosed it, how you fixed it; leave blank if nothing went wrong):

---
