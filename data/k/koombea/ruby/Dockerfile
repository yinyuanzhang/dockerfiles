# r2.6.3-alp3.9-n10.14.1 
FROM ruby:2.6.4-alpine3.9

LABEL Author="Carlos Caro <carlos.caro@koombea.com>"

RUN ln -sf /usr/share/zoneinfo/GMT /etc/localtime

ENV NODE_VERSION="v10.14.1"


RUN apk add --update --no-cache --virtual .build-dep curl \
    make \
    python \
    g++ \
    gcc \
    gcc-doc \
    linux-headers && \
    curl -L -O https://nodejs.org/dist/$NODE_VERSION/node-$NODE_VERSION.tar.gz && \
    tar xzf node-$NODE_VERSION.tar.gz && \
    cd node-$NODE_VERSION && \
    ./configure && \
    make && \
    make install && \
    cd / && \
    rm -rf node-$NODE_VERSION* && \
    apk del .build-dep
