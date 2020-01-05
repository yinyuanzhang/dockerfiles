FROM php:5.6-apache

RUN apt-get update \
 && apt-get install -y git zlib1g-dev libicu-dev g++ \
 && docker-php-ext-configure intl \
 && docker-php-ext-install pdo pdo_mysql zip intl \
 && a2enmod rewrite \
 && curl -sS https://getcomposer.org/installer \
  | php -- --install-dir=/usr/local/bin --filename=composer

RUN docker-php-ext-install zip

WORKDIR /var/www/html
