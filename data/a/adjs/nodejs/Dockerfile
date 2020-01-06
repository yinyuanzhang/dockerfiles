# Dockerfile for NODEJS
#
# Run Instructions - DETACHED
# docker run --name nodejs -d adjs/nodejs
#
# Run Instructions - INTERACTIVE
# docker run --name nodejs --rm -i -t adjs/nodejs /bin/bash
#
# Build Instructions
# docker build -t adjs/nodejs --rm /home/core/share/code/adjs/nodejs

# Pull from the latest Ubuntu release
FROM ubuntu:13.10

# File Author / Maintainer
MAINTAINER Scott Switzer <scott@switzer.org>

# Update apt-get
RUN apt-get update

# Upgrade packages
RUN apt-get -y upgrade

# Install build tools
RUN apt-get -y install build-essential python curl

# Set the Node version to be installed
ENV NODE_VERSION 0.10.26

# Download Node
RUN curl http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION.tar.gz  > /usr/src/node-v$NODE_VERSION.tar.gz

# Unpack the Node tarball
RUN cd /usr/src && tar xzf node-v$NODE_VERSION.tar.gz

# Configure Node source code
RUN cd /usr/src/node-v$NODE_VERSION && ./configure

# Compile the Node source code
RUN cd /usr/src/node-v$NODE_VERSION && make

# Install the Node source code
RUN cd /usr/src/node-v$NODE_VERSION && make install

# Install supervisord
RUN apt-get -y install supervisor

