FROM drupaldocker/php:7.1-fpm-2.x
MAINTAINER nymedia

# fix work iconv library with alphine
RUN apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/community/ --allow-untrusted gnu-libiconv icu-dev
ENV LD_PRELOAD /usr/lib/preloadable_libiconv.so php

# Install dependencies.
RUN apk --no-cache update \
    && apk --no-cache upgrade \
    && apk add --no-cache $PHPIZE_DEPS \
        freetype \
        freetype-dev \
        libjpeg-turbo \
        libjpeg-turbo-dev \
        libpng \
        libpng-dev && \
    docker-php-ext-configure gd --enable-gd-native-ttf --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ --with-png-dir=/usr/include/ && \
    docker-php-ext-configure intl --enable-intl && \
    docker-php-ext-install -j$(getconf _NPROCESSORS_ONLN) gd pcntl intl
