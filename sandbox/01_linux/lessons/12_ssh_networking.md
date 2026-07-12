# Lesson 12 — SSH & Basic Networking Commands

**Estimated effort:** Theory ~40 min · Guided practice ~30 min · Independent practice ~20 min

## Why This Matters

You already use SSH-style key authentication every time you `git push` to
GitHub over SSH — this lesson makes that mechanism explicit instead of
magic. Basic networking commands are what you'll reach for constantly from
Phase 03 onward to answer "can this thing even reach that thing?"

## Read This First: Risk Framing

This lesson has two tiers, deliberately:

- **Required (safe, client-only)**: understanding SSH concepts, generating
  your own keypair, and using key-based auth against a service you already
  trust (GitHub). This carries no risk of locking yourself out of anything.
- **Optional (advanced, server-side)**: running your own local SSH server
  and touching `/etc/ssh/sshd_config`. **This is where real risk lives** —
  a wrong edit to `sshd_config` (especially around authentication methods)
  can lock out remote access to a machine. On your local WSL machine the
  blast radius is small (you always have your Windows terminal to fix
  things from), but the *habit* of being careless with `sshd_config` is
  what causes real incidents on real servers later in your career. This
  course **never requires** disabling password authentication or editing
  `sshd_config` — that section is clearly marked optional, below the
  required material, with the risk explained again right before it.

## Learning Objectives

- Explain the SSH client/server model and why key-based auth is preferred over passwords.
- Understand public/private key pairs, `known_hosts`, and `authorized_keys`.
- Generate an SSH keypair and use it for real (via GitHub) with zero server risk.
- (Optional) Understand what `sshd_config` controls and why hardening it is risky if done carelessly.
- Use basic networking commands to check connectivity and inspect network state.

## WSL Context

| Aspect | Behavior in WSL2 |
|---|---|
| SSH client (`ssh`, `ssh-keygen`) | Fully normal — installed by default (`openssh-client`), no WSL-specific behavior. |
| SSH server (`sshd`) | **Not installed by default** on this reference machine (confirmed: no `openssh-server` package, no `/etc/ssh/sshd_config`). Installing it is optional and only needed for the advanced/optional section below. |
| Starting `sshd` | Same story as cron (Lesson 11) and other services (Lesson 06): needs systemd enabled (or a manual `service ssh start`) to run at all — it will not persist across a full WSL restart unless systemd is enabled and the service is enabled within it. |
| Networking commands (`ip`, `ping`, `ss`) | Mostly work normally. WSL2 networks through a virtual switch/NAT; **inbound** connections from your Windows LAN to a service running inside WSL need extra port-forwarding configuration not covered in this beginner course — treat anything beyond localhost/outbound connectivity as conceptual only. |

## Part A — SSH Concepts (Required)

### Terminology

| Term | Definition |
|---|---|
| SSH client | The program initiating a connection (`ssh user@host`). |
| SSH server (`sshd`) | The daemon listening for and accepting incoming SSH connections. |
| Key pair | A mathematically linked public key and private key. |
| Private key | Stays on your machine, **never shared**, proves your identity. |
| Public key | Safe to share; placed on servers you want to log into. |
| `known_hosts` | A file on the **client** recording which servers you've connected to and their fingerprints — protects you from silently connecting to an impostor server. |
| `authorized_keys` | A file on the **server** listing which public keys are allowed to log in as a given user. |

### Mental Model

```
Your machine (client)                    Server you're connecting to
──────────────────────                   ───────────────────────────
~/.ssh/id_ed25519       (private, secret, never leaves this machine)
~/.ssh/id_ed25519.pub   (public) ───copy───▶  ~/.ssh/authorized_keys
~/.ssh/known_hosts      (records the server's identity after first connect)

  ssh user@server
      │
      ▼
  1. Client checks known_hosts: "have I seen this server before,
     and does its key match what I remember?"
  2. Server checks authorized_keys: "does this client have the
     private key matching one of the public keys I trust?"
  3. If both check out: connected, no password needed.
```

**This is exactly what happens** when you `git push` to GitHub over SSH —
GitHub is the "server" with your public key in *their* version of
`authorized_keys` (added via your GitHub account settings).

### Theory

