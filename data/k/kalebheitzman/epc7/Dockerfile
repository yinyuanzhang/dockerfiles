# from https://www.drupal.org/docs/8/system-requirements/drupal-8-php-requirements
FROM php:7.1-apache

# Install Memcache
RUN apt-get update && apt-get install -y libz-dev libmemcached-dev
RUN pecl install memcached

# Install upload progress
# RUN pecl install uploadprogress

# set memcache settings
RUN { \
		echo 'extension=memcached.so'; \
	} > /usr/local/etc/php/conf.d/memcached.ini

# install the PHP extensions we need
RUN set -ex; \
	\
	if command -v a2enmod; then \
		a2enmod rewrite; \
		a2enmod headers; \
	fi; \
	\
	savedAptMark="$(apt-mark showmanual)"; \
	\
	apt-get update; \
	apt-get install -y --no-install-recommends \
		libjpeg-dev \
		libpng-dev \
		libpq-dev \
	; \
	\
	docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr; \
	docker-php-ext-install -j "$(nproc)" \
		gd \
		opcache \
		pdo_mysql \
		pdo_pgsql \
		zip \
		sockets \
	; \
	\
# reset apt-mark's "manual" list so that "purge --auto-remove" will remove all build dependencies
	apt-mark auto '.*' > /dev/null; \
	apt-mark manual $savedAptMark; \
	ldd "$(php -r 'echo ini_get("extension_dir");')"/*.so \
		| awk '/=>/ { print $3 }' \
		| sort -u \
		| xargs -r dpkg-query -S \
		| cut -d: -f1 \
		| sort -u \
		| xargs -rt apt-mark manual; \
	\
	apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false; \
	rm -rf /var/lib/apt/lists/*

# set recommended PHP.ini settings
# see https://secure.php.net/manual/en/opcache.installation.php
RUN { \
		echo 'opcache.memory_consumption=128'; \
		echo 'opcache.interned_strings_buffer=8'; \
		echo 'opcache.max_accelerated_files=4000'; \
		echo 'opcache.revalidate_freq=60'; \
		echo 'opcache.fast_shutdown=1'; \
		echo 'opcache.enable_cli=1'; \
	} > /usr/local/etc/php/conf.d/opcache-recommended.ini

# Copy configuration files to the image
COPY ./app/config/apache.conf /etc/apache2/sites-enabled/000-default.conf
COPY ./app/config/php.ini /usr/local/etc/php/conf.d/php.ini

# Set the Drush Launcher version.
ENV DRUSH_LAUNCHER_VERSION 0.6.0

# Install Drush 8 with the phar file.
# Install Dependencies
RUN apt-get update && apt-get install -y \
  curl \
  git \
  mysql-client \
  unzip \
  wget

# Install Drush
RUN wget -O drush.phar "https://github.com/drush-ops/drush-launcher/releases/download/$DRUSH_LAUNCHER_VERSION/drush.phar" && \
	chmod +x drush.phar && \
	mv drush.phar /usr/local/bin/drush

# Set the working directory
WORKDIR /var/www/html

# https://www.drupal.org/node/3060/release
# ENV DRUPAL_VERSION 7.64
# ENV DRUPAL_MD5 bbb3c4d8c2cba35c48380d34f122f750

# RUN curl -fSL "https://ftp.drupal.org/files/projects/drupal-${DRUPAL_VERSION}.tar.gz" -o drupal.tar.gz \
# 	&& echo "${DRUPAL_MD5} *drupal.tar.gz" | md5sum -c - \
# 	&& tar -xz --strip-components=1 -f drupal.tar.gz \
# 	&& rm drupal.tar.gz \
# 	&& chown -R www-data:www-data sites modules themes

# vim:set ft=dockerfile:

COPY ./app/web /var/www/html