FROM node:6-slim

LABEL maintainer="jason@ciandt.com"

RUN apt-get update \
  && apt-get install -y --no-install-recommends python build-essential apt-utils \
  && apt-get clean \
  && npm install -g gulp node-gyp \
  && npm cache clean --force
VOLUME /app

WORKDIR /app
