FROM ubuntu:16.04

LABEL maintainer="me@lehungio.com"

#  run sudo in docker ubuntu 16.04
# https://github.com/tianon/docker-brew-ubuntu-core/issues/48#issuecomment-215522746
RUN apt-get update && apt-get install -y sudo && rm -rf /var/lib/apt/lists/*

WORKDIR /code/frontend
USER root

# init
RUN apt-get update \
    && apt-get install -y git wget curl vim iputils-ping mysql-client make g++

# locale language pack
RUN apt-get install -y language-pack-ja-base

# node & npm
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
RUN apt-get install -y git nodejs
RUN npm install --quiet --production --no-progress --registry=${registry:-https://registry.npmjs.org} \
    && npm cache clean --force

# update package
RUN apt-get update
RUN npm update npm -g

# Install PM2
RUN npm install -g pm2

EXPOSE 8080
EXPOSE 38080

# get started
RUN npm install
RUN npm --version
CMD pm2 start --no-daemon npm -- start
