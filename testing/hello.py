from pyinfra.operations import apt, server

apt.update()

apt.upgrade(auto_remove=True)

apt.packages(
    name="install packages like fail2ban, ufw, etc",
    packages=["fail2ban", "ufw", "curl", "wget", "git", "python3-pip", "python3-venv", "python3-dev", "build-essential", "libssl-dev", "libffi-dev", "virtualenv", "virtualenvwrapper", "libxml2-dev", "libxslt1-dev", "zlib1g-dev", "libjpeg-dev", "libcurl4-openssl-dev", "libssl-dev", "libreadline-dev", "libncurses5-dev", "libgdbm-dev", "libc6-dev", "libsqlite3-dev", "tk-dev", "libbz2-dev"],
    update=True,
    latest=True
)

server.service(
    name="enable fail2ban",
    service="fail2ban",
    enabled=True,
    running=True
)
