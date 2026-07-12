## Lesson 04 — Users, Groups & Privilege Escalation: Guided

**Commands used** (paste the actual commands you ran, in order):

```bash
cd ~/Projects/Learn-DE/sandbox/01_linux/workspace

id

sudo useradd -m declab

id declab

getent passwd declab

sudo usermod -aG users declab

groups declab

sudo userdel -r declab

id declab
```

**Relevant terminal output** (paste the actual output — not a paraphrase):

```text
id declab
userdel: declab mail spool (/var/mail/declab) not found
id: 'declab': no such user
```

**Validation performed** (which validation command(s) you ran, and what they showed):

```text
I ran `id declab` after creating the practice account and confirmed that the user existed and had its own UID, GID, and primary group. I ran `getent passwd declab` to confirm that the account had an entry in the system user database and a home directory.

After adding `declab` to the `users` group, I ran `groups declab` and confirmed that the account belonged to both the `declab` and `users` groups. Finally, after deleting the account, I ran `id declab` again and received the `no such user` message, confirming that the practice account had been removed successfully.
```

**Short explanation** (2–4 sentences, in your own words: what did you do and why did it work?):

I first used `id` to record my current user identity and group memberships. I created the dedicated `declab` practice account with a home directory, verified its account information, and added it to the `users` supplementary group using `usermod -aG`. Finally, I removed the practice account and its home directory with `userdel -r`, then verified that the account no longer existed.

**Troubleshooting notes** (only if something went wrong — what broke, how you diagnosed it, how you fixed it; leave blank if nothing went wrong):

---
