FROM ubuntu:16.04
MAINTAINER Shining Yao <ysnlvlqw@msn.com>
ENV REFRESHED_AT 2017-07-01
RUN apt-get -yqq update
RUN apt-get -yqq install nodejs npm git
RUN ln -s /usr/bin/nodejs /usr/bin/node
RUN mkdir -p /workspace
WORKDIR /workspace

COPY package.json /workspace
RUN npm install

ADD . /workspace
RUN npm run build

EXPOSE 8080

