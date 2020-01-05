FROM ubuntu:18.04
ENV DEBIAN_FRONTEND noninteractive

### Adding source packages to apt lists, to manual build some packages
RUN grep '^deb ' /etc/apt/sources.list | \
  sed 's/^deb /deb-src /g' | \
  tee /etc/apt/sources.list.d/deb-src.list

### Adding custom APT sources, to provide latest software versions
RUN apt-get update && apt-get install -y curl software-properties-common apt-transport-https && rm -rf /var/lib/apt/lists/*
RUN add-apt-repository -y ppa:git-ftp/ppa
RUN add-apt-repository -y ppa:ubuntu-toolchain-r/test
RUN LC_ALL=C.UTF-8 add-apt-repository -y ppa:ondrej/php

RUN curl -sL https://deb.nodesource.com/setup_8.x -o nodesource_setup.sh
RUN echo "deb http://mirrors.kernel.org/ubuntu/ xenial main" | tee -a /etc/apt/sources.list
RUN bash nodesource_setup.sh

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
RUN chmod +x /usr/local/bin/docker-compose

### Install some dependencies
RUN apt-get update && apt-get install --allow-unauthenticated -y \
  build-essential \
  debhelper \
  libssh2-1-dev \
  libssl-dev \
  libpng12-0 \
  && rm -rf /var/lib/apt/lists/*

### Manually rebuild CURL to allow SSL and SFTP support
RUN mkdir -p /opt/curl
RUN cd /opt/curl && apt-get update && apt-get source curl && rm -rf /var/lib/apt/lists/*
RUN cd /opt/curl && cd curl* && cd debian && sed -i -- "s/--without-ssl/--with-ssl --with-libssh2/g" rules
RUN cd /opt/curl && cd curl* && ./configure --with-ssl --with-libssh2 && make && make install
RUN rm /usr/bin/curl && ln -s /usr/local/bin/curl /usr/bin/curl
RUN apt-get autoremove -y && rm -rf /opt/curl

### Install aditional packages for Deployment environment
RUN export DEBIAN_FRONTEND=noninteractive && \
  apt-get update && \
  apt-get install -y \
  unzip \
  zip \
  git-ftp \
  nodejs \
  php7.3 \
  php7.3-mbstring \
  php7.3-xml \
  php7.3-bcmath \
  php7.3-json \
  php7.3-mysql \
  php7.3-gd \
  php7.3-gettext \
  php7.3-curl \
  php7.3-zip \
  rsync \
  yarn && \
  rm -rf /var/lib/apt/lists/*  


RUN npm -g install eslint eslint-plugin-node eslint-plugin-standard eslint-plugin-promise eslint-config-standard eslint-plugin-import
ENV TMPDIR /tmp

ENV COMPOSER_ALLOW_SUPERUSER 1
RUN curl --silent --show-error https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

## GCloud SDK
RUN export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \
    echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    apt-get update -y && apt-get install google-cloud-sdk -y && rm -rf /var/lib/apt/lists/*

RUN apt-get clean -y && apt-get autoclean && apt-get -y autoremove

## Kubectl
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
RUN chmod +x ./kubectl
RUN mv ./kubectl /usr/local/bin/kubectl
