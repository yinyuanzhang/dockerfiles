FROM php:7-fpm

RUN apt-get update && \
  apt-get -y install libxml2 zlib1g-dev unzip libzip-dev

RUN pecl install grpc
RUN docker-php-ext-enable grpc
RUN docker-php-ext-install bcmath

RUN apt-get clean all

# RUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"
