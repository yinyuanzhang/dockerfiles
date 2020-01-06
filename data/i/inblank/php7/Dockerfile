FROM php:7.0-apache
RUN apt-get update && apt-get install -y \
        libapache2-mod-rpaf \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng-dev \
        libmemcached-dev \
        libicu-dev \
        libpq5 \
        libpq-dev \
        libssh2-1 \
        libssh2-1-dev \
        libssl-dev \
        librabbitmq-dev \
        libxml2-dev \
        libxslt1.1 \
        libxslt1-dev \
        unzip \
        git \
    && a2enmod rewrite rpaf \
    && docker-php-ext-install -j$(nproc) bcmath pdo_mysql mysqli mcrypt intl zip soap xsl pdo_pgsql exif opcache \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd \
    && pecl install memcached \
    && pecl install redis \
    && pecl install mongodb \
    && pecl install amqp \
    && pecl install ssh2-1.1.2 \
    && docker-php-ext-enable memcached redis mongodb amqp ssh2 \
    && apt-get remove libpq-dev -y \
    && apt-get autoremove -y
