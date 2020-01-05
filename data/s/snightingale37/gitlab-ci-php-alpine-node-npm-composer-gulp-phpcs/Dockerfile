# Use php 7.2
FROM php:7.2-alpine3.8

# Install and update items for everything to run inclduing docker
RUN apk add --no-cache freetype libpng libjpeg-turbo freetype-dev libpng-dev libjpeg-turbo-dev gnupg zip unzip git wget libmcrypt bash curl python && \
  docker-php-ext-configure gd \
    --with-gd \
    --with-freetype-dir=/usr/include/ \
    --with-png-dir=/usr/include/ \
    --with-jpeg-dir=/usr/include/ && \
  NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) && \
  docker-php-ext-install -j${NPROC} gd && \
  apk del --no-cache freetype-dev libpng-dev libjpeg-turbo-dev bash

# Install Node and NPM
RUN apk add --update nodejs nodejs-npm

# Install Gulp
RUN npm install -g gulp@3.9.1

# Install Composer
 RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

RUN composer global require \
"squizlabs/php_codesniffer=3.5.*" \
"phpcompatibility/php-compatibility=9.3.*" \
"wp-coding-standards/wpcs=2.1.*" \
"dealerdirect/phpcodesniffer-composer-installer=0.5.*" \
"sirbrillig/phpcs-variable-analysis=2.7.*"

RUN npm -v
RUN composer -V
RUN gulp -v
RUN composer global show -i