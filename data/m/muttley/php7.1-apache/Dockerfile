FROM php:7.1-apache

RUN groupadd -g 600 webmgr
RUN useradd -u 600 -g 600 webmgr

RUN apt-get update && apt-get install -y \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libmcrypt-dev \
    libpng12-dev \
    libmemcached-dev \
    zlib1g-dev \
    libltdl7 \
    libltdl-dev \
    libpq-dev \
    libsqlite3-dev \
    git \
    curl \
    libcurl3-dev \
    rsyslog \
    cron \
    supervisor \
    unzip \
    libicu-dev \
    --no-install-recommends \
    && docker-php-ext-install -j$(nproc) iconv mcrypt pdo_mysql pdo_pgsql pdo_sqlite zip curl\
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd

RUN pecl install apcu memcached mongodb redis \
	&& docker-php-ext-enable apcu memcached mongodb redis

RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/log/supervisor

RUN echo "date.timezone = Europe/Rome" >> /etc/php.ini
RUN curl -sS https://getcomposer.org/installer -o composer-setup.php
RUN php composer-setup.php --install-dir=/bin --filename=composer

RUN a2enmod ssl rewrite

ENV APACHE_RUN_USER webmgr
ENV APACHE_RUN_GROUP webmgr

RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf
RUN echo "export FORCE_HTTPS=\${HTTPS}" >> /etc/apache2/envvars

VOLUME [ "/var/www/html","/etc/apache2/sites-enabled/" ]
WORKDIR /var/www/html
