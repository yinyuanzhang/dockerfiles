FROM ruby:2-alpine

COPY Gemfile /app/
COPY Gemfile.lock /app/
RUN apk add --no-cache --virtual build-dependencies build-base && \
    gem install bundler && \
    cd /app; bundle install && \
    apk del build-dependencies build-base && \
    rm -r ~/.bundle/ /usr/local/bundle/cache
COPY src/ /app/

WORKDIR /app
