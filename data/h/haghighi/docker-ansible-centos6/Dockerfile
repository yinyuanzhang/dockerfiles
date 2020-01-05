FROM centos:6
LABEL maintainer="Ahmad Haghighi"
ENV container=docker

RUN yum makecache fast && yum -y install deltarpm epel-release \
    && yum -y update && yum clean all

# Install ansible and other requirements.
RUN yum -y install \
    python-pip \
    python3-pip \
    ansible \
    sudo \
    which \
    initscripts \
    python3-dnf \
    python2-dnf \
    python34 \
  && yum clean all

# Install Ansible inventory file.
RUN mkdir -p /etc/ansible
RUN echo -e '[local]\nlocalhost ansible_connection=local ' > /etc/ansible/hosts

VOLUME ["/sys/fs/cgroup", "/tmp", "/run"]
CMD ["/sbin/init"]
