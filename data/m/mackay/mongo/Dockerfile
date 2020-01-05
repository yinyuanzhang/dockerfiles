FROM mvertes/alpine-mongo:3.6.5-0
MAINTAINER Chris Garrett (https://github.com/chris-garrett/docker-mongo)
LABEL description="Mongo on Alpine + Utils 3.6.5-0"

ARG DOCKERIZE_VERSION=v0.6.1

RUN apk --no-cache add --update \
  mongodb-tools \
  && wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
  && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
  && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz
