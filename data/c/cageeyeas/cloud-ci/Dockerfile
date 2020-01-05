FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS base

# REPLACE SHELL
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# UPDATE
RUN apt-get update \
    && apt-get install -y curl \
    && apt-get -y autoclean

# NVM ENV
ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION 10.16.3

# INSTALL NVM
RUN curl --silent -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh | bash

# INSTALL NODE AND NMP
RUN source $NVM_DIR/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default

ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH

# UPDATE NPM
RUN npm i npm@latest -g

# CONFIRM
RUN node -v
RUN npm -v
RUN npm install -g gulp-cli
