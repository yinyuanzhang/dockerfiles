FROM ruby:2.4

ENV RUBYOPT -EUTF-8

RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs vim wget

ENV DOCKERIZE_VERSION v0.6.0
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
 && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
 && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

RUN mkdir /app
WORKDIR /app

ADD Gemfile      Gemfile
ADD Gemfile.lock Gemfile.lock

RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs vim

RUN bundle install -j4
