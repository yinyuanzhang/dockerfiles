FROM ruby:2.3.1-slim
# In bundler version 1.12 some changes were made to accomodate changes to path
# methods in newer rubygems versions, which broke nested 'bundle exec' calls.
# See bundler issue #4992 for a more detailed explanation.
# (https://github.com/bundler/bundler/pull/4992)
# This was fixed in bundler version >= 1.13.2, so make sure a bundler version
# >= 1.13.2 and a matching rubygems version is installed.
ENV RUBYGEMS_VERSION 2.6.7
RUN gem update --system "$RUBYGEMS_VERSION"
# use bundler version matching bundler version in Gemfile.lock
ENV BUNDLER_VERSION 1.13.7
RUN gem install bundler --version "$BUNDLER_VERSION"
# continue as before
RUN apt-get update -qq \
  && apt-get install -y build-essential libpq-dev postgresql-client imagemagick libfontconfig1 libfreetype6 netcat ssh curl xz-utils\
  && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN curl -Ls https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 \
  | tar --extract --bzip2 --strip-components 2 --directory /usr/local/bin --wildcards --no-anchored '*/bin/phantomjs'

# FROM: https://github.com/nodejs/docker-node/blob/e2b78b4bde9440f2189007004a2ae4880f3eb030/6.11/slim/Dockerfile
ENV NODE_VERSION 6.11.0
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz" \
  && tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-components=1 \
  && rm "node-v$NODE_VERSION-linux-x64.tar.xz" \
  && ln -s /usr/local/bin/node /usr/local/bin/nodejs