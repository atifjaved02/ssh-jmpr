import yaml
import subprocess
import sys
import os

CONFIG_FILE = os.path.expanduser("~/.ssh/servers.yaml")

def load_config():
    """Load server configuration from a YAML file."""
    if not os.path.exists(CONFIG_FILE):
        print(f"Config file '{CONFIG_FILE}' not found. Create it at {CONFIG_FILE}.")
        sys.exit(1)
    with open(CONFIG_FILE, "r") as file:
        return yaml.safe_load(file)

def ssh_login(alias):
    """Connect to a server using its case-sensitive alias."""
    config = load_config()
    server = config.get(alias)
    if not server:
        print(f"Alias '{alias}' not found in the configuration file.")
        sys.exit(1)

    user, host = server.get("user"), server.get("host")
    if not user or not host:
        print(f"Incomplete configuration for alias '{alias}'. Ensure 'user' and 'host' are defined.")
        sys.exit(1)

    subprocess.run(["ssh", f"{user}@{host}"])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ssh <alias>")
        sys.exit(1)
    ssh_login(sys.argv[1])
