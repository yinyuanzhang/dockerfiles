FROM php:5.6-apache

ENV ZURMO_VERSION "3.1.5"
ENV PHP_TIMEZONE "Australia/Sydney"

RUN apt-get update --no-install-recommends \
  && apt-get -yq upgrade --no-install-recommends \
  && apt-get -yq install --no-install-recommends \
    mysql-client \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libmcrypt-dev \
    libpng12-dev \
    libmemcached-dev \
    libxml2-dev \
    libc-client2007e-dev \
    libkrb5-dev \
    libcurl4-openssl-dev \
    wget \
    unzip \
  && docker-php-ext-configure imap --with-kerberos --with-imap-ssl \
  && pecl install memcache \
  && docker-php-ext-enable memcache \
  && docker-php-ext-install iconv mcrypt mbstring ctype soap imap curl pdo pdo_mysql zip \
  && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
  && docker-php-ext-install gd

RUN rm -R /var/www/html \
  && mkdir -p /var/www \
  && cd /var/www \
  && wget "http://bitbucket.org/zurmo/zurmo/get/$ZURMO_VERSION.zip"

RUN cd /var/www \
  && rm -R html \
  && unzip "$ZURMO_VERSION.zip" \
  && rm -f "$ZURMO_VERSION.zip" \
  && ls -l \
  && mv * temp \
  && mv temp/* ./ \
  && rm -Rf temp \
  && mv app html

COPY resources/ /
RUN chown -R www-data /var/www
VOLUME /var/www/
