FROM jenkins/jenkins:alpine

USER root

ARG user=root
ARG group=root

RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/community >> /etc/apk/repositories && \
    apk -U add docker && \
    apk -U add py-pip && \
    apk -U add python-dev libffi-dev openssl-dev gcc libc-dev make && \
    pip install docker-compose

RUN rm -rf /var/lib/apt/lists/* \
    /var/cache/apk/* \
    /usr/share/man \
    /tmp/*

VOLUME /var/run/docker.sock
