FROM ruby:2.6.3-alpine3.9

RUN apk add --update ruby-dev build-base pcre-dev postgresql-dev ruby-nokogiri tzdata yarn && rm -rf /var/cache/apk/*
RUN gem install bundler -v 1.17.3

ADD Gemfile* ./

RUN bundle
