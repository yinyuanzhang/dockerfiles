FROM php:apache

MAINTAINER Martin Aamodt & Mari Fjermestad

RUN apt-get update 
RUN apt-get install -y zlib1g-dev libmemcached-dev
RUN docker-php-ext-install mysqli && docker-php-ext-enable mysqli
RUN pecl install memcached
RUN docker-php-ext-enable memcached

COPY code/ /var/www/html/
COPY config.php /var/www/html

EXPOSE 80
