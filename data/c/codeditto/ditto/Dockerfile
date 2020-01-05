# Dockerfile for developing Ditto.
FROM ubuntu:18.04
MAINTAINER Jack Anthony <jack@codeditto.io>

# Set up.
RUN rm /bin/sh && ln -s /bin/bash /bin/sh # replace shell with bash
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get -y upgrade
ARG NVM_VERSION=v0.33.8
ARG HUGO_VERSION=0.42.2
ARG NODE_VERSION=v6.11.5
ARG NVM_DIR=/usr/local/nvm

# Install Node.js.
RUN apt-get install -y build-essential libssl-dev curl && apt-get clean
RUN curl -sL https://raw.githubusercontent.com/creationix/nvm/$NVM_VERSION/install.sh -o install_nvm.sh \
    && bash install_nvm.sh \
    && rm install_nvm.sh

RUN . $NVM_DIR/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default

# Install cloud tools.
RUN apt-get install -y lsb-release && apt-get clean
RUN export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \
    echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    apt-get update -y && apt-get install google-cloud-sdk -y
RUN . $NVM_DIR/nvm.sh \
    && npm install -g @google-cloud/functions-emulator \
    && npm install -g @google-cloud/datastore

# Install web tools.
RUN apt-get install -y wget && apt-get clean
RUN wget https://github.com/gohugoio/hugo/releases/download/v0.42.2/hugo_${HUGO_VERSION}_Linux-64bit.deb \
    && dpkg -i hugo_${HUGO_VERSION}_Linux-64bit.deb \
    && rm hugo_${HUGO_VERSION}_Linux-64bit.deb
RUN . $NVM_DIR/nvm.sh \
    && npm install -g firebase-tools
