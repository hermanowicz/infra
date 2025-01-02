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
    packages=["fail2ban", "ufw", "curl", "wget", "git", "python3-pip", "python3-venv", "python3-dev", "build-essential",
              "libssl-dev",
              "golang", "docker.io"],
    update=True,
    latest=True
)

server.shell(
    name="printing to tty hello,world",
    commands=["echo 'hello, world'"]
)

server.service(
    name="enable fail2ban",
    service="fail2ban",
    enabled=True,
    running=True
)

server.service(
    name="enabling docker",
    service="docker",
    enabled=True,
    running=True
)
