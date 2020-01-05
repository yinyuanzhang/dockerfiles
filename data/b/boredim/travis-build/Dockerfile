FROM ruby:2.5.1
LABEL maintainer Travis CI GmbH <support+travis-app-docker-images@travis-ci.com>
WORKDIR /usr/src/app
COPY . .
ARG GITHUB_OAUTH_TOKEN=notset
RUN bundle config --global frozen 1
RUN bundle install
RUN bundle exec rake assets:precompile GITHUB_OAUTH_TOKEN=$GITHUB_OAUTH_TOKEN
CMD bundle exec bin/server
