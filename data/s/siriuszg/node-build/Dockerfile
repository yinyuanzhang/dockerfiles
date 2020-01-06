FROM node:12.12.0-alpine

LABEL maintainer="zhigang52110@sina.com"

RUN apk update && apk upgrade && \
    apk add --no-cache git openssh

RUN mkdir -p /usr/local/node && mkdir -p /etc/node-cache

RUN npm config set cache "/etc/node-cache"

# RUN npm install -g yarn

COPY ./exec.sh /usr/local/node

RUN chmod +x /usr/local/node/exec.sh

WORKDIR /usr/src/app

ENTRYPOINT ["/bin/sh","/usr/local/node/exec.sh"]