import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_pacemaker_is_installed(host):

    package = host.package("pacemaker")
    assert package.is_installed
    assert package.version.startswith("1.1")

    package = host.package("corosync")
    assert package.is_installed
    assert package.version.startswith("2.4")

    package = host.package("pcs")
    assert package.is_installed
    assert package.version.startswith("0.9")


def test_pcsd_running_and_enabled(host):

    service = host.service("pacemaker")
    assert service.is_running
    assert not service.is_enabled

    service = host.service("corosync")
    assert service.is_running
    assert not service.is_enabled

    service = host.service("pcsd")
    assert service.is_running
    assert service.is_enabled
