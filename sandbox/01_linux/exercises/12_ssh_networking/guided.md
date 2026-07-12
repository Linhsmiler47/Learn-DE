# Guided Exercise — Lesson 12: SSH & Basic Networking Commands

## Safety Reminder

This exercise is entirely client-side and safe: no local SSH server,
no `sshd_config` edits. Use a **dedicated practice key**, never your
real/existing SSH key.

## Steps

1. ```bash
   ssh-keygen -t ed25519 -f ~/.ssh/declab_practice -C "declab-practice-key"
   ls -la ~/.ssh/declab_practice*
   cat ~/.ssh/declab_practice.pub
   ssh-keygen -l -f ~/.ssh/declab_practice.pub
   ```
2. Add the **public** key (`declab_practice.pub` contents) to your GitHub
   account: Settings → SSH and GPG keys → New SSH key. (If you don't want
   to use a real GitHub account for this, substitute any SSH-based service
   you already have key-auth access to, or note in your evidence that you
   performed this step conceptually and explain what you'd expect to see.)
3. ```bash
   ssh -T -i ~/.ssh/declab_practice git@github.com
   cat ~/.ssh/known_hosts | grep github
   ```
4. Basic networking commands:
   ```bash
   ip addr show | grep inet
   ping -c 4 github.com
   curl -I https://github.com
   ss -tulpn | grep LISTEN
   dig +short github.com
   ```

## Evidence to Record

In `notes/lesson_12_evidence.md`: the key generation output (fingerprint
only — never paste the private key), the GitHub auth confirmation message,
the `known_hosts` line, and all networking command output.

## Validation

- `ssh -T ... git@github.com` should return GitHub's "successfully
  authenticated" message, not a permission error.

## When You're Done

Move to [`independent.md`](independent.md).
