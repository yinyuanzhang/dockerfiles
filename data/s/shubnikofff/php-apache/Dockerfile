FROM php:5-apache

MAINTAINER Shubnikov Alexey

COPY ./icu_57.1-1_amd64.deb /tmp/icu_57.1-1_amd64.deb

RUN apt-get update && apt-get -y install \
	git \
	libssl-dev \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    && dpkg -i /tmp/icu_57.1-1_amd64.deb && rm /tmp/icu_57.1-1_amd64.deb \

    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \

    && docker-php-ext-install -j$(nproc) \
       gd \
       intl \
       pdo_mysql \
       zip \

#Install MongoDB Xdebug
    && pecl install mongodb xdebug \
    && docker-php-ext-enable mongodb \

#Install Composer
    && curl -sS https://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer \
    && composer global require "fxp/composer-asset-plugin:^1.2.0" \

#Enable Apache rewrite module
    && a2enmod rewrite

