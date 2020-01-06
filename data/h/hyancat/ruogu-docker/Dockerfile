FROM php:alpine
LABEL maintainer="hyancat.cn@gmail.com"

# PHP config
COPY php/fpm/conf/*.ini /usr/local/etc/php/

RUN apk add --no-cache curl imagemagick libzip
RUN apk add --no-cache --virtual .build-deps \
    $PHPIZE_DEPS curl-dev imagemagick-dev libtool libzip-dev libxml2-dev postgresql-dev sqlite-dev \
    && pecl install imagick && docker-php-ext-enable imagick \
    && docker-php-ext-configure zip --with-libzip \
    && docker-php-ext-install -j$(getconf _NPROCESSORS_ONLN) zip mbstring pdo_mysql opcache bcmath pcntl \
    && apk del .build-deps
