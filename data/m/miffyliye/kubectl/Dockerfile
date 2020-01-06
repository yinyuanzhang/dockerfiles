FROM ubuntu:16.04

MAINTAINER Wang, Tao <i@miffyliye.org>

ENV KUBECTL_CONFIG_DATA "Cg=="
ENV KUBECTL_COMMAND_TO_RUN "kubectl version"

RUN apt-get update \
    && apt-get install -y sudo \
    && apt-get install -y apt-transport-https ca-certificates curl \
    && curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add - \
    && echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list \
    && apt-get update \
    && apt-get install -y kubectl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD ./docker_entrypoint.sh /usr/local/bin/docker_entrypoint.sh

ENTRYPOINT [ "/bin/bash", "/usr/local/bin/docker_entrypoint.sh" ]
