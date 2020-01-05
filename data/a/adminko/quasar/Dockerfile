FROM node:alpine

RUN set -xe \
    && apk add --no-cache bash yarn
RUN yarn global add @quasar/cli

VOLUME /app
WORKDIR /app
EXPOSE 8080