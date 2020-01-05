FROM ubuntu:18.04

MAINTAINER Wang, Tao <i@miffyliye.org>

ENV USERNAME miffyliye
ENV SUDO 0

RUN apt-get update \
    && apt-get install -y openssh-server sudo \
    && mkdir -p /var/run/sshd \
    && mkdir -p /run/sshd \
    && mkdir -p /root/.ssh \
    && sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin no/' /etc/ssh/sshd_config \
    && sed -ri 's/^#?PasswordAuthentication\s+.*/PasswordAuthentication no/' /etc/ssh/sshd_config \
    && sed -ri 's/^#?PubkeyAuthentication\s+.*/PubkeyAuthentication yes/' /etc/ssh/sshd_config \
    && sed -ri 's/^#?UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD ./docker_entrypoint.sh /usr/local/bin/docker_entrypoint.sh

ENTRYPOINT [ "/bin/bash", "/usr/local/bin/docker_entrypoint.sh" ]
