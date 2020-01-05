FROM php:7.1-apache
MAINTAINER Bennet Klarhoelter <bennet.klarhoelter@twofour.de>

ENV APACHE_DOCUMENT_ROOT /var/www/public_html
RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-available/*.conf
RUN sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf

RUN apt-get update && apt-get install -y libmemcached-dev zlib1g-dev \
    && pecl install memcached-3.0.3 \
    && docker-php-ext-enable memcached

RUN docker-php-ext-install pdo pdo_mysql

RUN apt-get update && apt-get install -y libmagickwand-dev imagemagick \
    && yes "" | pecl install imagick-3.4.3 \
    && docker-php-ext-enable imagick

RUN docker-php-ext-install opcache
RUN touch /var/www/.opcache

RUN a2enmod rewrite
COPY build/php.ini /usr/local/etc/php/

ARG CI_BUILD_NAME
ENV YII_ENV production

# Set the working directory to the app directory
WORKDIR /var/www

# Copy the application files (needed for production)
COPY ./app /var/www

COPY ./build/bin/* /usr/local/bin

RUN cp configs/env.php.dist configs/env.php
RUN cp configs/env-local-db.php.dist configs/env-local-db.php

#RUN ./init --overwrite=All --env=$CI_BUILD_NAME

CMD init; apache2-foreground
