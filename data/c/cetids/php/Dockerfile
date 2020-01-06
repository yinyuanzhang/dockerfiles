FROM php:7.0-fpm
MAINTAINER xxz <xxz@cetids.com>

# Let the conatiner know that there is no tty
ENV DEBIAN_FRONTEND noninteractive


RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng12-dev \
        libmcrypt-dev \
        libpng12-dev \
        libcurl4-openssl-dev \
        libsqlite3-dev \
	libssl-dev \
        nano \
        bzip2 \
    && docker-php-ext-install -j$(nproc) iconv mcrypt zip pdo pdo_mysql mysqli \
    && docker-php-ext-configure gd --with-png-dir=/usr/include --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd 



RUN { \
		echo 'opcache.memory_consumption=128'; \
		echo 'opcache.interned_strings_buffer=8'; \
		echo 'opcache.max_accelerated_files=4000'; \
		echo 'opcache.revalidate_freq=60'; \
		echo 'opcache.fast_shutdown=1'; \
		echo 'opcache.enable_cli=1'; \
	} > /usr/local/etc/php/conf.d/opcache-recommended.ini


COPY ./php7.0/fpm/php.ini /usr/local/etc/php/php.ini
COPY ./php7.0/fpm/www.conf /usr/local/etc/php-fpm.d/www.conf
