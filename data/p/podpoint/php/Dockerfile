FROM php:7.2-fpm-alpine

RUN apk update \
    && apk add --no-cache $PHPIZE_DEPS bzip2-dev freetype-dev gmp-dev icu-dev libjpeg-turbo-dev libpng-dev libmemcached-dev libmcrypt-dev libxml2-dev zlib-dev \
    && NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \
    && docker-php-source extract \
    && docker-php-ext-configure gd \
        --with-gd \
        --with-freetype-dir=/usr/include/ \
        --with-png-dir=/usr/include/ \
        --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j${NPROC} bcmath bz2 gd gmp intl opcache pdo_mysql soap zip \
    && pecl install memcached \
    && pecl install redis \
    && docker-php-ext-enable memcached redis \
    && docker-php-source delete \
    && apk del $PHPIZE_DEPS \
    && rm -rf /tmp/* /var/cache/apk/*

MAINTAINER Pod-Point <software@pod-point.com>
