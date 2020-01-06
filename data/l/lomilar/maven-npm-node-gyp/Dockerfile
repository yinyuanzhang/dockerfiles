FROM node:12.7.0-alpine

ENV NPM_CONFIG_LOGLEVEL info
ENV NODE_VERSION 10.15.3

RUN apk update && apk add openjdk8 maven build-base git python bash

CMD ["mvn"]