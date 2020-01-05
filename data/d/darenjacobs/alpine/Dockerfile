FROM alpine:3.8
MAINTAINER Daren Jacobs <daren.jacobs@fhlbny.com>

ENV DOCKERIZE_VERSION=v0.6.1

RUN apk upgrade --update && \
    apk add \
      bash \
      tzdata \
      vim \
      tini \
      su-exec \
      gzip \
      tar \
      wget \
      curl && \
    # Network fix
    echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >> /etc/nsswitch.conf && \
    # Install dockerize
    wget -O /tmp/dockerize.tar.gz https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz && \
    tar -C /usr/local/bin -xzvf /tmp/dockerize.tar.gz && \
    # Clean up
    rm -rf /var/cache/apk/* && \
    rm -rf /tmp/* && \
    rm -rf /var/log/*

COPY bin/dockerwait.sh /usr/bin/dockerwait
