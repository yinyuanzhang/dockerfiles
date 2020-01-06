FROM debian

USER root

RUN apt-get update && \
    apt-get install -qq -y --no-install-recommends \
      apt-transport-https \
      ca-certificates \
      curl \
      dirmngr \
      telnet \
      netcat \
      traceroute \
      gnupg2 \
      software-properties-common \
      xz-utils


# Install kubectl, kubeadm
ENV KUBERNETES_VERSION="1.11.3"
RUN curl -L https://storage.googleapis.com/kubernetes-release/release/v${KUBERNETES_VERSION}/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl \
    && chmod +x /usr/local/bin/kubectl

RUN curl -L https://storage.googleapis.com/kubernetes-release/release/v${KUBERNETES_VERSION}/bin/linux/amd64/kubeadm -o /usr/local/bin/kubeadm \
    && chmod +x /usr/local/bin/kubeadm

# Install Helm
ENV HELM_VERSION="2.9.1"
RUN curl -L http://storage.googleapis.com/kubernetes-helm/helm-v${HELM_VERSION}-linux-amd64.tar.gz -o /tmp/helm.tar.gz \
    && tar -zxvf /tmp/helm.tar.gz -C /tmp \
    && cp /tmp/linux-amd64/helm /usr/local/bin/helm

# Install Docker
ENV DOCKER_VERSION="18.06.1"

RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    apt-key fingerprint 0EBFCD88 && \
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian stretch stable" && \
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian stretch stable" && \
    apt-get update && \
    apt-get install -qq -y --no-install-recommends docker-ce=${DOCKER_VERSION}~ce~3-0~debian

# Install the magic wrapper.
#RUN curl https://raw.githubusercontent.com/jpetazzo/dind/master/wrapdocker > /usr/local/bin/wrapdocker
#RUN chmod +x /usr/local/bin/wrapdocker

ARG DOCKER_COMPOSE_VERSION="1.21.1"
RUN curl -L https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose

# Install MongoDB
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4
RUN apt-get install -qq -y --no-install-recommends mongodb

# Cleanup
RUN apt-get clean \
    && rm -rf /tmp/* ~/*.tgz \
    && rm -rf /var/cache/apk/*

# Verify that everything has been installed
RUN kubectl version --client
RUN helm version --client
RUN docker -v
RUN docker-compose -v
RUN mongo --version

