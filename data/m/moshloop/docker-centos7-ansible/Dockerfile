FROM centos:7
LABEL maintainer="Moshe Immerman"
ENV container=docker
ARG ANSIBLE_VERSION=2.6.1
ARG SYSTOOLS_VERSION=3.0
# Install systemd -- See https://hub.docker.com/_/centos/
RUN yum -y update; yum clean all; \
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;

# Install Ansible and other requirements.
RUN yum makecache fast \
 && yum -y install deltarpm epel-release initscripts \
 && yum -y update \
 && yum -y install \
      which sudo redhat-lsb-core psmisc psutils \
      unzip zip tar gzip bzip2 \
      openssl sshpass openssh-clients krb5-libs krb5-devel \
      nano jq expect tree dos2unix xmlstarlet bash \
      wget curl net-tools git nmap-ncat \
      gcc gcc-c++ python-pip python-devel ruby ruby-devel \
      bats genisoimage dnsutils sudo \
 && yum clean all

RUN pip install --upgrade pip && pip install --upgrade setuptools && pip install ansible==$ANSIBLE_VERSION ansible-dependencies
RUN rpm -i https://packages.chef.io/files/stable/inspec/2.2.16/el/7/inspec-2.2.16-1.el7.x86_64.rpm && \
    rpm -i https://github.com/moshloop/systools/releases/download/${SYSTOOLS_VERSION}/systools-${SYSTOOLS_VERSION}-1.x86_64.rpm
RUN install_bin https://github.com/moshloop/waiter/releases/download/1.1/waiter \
    https://master.dockerproject.org/linux/x86_64/docker

RUN sed -i -e 's/^\(Defaults\s*requiretty\)/#--- \1/'  /etc/sudoers
RUN mkdir -p /etc/ansible
RUN echo -e '[local]\nlocalhost ansible_connection=local' > /etc/ansible/hosts

VOLUME ["/sys/fs/cgroup"]
CMD ["/usr/sbin/init"]
