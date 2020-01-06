FROM node:8-alpine

MAINTAINER Picter <developers@picter.com>

RUN apk add -Uuv \
  ca-certificates \
  git \
  gzip \
  jq \
  make \
  gcc \
  g++ \
  docker \
  openssh-client \
  python \
  py-pip \
  tar \
  && rm -rf /var/cache/apk/*
RUN pip install awscli
