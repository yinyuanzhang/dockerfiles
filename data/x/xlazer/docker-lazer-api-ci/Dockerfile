FROM php:7.2-alpine3.8

RUN apk add --no-cache \
        libssl1.0 \
	&& apk add --no-cache --virtual .persistent-deps \
		ca-certificates \
		curl \
		git \
		gmp \
		icu-libs \
		zlib

ENV APCU_VERSION 5.1.9

RUN set -xe \
	&& apk add --no-cache --virtual .build-deps \
		$PHPIZE_DEPS \
		gmp-dev \
		icu-dev \
		zlib-dev \
		libxml2-dev \
	&& docker-php-ext-install \
		bcmath \
		gmp \
		intl \
		zip \
		soap \
	&& pecl install \
		apcu-$APCU_VERSION \
		ds \
		mongodb \
	&& docker-php-ext-enable --ini-name 05-opcache.ini opcache \
	&& docker-php-ext-enable --ini-name 20-apcu.ini apcu \
	&& docker-php-ext-enable \
		ds \
		mongodb \
	&& apk del .build-deps

COPY install-composer.sh /usr/local/bin/docker-app-install-composer
RUN chmod +x /usr/local/bin/docker-app-install-composer

RUN set -xe \
	&& apk add --no-cache --virtual .fetch-deps \
		openssl \
	&& docker-app-install-composer \
	&& mv composer.phar /usr/local/bin/composer \
	&& apk del .fetch-deps

# https://getcomposer.org/doc/03-cli.md#composer-allow-superuser
ENV COMPOSER_ALLOW_SUPERUSER 1

ENV COMPOSER_HOME /root/.composer
ENV PATH $PATH:$COMPOSER_HOME/vendor/bin

COPY composer.json /root/.composer
COPY php.ini /usr/local/etc/php/

RUN composer global update --prefer-dist --no-progress --no-suggest --optimize-autoloader --classmap-authoritative \
	&& composer clear-cache
