FROM debian:stretch
MAINTAINER Christoph Föhrdes <christoph.foehrdes@leaphub.de>

# general stuff
RUN apt-get update
RUN apt-get install -y git curl procps gnupg2 apt-transport-https lsb-release ca-certificates

# configure container timezone
ENV TZ="Europe/Berlin"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# ansible (using ubuntu repo as told in ansible docs)
RUN echo "deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main" > /etc/apt/sources.list.d/ansible.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367
RUN apt-get update && apt-get install -y ansible

# php 7
RUN curl -sS https://packages.sury.org/php/apt.gpg | apt-key add -
RUN echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" > /etc/apt/sources.list.d/php7.list
RUN apt-get update && apt-get install -y \
    php7.3-cli \
    php7.3-curl \
    php7.3-imap \
    php7.3-imagick \
    php7.3-gd \
    php7.3-intl \
    php7.3-sqlite3 \
    php7.3-mysql \
    php7.3-mbstring \
    php7.3-xml \
    php7.3-xmlrpc \
    php7.3-soap \
    php7.3-zip \
    php7.3-memcached

# ruby
RUN apt-get install -y ruby bundler

# composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# node
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y nodejs

# gulp
RUN npm install -g gulp

# bower
RUN npm install -g bower

# yarn
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" > /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install -y yarn

# AWS cli
RUN apt-get install -y python-pip
RUN pip install awscli --upgrade

# Sentry CLI
RUN curl -sL https://sentry.io/get-cli/ | bash

# jenkins setup
RUN useradd -r -m -d /home/jenkins -s /bin/bash -u 1100 jenkins
USER jenkins
RUN mkdir -p /home/jenkins/.ssh
RUN echo "\nHost *\n   StrictHostKeyChecking no\n   UserKnownHostsFile=/dev/null\n" >> /home/jenkins/.ssh/config
