FROM php:5.6-apache

RUN apt-get update && apt-get install -y --no-install-recommends \
  imagemagick \
  libmagickwand-dev \
  libmagickcore-dev \
  libssl-dev \
  libxml2-dev \
  libmcrypt-dev \
  vim \
  gnupg2 \
  libcap2-bin \
  wget \
  zip \
  && rm -rf /var/lib/apt/lists/* && apt-get clean

RUN \
  docker-php-ext-install soap && \
  docker-php-ext-install zip

RUN \
  ln -s /etc/alternatives/convert /usr/local/bin/convert && \
  ln -s /usr/lib/x86_64-linux-gnu/ImageMagick-6.9.7/bin-q16/MagickWand-config /usr/local/bin/MagickWand-config

RUN yes "" | pecl install \
  igbinary-2.0.1 \
  imagick-3.4.3 \
  mongo-1.6.12 \
  redis-2.2.5

RUN \
  docker-php-ext-enable igbinary && \
  docker-php-ext-enable imagick && \
  docker-php-ext-enable mongo && \
  docker-php-ext-enable opcache && \
  docker-php-ext-enable redis && \
  docker-php-ext-install mcrypt

# Apache Modules
RUN a2enmod \
  rewrite \
  vhost_alias \
  remoteip

RUN setcap CAP_NET_BIND_SERVICE=+eip /usr/sbin/apache2

# New Relic
RUN echo 'deb http://apt.newrelic.com/debian/ newrelic non-free' | tee /etc/apt/sources.list.d/newrelic.list
RUN wget -O- https://download.newrelic.com/548C16BF.gpg | apt-key add -
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get -y install newrelic-php5 && rm -rf /var/lib/apt/lists/* && apt-get clean
RUN yes "" | newrelic-install install

# Copy Configs
COPY files/vhost.conf /etc/apache2/sites-available/000-default.conf
COPY files/apache2.conf /etc/apache2/apache2.conf

COPY files/php.ini /usr/local/etc/php/
COPY files/docker-php-ext-opcache.ini /usr/local/etc/php/conf.d/docker-php-ext-opcache.ini
COPY files/docker-php-ext-newrelic.ini /usr/local/etc/php/conf.d/newrelic.ini

ARG APACHE_MaxClients=20
ENV APACHE_MaxClients=$APACHE_MaxClients
