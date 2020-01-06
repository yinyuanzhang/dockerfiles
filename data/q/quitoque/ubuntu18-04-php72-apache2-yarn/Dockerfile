FROM quitoque/ubuntu18-04-php72-apache2

MAINTAINER Jérôme Arzel <jerome@quitoque.fr>

# Adding Yarn repository
RUN apt-get update && apt-get -qq -y install make build-essential gnupg ca-certificates curl apt-transport-https bzip2 && \
  curl -sS https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - && \
  echo 'deb https://deb.nodesource.com/node_11.x bionic main' | \
    tee /etc/apt/sources.list.d/nodejs.list && \
  curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
  echo 'deb https://dl.yarnpkg.com/debian/ stable main' | \
    tee /etc/apt/sources.list.d/yarn.list && \
  apt-get update && apt-get -qq -y install nodejs yarn && \
  rm /etc/apt/sources.list.d/nodejs.list /etc/apt/sources.list.d/yarn.list && \
  apt-get -qq -y autoremove && apt-get -qq -y autoclean && \
  apt-get -qq -y clean && rm -rf /var/lib/apt/lists/*
