FROM ubuntu:16.04
LABEL maintainer="danny@wunderflats.com"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update
RUN apt install -yq software-properties-common

# PPA for up to date version of git (needed for --porcelain=2)
RUN add-apt-repository -y ppa:git-core/ppa
# Needed for installing jq
RUN add-apt-repository universe
RUN apt update

# UTILS
# libxml2-utils - contains xmllint, necessary for ebay-service tests
# jq, necessary for website predeploy script
RUN apt install -yq gettext-base curl apt-transport-https ca-certificates gnupg2 software-properties-common git libxml2-utils moreutils jq

# Yarn
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt install -yq nodejs
RUN node --version
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" > /etc/apt/sources.list.d/yarn.list
RUN apt update && apt install -yq yarn

# n
RUN yarn global add n

# MongoDB
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4
RUN echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/4.0 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.0.list
RUN apt update && apt install -yq mongodb-org

# Install UnicodeData.txt locally so we don't need to download it from unicode.org, which is rate limitted
RUN apt install -yq unicode-data

# Git
RUN apt install -yq git
RUN git config --global user.email "bitbucket-ci@bitbucket.org"
RUN git config --global user.name "Bitbucket Pipelines"
RUN git config --global push.default simple

# Docker
RUN apt install -yq docker.io

# phantomjs dependency
RUN apt install -yq libfontconfig

# node-gyp dependency
RUN apt install -yq python

# sharp dependency
RUN apt install -yq build-essential


# Java
RUN apt install -yq openjdk-8-jre

# Chrome
## See https://crbug.com/795759
RUN apt install -yq libgconf-2-4

# Cypress requirements
RUN apt install -yq xvfb libgtk2.0-0 libnotify-dev libgconf-2-4 libnss3 libxss1 libasound2

RUN apt install -yq --no-install-recommends wget \
  && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
  && apt update \
  && apt install -qy --no-install-recommends google-chrome-unstable fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst ttf-freefont \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /src/*.deb

## Add user so we don't need --no-sandbox.
RUN groupadd -r pptruser && useradd -r -g pptruser -G audio,video pptruser \
  && mkdir -p /home/pptruser/Downloads \
  && chown -R pptruser:pptruser /home/pptruser

# killall
RUN apt-get update \
 && apt-get install --no-install-recommends -y psmisc=22.21-2.1build1 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
