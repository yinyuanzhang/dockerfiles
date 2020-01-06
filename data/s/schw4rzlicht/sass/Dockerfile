FROM ruby:alpine

RUN apk update && \
    apk add --virtual build-dependencies build-base gcc

RUN gem install sass --no-user-install
