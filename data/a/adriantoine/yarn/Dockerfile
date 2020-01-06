FROM node:latest

MAINTAINER Adrien Antoine <adriantoine@gmail.com>

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb http://nightly.yarnpkg.com/debian/ nightly main" | tee /etc/apt/sources.list.d/yarn-nightly.list
RUN apt-get update && apt-get install -y yarn

WORKDIR /workspace
