FROM php:7.2-fpm

COPY 99fixbadproxy /etc/apt/apt.conf.d/99fixbadproxy

RUN apt-get clean \
    && apt-get update \
    && apt-get install -y \
        libfreetype6-dev \
        libicu-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng-dev \
        libxslt1-dev \
        libpcre3-dev \
        sudo \
    && docker-php-ext-configure \
        gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install \
        dom \
        gd \
        intl \
        mbstring \
        pdo_mysql \
        xsl \
        zip \
        soap \
        bcmath \
        opcache \
    && pecl config-set php_ini /usr/local/etc/php.ini \
    && pecl install redis \
    && pecl install xdebug \
    && docker-php-ext-enable redis xdebug

COPY php.ini /usr/local/etc/php
COPY zz-app.ini /usr/local/etc/php/conf.d
COPY zz-xdebug.ini /usr/local/etc/php/conf.d
COPY php-fpm.conf /usr/local/etc

WORKDIR /usr/share/src

CMD ["php-fpm", "-F"]