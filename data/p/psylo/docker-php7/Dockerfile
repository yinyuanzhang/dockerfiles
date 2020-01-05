FROM php:7.1.13-fpm
MAINTAINER Laurent Masforne <laurent.masforne@gmail.com>
ENV PHP_APCU_VERSION 5.1.8
RUN apt-get update \
    && apt-get install -y \
        libicu-dev \
        zlib1g-dev \
        xvfb libfontconfig wkhtmltopdf \
    && apt-get install git zip libpng-dev wget sqlite3 libsqlite3-dev -yqq \
    && docker-php-source extract \
    && curl -L -o /tmp/apcu-$PHP_APCU_VERSION.tgz https://pecl.php.net/get/apcu-$PHP_APCU_VERSION.tgz \
    && tar xfz /tmp/apcu-$PHP_APCU_VERSION.tgz \
    && rm -r \
        /tmp/apcu-$PHP_APCU_VERSION.tgz \
    && mv apcu-$PHP_APCU_VERSION /usr/src/php/ext/apcu \
    && docker-php-ext-install \
        apcu \
        intl \
        mbstring \
        mysqli \
        zip \
        pdo_mysql \
        pdo_sqlite \
        gd \
        bcmath \
    && pecl install apcu_bc-1.0.3 \
    && docker-php-source delete \
    && php -r "readfile('https://getcomposer.org/installer');" | php -- --install-dir=/usr/local/bin --filename=composer \
    && chmod +x /usr/local/bin/composer \
    && wget https://phar.phpunit.de/phpunit-6.5.5.phar \
    && chmod +x phpunit-6.5.5.phar \
    && mv phpunit-6.5.5.phar /usr/local/bin/phpunit \
