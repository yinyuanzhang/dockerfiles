FROM fedora:29
LABEL maintainer="Ahmad Haghighi"
ENV container=docker

RUN dnf -y update && dnf clean all

# Install ansible and other requirements.
RUN dnf --refresh -y install \
    python-pip \
    python3-pip \
    #ansible \
    sudo \
    which \
    python3-dnf \
    python2-dnf \ 
    yum-plugin-ovl \
    dnf-plugin-ovl \
  && dnf clean all


# Install Ansible via pip
RUN pip2 install ansible cryptography && pip3 install dnf cryptography

# Install Ansible inventory file.
RUN mkdir -p /etc/ansible && echo -e '[local]\nlocalhost ansible_connection=local ansible_python_interpreter=python2' > /etc/ansible/hosts

# Fix ansible 
VOLUME ["/sys/fs/cgroup", "/tmp", "/run"]
CMD ["/usr/sbin/init"]
