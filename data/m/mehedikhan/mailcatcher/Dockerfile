FROM alpine:3.7

MAINTAINER Mehedi Khan <mehedi.xpres@gmail.com>

RUN apk add --no-cache ca-certificates openssl

RUN apk add --no-cache ruby ruby-bigdecimal ruby-json sqlite-libs libstdc++

ARG MAILCATCHER_VERSION=0.6.5

RUN apk add --no-cache --virtual .build-deps \
        ruby-dev \
        make g++ \
        sqlite-dev \
        && \
    gem install -v $MAILCATCHER_VERSION mailcatcher --no-ri --no-rdoc && \
    apk del .build-deps

#smtp port 1025 | http port 1080
EXPOSE 1080 1025

CMD ["mailcatcher", "--no-quit", "--foreground", "--ip=0.0.0.0"]