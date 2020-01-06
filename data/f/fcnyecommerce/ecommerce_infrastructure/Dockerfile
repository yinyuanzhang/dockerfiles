FROM php:7.3.10-apache-stretch
MAINTAINER Courtney <courtney@sellry.com>

RUN requirements="libmcrypt-dev libmcrypt4 libcurl3-dev libfreetype6 libjpeg62-turbo libwebp6 libfreetype6-dev libjpeg62-turbo-dev libwebp-dev mysql-client imagemagick libxml2-dev libpng-dev gnupg curl git wget vim net-tools apt-utils procps libmagickwand-6.q16-dev" \
    && apt-get update && apt-get upgrade -y && apt-get install -y $requirements && rm -rf /var/lib/apt/lists/* \
    && docker-php-ext-install pdo_mysql \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ --with-png-dir --with-zlib-dir --with-webp-dir=/usr/include/ \
    && docker-php-ext-install gd \
    && docker-php-ext-install mbstring \
    && docker-php-ext-install soap \
    && docker-php-ext-install opcache \
    && pecl install imagick-3.4.4 \
    && pecl install lzf-1.6.7 \
    && docker-php-ext-enable imagick lzf \
    && requirementsToRemove="libpng-dev libmcrypt-dev libcurl3-dev libfreetype6-dev libjpeg62-turbo-dev libwebp-dev" \
    && apt-get purge --auto-remove -y $requirementsToRemove

RUN mkdir -p /tmp/redis                 \
    && cd /tmp/redis                    \
    && pecl download redis-5.0.2        \
    && tar xvzf redis-5.0.2.tgz         \
    && cd redis-5.0.2                   \
    && phpize                           \
    && ./configure --enable-redis-lzf   \
    && make                             \
    && make install                     \
    && docker-php-ext-enable redis      \
    && rm -rf /tmp/redis

ENV N98_MAGERUN_URL https://files.magerun.net/n98-magerun.phar

RUN curl -o /usr/local/bin/n98-magerun $N98_MAGERUN_URL \
    && chmod +x /usr/local/bin/n98-magerun

# New Relic
RUN echo 'deb http://apt.newrelic.com/debian/ newrelic non-free' | tee /etc/apt/sources.list.d/newrelic.list \
    && wget -O- https://download.newrelic.com/548C16BF.gpg | apt-key add - \
    && DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y newrelic-php5 && rm -rf /var/lib/apt/lists/*

RUN a2dissite 000-default \
    && a2disconf other-vhosts-access-log \
    && a2enmod rewrite

RUN usermod -u 1000 www-data

WORKDIR /var/www/htdocs
