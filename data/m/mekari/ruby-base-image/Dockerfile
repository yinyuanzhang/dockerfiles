# Base image:
FROM ruby:2.6.5-alpine

# Install dependencies
RUN apk update \
  && apk upgrade --available \
  && apk --no-cache add \
  build-base \
  gcc \
  git \
  libpq \
  ca-certificates