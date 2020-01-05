FROM php:7.0-apache

RUN apt-get update && apt-get install -y \
    libpng-dev \
 && docker-php-ext-configure gd \
 && docker-php-ext-install gd \
 && docker-php-ext-configure pdo_mysql \
 && docker-php-ext-install pdo_mysql \
 && docker-php-ext-configure mysqli \
 && docker-php-ext-install mysqli \
 && a2enmod rewrite \
 && pecl install xdebug \
 && echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \
 && echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini \
 && echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/xdebug.ini \
 && echo "xdebug.remote_connect_back=1" >> /usr/local/etc/php/conf.d/xdebug.ini
