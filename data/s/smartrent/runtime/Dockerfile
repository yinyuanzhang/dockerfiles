# Updated to this weird tag because of CVE-2019-14697
FROM alpine:20191114

ENV REPLACE_OS_VARS=true \
  SHELL=/bin/bash

RUN apk add --no-cache \
  bash \
  openssl-dev \
  libstdc++ \
  curl \
  postgresql-client

WORKDIR /opt/app
