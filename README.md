# ssh-jmpr | SSH Alias Manager

A lightweight python script to manage SSH connections using YAML-based aliases to streamline server management.

## Features
- YAML configuration for case-sensitive aliases.
- Lightweight and easy to set up.
- Open-source and extensible.

## Prerequisites
- **pyyaml**: Install using `pip install pyyaml`.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/atifjaved02/ssh-jmpr.git
   cd ssh-jmpr

2. Add your server configuration to ~/.ssh/servers.yaml:
   ```bash
   server1:
      user: Admin
      host: 192.168.1.1

   server2:
      user: ubuntu
      host: 192.168.1.2

3. Run the script:
   ```bash
   python ssh-manager.py server1

4. Add an Alias : Add this to your shell configuration:
    ```bash
    alias ssh-jmpr="python3 /path/to/ssh-jmpr/ssh-manager.py"

Security:
Keep your servers.yaml file secure with:
    
    chmod 600 ~/.ssh/servers.yaml
