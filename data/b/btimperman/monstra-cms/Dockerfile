FROM php:5.3-apache

RUN apt-get update && \
    apt-get install -y unzip wget && \
    wget -O monstra.zip https://github.com/Awilum/monstra-cms/releases/download/v3.0.1/monstra-3.0.1.zip && \
    unzip monstra.zip -d /var/www/html && \
    chmod -R a+rw /var/www/html && \
    rm monstra.zip && \
    a2enmod rewrite

VOLUME /var/www/html/storage

ADD php.ini /usr/local/etc/php

