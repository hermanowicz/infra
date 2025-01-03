from pyinfra import host
from pyinfra.operations import apt, server

apt.update(
    name="Init pull of repos after os install",
    cache_time=3600
)

apt.upgrade(
    name="os upgrade",
    auto_remove=True)

apt.packages(
    name="install packages like fail2ban, ufw, etc",
    packages=["fail2ban", "ufw", "unattended-upgrades",
              "curl", "wget", "git", "python3-pip",
              "python3-dev", "build-essential",
              "libssl-dev"],
    update=True,
    latest=True
)

server.shell(
    name="Enable UFW",
    commands=[
        "ufw default deny incoming",
        "ufw default allow outgoing",
        "ufw allow ssh",
        "ufw --force enable",
    ],
)

server.service(
    name="enable fail2ban",
    service="fail2ban",
    enabled=True,
    running=True
)