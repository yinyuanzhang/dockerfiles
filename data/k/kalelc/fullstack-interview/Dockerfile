FROM ruby:2.4.1

MAINTAINER andreskal@gmail.com

RUN apt-get update
RUN apt-get install -y zlib1g-dev \
build-essential \
libssl-dev \
libyaml-dev \
libsqlite3-dev \
sqlite3 \
libxml2-dev \
libxslt1-dev \
libcurl4-openssl-dev \
python-software-properties \
libffi-dev \
nodejs \
nodejs-legacy \
libreadline-dev \
npm

RUN mkdir -p /app
RUN mkdir -p /app/pids
RUN mkdir -p /app/sockets

WORKDIR /app

COPY Gemfile Gemfile.lock ./
RUN gem install bundler

RUN bundle install --jobs 20 --retry 5

COPY . ./

ARG ENVIRONMENT
ENV RAILS_ENV $ENVIRONMENT
