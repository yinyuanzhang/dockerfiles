FROM php:5.6.34-apache

RUN apt-get update

RUN apt-get install -y libfreetype6-dev libjpeg62-turbo-dev
RUN apt-get install -y libmcrypt-dev

RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ && \
    docker-php-ext-install gd

RUN docker-php-ext-configure mcrypt && docker-php-ext-install mcrypt

RUN docker-php-ext-install mysql mysqli

RUN docker-php-ext-install pdo pdo_mysql

RUN docker-php-ext-install zip


# Clean up
RUN \
  apt-get autoremove -y && \
  apt-get autoclean && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

