FROM ruby:2.6.5-alpine3.10
ENV LANG C.UTF-8

RUN \
  apk --update add alpine-sdk postgresql-dev postgresql-client nodejs yarn

RUN \
  echo 'gem: --no-rdoc --no-ri' >> /.gemrc && \
  gem install bundler
