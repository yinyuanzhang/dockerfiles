FROM ruby:2.5.1-alpine

WORKDIR /tmp
RUN apk add --update --no-cache curl && \
    curl -O "http://dl-4.alpinelinux.org/alpine/edge/community/x86_64/imagemagick6-{6.9.9.51-r0,c%2B%2B-6.9.9.51-r0,dev-6.9.9.51-r0,doc-6.9.9.51-r0,libs-6.9.9.51-r0}.apk" && \
    apk add --no-cache \
    imagemagick6-c%2B%2B-6.9.9.51-r0.apk \
    imagemagick6-dev-6.9.9.51-r0.apk \
    imagemagick6-libs-6.9.9.51-r0.apk \
    imagemagick6-6.9.9.51-r0.apk

RUN apk update && \
    apk add \
    mysql-client mysql-dev \
    nodejs \
    git less \
    tzdata \
    build-base \
    libxml2 libxml2-dev \
    libxslt libxslt-dev && \
    rm -fr /var/cache/apk/*

RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
