FROM composer:1.8.4

# Composer uses php7-alpine:v3.8
# Set fixed node version for alpine 3.8, see https://pkgs.alpinelinux.org/packages?name=nodejs&branch=v3.8 for latest version
ENV NODEJS_VERSION 8.14.0-r0

# Install base dependencies
RUN apk add --update \
        nodejs=${NODEJS_VERSION} \
        nodejs-npm=${NODEJS_VERSION} \
        rsync \
        libpng-dev \
        autoconf \
        automake \
        g++ \
        nasm \
    && docker-php-ext-install \
        sockets \
        gd

# Create dirs and users
RUN mkdir -p /opt/atlassian/pipelines/agent/build

WORKDIR /opt/atlassian/pipelines/agent/build
ENTRYPOINT /bin/bash