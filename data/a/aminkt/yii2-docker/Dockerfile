FROM alpine:3.10

MAINTAINER Amin Keshavarz <ak_1596@yahoo.com>

ENV PHP_INI_DIR /etc/php7
ENV PHP_VERSION 7

# persistent / runtime deps
RUN apk update && apk add --no-cache \
		ca-certificates \
		bash \
		curl \
		tar \
		xz \
		openssl \
		zip unzip \
		git \
		# Install php and php extensions
        php$PHP_VERSION \
        php$PHP_VERSION-fpm \
        php$PHP_VERSION-opcache \
        php$PHP_VERSION-redis \
        php$PHP_VERSION-zlib \
        php$PHP_VERSION-mysqli \
        php$PHP_VERSION-pdo \
        php$PHP_VERSION-pdo_sqlite \
        php$PHP_VERSION-pdo_mysql \
        php$PHP_VERSION-intl \
        php$PHP_VERSION-curl \
        php$PHP_VERSION-gd \
        php$PHP_VERSION-mbstring \
        php$PHP_VERSION-json \
        php$PHP_VERSION-phar \
        php$PHP_VERSION-dom \
        php$PHP_VERSION-xml \
        php$PHP_VERSION-xmlwriter \
        php$PHP_VERSION-tokenizer \
        php$PHP_VERSION-ctype \
        php$PHP_VERSION-apcu \
        php$PHP_VERSION-fileinfo \
        php$PHP_VERSION-zip && \
        rm -rf /var/cache/apk/* && \
        # ensure www-data user exists
        set -eux; \
        	addgroup -g 82 -S www-data; \
        	adduser -u 82 -D -S -G www-data www-data && \
        # Install composer
        curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Set php configuration mountable
VOLUME ["$PHP_INI_DIR/conf.d", "$PHP_INI_DIR/php-fpm.d"]

# This entrypoint can override in child docker file.
ENTRYPOINT ["/bin/bash"]