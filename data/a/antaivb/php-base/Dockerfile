FROM php:7.3-fpm as php-builder

USER root

RUN apt-get update \
    && \
        apt-get install -y git \
        bzip2 \
        gnupg \
        libc6-dev \
        libbz2-dev \
        libzip-dev \
        libcurl4-openssl-dev \
        libmcrypt-dev \
        libgmp-dev \
        libsodium-dev \
        libssl-dev \
        libxml2 \
        libxml2-dev \
        libicu-dev \
        libzip4 \
        curl \
        mysql-client \
    && \
        apt-get clean all

RUN apt-get update && \
        apt-get install aptitude -y && \
        aptitude install libxft-dev -y \
        && apt-get clean all

#RUN pecl install grpc \
#    && pecl install protobuf
#RUN echo extension=grpc.so > /usr/local/etc/php/conf.d/grpc.ini \
#    && echo extension=protobuf.so > /usr/local/etc/php/conf.d/protobuf.ini

ENV PHPREDIS_VERSION 4.1.1

RUN mkdir -p /usr/src/php/ext/redis \
    && curl -L https://github.com/phpredis/phpredis/archive/$PHPREDIS_VERSION.tar.gz | \
        tar xvz -C /usr/src/php/ext/redis --strip 1 \
    && echo 'redis' >> /usr/src/php-available-exts \
    && docker-php-ext-install redis

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install -y wget nodejs

RUN docker-php-ext-install bz2
RUN docker-php-ext-install bcmath
RUN docker-php-ext-install calendar
RUN docker-php-ext-install curl
RUN docker-php-ext-install mysqli
RUN docker-php-ext-install pdo
RUN docker-php-ext-install pdo_mysql
RUN docker-php-ext-install phar
RUN docker-php-ext-install sodium
RUN docker-php-ext-install opcache
RUN docker-php-ext-install gmp
RUN docker-php-ext-install zip
RUN docker-php-ext-install intl
RUN echo yes | pecl install xdebug

WORKDIR /tmp
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
RUN php composer-setup.php

FROM php:7.3-fpm

USER root

RUN apt-get update \
  && \
    apt-get install -y \
    bzip2 \
    gnupg \
    libxml2 \
    libsodium18 \
    curl \
    zip \
    mysql-client \
    procps \
    nginx \
    libzip4 \
  && \
    apt-get clean all

RUN apt-get update \
  && apt-get clean all

COPY --from=php-builder /tmp/composer.phar /usr/local/bin/composer

WORKDIR /usr/local/lib/php/extensions/no-debug-non-zts-20180731
COPY --from=php-builder /usr/local/lib/php/extensions/no-debug-non-zts-20180731 .

WORKDIR /usr/local/etc/php
COPY --from=php-builder /usr/local/etc/php/conf.d conf.d/
COPY php.ini .

RUN mkdir -p /var/www/source

WORKDIR /var/www/source
