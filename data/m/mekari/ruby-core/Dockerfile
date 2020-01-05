# Base image:
FROM ruby:2.5.1-alpine

# Install dependencies
RUN apk update \
  && apk upgrade --available \
  && apk --no-cache add \
  build-base \
  gcc \
  git \
  libpq \
  ca-certificates