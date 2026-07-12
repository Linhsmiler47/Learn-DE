# Independent Exercise — Lesson 12: SSH & Basic Networking Commands

## Goal

Document your own machine's networking posture and (optionally) complete
the safe, local, key-based server login loop.

## Task — Required Part

Using the networking commands from the lesson, produce a short written
profile of your own machine's network setup: its IP address, whether it
can resolve DNS for at least two different domains, whether it can reach
those domains over HTTP, and what (if anything) is listening on local
ports. You choose which domains and which commands to combine.

## Task — Optional Advanced Part

If you completed the optional server-side section in Lesson 12
(`openssh-server` installed locally), demonstrate a full local key-based
login loop: add your practice public key to `~/.ssh/authorized_keys`, then
`ssh -i ~/.ssh/declab_practice <you>@localhost` and confirm no password was
requested. **Do not** modify `/etc/ssh/sshd_config` as part of this —
if you want to explore a hardening setting conceptually, write about what
it would do instead of applying it.

## Constraints

- Do not paste any private key contents into your evidence — fingerprints
  and public key contents only.
- Do not edit `/etc/ssh/sshd_config`.

## Expected Behavior

A clear, evidence-backed written profile of your network setup, and
(optionally) proof of a working local key-based SSH login loop.

## Validation Commands

- `ip addr`, `dig +short <domain>`, `curl -I <url>`, `ss -tulpn` (required part)
- `ssh -i ~/.ssh/declab_practice <you>@localhost` (optional part only)

## Evidence to Submit

In `notes/lesson_12_evidence.md`: all command output for the required
network profile, your written summary, and (if attempted) the optional
part's login proof — with an explicit note confirming `sshd_config` was
not modified.

## Do Not

- Do not modify `/etc/ssh/sshd_config`.
- Do not disable password authentication.
- Do not paste a private key anywhere in your evidence.
