# direct copy/paste from https://github.com/docker-library/rails/blob/master/onbuild/Dockerfile
# with additional qt5-default install for capybara
FROM ruby:2.3.1

RUN apt-get update && \
    grep security /etc/apt/sources.list > /tmp/security.list && \
    apt-get install -y qt5-default libqt5webkit5-dev && \
    apt-get install -y nodejs --no-install-recommends && \
    apt-get upgrade -oDir::Etc::Sourcelist=/tmp/security.list -y && \
    rm -rf /var/lib/apt/lists/*.lz4 && \
    rm -rf /tmp/security.list

ONBUILD RUN apt-get update && \
    grep security /etc/apt/sources.list > /tmp/security.list && \
    apt-get upgrade -oDir::Etc::Sourcelist=/tmp/security.list -y && \
    rm -rf /var/lib/apt/lists/*.lz4 && \
    rm -rf /tmp/security.list

ONBUILD RUN mkdir -p /usr/src/app
ONBUILD WORKDIR /usr/src/app

ONBUILD ADD Gemfile /usr/src/app/
ONBUILD ADD Gemfile.lock /usr/src/app/
ONBUILD RUN bundle install --system

ONBUILD ADD . /usr/src/app

ENV RAILS_VERSION 4.1.16

RUN gem install rails --version "$RAILS_VERSION"

EXPOSE 3000
CMD ["rails", "server"]
