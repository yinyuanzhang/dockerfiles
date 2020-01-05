FROM ruby:2.3
MAINTAINER fn.sauter@gmail.com

ENV RAILS_VERSION="4.2.7" \
    TEST_PACKAGES="git build-essential postgresql-client nodejs-legacy npm --no-install-recommends" \
    NPM_PACKAGES="phantomjs-prebuilt"

RUN apt-get update -qq && apt-get install -y $TEST_PACKAGES && npm install -g $NPM_PACKAGES

RUN gem install -N rails --version "$RAILS_VERSION" && \
    gem install -N bundler && \
    gem install -N rubocop && \
    gem install -N rspec

# Preinstall test dependencies so we save time during the test execution using e.g. bitbucket pipelines.
RUN git clone https://amos-erp:ZyWGvXC7au24JcQk6JL1ksCi7Lu2aNQu@bitbucket.org/amos-erp/amos-core.git && \
    cd amos-core  && \
    bundle install --jobs 20 --system && \
    cd ..  && \
    rm -r amos-core

# Setup rubocop guidelines
COPY .rubocop.yml /
