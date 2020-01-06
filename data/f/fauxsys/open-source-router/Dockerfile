FROM centos:latest
FROM centos/systemd

LABEL maintainer="Fauxsys"

ENV container docker

RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == \
systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;
VOLUME [ "/sys/fs/cgroup" ]
CMD ["/usr/sbin/init"]

RUN yum install https://repo.saltstack.com/yum/redhat/salt-repo-latest-2.el7.noarch.rpm  -y; \
yum install salt-master salt-minion -y; \
systemctl enable salt-master salt-minion; \
yum install -y iproute openssh-server; \
yum update -y; \
yum clean all;
