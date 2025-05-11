---
name: SSH Remote Connection
type: knowledge
version: 1.0.0
agent: CodeActAgent
triggers:
  - ssh remote
  - remote into
  - remote connection
  - connect to server
  - connect to machine
  - remote machine
  - remote server
  - remote host
---

# SSH Remote Connection Microagent

This microagent provides capabilities for establishing SSH connections to remote machines and properly exiting when finished.

## Capabilities

- Connect to remote machines using SSH
- Execute commands on remote machines
- Transfer files between local and remote machines
- Properly exit remote sessions
- Handle connection issues

## Basic SSH Connection

To connect to a remote machine:

```bash
ssh username@hostname
```

Example:
```bash
ssh admin@192.168.1.100
```

## Connection Options

- Connect to a specific port:
  ```bash
  ssh -p 2222 username@hostname
  ```

- Connect with verbose output (helpful for debugging):
  ```bash
  ssh -v username@hostname
  ```

- Connect with a specific identity file (SSH key):
  ```bash
  ssh -i ~/.ssh/my_key username@hostname
  ```

## Exiting SSH Sessions

To properly exit an SSH session:

1. Type `exit` or `logout` at the remote shell prompt
2. Press `Ctrl+D` at the remote shell prompt

Example:
```
username@remote:~$ exit
Connection to hostname closed.
```

## Handling Stuck Sessions

If a session appears to be stuck:

1. Press `Enter` to ensure you're at a prompt
2. Try `exit` or `Ctrl+D`
3. If still stuck, press `~.` (tilde followed by period) to force disconnect

Note: The `~.` escape sequence must be typed at the beginning of a line.

## Running Commands Without Staying Connected

To run a command on a remote machine without maintaining an interactive session:

```bash
ssh username@hostname "command"
```

Example:
```bash
ssh admin@192.168.1.100 "ls -la /var/log"
```

## Keeping SSH Sessions Alive

To prevent timeouts for long-running sessions:

```bash
ssh -o ServerAliveInterval=60 username@hostname
```

## SSH Config for Easier Connections

Create or edit `~/.ssh/config`:

```
Host myserver
    HostName 192.168.1.100
    User admin
    Port 22
    IdentityFile ~/.ssh/my_key
    ServerAliveInterval 60
```

Then connect simply with:
```bash
ssh myserver
```

## Troubleshooting Connection Issues

- Check if the remote server is running SSH:
  ```bash
  nc -zv hostname 22
  ```

- Debug connection issues:
  ```bash
  ssh -vvv username@hostname
  ```

- If you get "Host key verification failed":
  ```bash
  ssh-keygen -R hostname
  ```

## Security Best Practices

- Use key-based authentication instead of passwords
- Use strong, unique keys (ED25519 or RSA with at least 4096 bits)
- Protect private keys with passphrases
- Never leave SSH sessions unattended
- Always exit SSH sessions properly when finished
- Consider using SSH agent for key management