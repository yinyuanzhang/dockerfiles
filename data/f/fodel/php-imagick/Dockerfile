FROM php:5.6-apache

MAINTAINER WajidAbid <wajid@fo-del.com>

RUN \
  echo "deb http://archive.ubuntu.com/ubuntu trusty-backports main restricted universe multiverse" >> /etc/apt/sources.list

RUN apt-get update
RUN apt-get --yes install php-pear
RUN pear config-set php_ini /usr/local/etc/php/5.6/php.ini
RUN apt-get --yes install libmagickwand-dev libmagickcore-dev
RUN pecl install imagick

RUN apt-get update \
    && apt-get install -y \
    && docker-php-ext-install mysql \
    && docker-php-ext-install mysqli \
        && docker-php-ext-install gd
