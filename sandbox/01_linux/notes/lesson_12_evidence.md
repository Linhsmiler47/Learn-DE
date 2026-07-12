# Lesson 12 — SSH & Basic Networking Commands Evidence

---

## Lesson 12 — Guided Exercise

### Commands used

```bash
cd ~/Projects/Learn-DE/sandbox/01_linux

mkdir -p ~/.ssh
chmod 700 ~/.ssh

ssh-keygen -t ed25519 \
  -f ~/.ssh/declab_practice \
  -C "declab-practice-key"

ls -la ~/.ssh/declab_practice*

cat ~/.ssh/declab_practice.pub

ssh-keygen -l -f ~/.ssh/declab_practice.pub
```

I copied only the contents of the following public key file:

```text
~/.ssh/declab_practice.pub
```

I added that public key to:

```text
GitHub → Settings → SSH and GPG keys → New SSH key
```

I did not copy, display, or upload the private key:

```text
~/.ssh/declab_practice
```

After adding the public key to GitHub, I ran:

```bash
ssh -T -i ~/.ssh/declab_practice git@github.com

grep github ~/.ssh/known_hosts
```

I then ran the basic networking commands:

```bash
ip addr show | grep inet

ping -c 4 github.com

curl -I https://github.com

ss -tulpn | grep LISTEN

dig +short github.com
```

If `dig` was not installed, I recorded the error and installed the appropriate DNS utility package before retrying.

---

### SSH key-generation output

```text
$ ssh-keygen -t ed25519 -f ~/.ssh/declab_practice -C "declab-practice-key"
Generating public/private ed25519 key pair.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/<username>/.ssh/declab_practice
Your public key has been saved in /home/<username>/.ssh/declab_practice.pub
The key fingerprint is:
SHA256:<PASTE-YOUR-ACTUAL-FINGERPRINT> declab-practice-key
The key's randomart image is:
+--[ED25519 256]--+
| <PASTE ACTUAL RANDOMART OR OMIT IF NOT REQUIRED> |
+----[SHA256]-----+
```

The private-key contents were not displayed or copied.

---

### Generated key files

```text
$ ls -la ~/.ssh/declab_practice*
-rw------- 1 <username> <username> ... /home/<username>/.ssh/declab_practice
-rw-r--r-- 1 <username> <username> ... /home/<username>/.ssh/declab_practice.pub
```

The private key had restrictive permissions and was readable only by my user account.

---

### Public key

The following is a public key and is safe to include in this evidence file:

```text
$ cat ~/.ssh/declab_practice.pub
ssh-ed25519 <PASTE-YOUR-ACTUAL-PUBLIC-KEY-DATA> declab-practice-key
```

I did not paste the contents of `~/.ssh/declab_practice`.

---

### Public-key fingerprint

```text
$ ssh-keygen -l -f ~/.ssh/declab_practice.pub
256 SHA256:<PASTE-YOUR-ACTUAL-FINGERPRINT> declab-practice-key (ED25519)
```

The fingerprint matched the fingerprint printed when the key pair was generated.

---

### GitHub SSH authentication

On the first connection, SSH may ask whether the GitHub host key should be trusted:

```text
$ ssh -T -i ~/.ssh/declab_practice git@github.com
The authenticity of host 'github.com (...)' can't be established.
ED25519 key fingerprint is SHA256:<HOST-FINGERPRINT>.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'github.com' (...) to the list of known hosts.
Hi <github-username>! You've successfully authenticated, but GitHub does not provide shell access.
```

Replace the block above with the actual output from the terminal.

The command may return exit code `1` even after successful GitHub authentication because GitHub does not provide an interactive shell. The important validation evidence is the message stating that authentication succeeded rather than `Permission denied (publickey)`.

I checked the exit status immediately after the command:

```bash
echo "exit code: $?"
```

```text
$ echo "exit code: $?"
<PASTE-ACTUAL-EXIT-CODE>
```

