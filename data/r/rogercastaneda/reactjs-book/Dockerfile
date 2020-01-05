FROM node:10.12.0-alpine

LABEL version="0.1"
LABEL maintainer="rogercastanedag@gmail..com"

RUN \
  apk add --update && \
  apk add nodejs git && \
  npm install -g yarn node-static && \
  mkdir -p /app

# Change directory so that our commands run inside this new directory
WORKDIR /app