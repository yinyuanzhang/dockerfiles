FROM php:7.1-fpm

MAINTAINER tthd@163.com

RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng-dev \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd pdo_mysql mysqli

RUN pecl install redis  \
    && pecl install mongodb \
    && docker-php-ext-enable redis mongodb

STOPSIGNAL SIGQUIT

EXPOSE 9000
CMD ["php-fpm"]