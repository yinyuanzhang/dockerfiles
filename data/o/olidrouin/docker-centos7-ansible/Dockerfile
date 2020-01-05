FROM centos:7
LABEL maintainer="Oli Drouin"
ENV container=docker

ENV pip_packages "setuptools ansible yamllint ansible-lint flake8 testinfra molecule"

USER root
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

# Install requirements.
RUN yum makecache fast \
 && yum -y install deltarpm epel-release initscripts \
 && yum -y update \
 && yum -y install \
      sudo \
      which \
      openssl \
      python3-pip \
      python3-devel \
      @development \
 && yum clean all

RUN useradd -m -p "$(openssl passwd -1 ansible)" -g wheel -s /bin/bash ansible

# Install Ansible via Pip.
#RUN pip install $pip_packages

# Disable requiretty.
RUN sed -i -e 's/^\(Defaults\s*requiretty\)/#--- \1/'  /etc/sudoers

# Install Ansible inventory file.
RUN mkdir -p /etc/ansible
RUN echo -e '[local]\nlocalhost ansible_connection=local' > /etc/ansible/hosts

VOLUME ["/sys/fs/cgroup"]
CMD ["/usr/lib/systemd/systemd"]

USER ansible
WORKDIR /home/ansible

RUN pip3 install $pip_packages --user ansible

USER root

VOLUME ["/sys/fs/cgroup"]
CMD ["/usr/lib/systemd/systemd"]
