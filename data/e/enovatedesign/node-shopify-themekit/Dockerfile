FROM ubuntu:16.04

MAINTAINER Enovate Design Ltd (Michael Walsh)

ENV DEBIAN_FRONTEND noninteractive

# Versions

ENV NODE_VERSION 9.x

# Base setup and install dependencies

RUN apt-get update \
    && apt-get install -y locales \
    && locale-gen en_US.UTF-8

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN apt-get update \
    && apt-get update >/dev/null \
    && apt-get install -y git zip unzip curl build-essential python make g++ libfontconfig \
    software-properties-common rsync acl zlib1g-dev apt-utils

# Install NodeJS

RUN curl -sL https://deb.nodesource.com/setup_$NODE_VERSION -o nodesource_setup.sh \
    && bash ./nodesource_setup.sh \
    && apt-get update \
    && apt-get install -y nodejs

CMD [ "node" ]

# Install PHP, Composer, PHP extensions and configure Nginx

RUN add-apt-repository -y universe \
    && apt-get update \
    && apt-get install -y \
    && apt-get remove -y --purge software-properties-common \
    && apt-get -y autoremove \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Update NPM to the latest version

RUN npm i -g npm@latest

# Install Gulp.js globally

RUN npm i -g gulp@3.9.1

# Install Shopify Themekit

RUN curl -s https://shopify.github.io/themekit/scripts/install.py | python
