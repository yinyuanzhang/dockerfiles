FROM ubuntu:16.04

ENV CONTAINER=docker
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        bash \
        python-pip \
        python3-pip \
        sudo \
        ca-certificates \
        software-properties-common \
        systemd systemd-cron sudo curl \
    && rm -rf /var/lib/apt/lists/* \
    && rm -Rf /usr/share/doc && rm -Rf /usr/share/man \
    && apt-get clean

RUN apt-add-repository ppa:ansible/ansible \
    && apt-get update \
    && apt-get upgrade -y --no-install-recommends \
    && apt-get install -y ansible \
    && rm -rf /var/lib/apt/lists/* \
    && rm -Rf /usr/share/doc && rm -Rf /usr/share/man \
    && apt-get clean \
    && touch -m -t 201701010000 /var/lib/apt/lists/

# Install Ansible inventory file.
RUN echo '[local]\nlocalhost ansible_connection=local' > /etc/ansible/hosts

VOLUME ["/sys/fs/cgroup", "/tmp", "/run"]
CMD ["/lib/systemd/systemd"]
