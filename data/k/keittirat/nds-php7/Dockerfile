# FOR API USAGE ONLY #
FROM php:7.1.8-fpm-alpine

EXPOSE 9000
WORKDIR /var/www/html

RUN apk update && apk add --no-cache \
		$PHPIZE_DEPS \
		openssl-dev \
        icu-dev \
        gettext-dev \
        bash

RUN docker-php-ext-install intl mysqli pdo_mysql gettext json zip
RUN pecl channel-update pecl.php.net
RUN pecl install mongodb-1.4.4
RUN docker-php-ext-enable mongodb
RUN docker-php-source delete