FROM php:7.0-apache

WORKDIR /tmp

RUN apt-get update -y && \
    apt-get install -y curl git unzip && \
    curl -sS https://getcomposer.org/installer | php && \
    mv composer.phar /usr/local/bin/composer && \
    composer self-update

RUN curl -sL https://deb.nodesource.com/setup_4.x | bash - && \
    apt install -y nodejs && \
    npm install -g bower

RUN a2enmod rewrite
RUN docker-php-ext-install pdo pdo_mysql

WORKDIR /var/www