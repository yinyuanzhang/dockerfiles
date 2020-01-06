FROM ruby:2.6.2
MAINTAINER Blabo <dev@bla.bo>
ENV LANG C.UTF-8

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - >/dev/null
RUN \
  curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
  echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN \
  apt-get update -qq && \
  apt-get install -y build-essential libpq-dev postgresql-client nodejs yarn

RUN \
  echo 'gem: --no-rdoc --no-ri' >> /.gemrc && \
  gem install bundler
