FROM ruby:2.5.3

ENV LC_ALL=C.UTF-8

RUN \
  curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
  curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
  echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
  curl -sS https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
  echo "deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main" |  tee /etc/apt/sources.list.d/pgdg.list && \
  apt-get update && \
  apt-get install -y --no-install-recommends \
      mysql-client \
      postgresql-client-10 \
      sqlite3 \
      nodejs \
      yarn \
      imagemagick \
      mecab libmecab-dev mecab-ipadic-utf8 && \
  mkdir /tmp/phantomjs && \
  curl -L https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 \
      | tar -xj --strip-components=1 -C /tmp/phantomjs && \
  mv /tmp/phantomjs/bin/phantomjs /usr/local/bin && \
  rm -rf /var/lib/apt/lists/*  /tmp/*
