FROM php:7.1

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/bin --filename=composer

RUN pecl install xdebug

RUN docker-php-ext-enable xdebug

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    git \
    unzip
