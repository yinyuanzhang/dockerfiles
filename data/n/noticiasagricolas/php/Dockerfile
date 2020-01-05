FROM php:7.3.12-fpm-alpine

# Use the default production configuration
RUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"

ENV MEMCACHED_DEPS zlib-dev libmemcached-dev cyrus-sasl-dev
ENV GD_DEPS libjpeg-turbo-dev libpng-dev libwebp-dev
RUN set -xe \
  && apk add --no-cache --update \
    libjpeg-turbo \
    libmemcached-libs \
    libpng \
    libwebp \
    zip \
    zlib \
  && apk add --no-cache --update --virtual .phpize-deps $PHPIZE_DEPS \
  && apk add --no-cache --update --virtual .memcached-deps $MEMCACHED_DEPS \
  && apk add --no-cache --update --virtual .gd-deps $GD_DEPS \
  && echo $PHPIZE_DEPS \
  && pecl install \
    memcached \
    igbinary \
  && docker-php-ext-install \
    pdo_mysql \
    gd \
  && docker-php-ext-enable \
    igbinary \
    memcached \
    opcache \
  && rm -rf /usr/share/php7 \
  && rm -rf /tmp/* \
  && apk del .memcached-deps .phpize-deps .gd-deps

# Add Composer
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar /usr/local/bin/composer
