FROM php:7.3-fpm-stretch

# SETTING ENVIRONMENT
ENV ENVIRONMENT docker

RUN apt-get update

RUN docker-php-ext-install pcntl

RUN pecl install ast-1.0.1
RUN echo extension=ast.so > /usr/local/etc/php/conf.d/docker-php-ext-ast.ini

# SANITIZE FOLDER STRUCTURE
RUN rm -r /var/www/html
WORKDIR /var/www
