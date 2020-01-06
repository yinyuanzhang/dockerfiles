FROM php:7.3-fpm-alpine
RUN apk update && apk add ssmtp libpng-dev libjpeg-turbo-dev
RUN docker-php-ext-configure gd --with-png-dir=/usr/include/ --with-jpeg-dir=/usr/include/
RUN docker-php-ext-install mysqli pdo_mysql gd
