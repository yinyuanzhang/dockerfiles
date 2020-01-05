FROM ruby:2.6.0-alpine3.7

LABEL maintainer oltruong<contact@oltruong.com>

RUN apk add --update bash build-base libffi-dev openssh rsync nodejs
RUN gem install bundler
RUN npm install -g firebase-tools
