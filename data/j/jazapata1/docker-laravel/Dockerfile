FROM php:7.1
MAINTAINER Jesus Zapata <chuchocorleone@gmail.com>

RUN apt-get update -yqq && \
    apt-get install git libcurl4-gnutls-dev libicu-dev libvpx-dev libjpeg-dev libpng-dev libxpm-dev zlib1g-dev libfreetype6-dev libxml2-dev libexpat1-dev libbz2-dev libgmp3-dev libldap2-dev unixodbc-dev libpq-dev libsqlite3-dev libaspell-dev libsnmp-dev libpcre3-dev libtidy-dev -yqq

RUN docker-php-ext-install mbstring pdo_mysql curl json intl gd xml zip bz2

RUN pecl install xdebug && \
    docker-php-ext-enable xdebug

RUN curl -sS https://getcomposer.org/installer | php && \
    mv composer.phar /usr/local/bin/composer  && \
    composer global require "laravel/installer"
