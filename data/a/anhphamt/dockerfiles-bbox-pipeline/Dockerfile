FROM php:apache

MAINTAINER anhphamt.la@gmail.com

RUN apt-get update && apt-get install -y git libssl-dev

RUN 	   pecl install mongodb \
	&& pecl install xdebug-beta \
	&& docker-php-ext-enable xdebug

RUN echo "extension=mongodb.so" > $PHP_INI_DIR/conf.d/mongodb.ini

RUN     	docker-php-ext-install zip \
	 && 	docker-php-ext-install mbstring

RUN apt-get -qq install git-ftp


ENV COMPOSER_VERSION 1.0.0-alpha10

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer --version=${COMPOSER_VERSION}
