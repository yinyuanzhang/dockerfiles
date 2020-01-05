FROM php:7.1-fpm
COPY sources.list /etc/apt/sources.list

RUN apt-get update && apt-get install -y \
		libfreetype6-dev \
		libjpeg62-turbo-dev \
		libmcrypt-dev \
		libpng-dev \
	&& rm -rf /var/lib/apt/lists/* \
	&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
	&& docker-php-ext-install -j$(nproc) gd \
	&& docker-php-ext-install sockets shmop mcrypt gettext pdo pdo_mysql

RUN pecl install mongodb redis \
	&& docker-php-ext-enable mongodb redis

COPY loader-wizard.php /root/loader-wizard.php
COPY ioncube_loader_lin_7.1.so /usr/local/lib/php/extensions/no-debug-non-zts-20160303/ioncube_loader_lin_7.1.so
COPY docker-php-ext-ioncube.ini /usr/local/etc/php/conf.d/docker-php-ext-ioncube.ini
COPY php-custom.ini /usr/local/etc/php/conf.d/php-custom.ini
EXPOSE 8080
