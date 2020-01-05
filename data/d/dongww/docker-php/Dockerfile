FROM php:7.0-apache

RUN pecl install redis-3.1.0 \
    && docker-php-ext-enable redis

RUN apt-get update && apt-get install -y \
        git \
        zlib1g-dev \
        libicu-dev \
        libmemcached-dev \
        vim \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
    && docker-php-ext-install -j$(nproc) iconv mcrypt \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd \
    && docker-php-ext-install opcache \
    && docker-php-ext-install intl \
    && docker-php-ext-install pdo_mysql \
    && docker-php-ext-install zip \
    && rm -rf /var/lib/apt/lists/*

# install memcached extension
RUN git clone --branch php7 https://github.com/php-memcached-dev/php-memcached /usr/src/php/ext/memcached \
  && cd /usr/src/php/ext/memcached \
  && docker-php-ext-configure memcached \
  && docker-php-ext-install memcached

COPY _config/php.ini /usr/local/etc/php/