---

### Known-hosts evidence

```text
$ grep github ~/.ssh/known_hosts
<PASTE-YOUR-ACTUAL-GITHUB-KNOWN_HOSTS-LINE>
```

Depending on the SSH configuration, the hostname may be stored in hashed form. If `grep github` returned nothing, I checked the file without publishing unrelated entries:

```bash
ssh-keygen -F github.com -f ~/.ssh/known_hosts
```

```text
$ ssh-keygen -F github.com -f ~/.ssh/known_hosts
<PASTE-ACTUAL-OUTPUT>
```

This output confirmed that a host key for `github.com` had been recorded after the SSH connection.

---

### IP-address output

```text
$ ip addr show | grep inet
<PASTE-YOUR-ACTUAL-OUTPUT>
```

Example interpretation only:

```text
127.0.0.1/8 is the IPv4 loopback address.
::1/128 is the IPv6 loopback address.
The non-loopback address assigned to my active interface was:
<YOUR-ACTUAL-IP-ADDRESS>
```

---

### Ping output

```text
$ ping -c 4 github.com
<PASTE-YOUR-ACTUAL-OUTPUT>
```

The output should include the resolved destination address, packet counts, packet loss and timing statistics.

If ping failed but DNS and HTTPS worked, I documented that result rather than claiming the host was unreachable. Some networks or hosts may filter ICMP traffic even while normal HTTPS traffic remains available.

---

### HTTP-header output

```text
$ curl -I https://github.com
<PASTE-YOUR-ACTUAL-OUTPUT>
```

The response contained an HTTP status line and headers, proving that my machine could establish an HTTPS connection to GitHub.

Actual status line observed:

```text
<PASTE-ACTUAL-HTTP-STATUS-LINE>
```

---

### Listening-port output

```text
$ ss -tulpn | grep LISTEN
<PASTE-YOUR-ACTUAL-OUTPUT>
```

If the command printed no lines, I recorded:

```text
No matching listening TCP sockets were displayed for my user with this command.
```

If process names were hidden because the command was run without elevated privileges, I retained the available socket and port information. I did not use this exercise to modify or disable any services.

---

### DNS-resolution output

```text
$ dig +short github.com
<PASTE-YOUR-ACTUAL-OUTPUT>
```

The returned address or addresses showed that DNS resolution for `github.com` succeeded.

---

### Validation performed

```text
I generated a dedicated ED25519 practice key pair and confirmed that both
the private and public key files existed. I recorded only the public key
and its SHA256 fingerprint; I did not display or paste the private key.

After adding the public key to my GitHub account, I connected with the
dedicated identity file. GitHub returned its successful-authentication
message instead of a public-key permission error.

I confirmed that the GitHub host key was represented in my known_hosts
file. I also inspected my IP addresses, tested DNS resolution, sent four
ICMP echo requests, retrieved HTTPS response headers, and listed locally
listening sockets.
```

---

### Short explanation

SSH uses a key pair in which the private key remains on the client machine and the public key is registered with the remote service. During authentication, the client proves possession of the private key without transmitting the private key itself. The `known_hosts` entry is a separate security mechanism that records the remote server's host identity and helps detect unexpected host-key changes.

The networking commands tested different layers of connectivity. `ip addr` showed local interface addresses, `dig` tested DNS resolution, `ping` tested ICMP reachability, `curl -I` tested HTTPS connectivity, and `ss -tulpn` displayed sockets listening on the local machine.

---

### Troubleshooting notes

Leave this section blank if nothing went wrong.

Possible documented issues include:

