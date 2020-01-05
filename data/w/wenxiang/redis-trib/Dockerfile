FROM ruby:2.5-alpine

WORKDIR /app

RUN gem install redis
RUN wget http://download.redis.io/redis-stable/src/redis-trib.rb

ENTRYPOINT ["ruby", "redis-trib.rb"]
