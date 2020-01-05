# This Dockerfile builds the base image for CircleCI tests.
#
# Put all permanent dependencies here instead of installing them for each run.
#
# Short build instructions:
#
# cd ci_base
# docker build -f Dockerfile -t brightbytes/ci_base .
# docker tag brightbytes/ci_base brightbytes/ci_base:0.0.2 # whatever the next version is
# docker push brightbytes/ci_base:0.0.2 # whatever you picked on the previous line

# Add changes to CHANGELOG
#
# To start locally:
#
# docker run -it brightbytes/ci_base:0.0.2 /bin/bash # match the tagged version

FROM ubuntu:bionic

ENV DEBIAN_FRONTEND=noninteractive

# Install packages from repos
RUN \
  apt-get update && apt-get install -y gnupg curl && \
  echo "deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main" > /etc/apt/sources.list.d/pgdg.list && \
  curl https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
  apt-get update && apt-get install -y \
    bzip2 \
    git \
    imagemagick \
    libfontconfig \
    libmagickwand-dev \
    libpq-dev \
    libsodium-dev \
    libsqlite3-dev \
    make \
    postgresql-client-9.6 \
    unzip \
    tzdata \
    xvfb \
    locales \
    # Install Cypress dependencies from https://github.com/cypress-io/cypress-docker-images/blob/master/base/10/Dockerfile
    libgtk2.0-0 \
    libnotify-dev \
    libgconf-2-4 \
    libnss3 \
    libxss1 \
    libasound2    

# Set default locale to UTF-8
RUN \
  sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
  echo 'LANG="en_US.UTF-8"'>/etc/default/locale && \
  dpkg-reconfigure --frontend=noninteractive locales && \
  update-locale LANG=en_US.UTF-8

ENV LANGUAGE=en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8

# Install our ruby version (2.5.5)
RUN \
  mkdir -p ~/ruby-install && \
  curl -L https://github.com/postmodern/ruby-install/archive/v0.6.1.tar.gz \
  | tar -xz -C ~/ruby-install --strip-components=1 && \
  ~/ruby-install/bin/ruby-install --system ruby 2.5.5 && \
  rm -rf ~/ruby-install && \
  gem update --system

# specific version of node
RUN mkdir ~/node && \
  curl -L https://nodejs.org/download/release/v10.15.3/node-v10.15.3-linux-x64.tar.gz \
  | tar -xz -C ~/node --strip-components=1

# yarn
RUN mkdir ~/yarn && \
  curl -L https://github.com/yarnpkg/yarn/releases/download/v1.15.2/yarn-v1.15.2.tar.gz \
  | tar -xz -C ~/yarn --strip-components=1

# phantomjs 2
RUN mkdir ~/phantomjs && \
  curl -L https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 \
  | tar -xj -C ~/phantomjs --strip-components=1

# Latest release of Chrome (at the time the dockerfile is built!) with ALL dependencies
# We disable Chome sandbox so it runs fine under root. The easiest way to do this is with a shim.
RUN curl -o ~/chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
  dpkg --force-all -i ~/chrome.deb; \
  apt-get update && apt-get -y -f install && \
  rm -r ~/chrome.deb && \
  mv /opt/google/chrome/google-chrome /opt/google/chrome/google-chrome.original && \
  printf '#!/bin/bash'"\n"'/opt/google/chrome/google-chrome.original --no-sandbox --disable-setuid-sandbox "$@"'"\n" >/opt/google/chrome/google-chrome && \
  chmod +x /opt/google/chrome/google-chrome

RUN mkdir ~/chromedriver && \
  curl -o ~/chromedriver.zip -L 'https://chromedriver.storage.googleapis.com/2.46/chromedriver_linux64.zip' && \
  unzip ~/chromedriver.zip -d ~/chromedriver && \
  rm ~/chromedriver.zip

# Just put additional deps here instead of at the start of the file.
# This way you don't have to rebuild everything.
#
# But when you rebuild everything, do move the deps into the topmost apt-get install
