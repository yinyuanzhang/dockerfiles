FROM node:8.14.0-alpine

LABEL maintainer="docker@bajotumn.com"

RUN apk update \
    && apk upgrade \
    && apk add --no-cache \
    git \
    && rm -rf /var/cache/apk/*

RUN npm install --no-progress -g typescript
RUN npm install --no-progress -g @google/clasp @types/google-apps-script