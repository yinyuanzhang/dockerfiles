FROM node:8.9.3-alpine

MAINTAINER product-team@saagie/com

RUN apk update && apk add git && rm -rf /var/cache/apk/* && \
    npm install -g bower && \
    echo '{ "allow_root": true }' > /root/.bowerrc
