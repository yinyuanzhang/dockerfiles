FROM ruby:alpine

RUN apk add -U postgresql-dev build-base postgresql-dev zlib-dev libxml2-dev libxslt-dev
RUN gem install ridgepole pg dotenv-rails

CMD ridgepole
