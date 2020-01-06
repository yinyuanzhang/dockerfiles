#//----------------------------------------------------------------------------
#// PHP7 FastCGI Server ( for KUSANAGI Runs on Docker )
#//----------------------------------------------------------------------------
FROM php:7.2.9-fpm-alpine3.7
MAINTAINER kusanagi@prime-strategy.co.jp

# Environment variable
ARG MYSQL_VERSION=10.1.32-r0
ARG APCU_VERSION=5.1.12
ARG APCU_BC_VERSION=1.0.4

RUN apk update \
	&& apk add --no-cache \
		libbz2 \
		gd \
		gettext \
		libxslt \
	&& apk add --no-cache --virtual .build-php \
		$PHPIZE_DEPS \
		mariadb=$MYSQL_VERSION \
		mariadb-dev=$MYSQL_VERSION \
		gd-dev \
		jpeg-dev \
		libpng-dev \
		libwebp-dev \
		libxpm-dev \
		zlib-dev \
		freetype-dev \
		bzip2-dev \
		libexif-dev \
		xmlrpc-c-dev \
		pcre-dev \
		gettext-dev \
		libxslt-dev \
	&& pecl install apcu-$APCU_VERSION \
	&& docker-php-ext-enable apcu \
	&& pecl install apcu_bc-$APCU_BC_VERSION \
	&& docker-php-ext-enable apc \
	&& docker-php-ext-install \
		mysqli \
		opcache \
		gd \
		bz2 \
		pdo pdo_mysql \
		bcmath exif gettext pcntl \
		soap sockets sysvsem sysvshm xmlrpc xsl zip \
	&& apk del .build-php \
	&& rm -f /usr/local/etc/php/conf.d/docker-php-ext-apc.ini \
	&& rm -f /usr/local/etc/php/conf.d/docker-php-ext-apcu.ini \
	&& rm -f /usr/local/etc/php/conf.d/docker-php-ext-opcache.ini \
	&& mkdir -p /etc/php.d/

COPY files/*.ini /usr/local/etc/php/conf.d/
COPY files/opcache*.blacklist /etc/php.d/
