FROM php:7.3-fpm

MAINTAINER AttractGroup

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        libmemcached-dev \
        libz-dev \
        libjpeg-dev \
        libpng-dev \
        libfreetype6-dev \
        libssl-dev \
        libmcrypt-dev \
        git \
        mysql-client \
        libpq-dev \
        zlib1g-dev \
        libpng-dev \
        libicu-dev \
        supervisor \
        libssl-dev \
        libzip-dev \
        libc-client2007e-dev \
        libkrb5-dev

# Install the PHP pdo_mysql extention
RUN docker-php-ext-install pdo_mysql

RUN docker-php-ext-configure imap --with-imap-ssl --with-kerberos \
        && docker-php-ext-install imap \
        && docker-php-ext-install opcache \
        && docker-php-ext-configure gd --with-jpeg-dir=/usr/include/ --with-png-dir=/usr/include \
        && docker-php-ext-configure intl \
        && docker-php-ext-install -j$(nproc) gd \
        && docker-php-ext-install opcache \
        && docker-php-ext-install gettext \
        && docker-php-ext-install intl \
        && docker-php-ext-install exif \
        && docker-php-ext-install bcmath \
        && docker-php-ext-install mbstring


#####################################
# OpCahce
#####################################
RUN { \
		echo 'opcache.memory_consumption=128'; \
		echo 'opcache.interned_strings_buffer=8'; \
		echo 'opcache.max_accelerated_files=4000'; \
		echo 'opcache.revalidate_freq=60'; \
		echo 'opcache.fast_shutdown=1'; \
		echo 'opcache.enable_cli=1'; \
	} > /usr/local/etc/php/conf.d/opcache-recommended.ini

#####################################
# ZipArchive:
#####################################

RUN docker-php-ext-install zip && \
    docker-php-ext-enable zip

#####################################
# Composer:
#####################################

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

#####################################
# Set Timezone
#####################################

ARG TZ=UTC
ENV TZ ${TZ}
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
ENV COMPOSER_ALLOW_SUPERUSER 1
RUN composer global require "hirak/prestissimo:^0.3"