```text
The first SSH connection displayed a host-authenticity prompt because
github.com was not yet present in my known_hosts file. After verifying the
prompt and accepting it, SSH recorded the host key.

The SSH test initially returned `Permission denied (publickey)`. I checked
that I had uploaded the contents of declab_practice.pub rather than the
private key, confirmed the fingerprint, and retried with the explicit
`-i ~/.ssh/declab_practice` option.

The `dig` command was initially unavailable. I recorded the command-not-found
message, installed the DNS utilities package appropriate for my system,
and then reran the command.

The `ss -tulpn` output did not display every process name because I ran it
without sudo. The listening addresses and ports were still visible, which
was sufficient for the client-side exercise.
```

---

## Lesson 12 — Independent Exercise

### Required network-profile commands

```bash
cd ~/Projects/Learn-DE/sandbox/01_linux

ip addr show

dig +short github.com
dig +short example.com

curl -I https://github.com
curl -I https://example.com

ss -tulpn
```

I optionally used the following commands to make the profile easier to read:

```bash
ip -brief addr

ip route

getent hosts github.com
getent hosts example.com
```

---

### Local IP-address evidence

```text
$ ip addr show
<PASTE-YOUR-ACTUAL-OUTPUT>
```

A shorter view, if used:

```text
$ ip -brief addr
<PASTE-YOUR-ACTUAL-OUTPUT>
```

My active non-loopback interface was:

```text
Interface: <ACTUAL-INTERFACE-NAME>
IPv4 address: <ACTUAL-IPV4-ADDRESS>
IPv6 address: <ACTUAL-IPV6-ADDRESS-OR-NOT-OBSERVED>
```

I excluded `127.0.0.1` and `::1` from the main machine-address summary because those are loopback addresses.

---

### DNS-resolution evidence

First domain:

```text
$ dig +short github.com
<PASTE-YOUR-ACTUAL-OUTPUT>
```

Second domain:

```text
$ dig +short example.com
<PASTE-YOUR-ACTUAL-OUTPUT>
```

Both commands returned at least one address, confirming that my machine could resolve two different domain names through DNS.

If one domain returned multiple addresses, I retained all addresses in the evidence.

---

### HTTP/HTTPS reachability evidence

First site:

```text
$ curl -I https://github.com
<PASTE-YOUR-ACTUAL-OUTPUT>
```

Observed HTTP status:

```text
<PASTE-ACTUAL-GITHUB-STATUS>
```

Second site:

```text
$ curl -I https://example.com
<PASTE-YOUR-ACTUAL-OUTPUT>
```

Observed HTTP status:

```text
<PASTE-ACTUAL-EXAMPLE-DOT-COM-STATUS>
```

The presence of HTTP response headers showed that DNS resolution, network routing, TCP connection establishment and TLS/HTTP communication worked for the tested destinations.

A redirect response such as `301`, `302`, `307` or `308` still demonstrates HTTP reachability. It does not have to be a `200` response.

---

### Local listening-port evidence

```text
$ ss -tulpn
<PASTE-YOUR-ACTUAL-OUTPUT>
```

Summary of listening sockets observed:

```text
Protocol: <tcp/udp>
Local address: <ADDRESS>
Port: <PORT>
Process or service: <PROCESS-NAME-IF-VISIBLE>
Exposure: <loopback-only / all-interfaces / specific-interface>
```

Repeat the summary above for each relevant listening socket.

If no listening sockets were found, record:

```text
No listening sockets were displayed by `ss -tulpn` during this test.
```

If a listener used `127.0.0.1`, `::1`, or `localhost`, I classified it as loopback-only. If it used `0.0.0.0`, `[::]`, or an external interface address, I noted that it was bound beyond the loopback interface. This describes the bind address only and does not by itself prove that the port is reachable through a firewall or router.

---

### Written network profile

My machine had the non-loopback IP address `<ACTUAL-IP-ADDRESS>` on interface `<ACTUAL-INTERFACE>`. The loopback addresses `127.0.0.1` and `::1` were also present for communication within the local machine.

DNS resolution worked for both `github.com` and `example.com`, as `dig +short` returned address records for each domain. HTTPS connectivity also worked: `curl -I` received HTTP response headers from both sites.

