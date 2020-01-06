FROM node:8.14.0-alpine

LABEL maintainer="docker@bajotumn.com"

RUN apk update \
 && apk upgrade \
 && apk add --no-cache \
            rsync \
            openssh-client \
            bash \
 && rm -rf /var/cache/apk/*