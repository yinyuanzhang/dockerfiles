FROM php:7.3.11-alpine

# Set default folder
WORKDIR /app

# Add project files in /app folder
ADD ./ /app

# Install dependencies
RUN apk update &&\
    apk add git libzip-dev

# Install mysqli php driver
RUN docker-php-ext-install mysqli &&\
    docker-php-ext-install pdo_mysql &&\
    docker-php-ext-configure zip --with-libzip=/usr/include &&\
    docker-php-ext-install zip

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php

# Install app
RUN php composer.phar install

ENTRYPOINT ["/app/start.sh"]
