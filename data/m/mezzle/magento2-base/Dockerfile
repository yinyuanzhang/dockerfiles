FROM php:7.1-apache

RUN apt-get update -y && apt-get install -y libmcrypt-dev libxslt-dev \
    zlib1g-dev libjpeg-dev libpng-dev libfreetype6-dev \
    && docker-php-ext-install -j$(nproc) mcrypt \
    && docker-php-ext-install -j$(nproc) xsl \
    && docker-php-ext-install -j$(nproc) intl \
    && docker-php-ext-install -j$(nproc) pdo_mysql \
    && docker-php-ext-install -j$(nproc) soap \
    && docker-php-ext-install -j$(nproc) zip \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \
    --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd

RUN a2enmod rewrite
