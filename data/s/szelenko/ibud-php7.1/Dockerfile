FROM php:7.1-fpm-stretch

RUN useradd -m -u 1000 ibud

RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt-get upgrade -y
RUN apt-get install -y mc libicu-dev g++ libmagickwand-dev git wget

RUN yes | pecl install xdebug

RUN docker-php-ext-install bcmath
RUN docker-php-ext-install zip
RUN docker-php-ext-install pdo_mysql
RUN docker-php-ext-install mysqli
RUN docker-php-ext-install sockets
RUN docker-php-ext-install gd

RUN pecl install imagick redis
RUN docker-php-ext-enable imagick
RUN docker-php-ext-enable xdebug
RUN docker-php-ext-enable redis

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt install -y nodejs

COPY --from=composer:latest /usr/bin/composer /usr/bin/composer
