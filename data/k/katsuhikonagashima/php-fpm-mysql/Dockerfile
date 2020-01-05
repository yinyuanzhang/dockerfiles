FROM php:7.2-fpm-stretch

LABEL maintainer="Katsuhiko Nagashima <katsuhiko.nagashima@gmail.com>"

RUN apt-get update && apt-get install -y git zlib1g-dev zip unzip
RUN docker-php-ext-install zip

RUN docker-php-ext-install pdo_mysql
