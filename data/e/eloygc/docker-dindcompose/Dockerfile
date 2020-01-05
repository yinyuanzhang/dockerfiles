FROM docker:latest

LABEL maintainer "Eloy Gómez <sr.eloy@gmail.com>"

ARG compose_version=1.14.0-rc1
ARG glibc_version=2.25-r0

RUN apk update && apk add --no-cache curl openssl ca-certificates \
    && apk add gettext \
    && apk add bash git openssh \
    && curl -L https://github.com/docker/compose/releases/download/${compose_version}/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose \
    && wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub \
    && wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${glibc_version}/glibc-${glibc_version}.apk \
    && apk add --no-cache glibc-${glibc_version}.apk && rm glibc-${glibc_version}.apk \
    && ln -s /lib/libz.so.1 /usr/glibc-compat/lib/ \
    && ln -s /lib/libc.musl-x86_64.so.1 /usr/glibc-compat/lib \
    && rm -rf /var/cache/apk/*
