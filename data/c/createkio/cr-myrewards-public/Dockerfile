FROM createkio/docker-ruby:2.3.3-slim

MAINTAINER CreatekIO

WORKDIR /app

COPY Gemfile Gemfile.lock ./
RUN bundle install --jobs 20 --retry 5 && \
      rm -rf /app/*

RUN apt-get update && \
  apt-get install -y --no-install-recommends cmake && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY tools/Gemfile tools/Gemfile.lock ./tools/
RUN cd tools && bundle install --jobs 20 --retry 5 && \
      rm -rf /app/*
