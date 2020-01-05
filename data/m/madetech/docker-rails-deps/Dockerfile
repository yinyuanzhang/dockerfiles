FROM ubuntu:18.04

RUN apt-get update -qq
RUN apt-get -y install build-essential git openssl libreadline-dev curl git-core zlib1g zlib1g-dev libssl-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt-dev libmysqlclient-dev libpq-dev imagemagick libmagickwand-dev libffi-dev mysql-client nodejs
RUN apt-get -y install nodejs-dev node-gyp libssl1.0-dev
RUN apt-get -y install npm 

RUN npm install -g phantomjs

RUN git clone https://github.com/sstephenson/ruby-build.git /tmp/ruby-build && \
  cd /tmp/ruby-build && \
  ./install.sh && \
  cd / && \
  rm -rf /tmp/ruby-build

RUN ruby-build -v 2.6.3 /usr/local
RUN gem install bundler rubygems-bundler
RUN gem regenerate_binstubs
