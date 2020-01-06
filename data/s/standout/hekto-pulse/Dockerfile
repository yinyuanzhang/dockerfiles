FROM ruby:2.5.5-alpine3.8

RUN mkdir -p /app

WORKDIR /app

COPY Gemfile .
COPY Gemfile.lock .

RUN bundle install

COPY . .

CMD rackup -o 0.0.0.0
