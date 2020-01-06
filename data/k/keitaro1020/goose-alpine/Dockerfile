FROM golang:1.9-alpine
MAINTAINER keitaro1020

RUN set -ex \
        && apk add --no-cache --virtual build-dependencies \
            build-base \
            git \
        && go get -ldflags "-extldflags -static" bitbucket.org/liamstask/goose/cmd/goose \
        && apk del build-dependencies \
        && apk add --no-cache mysql-client

