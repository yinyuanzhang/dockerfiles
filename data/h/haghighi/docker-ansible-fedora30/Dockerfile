FROM fedora:30
LABEL maintainer="Ahmad Haghighi"
ENV container=docker

RUN dnf -y update && dnf clean all

# Install ansible and other requirements.
RUN dnf --refresh -y install \
    python-pip \
    ansible \
    sudo \
    which \
    python3-dnf \
  && dnf clean all

# Install Ansible inventory file.
RUN mkdir -p /etc/ansible
RUN echo -e '[local]\nlocalhost ansible_connection=local ansible_python_interpreter=python3' > /etc/ansible/hosts

VOLUME ["/sys/fs/cgroup", "/tmp", "/run"]
CMD ["/usr/sbin/init"]
