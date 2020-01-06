FROM ubuntu:18.04

MAINTAINER Mikihito MOROSAWA

RUN apt-get update && apt-get install -y vim curl && \
    curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash

ONBUILD ARG NODE_VERSION="v8.11.4"

ONBUILD RUN	. /root/.bashrc && \
            nvm install $NODE_VERSION && \
            nvm alias default $NODE_VERSION
