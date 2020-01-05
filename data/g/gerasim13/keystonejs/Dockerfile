FROM gerasim13/nodejs
MAINTAINER Pavel Litvinenko <gerasim13@gmail.com>
RUN apk --update add python nodejs-dev gcc make build-base
RUN apk --update --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted add py-kerberos && \
    rm -rf /var/cache/apk/* && \
    rm -rf /tmp/*
ENV NODE_PATH /usr/lib/node_modules
RUN npm install -g underscore
RUN npm install -g keystone
RUN npm install -g keystone-rest
RUN apk del gcc make build-base nodejs-dev && \
    rm -rf /var/cache/apk/* && \
    rm -rf /tmp/*
