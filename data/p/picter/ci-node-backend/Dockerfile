FROM node:8.15.0-alpine

LABEL maintainer="Picter <developers@picter.com>"

RUN apk add -Uuv \
  ca-certificates \
  git \
  gzip \
  docker \
  openssh-client \
  python \
  py-pip \
  tar \
  bash \
  zip \
  jq \
  && rm -rf /var/cache/apk/*
RUN pip install awscli
