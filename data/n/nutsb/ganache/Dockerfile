# Name:ganache
FROM node:10.8-stretch

MAINTAINER "nutsbest@protonmail.com"

ENV DEBIAN_FRONTEND noninteractive

RUN npm install -g truffle && \
    npm install -g ganache-cli

EXPOSE 7545 8080 9545
