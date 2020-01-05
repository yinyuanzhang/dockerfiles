FROM ubuntu:18.04

MAINTAINER Mihail Boiko <mboikoinbox@gmail.com>

# Set environment variables
ENV HOME /root

# Cloudflare DNS
RUN echo "nameserver 1.1.1.1" | tee /etc/resolv.conf > /dev/null

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get upgrade -y && \
    DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    software-properties-common \
    git \
    ca-certificates \
    unzip \
    mcrypt \
    wget \
    openssl \
    ssh \
    locales \
    less \
    composer \
    sudo \
    curl \
    gnupg \
    nodejs \
    --no-install-recommends && \
    add-apt-repository ppa:ondrej/php

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

# Install packages
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get upgrade -y && \
    DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    php-pear php7.3-mysql php7.3-xdebug php7.3-zip php7.3-xml php7.3-redis php7.3-bcmath php7.3-mbstring php7.3-curl php7.3-json php7.3-pdo php7.3-tokenizer php7.3-cli php7.3-imap php7.3-intl php7.3-gd php7.3-soap php7.3-gmp\
    --no-install-recommends && \
    apt-get clean -y && \
    apt-get autoremove -y && \
    apt-get autoclean -y && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Ensure UTF-8
ENV LANG       en_US.UTF-8
ENV LC_ALL     en_US.UTF-8
RUN locale-gen en_US.UTF-8

# Timezone & default bitbucket memory limit
RUN echo "date.timezone=Europe/Paris" > /etc/php/7.3/cli/conf.d/date_timezone.ini && echo "memory_limit=1G" >> /etc/php/7.3/cli/php.ini

WORKDIR /tmp