FROM ruby:2.6-alpine
LABEL maintainer "Ben Jackson <ben@damnfine.com>"
# update and upgrade packages
RUN apk update && apk upgrade && apk add --repository http://dl-cdn.alpinelinux.org/alpine/edge/main/ --no-cache --update \
  alpine-sdk \
  nodejs=10.15.3-r0 \
  nodejs-npm=10.15.3-r0 \
  yarn