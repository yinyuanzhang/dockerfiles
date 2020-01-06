#
#--------------------------------------------------------------------------
# Image Setup
# Based on https://github.com/laradock/php-fpm/blob/master/Dockerfile-73
#--------------------------------------------------------------------------
#

FROM php:7.3-fpm

MAINTAINER Jagg Man <jaggman@mail.ru>

#
#--------------------------------------------------------------------------
# Software's Installation
#--------------------------------------------------------------------------
#
# Installing tools and PHP extentions using "apt", "docker-php", "pecl",
#

# Install "vim", "zip", "git", "wget",
#         "curl", "libmemcached-dev", "libpq-dev", "libjpeg-dev",
#         "libpng-dev", "libfreetype6-dev", "libssl-dev", "libmcrypt-dev",
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    vim zip git wget \
    curl \
    libmemcached-dev \
    libz-dev \
    libpq-dev \
    libjpeg-dev \
    libpng-dev \
    libfreetype6-dev \
    libssl-dev \
    libmcrypt-dev \
    libc-client-dev libkrb5-dev \
  && rm -rf /var/lib/apt/lists/*

# Install composer
RUN wget -O- https://getcomposer.org/installer | php -- --install-dir="/usr/local/bin" --filename="composer"
 
# Install the PHP pdo_mysql extention
RUN docker-php-ext-install pdo_mysql \
  # Install the PHP pdo_pgsql extention
  && docker-php-ext-install pdo_pgsql \
  # Install the PHP gd library
  && docker-php-ext-configure gd \
    --with-jpeg-dir=/usr/lib \
    --with-freetype-dir=/usr/include/freetype2 \
  && docker-php-ext-install gd \
  && docker-php-ext-configure imap \
    --with-kerberos \
    --with-imap-ssl \
  && docker-php-ext-install imap \
  # Install the PHP mongodb extention
  && pecl install mongodb \
  && docker-php-ext-enable mongodb
