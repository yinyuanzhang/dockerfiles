FROM php:7.3.2-fpm

RUN apt-get update && apt-get install -y zlib1g-dev libicu-dev libpq-dev libmemcached-dev curl wget sudo gnupg2

RUN docker-php-ext-install opcache
RUN docker-php-ext-install intl
RUN docker-php-ext-install mysqli
RUN docker-php-ext-install pdo_mysql
RUN wget -O- https://download.newrelic.com/548C16BF.gpg | sudo apt-key add
RUN echo "deb http://apt.newrelic.com/debian/ newrelic non-free" > /etc/apt/sources.list.d/newrelic.list
RUN apt-get update
RUN apt-get install -y newrelic-php5
RUN newrelic-install install

EXPOSE 9000
