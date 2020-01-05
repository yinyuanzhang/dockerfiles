# https://hub.docker.com/_/node/
FROM node:alpine

MAINTAINER Instrumentisto Team <developer@instrumentisto.com>


RUN apk add --update --no-cache \
            ca-certificates \
            git \
            openjdk8-jre-base \
            make \
 && update-ca-certificates \
 && rm -rf /var/cache/apk/*


VOLUME ["/app"]

WORKDIR /app


CMD ["node"]
