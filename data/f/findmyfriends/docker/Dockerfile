FROM php:fpm-alpine

ENV COMPOSER_ALLOW_SUPERUSER=1

RUN apk update \
	&& apk add --no-cache git postgresql-dev zip unzip zlib-dev g++ make autoconf libxslt-dev \
	&& docker-php-ext-install pdo_pgsql zip bcmath xsl \
	&& pecl install apcu \
	&& pecl install igbinary \
	&& pecl install redis \
	&& curl -sS https://getcomposer.org/installer | php && mv composer.phar /usr/local/bin/composer \
	&& curl -sSL https://github.com/xdebug/xdebug/archive/4ada850.zip -o /tmp/xdebug.zip \
		&& unzip /tmp/xdebug.zip -d /tmp \
		&& cd /tmp/xdebug-* \
		&& phpize \
		&& ./configure \
		&& make \
		&& make install \
		&& rm -rf /tmp/xdebug* \
	&& rm -rf /var/cache/apk/*
