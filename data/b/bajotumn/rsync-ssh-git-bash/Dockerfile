FROM alpine:3.8

LABEL maintainer="docker@bajotumn.com"

RUN apk update \
 && apk upgrade \
 && apk add --no-cache \
            rsync \
            openssh-client \
            git \
            bash \
 && rm -rf /var/cache/apk/*