FROM node:11-alpine
MAINTAINER Juan Ramón Guerrero <juanra@glampinghub.com>

RUN apk add --no-cache \
        git python2 make g++ openssh-client py2-pip \
    && pip install awscli \
    && rm -rf /var/cache/apk/*
