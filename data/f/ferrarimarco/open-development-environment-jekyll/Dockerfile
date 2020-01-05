FROM ruby:2.5.1-alpine

RUN apk add --update --no-cache \
  nodejs

COPY package.json package.json
# Get the version specified in package.json (that may be automatically updated when new package versions are pushed)
RUN \
  npm install -g fs-extra@$(cat package.json | grep fs-extra | awk -F '"' '{print $4}')

COPY Gemfile Gemfile
RUN \
  gem install bundler \
  && bundle install
