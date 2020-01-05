FROM fedora:24
MAINTAINER phoracek@redhat.com

ENV OVS_LOGDIR=/var/ovs
ENV OVS_RUNDIR=/var/ovs
ENV OVS_DBDIR=/var/ovs

RUN \
  dnf -y install dnf-plugins-core; \
  dnf -y copr enable leifmadsen/ovs-master

RUN \
  dnf -y install openvswitch-ovn-central hostname

CMD \
  mkdir /var/ovs; \
  /usr/share/openvswitch/scripts/ovs-ctl \
    --system-id=random \
	start; \
  /usr/share/openvswitch/scripts/ovn-ctl \
	start_northd; \
  tail -f /var/ovs/ovn-northd.log
