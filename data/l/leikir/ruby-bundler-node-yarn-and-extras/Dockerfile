FROM leikir/ruby-bundler-node-yarn:ruby-2.6.3-node-10.16.0-slim

MAINTAINER Leikir Web <web@leikir.io>

ENV DOCKERIZE_VERSION 0.6.1

RUN apt-get update \
  && apt-get install -qq -y --no-install-recommends \
    apt-transport-https \
    build-essential \
    curl \
    file \
    git-core \
    gnupg \
    imagemagick \
    libcurl4-openssl-dev \
    libpq-dev

RUN gem install rake --no-document

RUN curl -L https://github.com/jwilder/dockerize/releases/download/v$DOCKERIZE_VERSION/dockerize-linux-amd64-v$DOCKERIZE_VERSION.tar.gz | tar xz && mv dockerize /usr/bin/
