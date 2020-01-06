FROM ruby:2.5.5-alpine as builder
ENV LANG=ja_JP.UTF-8 \
    BUNDLE_JOBS=4 \
    RAILS_ENV=development
WORKDIR /tmp
COPY Gemfile Gemfile
COPY Gemfile.lock Gemfile.lock

RUN apk --update --no-cache add --virtual build-dependencies \
    build-base \
    curl-dev \
    mysql-dev \
    linux-headers \
    && gem install bundler \
    && bundle install \
    && apk del build-dependencies

# development
FROM ruby:2.5.5-alpine as development
ENV LANG=ja_JP.UTF-8 \
    BUNDLE_JOBS=4 \
    RAILS_ENV=development
RUN apk --update --no-cache add \
    bash \
    nodejs \
    mariadb-dev \
    tzdata \
    less
COPY --from=builder /usr/local/bundle/bin/bundler /usr/local/bundle/bin/bundler
COPY --from=builder /usr/local/bundle /usr/local/bundle

RUN mkdir -p /daps-rails
WORKDIR /daps-rails
COPY . /daps-rails

# production
FROM ruby:2.5.5-alpine as production-builder
ARG MYSQL_DATABASE
ARG MYSQL_USER
ARG MYSQL_PASSWORD
ARG MYSQL_HOST
ARG TWITTER_CONSUMER_API_KEY
ARG TWITTER_CONSUMER_API_SECRET
ARG GOOGLE_CLIENT_ID
ARG GOOGLE_CLIENT_SECRET
ARG AWS_S3_BUCKET
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_REGION
ARG AWS_S3_HOST
ARG AWS_ACCESS_KEY

ENV LANG=ja_JP.UTF-8 \
    BUNDLE_JOBS=4 \
    RAILS_ENV=production

WORKDIR /tmp
COPY Gemfile Gemfile
COPY Gemfile.lock Gemfile.lock

RUN apk --update --no-cache add --virtual build-dependencies \
    build-base \
    curl-dev \
    mysql-dev \
    linux-headers \
    && gem install bundler \
    && bundle install --without development test \
    && apk del build-dependencies

FROM ruby:2.5.5-alpine as production
ARG MYSQL_DATABASE
ARG MYSQL_USER
ARG MYSQL_PASSWORD
ARG MYSQL_HOST
ARG TWITTER_CONSUMER_API_KEY
ARG TWITTER_CONSUMER_API_SECRET
ARG GOOGLE_CLIENT_ID
ARG GOOGLE_CLIENT_SECRET
ARG AWS_S3_BUCKET
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_REGION
ARG AWS_S3_HOST
ARG AWS_ACCESS_KEY
ARG SECRET_KEY_BASE

ENV LANG=ja_JP.UTF-8 \
    BUNDLE_JOBS=4 \
    RAILS_ENV=production \
    MYSQL_DATABASE=$MYSQL_DATABASE \
    MYSQL_USER=$MYSQL_USER \
    MYSQL_PASSWORD=$MYSQL_PASSWORD \
    MYSQL_HOST=$MYSQL_HOST \
    TWITTER_CONSUMER_API_KEY=$TWITTER_CONSUMER_API_KEY \
    TWITTER_CONSUMER_API_SECRET=$TWITTER_CONSUMER_API_SECRET \
    GOOGLE_CLIENT_ID=$GOOGLE_CLIENT_ID \
    GOOGLE_CLIENT_SECRET=$GOOGLE_CLIENT_SECRET \
    AWS_REGION=$AWS_REGION \
    AWS_S3_BUCKET=$AWS_S3_BUCKET \
    AWS_S3_HOST=$AWS_S3_HOST \
    AWS_ACCESS_KEY=$AWS_ACCESS_KEY \
    AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
    SECRET_KEY_BASE=$SECRET_KEY_BASE

RUN apk --update --no-cache add \
    nodejs\
    mariadb-dev \
    tzdata \
    nginx \
    openrc \
    less \
    && mkdir -p /daps-rails
COPY --from=production-builder /usr/local/bundle/bin/bundler /usr/local/bundle/bin/bundler
COPY --from=production-builder /usr/local/bundle /usr/local/bundle

RUN mkdir -p /daps-rails
WORKDIR /daps-rails
COPY . /daps-rails

ADD nginx/daps.conf /etc/nginx/conf.d/default.conf
RUN mkdir -p /run/nginx

RUN rails assets:precompile

CMD sh -c "nginx && pumactl start"
