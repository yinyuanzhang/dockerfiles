# Based on https://github.com/jonaskello/docker-and-compose
# includes docker-compose and additionally git, rsync and openssh-client
# Docker image that can be used for dind and as such as base image to build docker containers

FROM docker:1.12.3

MAINTAINER Felix Zumstein <felix.zumstein@zoomeranalytics.com>

ARG compose_version=1.8.1

# Install docker-compose (extra complicated since the base image uses alpine as base)
RUN apk update && apk add --no-cache \
    curl openssl ca-certificates rsync openssh-client git\
    && curl -L https://github.com/docker/compose/releases/download/${compose_version}/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose \
    && wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub \
    && wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.23-r3/glibc-2.23-r3.apk \
    && apk add --no-cache glibc-2.23-r3.apk && rm glibc-2.23-r3.apk \
    && ln -s /lib/libz.so.1 /usr/glibc-compat/lib/ \
    && ln -s /lib/libc.musl-x86_64.so.1 /usr/glibc-compat/lib \

