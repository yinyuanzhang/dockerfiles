# Image to install NVM and AWS CLI for use with CI

# set the base image to Debian
FROM debian:latest

# nvm environment variables
ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION 8.11.0
ENV NVM_VERSION v0.33.11


# update the repository sources list + install dependencies
RUN apt-get update \
    && apt-get install -y curl python-dev git zip \
    && apt-get -y autoclean

# replace shell with bash so we can source files
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# install nvm
RUN mkdir $NVM_DIR
# https://github.com/creationix/nvm#install-script
RUN curl --silent -o- https://raw.githubusercontent.com/creationix/nvm/$NVM_VERSION/install.sh | bash

# install node and npm
RUN source $NVM_DIR/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default

# add node and npm to path so the commands are available
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH

#install PIP
RUN curl -O https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
RUN rm get-pip.py 

#install AWS CLI
RUN pip install awscli


# verify installation
RUN python -V
RUN pip -V
RUN node -v
RUN npm -v