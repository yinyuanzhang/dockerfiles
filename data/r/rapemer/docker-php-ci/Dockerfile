FROM php:7.2-cli

ARG DEBIAN_FRONTEND=noninteractive

RUN pecl channel-update pecl.php.net
RUN apt-get update
RUN apt-get install build-essential apt-utils ssh openssh-client -y --no-install-recommends

# APCU:
RUN pecl install apcu
RUN docker-php-ext-enable apcu

# BCMATH:
RUN docker-php-ext-install bcmath

# CALENDAR:
RUN docker-php-ext-install calendar

# EXIF:
RUN docker-php-ext-install exif

# GETTEXT:
RUN docker-php-ext-install gettext

# GD:
RUN apt-get install libgd-dev libfreetype6-dev -y --no-install-recommends
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ --with-png-dir=/usr/include/
RUN docker-php-ext-install gd

# IMAGICK:
RUN apt-get install libmagickwand-dev -y --no-install-recommends
RUN pecl install imagick
RUN docker-php-ext-enable imagick

# INTL:
RUN apt-get install libicu-dev -y --no-install-recommends
RUN docker-php-ext-configure intl
RUN docker-php-ext-install intl

# MEMCACHED:
RUN apt-get install libmemcached-dev zlib1g-dev -y --no-install-recommends
RUN curl -L -o /tmp/memcached.tar.gz "https://github.com/php-memcached-dev/php-memcached/archive/v3.1.3.tar.gz" && \
    mkdir -p /usr/src/php/ext/memcached && \
    tar -C /usr/src/php/ext/memcached -zxvf /tmp/memcached.tar.gz --strip 1 && \
    docker-php-ext-configure memcached && \
    docker-php-ext-install memcached && \
    rm /tmp/memcached.tar.gz

# OPCACHE:
RUN docker-php-ext-install opcache

# PCNTL:
RUN docker-php-ext-install pcntl

# PDO:
RUN docker-php-ext-install pdo_mysql mysqli

# PostgreSQL
RUN apt-get install libpq-dev -y --no-install-recommends
RUN docker-php-ext-install pdo_pgsql pgsql

# REDIS
RUN pecl install -o -f redis
RUN rm -rf /tmp/pear
RUN docker-php-ext-enable redis

# SOAP:
RUN apt-get install libxml2-dev -y --no-install-recommends
RUN docker-php-ext-install soap

# SOCKETS:
RUN docker-php-ext-install sockets

# XSL:
RUN apt-get install libxslt-dev -y --no-install-recommends
RUN docker-php-ext-install xsl

# ZIP:
RUN apt-get install libzip-dev unzip -y --no-install-recommends
RUN docker-php-ext-configure zip --with-libzip
RUN docker-php-ext-install zip

# COMPOSER:
ENV COMPOSER_ALLOW_SUPERUSER=1
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# PHP settings for CI/CD
RUN echo "memory_limit = -1;" > $PHP_INI_DIR/conf.d/memory_limit.ini
RUN echo "max_execution_time = 0;" > $PHP_INI_DIR/conf.d/max_execution_time.ini
RUN echo "date.timezone = UTC;" > $PHP_INI_DIR/conf.d/timezone.ini