The private key never travels anywhere — proof of identity works because
only someone holding the private key can correctly respond to a
cryptographic challenge tied to the matching public key. This is why
sharing a *public* key is safe (it's public by design) but sharing a
*private* key is equivalent to handing someone your identity outright.

`known_hosts` protects the *client* from connecting to an impostor
pretending to be a server you trust (a machine-in-the-middle attack) — the
first time you connect to a new host, SSH shows you its key fingerprint and
asks you to confirm; after that, if the fingerprint ever changes
unexpectedly, SSH refuses to connect and warns you loudly.

### Command Syntax and Safety Notes

| Command | What it changes | Why elevated permission is required | Risk level | How to verify | How to undo |
|---|---|---|---|---|---|
| `ssh-keygen -t ed25519 -f <path>` | Creates a new key pair at `<path>` and `<path>.pub` | No `sudo` needed — it's your own files | **Low** — creates new files, doesn't touch anything existing unless you overwrite a path in use | `ls -la ~/.ssh/`, `ssh-keygen -l -f <path>.pub` (shows fingerprint) | Delete both files if unused: `rm <path> <path>.pub` |
| `ssh -T git@github.com` | Nothing — tests auth only | No | None | Prints a greeting with your GitHub username if the key works | N/A |
| `chmod 600 ~/.ssh/id_ed25519` | Restricts the private key to owner-read/write only | No `sudo` needed | **Low**, and actually a *safety improvement* — SSH refuses to use overly-permissive private keys | `ls -l ~/.ssh/id_ed25519` should show `-rw-------` | `chmod 644` reverts it (but SSH will then refuse to use the key — don't do this) |

### Step-by-Step Example (Client-Only, Safe)

```bash
# Generate a NEW keypair specifically for this practice — don't reuse
# a real production key for learning exercises.
$ ssh-keygen -t ed25519 -f ~/.ssh/declab_practice -C "declab-practice-key"
Generating public/private ed25519 key pair.
Enter passphrase (empty for no passphrase): [press enter, or set one]
...
$ ls -la ~/.ssh/declab_practice*
-rw------- 1 linhtran linhtran  411 Jul 12 16:00 declab_practice
-rw-r--r-- 1 linhtran linhtran  103 Jul 12 16:00 declab_practice.pub

$ cat ~/.ssh/declab_practice.pub
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAI... declab-practice-key

$ ssh-keygen -l -f ~/.ssh/declab_practice.pub
256 SHA256:xxxxxxxxxxxxxxxxxxxxxx declab-practice-key (ED25519)
```

To use it for real, with zero server-management risk: add the `.pub`
contents to your GitHub account (Settings → SSH and GPG keys), then:

```bash
$ ssh -T -i ~/.ssh/declab_practice git@github.com
Hi <your-username>! You've successfully authenticated, but GitHub does not
provide shell access.

$ cat ~/.ssh/known_hosts | grep github
github.com ssh-ed25519 AAAA...
```

That last line is `known_hosts` in action — your client now remembers
GitHub's server key.

## Part A (Optional, Advanced) — Running Your Own SSH Server

**Read the risk framing at the top of this lesson again before continuing.**
This entire section is optional. Skip it if you're not specifically
curious about the server side.

Installing and running `sshd` locally lets you practice `authorized_keys`
from the server's perspective, against `localhost`, with no external
exposure:

```bash
$ sudo apt install openssh-server
$ sudo service ssh start          # or: sudo systemctl start ssh (if systemd enabled)
$ mkdir -p ~/.ssh && chmod 700 ~/.ssh
$ cat ~/.ssh/declab_practice.pub >> ~/.ssh/authorized_keys
$ chmod 600 ~/.ssh/authorized_keys

$ ssh -i ~/.ssh/declab_practice linhtran@localhost
(should log in without a password prompt)
```

**Do not** edit `/etc/ssh/sshd_config` to disable password authentication
as part of this course. If you want to explore hardening conceptually:
`PasswordAuthentication no` in `sshd_config` forces key-only login — on a
remote server, getting this wrong *before* confirming key-based login
already works is a classic way to lock yourself out permanently. If you
ever do this on a real remote machine, always keep an existing session open
and test the new config in a **second** connection before closing the
first. On this local WSL setup, treat it as a read-only "understand what
this line does" exercise, not something to actually toggle — that's the
optional challenge at the end of this lesson.

## Part B — Basic Networking Commands

### Command Syntax

| Command | Purpose | Common flags |
|---|---|---|
| `ip addr` | Show network interfaces and IP addresses | `ip a` (short form) |
| `ping <host>` | Test basic reachability | `-c 4` (send 4 packets and stop) |
| `curl <url>` | Make an HTTP request from the command line | `-I` (headers only), `-v` (verbose) |
| `ss -tulpn` | Show listening ports and the process using them | `-t` (TCP), `-u` (UDP), `-l` (listening), `-p` (process), `-n` (numeric) |
| `dig <domain>` / `nslookup <domain>` | DNS lookup | `dig +short <domain>` |

### Step-by-Step Example

```bash
$ ip addr show eth0 | grep inet
    inet 172.20.xxx.xxx/20 brd 172.20.xxx.255 scope global eth0

$ ping -c 4 github.com
PING github.com (140.82.x.x): 56 data bytes
64 bytes from 140.82.x.x: icmp_seq=0 ttl=59 time=12.3 ms
...

$ curl -I https://github.com
HTTP/2 200
...

$ ss -tulpn | grep LISTEN
(shows any locally listening services, e.g. a Docker daemon in later phases)

$ dig +short github.com
140.82.x.x
```

## Guided Practice

See [`exercises/12_ssh_networking/guided.md`](../exercises/12_ssh_networking/guided.md).

## Common Mistakes

- Generating a practice key and accidentally reusing/overwriting your real
  `~/.ssh/id_ed25519` (or `id_rsa`) — always use a distinctly named key for
  practice (e.g., `declab_practice`).
- Pasting a **private** key anywhere (chat, a file that gets committed,
  this repository) — only the `.pub` file is ever meant to be shared.
- Treating `sshd_config` edits as low-stakes because "it's just my own
  laptop" — the habit is what matters, not just this specific machine.
- Running `ping` against arbitrary external hosts as a networking "test" —
  fine for `github.com`, but don't script repeated pings at services you
  don't control.

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| `Permission denied (publickey)` connecting to GitHub | Public key not added to your GitHub account, or wrong key specified | Re-check GitHub Settings → SSH keys; specify the key explicitly with `-i` |
| `ssh-keygen` key has loose permissions warning | Private key file permissions too open | `chmod 600 <private_key_path>` |
| `sshd` (optional section) won't start | systemd not enabled, or already running | `service ssh status`; if systemd isn't enabled, this is a known WSL limitation, not a mistake you made |
| `ping` hangs with no response | Some networks/firewalls block ICMP; not necessarily a real problem | Try `curl -I <url>` instead — HTTP reachability matters more for DE work than raw ping |

## Knowledge Check

1. **Which file lives on the server and which lives on the client: `authorized_keys` or `known_hosts`?**
   *Answer: `authorized_keys` lives on the server (lists which public keys may log in); `known_hosts` lives on the client (remembers servers' identities).*
2. **Why is it safe to share your public key but never your private key?**
   *Answer: The private key is what actually proves identity cryptographically; the public key only allows verifying that proof and is useless without the matching private key.*
3. **What's the single biggest risk when editing `sshd_config` to disable password authentication?**
   *Answer: Locking yourself out of remote access if key-based auth wasn't already confirmed working — always test in a second session before closing the first.*

## Completion Checklist

- [ ] You can explain the SSH client/server model and where each key/file lives.
- [ ] You've generated a dedicated practice keypair (not reused a real one).
- [ ] You've used key-based auth for real, against GitHub, with no server risk.
- [ ] You did **not** modify `/etc/ssh/sshd_config` as a required step.
- [ ] You can run `ip addr`, `ping`, `curl -I`, and `ss -tulpn` and explain their output.

## Reference Materials

- [Ubuntu network administration commands](../../../ref%20roadmap/My%20mentor/BUỔI%202/BÀI%20GIẢNG/HỆ%20ĐIỀU%20HÀNH/LINUX%20OS%20-%20UBUNTU/LESSON%202%20-%20UBUNTU%20-%20Cac%20lenh%20ve%20quan%20trị%20mang.docx) — command reference supplement; concepts and safety framing above are authored fresh (no direct SSH-concept source in `ref roadmap/`).

## Next

Guided practice: [`exercises/12_ssh_networking/guided.md`](../exercises/12_ssh_networking/guided.md)
Independent exercise: [`exercises/12_ssh_networking/independent.md`](../exercises/12_ssh_networking/independent.md)
Next: [`../assessment/README.md`](../assessment/README.md) — the Phase 01 practical assessment.
