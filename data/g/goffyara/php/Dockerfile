FROM php:7.0-cli
ENV DEBIAN_FRONTEND noninteractive
ENV COMPOSER_ALLOW_SUPERUSER 1

RUN apt-get update && apt-get install -y --no-install-recommends \
        git \
        #mcrypt
        mcrypt \
        libmcrypt-dev \
        #curl
        libcurl4-openssl-dev \
        #gd
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng-dev \
        #memcached
        libmemcached-dev \
        zlib1g-dev \
        #intl
        libicu-dev \
        #xml
        libxml2-dev \
        #pdo_pgsql
        libpq-dev \
        #imagick
        libmagickwand-dev \
    && docker-php-ext-configure \
        gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-configure intl --with-icu-dir=/usr \
    && docker-php-ext-configure opcache --enable-opcache \
    && docker-php-ext-install -j$(nproc) \
        curl \
        pdo_pgsql \
        pdo_mysql \
        gd \
        intl \
        mbstring \
        xml \
        bcmath \
        zip \
        pcntl \
        opcache \
    && pecl install \
        xdebug-2.6.0  \
        memcached-3.0.3 \
        imagick-3.4.3 \
        apcu-5.1.12 \
    && docker-php-ext-enable memcached xdebug imagick apcu \
    && apt-get autoremove -y \
    && apt-get autoclean -y \
    && curl -sS https://getcomposer.org/installer | php && mv composer.phar /usr/local/bin/composer
CMD ["php -a"]