FROM composer:latest AS composer
FROM php:7.2-fpm

COPY --from=composer /usr/bin/composer /usr/bin/composer
RUN apt update && apt install -y git
RUN apt-get install -y zlib1g-dev libicu-dev g++
RUN apt-get install -y sqlite3 libsqlite3-dev
RUN apt-get install -y libmagick++-dev libmagickwand-dev

RUN apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng-dev \
    && docker-php-ext-install -j$(nproc) iconv \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd

RUN docker-php-ext-install exif
RUN docker-php-ext-install intl
RUN docker-php-ext-install pdo_mysql pdo_sqlite

RUN pecl install redis-4.3.0
RUN pecl install imagick
RUN docker-php-ext-enable redis imagick


RUN apt-get -y --allow-unauthenticated install libgearman-dev wget unzip \
    && cd /tmp \
    && wget https://github.com/wcgallego/pecl-gearman/archive/gearman-2.0.3.zip \
    && unzip gearman-2.0.3.zip \
    && mv pecl-gearman-gearman-2.0.3 pecl-gearman \
    && cd pecl-gearman \
    && phpize \
    && ./configure \
    && make -j$(nproc) \
    && make install \
    && cd / \
    && rm /tmp/gearman-2.0.3.zip \
    && rm -r /tmp/pecl-gearman \
    && docker-php-ext-enable gearman

RUN git clone https://github.com/nrk/predis.git /usr/local/lib/php/predis && \
    git clone https://github.com/markhilton/redis-http-cache.git /usr/local/lib/php/redis-http-cache

ENV COMPOSER_ALLOW_SUPERUSER 1
ENV RUN_SCRIPTS=1

EXPOSE 9000
