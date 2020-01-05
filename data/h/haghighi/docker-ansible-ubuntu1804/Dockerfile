FROM ubuntu:18.04
LABEL maintainer="Ahmad Haghighi"

ENV DEBIAN_FRONTEND noninteractive

# Install dependencies.
RUN apt update && apt upgrade -y \
    && apt install -y \
       apt-utils \
       ansible \
       python-setuptools \
       python-pip \
       python3-pip \
       software-properties-common \
       rsyslog systemd systemd-cron sudo iproute2 \
    && rm -Rf /var/lib/apt/lists/* \
    && apt clean

# Install Ansible inventory file.
RUN mkdir -p /etc/ansible
RUN echo "[local]\nlocalhost ansible_connection=local" > /etc/ansible/hosts

VOLUME ["/sys/fs/cgroup", "/tmp", "/run"]
CMD ["/lib/systemd/systemd"]
