FROM ruby:2.6.5-slim

MAINTAINER Dru Jensen <drujensen@gmail.com>

ENV BASH_PACKAGES bash curl git vim grep tmux netcat default-mysql-client
ENV RUBY_PACKAGES build-essential libxml2-dev libxslt-dev libssl-dev default-libmysqlclient-dev imagemagick
ENV CHROME_PACKAGES libdbus-glib-1-2 xvfb chromium

# install bash, command line tools, ruby and chromium
RUN apt-get update && \
    apt-get install -y $BASH_PACKAGES && \
    apt-get install -y $RUBY_PACKAGES && \
    apt-get install -y $CHROME_PACKAGES

# add nodejs stable sources
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -

# install nodejs and cleanup packages
RUN apt-get update && \
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/* \
      /var/cache/apk/* \
      /usr/share/man \
      /tmp/* \
      /usr/lib/node_modules/npm/man \
      /usr/lib/node_modules/npm/doc \
      /usr/lib/node_modules/npm/html \
      /usr/lib/node_modules/npm/scripts

# setup chrome environment
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROME_PATH=/usr/lib/chromium/
