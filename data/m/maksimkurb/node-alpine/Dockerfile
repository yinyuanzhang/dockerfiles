FROM node:10-alpine

WORKDIR /app

RUN apk add --update \
      bash \
      lcms2-dev \
      libpng-dev \
      gcc \
      g++ \
      make \
      autoconf \
      automake && \
    rm -rf /var/cache/apk/*
