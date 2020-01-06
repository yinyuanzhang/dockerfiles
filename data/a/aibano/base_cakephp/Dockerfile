#
# Base Image for Cakephp 2.8.x application. 2016
#


FROM php:7.0.2-apache

MAINTAINER Osama Alaiban, megdam@gmail.com

# Enable mod_rewrite
RUN a2enmod rewrite
# Enable mod_expires
RUN a2enmod expires
# Enable mod_filter
RUN a2enmod filter
# Enable mod_deflate
RUN a2enmod deflate

RUN usermod -u 1000 www-data
RUN apt-get update
RUN requirements="libmcrypt-dev g++ libicu-dev libmcrypt4 libicu52 libfreetype6-dev libjpeg62-turbo-dev libpng12-dev" \
    && apt-get install -y $requirements
RUN docker-php-ext-install pdo_mysql
RUN docker-php-ext-install mcrypt
RUN docker-php-ext-install mbstring
RUN docker-php-ext-install intl
RUN docker-php-ext-install calendar
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/
RUN docker-php-ext-install gd

## RUN requirementsToRemove="libmcrypt-dev g++ libicu-dev"

RUN curl -sSL https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer
RUN apt-get update && apt-get install -y zlib1g-dev git
RUN docker-php-ext-install zip
## RUN apt-get purge -y --auto-remove zlib1g-dev
## RUN rm -rf /var/lib/apt/lists/*
RUN php -m
