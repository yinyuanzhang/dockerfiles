FROM ruby:alpine

RUN gem install mina -v 1.0.7 && gem install mina-npm --pre

RUN apk update && apk add openssh-client bash

RUN apk --no-cache update && \
    apk --no-cache add curl git openssh-client bash python py-pip py-setuptools ca-certificates groff less && \
    rm -rf /var/cache/apk/*
    
# ENV SSH_AUTH_SOCK /root/ssh-agent

WORKDIR /root/workdir
