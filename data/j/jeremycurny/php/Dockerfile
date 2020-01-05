FROM php:7.1-cli-alpine

MAINTAINER "Jeremy CURNY" <jeremy.curny.pro@gmail.com>

ENV COMPOSER_ALLOW_SUPERUSER 1

RUN apk update

RUN apk add --no-cache \
        bash curl git openrc rsync tree unzip zip \
        libxml2-dev \
    && rm -rf /var/cache/apk/*

RUN docker-php-ext-install \
    dom mbstring zip

RUN curl -sL -o /usr/local/bin/composer https://getcomposer.org/composer.phar \
    && chmod +x /usr/local/bin/composer
