FROM kalicki2k/alpine-apache-php:7.1

MAINTAINER Sebastian Kalicki (https://github.com/kalicki2k)

COPY Dockerfiles/. /

RUN apk update && apk upgrade && \
    apk add postfix && \
    chmod +x /run.sh && \
    rm -rf /var/cache/apk/*
