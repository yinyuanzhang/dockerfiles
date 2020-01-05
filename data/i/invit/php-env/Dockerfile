FROM php:7.2.12-fpm

MAINTAINER Toni Rudolf <toni.rudolf@weekend4two.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y update && apt-get install -y \
    procps \
    curl \
    gnupg2 \
    rsyslog \
    supervisor \
    sudo \
    wget \
    libfontconfig

RUN echo 'deb http://s3-eu-west-1.amazonaws.com/tideways/packages debian main' > /etc/apt/sources.list.d/tideways.list \
    && curl -sSL https://s3-eu-west-1.amazonaws.com/tideways/packages/EEB5E8F4.gpg | apt-key add -

RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev libpng-dev \
        libxrender1 libxext6 \
        tideways-php tideways-daemon \
        # imap
        libc-client-dev libkrb5-dev \
        # intl
        libicu-dev \
        # soap
        libxml2-dev \
        # zip
        libzip-dev \
        # ssh2
        libssh2-1-dev \
        # amqp
        librabbitmq-dev \
    && docker-php-source extract \
    && docker-php-ext-install -j$(nproc) gd \
    && docker-php-ext-configure imap --with-kerberos --with-imap-ssl && docker-php-ext-install -j$(nproc) imap \
    && docker-php-ext-install -j$(nproc) intl \
    && docker-php-ext-install -j$(nproc) opcache \
    && docker-php-ext-install -j$(nproc) bcmath \
    && docker-php-ext-install -j$(nproc) pdo_mysql \
    && docker-php-ext-configure zip --with-libzip && docker-php-ext-install -j$(nproc) zip \
    && docker-php-ext-install -j$(nproc) soap \
    && pecl install ssh2-1.1.2 && docker-php-ext-enable ssh2 \
    # snc redis does not support redis >3
    && pecl install redis-3.1.6 && docker-php-ext-enable redis \
    && pecl install amqp-1.9.3 && docker-php-ext-enable amqp \
    && pecl install apcu-5.1.14 && docker-php-ext-enable --ini-name 10-apcu.ini apcu \
    && pecl install apcu_bc-1.0.4 && docker-php-ext-enable --ini-name 20-apc.ini apc \
    && docker-php-ext-enable tideways \
    && docker-php-source delete

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN ln -fs /usr/share/zoneinfo/Europe/Zurich /etc/localtime && dpkg-reconfigure -f noninteractive tzdata

RUN usermod -u 1000 www-data

COPY loggly-syslog.conf /etc/rsyslog.d/
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.syslog.conf

WORKDIR /var/www/weekend4two
