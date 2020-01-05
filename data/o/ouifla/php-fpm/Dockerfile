FROM php:7.3-fpm

MAINTAINER Remi FUSSIEN <remi.fussien@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    curl \
    g++ \
    libfreetype6-dev \
    libicu-dev \
    libjpeg-dev \
    libmcrypt-dev \
    libmemcached-dev \
    libpng-dev \
    libpq-dev \
    libssl-dev \
    libz-dev \
    libzip-dev \
    libmagickwand-dev \
    imagemagick \
    supervisor \
    unzip \
    zlib1g-dev \
  && pecl install -o -f \
    imagick \
    redis \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /tmp/pear

RUN docker-php-ext-configure intl \
  && docker-php-ext-configure gd \
    --with-jpeg-dir=/usr/lib \
    --with-freetype-dir=/usr/include/freetype2 \
  && docker-php-ext-configure zip \
    --with-libzip

RUN docker-php-ext-install \
    bcmath \
    exif \
    gd \
    intl \
    opcache \
    pcntl \
    pdo_mysql \
    zip

RUN docker-php-ext-enable \
    imagick

RUN curl -s http://getcomposer.org/installer | \
    php -- --install-dir=/usr/local/bin --filename=composer --quiet

