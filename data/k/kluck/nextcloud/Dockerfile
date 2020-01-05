FROM php:7.0-apache

RUN apt-get update && apt-get install -y \
	bzip2 \
	libcurl4-openssl-dev \
	libfreetype6-dev \
	libicu-dev \
	libjpeg-dev \
	libmcrypt-dev \
	libmemcached-dev \
	libpng12-dev \
	libpq-dev \
	libxml2-dev \
	aria2 \
	&& rm -rf /var/lib/apt/lists/*

#gpg key from https://nextcloud.com/nextcloud.asc
RUN curl -fsSL -o nextcloud.asc \
        "https://nextcloud.com/nextcloud.asc" \
    && gpg --import nextcloud.asc \
    && rm nextcloud.asc

# https://doc.owncloud.org/server/8.1/admin_manual/installation/source_installation.html#prerequisites
RUN docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
	&& docker-php-ext-install gd intl mbstring mcrypt opcache pdo_pgsql pgsql zip

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

# PECL extensions
RUN pecl install APCu \
	&& docker-php-ext-enable apcu

RUN a2enmod rewrite

ENV NEXTCLOUD_VERSION 10.0.0
VOLUME /var/www/html

RUN curl -fsSL -o nextcloud.tar.bz2 \
		"https://download.nextcloud.com/server/releases/nextcloud-${NEXTCLOUD_VERSION}.tar.bz2" \
	&& curl -fsSL -o nextcloud.tar.bz2.asc \
		"https://download.nextcloud.com/server/releases/nextcloud-${NEXTCLOUD_VERSION}.tar.bz2.asc" \
	&& gpg --verify nextcloud.tar.bz2.asc \
	&& tar -xjf nextcloud.tar.bz2 -C /usr/src/ \
	&& rm nextcloud.tar.bz2 nextcloud.tar.bz2.asc

COPY docker-entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["apache2-foreground"]
