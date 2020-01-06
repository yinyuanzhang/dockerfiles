FROM php:7.1.5-apache
RUN apt-get update && apt-get install -y \
        libapache2-mod-rpaf \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
        libmemcached-dev \
        libicu-dev \
        libpq5 \
        libpq-dev \
    && a2enmod rewrite rpaf \
    && docker-php-ext-install -j$(nproc) pdo_mysql mysqli mcrypt intl pdo_pgsql \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd \
    && docker-php-ext-install zip \
    && pecl install memcached \
    && docker-php-ext-enable memcached \
    && apt-get remove libpq-dev -y \
    && apt-get autoremove -y
