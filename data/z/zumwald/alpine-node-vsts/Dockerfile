FROM mhart/alpine-node:8

RUN apk update \
  && apk add git

RUN npm i -g better-vsts-npm-auth@3.1.0 \
  && npm cache clean --force
