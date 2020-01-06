FROM node:alpine

WORKDIR /etc/www/

RUN apk update && apk upgrade && \
    npm i -g serve && \
    rm -rf /var/cache/apk/* && \
    yarn cache clean
