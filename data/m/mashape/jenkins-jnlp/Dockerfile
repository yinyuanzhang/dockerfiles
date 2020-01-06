FROM jenkinsci/jnlp-slave:3.16-1

ARG DOCKER_VERSION=17.06.2~ce-0~debian
ARG DC_VERSION=1.18.0

USER root

RUN apt-get update && \
    apt-get install -qq -y \
      curl \
      locales \
      openssh-client && \
    curl -L -O https://github.com/tmate-io/tmate/releases/download/2.2.1/tmate-2.2.1-static-linux-amd64.tar.gz && \
    tar -xzvf tmate-2.2.1-static-linux-amd64.tar.gz && \
    mv tmate-2.2.1-static-linux-amd64/tmate /usr/local/bin/tmate && \
    ssh-keygen -t rsa -N '' -f /root/.ssh/id_rsa

RUN apt-get install -qq -y --no-install-recommends \
      apt-transport-https \
      ca-certificates \
      gnupg2 \
      software-properties-common && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    apt-key fingerprint 0EBFCD88 && \
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian stretch stable" && \
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian stretch stable" && \
    apt-get update && \
    apt-get install -qq -y --no-install-recommends docker-ce=${DOCKER_VERSION} && \
    curl -L https://github.com/docker/compose/releases/download/${DC_VERSION}/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
