FROM ubuntu:trusty
MAINTAINER Karl Jahn <kajahno@gmail.com>

# Prevent dpkg errors
ENV TERM=xterm-256color

# Set mirrors to UK
RUN sed -i "s/http:\/\/archive./http:\/\/uk.archive./g" /etc/apt/sources.list

# Install nodejs
RUN apt-get update && \
    apt-get install -qy curl  && \
    curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash - && \
    apt-get install -y nodejs

COPY . /app
WORKDIR /app

# Install application dependencies
RUN npm install -g mocha && \
    npm install 

# Set mocha as test running entrypoing
ENTRYPOINT mocha --reporter mocha-jenkins-reporter -- tests/*.js
