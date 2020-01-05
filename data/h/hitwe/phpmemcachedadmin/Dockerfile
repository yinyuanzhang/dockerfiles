FROM php:5.6-apache

MAINTAINER Marko OS

# Enable apache rewrite module
RUN ln -s /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-enabled/

# Copy PHP configuration file
COPY build/php.ini /usr/local/etc/php/

# Install utils
RUN apt-get update && apt-get install -y unzip curl nano git libmemcached-dev zlib1g-dev
RUN pecl install memcached-2.2.0
RUN docker-php-ext-enable memcached 

RUN curl -L https://github.com/elijaa/phpmemcachedadmin/archive/1.3.0.tar.gz -o /tmp/1.3.0.tar.gz \
    && tar xfz /tmp/1.3.0.tar.gz -C /tmp \
    && cp -r /tmp/phpmemcachedadmin-1.3.0/* /var/www/html/ \
    && rm  /var/www/html/Config/Memcache.sample.php

COPY build/Memcache.php /var/www/html/Config/

RUN chown -R  www-data:www-data /var/www/html \
    &&  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* 
