FROM ruby:2.3.7-alpine
MAINTAINER Roman Z <imakegreat.com@gmail.com>

RUN apk --update add --virtual build-dependencies \
                                # bundler \
                                libcurl \
                                curl \
                                build-base \
                                libxml2-dev \
                                libxslt-dev \
                                sqlite-dev \
                                nodejs \
                                tzdata \
                                && rm -rf /var/cache/apl/*

RUN apk update && apk add libffi-dev

RUN apk update && apk upgrade
RUN apk add postgresql-client build-dependencies postgresql-dev postgresql

RUN bundle config build.nokogiri --use-system-libraries

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app

RUN gem update bundler
RUN bundle install
RUN bundle exec rake RAILS_ENV=production DATABASE_URL=postgresql://user:pass@127.0.0.1/dbname SECRET_TOKEN=pickasecuretoken assets:precompile
# RUN bundle exec rake db:create db:migrate
CMD npm run start_prod

EXPOSE 3000