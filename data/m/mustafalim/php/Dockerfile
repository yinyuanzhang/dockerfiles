FROM php:7.0.33-fpm

LABEL maintainer="Mustafa Salim <mustafalim225@gmail.com>"

# install dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        apt-utils \
        apt-transport-https \
        gnupg \
        libpq-dev \
        zlib1g-dev \
        libicu-dev  \
        libbz2-dev \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng-dev \
        libmemcached-dev \
        zlib1g-dev\
        libxrender1 \
        libfontconfig1 \
        libxext6 \
        libzip-dev \
        libmagickwand-dev \
        git \
        vim

# core extension
RUN docker-php-ext-install -j$(nproc) bcmath bz2 exif intl mysqli opcache pdo_mysql pdo_pgsql sockets zip

# gd extension
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd

# redis, memcached, xdebug & imagick extension
RUN pecl install redis-4.3.0 memcached-3.1.3 xdebug-2.7.2 imagick-3.4.4 \
    && docker-php-ext-enable redis memcached xdebug imagick

# sqlsrv dependencies
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/9/prod.list \
        > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y --no-install-recommends \
        unixodbc-dev \
        msodbcsql17

# sqlsrv extension
RUN pecl install sqlsrv-5.3.0 pdo_sqlsrv-5.3.0 \
    && docker-php-ext-enable sqlsrv pdo_sqlsrv

# composer
RUN curl --silent --fail --location --retry 3 --output /tmp/installer.php \
    --url https://raw.githubusercontent.com/composer/getcomposer.org/cb19f2aa3aeaa2006c0cd69a7ef011eb31463067/web/installer \
    && php -r " \
        \$signature = '48e3236262b34d30969dca3c37281b3b4bbe3221bda826ac6a9a62d6444cdb0dcd0615698a5cbe587c3f0fe57a54d8f5'; \
        \$hash = hash('sha384', file_get_contents('/tmp/installer.php')); \
        if (! hash_equals(\$signature, \$hash)) { \
            unlink('/tmp/installer.php'); \
            echo 'Integrity check failed, installer is either corrupt or worse.' . PHP_EOL; \
            exit(1); \
        }" \
    && php /tmp/installer.php --no-ansi --install-dir=/usr/bin --filename=composer --version=1.8.5 \
    && composer --ansi --version --no-interaction \
    && rm -f /tmp/installer.php

# clear cache
RUN apt-get clean \
    && apt-get autoremove --purge \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# mount point
VOLUME /var/www

# working directory
WORKDIR /var/www
