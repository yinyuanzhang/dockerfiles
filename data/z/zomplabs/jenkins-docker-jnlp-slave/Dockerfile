FROM jenkinsci/jnlp-slave
MAINTAINER Zane Cahill <zcahill@zomplabs.com>

ENV DOCKER_BUCKET get.docker.com
ENV DOCKER_VERSION 1.9.1
ENV DOCKER_SHA256 52286a92999f003e1129422e78be3e1049f963be1888afc3c9a99d5a9af04666
ENV DOCKER_HOME /usr/bin/docker
ENV DOCKER_HOST unix:///var/run/docker.sock
# GID currently in use by AWS EC2 Container Service
ENV DOCKER_GID 497

USER root

RUN curl -fSL "https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-$DOCKER_VERSION" -o ${DOCKER_HOME} \
    && echo "${DOCKER_SHA256} ${DOCKER_HOME}" | sha256sum -c - \
    && chmod +x ${DOCKER_HOME}

RUN groupadd -g ${DOCKER_GID} docker
RUN usermod -G docker jenkins

USER jenkins
