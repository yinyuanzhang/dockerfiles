FROM ubuntu:16.04

MAINTAINER pykiss

LABEL version="2.1"

RUN apt-get update -yqq
RUN apt-get install curl -yqq
RUN apt-get install nodejs -yqq
RUN apt-get install npm -yqq
RUN apt-get install sudo -yqq
RUN ln /usr/bin/nodejs /usr/bin/node

VOLUME /src
WORKDIR /src

env NODE_ENV production
env NPM_SCRIPT start
env HOME /src
cmd /root/start.sh


ADD start.sh /root/start.sh
RUN chmod +x /root/start.sh
