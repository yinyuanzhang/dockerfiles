FROM ubuntu:16.04

MAINTAINER Purelabio

##
#  Dependencies
##

RUN echo "Purelabio — build container for Drone started"

RUN apt-get update                                        && \
  apt-get install -y curl git postgresql-client docker.io && \
  rm -rf /var/lib/apt/lists/*

## Install docker-machine
RUN base=https://github.com/docker/machine/releases/download/v0.14.0            \
  && curl -L $base/docker-machine-$(uname -s)-$(uname -m) > /tmp/docker-machine \
  && install /tmp/docker-machine /usr/local/bin/docker-machine

## Install docker-compose
RUN base=https://github.com/docker/compose/releases/download/1.21.0             \
  && curl -L $base/docker-compose-$(uname -s)-$(uname -m) > /tmp/docker-compose \
  && install /tmp/docker-compose /usr/local/bin/docker-compose