The `ss -tulpn` output showed `<NUMBER>` listening socket or sockets. `<DESCRIBE WHETHER THEY WERE LOOPBACK-ONLY OR BOUND TO OTHER INTERFACES, AND LIST IMPORTANT PORTS>`. Based on this client-side inspection, my machine could resolve domain names and reach external HTTPS services, while the local listening services were `<BRIEF EVIDENCE-BASED DESCRIPTION>`.

---

### Required-part validation

```text
I validated the machine's network profile with four categories of evidence:

1. `ip addr show` identified the local interfaces and IP addresses.
2. `dig +short` resolved two different domains.
3. `curl -I` returned HTTP response headers from both domains.
4. `ss -tulpn` showed the machine's locally listening sockets.

The written profile above is based directly on those command outputs.
```

---

## Optional Advanced Part — Local Key-Based SSH Login

Complete this section only if a local OpenSSH server was already installed and running. I did not install or reconfigure a server merely to fill in this section.

### Safety confirmation

```text
I did not edit /etc/ssh/sshd_config.
I did not disable password authentication.
I used only the dedicated Lesson 12 practice key.
```

### Commands used

```bash
whoami

test -f ~/.ssh/declab_practice.pub
echo "public key check exit code: $?"

mkdir -p ~/.ssh
chmod 700 ~/.ssh

touch ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys

grep -qxF "$(cat ~/.ssh/declab_practice.pub)" ~/.ssh/authorized_keys \
  || cat ~/.ssh/declab_practice.pub >> ~/.ssh/authorized_keys

ssh-keygen -l -f ~/.ssh/declab_practice.pub

ssh -i ~/.ssh/declab_practice "$(whoami)"@localhost
```

The `grep` check prevented the same practice public key from being appended repeatedly.

Inside the SSH session, I ran:

```bash
whoami
hostname
echo "$SSH_CONNECTION"
exit
```

---

### Local SSH login output

```text
$ ssh -i ~/.ssh/declab_practice <username>@localhost
The authenticity of host 'localhost (...)' can't be established.
<HOST-KEY-TYPE> key fingerprint is SHA256:<HOST-FINGERPRINT>.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'localhost' (...) to the list of known hosts.
<PASTE-ACTUAL-LOGIN-BANNER-IF-ANY>

$ whoami
<username>

$ hostname
<hostname>

$ echo "$SSH_CONNECTION"
<client-address> <client-port> <server-address> 22

$ exit
logout
Connection to localhost closed.
```

No account-password prompt appeared during the login. If the private practice key was protected with a passphrase, a private-key passphrase prompt may have appeared; that is different from the remote account asking for its login password.

---

### Optional-part validation

```text
I added only the dedicated practice public key to my user account's
authorized_keys file. I connected to localhost while explicitly selecting
the corresponding private key with `-i`.

The remote shell opened successfully, and `whoami` showed my expected
local username. The login did not request my account password, confirming
that public-key authentication completed the local client/server loop.

I did not modify /etc/ssh/sshd_config at any point.
```

---

### Optional-part troubleshooting notes

Leave blank if the optional section was not attempted or no issue occurred.

Possible example:

```text
The localhost connection initially returned "Connection refused". I
confirmed that no local SSH server was listening on port 22 and therefore
did not attempt the optional section. The required client-side networking
profile was still completed.

The server accepted a password instead of the practice key. I checked the
permissions of ~/.ssh and ~/.ssh/authorized_keys, verified that the public
key fingerprint matched the dedicated private key, and retried with
`ssh -i ~/.ssh/declab_practice`.

I did not modify sshd_config while troubleshooting.
```

---

## Final Safety Confirmation

```text
- I used a dedicated practice SSH key.
- I did not paste or submit the private key.
- I included only the public key and fingerprint where required.
- I did not modify /etc/ssh/sshd_config.
- I did not disable password authentication.
- The required exercise remained client-side.
```

---
