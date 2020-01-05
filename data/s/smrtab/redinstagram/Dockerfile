FROM php:7.0-fpm

#Own PHP config
COPY ./__build/php.ini /usr/local/etc/php

#Should copy app into the work folder
COPY ./application /redinstagram

EXPOSE 9000

ENV COMPOSER_ALLOW_SUPERUSER 1

# Install required
RUN apt-get update  \
	&& apt-get install -y --no-install-recommends \
	git \
	wget \
	zip \
	unzip \
	libpq-dev
	
# Install PHP extensions and Composer
RUN docker-php-ext-install pdo_pgsql pgsql \
	&& curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

WORKDIR /redinstagram

#Set user and group to folder recoursively
RUN mkdir -p /storage/app/public  \
	&& mkdir -p /storage/framework/cache && mkdir /storage/framework/sessions && mkdir /storage/framework/testing && mkdir /storage/framework/views \
	&& mkdir -p /storage/logs \
	&& chown -R www-data:www-data ../redinstagram \
	&& chmod -R 777 /storage

USER www-data
	
RUN /usr/local/bin/composer install --no-ansi --no-dev --no-interaction --no-progress --no-scripts --optimize-autoloader
	






	

