FROM php:7.0-fpm

ENV COMPOSER_ALLOW_SUPERUSER 1

RUN apt-get update && apt-get install -y \
    libcurl3-dev \
    zlib1g-dev \
    libicu-dev \
    libzzip-dev \
    g++ \
    git \
    unzip

RUN docker-php-ext-configure intl

RUN docker-php-ext-install intl json zip curl

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/ --filename=composer

RUN composer global require hirak/prestissimo

RUN echo "Europe/Paris" > /etc/timezone

EXPOSE 9000