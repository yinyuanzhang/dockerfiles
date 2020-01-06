FROM node:8.12-alpine
MAINTAINER wish@baffedu.com

# RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories

RUN set x=1 && \
    apk update && \
    apk add --no-cache --virtual .tools rsync && \
    # apk del -f .build-deps && \
    npm install -g @angular/cli node-gyp && \
    rm -rf /tmp/* /var/cache/apk/*
