FROM php:7.1-fpm

RUN apt-get update \
    && apt-get install -y nodejs zlib1g-dev

RUN apt-get -y --force-yes install yasm ffmpeg

RUN docker-php-ext-install pdo_mysql
RUN docker-php-ext-install opcache
RUN docker-php-ext-install zip

RUN ln -s /usr/bin/nodejs /usr/bin/node
