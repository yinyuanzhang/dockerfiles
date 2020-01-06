FROM php:5.6-fpm

RUN apt-get update -y && apt-get install -y libmcrypt-dev git zlib1g-dev

RUN docker-php-ext-install mbstring
RUN docker-php-ext-install mcrypt
RUN docker-php-ext-install bcmath
RUN docker-php-ext-install zip
RUN docker-php-ext-install pcntl

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/ --filename=composer

# Install composer package "Laravel installer"
RUN composer global require "laravel/installer" && PATH=$PATH:/root/.composer/vendor/bin

RUN mkdir -p /data

WORKDIR /data
