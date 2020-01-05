FROM php:7.2-cli
MAINTAINER Thiago Pereira Rosa <thiagor@engineer.com>

RUN apt-get update
RUN apt-get install -y zip unzip git awscli

RUN pecl install xdebug mongodb \
    && docker-php-ext-enable xdebug mongodb

RUN docker-php-ext-install bcmath pdo_mysql exif

RUN curl --silent --show-error https://getcomposer.org/installer | php
RUN mv composer.phar composer
