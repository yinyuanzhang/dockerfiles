FROM ubuntu:18.04

MAINTAINER Wang, Tao <i@miffyliye.org>

ENV SSH_PRIVATE_KEY_DATA "Cg=="

RUN apt-get update \
    && apt-get install -y openssh-client sshpass \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD ./docker_entrypoint.sh /usr/local/bin/docker_entrypoint.sh

ENTRYPOINT [ "/bin/bash", "/usr/local/bin/docker_entrypoint.sh" ]
