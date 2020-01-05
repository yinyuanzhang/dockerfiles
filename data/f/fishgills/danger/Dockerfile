FROM ruby:alpine
MAINTAINER Charlie Davis <fishgills@fishgills.net>
COPY Gemfile Gemfile

RUN apk add git
RUN gem install bundler
RUN bundle install

WORKDIR /danger
