terraform {
  required_providers {
    hcloud = {
      source  = "hetznercloud/hcloud"
      version = "~> 1.45"
    }
  }
}

# Configure the Hetzner Cloud Provider
provider "hcloud" {}

resource "hcloud_network" "main-net" {
  name     = "main-net"
  ip_range = "10.0.0.0/16"
}

resource "hcloud_network_subnet" "network-subnet" {
  type         = "cloud"
  network_id   = hcloud_network.main-net.id
  network_zone = "eu-central"
  ip_range     = "10.0.1.0/24"
}

resource "hcloud_server" "server-1" {
  name        = "pyinfra-1"
  server_type = "cx22"
  image       = "ubuntu-24.04"
  location    = "fsn1"

  ssh_keys = [
    "hetzner_key"
  ]

  network {
    network_id = hcloud_network.main-net.id
    ip         = "10.0.1.5"
    # alias_ips = [
    #   "10.0.1.6",
    #   "10.0.1.7"
    # ]
  }

  depends_on = [
    hcloud_network_subnet.network-subnet
  ]
}

resource "hcloud_server" "server-2" {
  name        = "pyinfra-2"
  server_type = "cx22"
  image       = "ubuntu-24.04"
  location    = "fsn1"

  ssh_keys = [
    "hetzner_key"
  ]

  network {
    network_id = hcloud_network.main-net.id
    ip         = "10.0.1.6"
  }

  depends_on = [
    hcloud_network_subnet.network-subnet
  ]
}

resource "hcloud_server" "server-3" {
  name        = "pyinfra-3"
  server_type = "cx22"
  image       = "ubuntu-24.04"
  location    = "fsn1"

  ssh_keys = [
    "hetzner_key"
  ]

  network {
    network_id = hcloud_network.main-net.id
    ip         = "10.0.1.7"
  }

  depends_on = [
    hcloud_network_subnet.network-subnet
  ]
}

output "server-1-public-ip" {
  value = hcloud_server.server-1.ipv4_address
}

output "server-2-public-ip" {
  value = hcloud_server.server-2.ipv4_address
}

output "server-3-public-ip" {
  value = hcloud_server.server-3.ipv4_address
}