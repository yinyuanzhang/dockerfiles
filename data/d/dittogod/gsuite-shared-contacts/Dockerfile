FROM php:7.1.8-apache

MAINTAINER DittoGod

COPY . /srv/app
COPY .docker/vhost.conf /etc/apache2/sites-available/000-default.conf
COPY --from=composer:1.5 /usr/bin/composer /usr/bin/composer

WORKDIR /srv/app/
#RUN apt-get update
#RUN apt-get upgrade -y
RUN chown -R www-data:www-data /srv/app \
    && a2enmod rewrite
RUN chown -R root:root /srv/app/app
RUN service apache2 restart