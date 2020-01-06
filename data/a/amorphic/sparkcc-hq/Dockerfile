FROM php:7.2-apache

RUN \
  apt-get -y update && \
  apt-get install -y git && \
  apt-get clean

# Additional modules that we need.
RUN docker-php-ext-install mysqli
RUN a2enmod rewrite

COPY . /var/www/html
LABEL com.centurylinklabs.watchtower.enable="true"
