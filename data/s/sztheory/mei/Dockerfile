# Ruby + Node are necessary for a Rails app (Node is needed for asset pipeline)
FROM sztheory/rubynode:2.5.1_8.11.0
MAINTAINER sztheory

# Install apt based dependencies required to run Rails as well as RubyGems and any other gem deps.
# As the Ruby image itself is based on an Alpine image, we use apk to install those
RUN apk add --no-cache \
    bash \
    binutils-gold \
    curl \
    g++ \
    gcc \
    imagemagick \
    make \
    libressl-dev \
    libssl1.0 \
    libxml2-dev \
    libxslt-dev \
    postgresql-dev \
    readline-dev \
    tzdata

ARG GIT_COMMIT=346cb8b
ARG GITHUB_USER=szTheory
ARG GITHUB_REPO=mei
ARG GITHUB_BASE_URL=https://github.com/$GITHUB_USER/$GITHUB_REPO/tarball
ARG GITHUB_URL=$GITHUB_BASE_URL/$GIT_COMMIT

ARG TARBALL_FILENAME=code.tar.gz
ARG EXTRACTED_TARBALL_DIR=$GITHUB_USER-$GITHUB_REPO-$GIT_COMMIT

ENV APP_DIR /app

# Pull down code with Github Contents API
RUN curl -L --retry 3 $GITHUB_URL > $TARBALL_FILENAME \
    && tar -xvf $TARBALL_FILENAME \
    && mv $EXTRACTED_TARBALL_DIR $APP_DIR \
    && cp $APP_DIR/config/database.yml.example $APP_DIR/config/database.yml \
    && cp $APP_DIR/config/environments/default.yml.example $APP_DIR/config/environments/default.yml

WORKDIR $APP_DIR

# optimal bundler job count is 1 less than the number of cores in your machine
# source: https://robots.thoughtbot.com/parallel-gem-installing-using-bundler#fn-2013-08-27-2
ARG BUNDLER_NUM_JOBS=3
ARG BUNDLER_RETRY_COUNT=5
# TODO: move this to its own step above with just
# Gemfile and Gemfile.lock to cache deps when no changes made?
RUN bundle install --jobs $BUNDLER_NUM_JOBS --retry $BUNDLER_RETRY_COUNT --without development test doc darwin