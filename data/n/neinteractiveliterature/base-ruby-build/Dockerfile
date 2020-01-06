ARG RUBY_VERSION=2.6.5

FROM ruby:${RUBY_VERSION}-alpine as build

RUN apk add \
  --no-cache \
  build-base git postgresql-dev curl python tzdata less bash nodejs yarn openssl

RUN mkdir -p /usr/src/build \
  && addgroup -S www \
  && adduser -G www -S www \
  && chown www:www /usr/src/build
USER www

WORKDIR /usr/src/build
