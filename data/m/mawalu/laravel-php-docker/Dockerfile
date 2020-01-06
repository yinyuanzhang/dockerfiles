FROM php:7.2-fpm

MAINTAINER Codelayer <docker@codelayer.de>

RUN apt-get update && \
  apt-get install -y --no-install-recommends libmagickwand-dev zip curl libpng-dev libgd-dev netcat libnss3 libgconf-2-4 zlib1g-dev libicu-dev libpq-dev libxml2-dev libpng-dev libjpeg62-turbo-dev libfreetype6-dev libwebp-dev libxpm-dev iproute2 && \
  docker-php-ext-configure intl && \
  docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ && \
  docker-php-ext-install zip intl pdo_pgsql soap xml gd bcmath exif pcntl && \
  pecl install pecl install imagick-3.4.3 && \
  docker-php-ext-enable bcmath imagick

RUN echo "memory_limit=1024M" > /usr/local/etc/php/conf.d/memory-limit.ini

