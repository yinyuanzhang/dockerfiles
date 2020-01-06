FROM fedora:24
MAINTAINER phoracek@redhat.com

RUN \
  dnf -y install dnf-plugins-core; \
  dnf -y copr enable leifmadsen/ovs-master

RUN \
  dnf -y copr enable phoracek/ovirt-provider-ovn; \
  dnf -y install ovirt-provider-ovn

CMD \
  /usr/bin/python /usr/share/ovirt-provider-ovn/ovirt_provider_ovn.py
