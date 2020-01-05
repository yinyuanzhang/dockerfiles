FROM php:7.2-fpm
RUN apt-get update && apt-get install -y \
        libpng-dev \
        libjpeg62-turbo-dev \
        unzip \
    && docker-php-ext-install mysqli \
    && docker-php-ext-configure gd --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd
