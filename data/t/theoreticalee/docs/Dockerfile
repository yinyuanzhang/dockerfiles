FROM php:7.0-apache

RUN a2enmod rewrite

COPY config/apache/aws.conf /etc/apache2/sites-enabled/000-default.conf

RUN mkdir -p /usr/src/app

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN ln -fs /usr/share/zoneinfo/America/Los_Angeles /etc/localtime
RUN echo America/Los_Angeles > /etc/timezone

RUN ln -s /usr/src/app/web /var/www/html/quicksight
