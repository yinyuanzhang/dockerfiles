FROM php:7.2-fpm

RUN     docker-php-source extract && \
        apt-get update && \
        pecl install igbinary && docker-php-ext-enable igbinary && \
        docker-php-ext-install fileinfo && \
        apt-get -y --no-install-recommends install libzip-dev libicu-dev gnupg libfreetype6-dev libjpeg62-turbo-dev libpng-dev \
        libxslt-dev mariadb-client libpcre3-dev openssh-client && \
        docker-php-ext-install zip && \
        docker-php-ext-install opcache && \
        docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ && docker-php-ext-install gd && \
        docker-php-ext-install intl && \
        docker-php-ext-install mysqli && \
        docker-php-ext-install pdo_mysql && \
        docker-php-ext-install soap && \
        docker-php-ext-install xsl && \
        docker-php-source delete && \
        (cat $PHP_INI_DIR/php.ini-production | \
        sed -E 's/^.*session.cookie_httponly ?=.*$/session.cookie_httponly = 1/' | \
        sed -E 's/^.*session.cookie_secure ?=.*$/session.cookie_secure = 1/' | \
        sed -E 's/^.*opcache.enable ?=.*$/opcache.enable = 1/' | \
        sed -E 's/^.*opcache.memory_consumption ?=.*$/opcache.memory_consumption = 128/' | \
        sed -E 's/^.*opcache.max_accelerated_files ?=.*$/opcache.max_accelerated_files = 20000/' | \
        sed -E 's/^.*opcache.validate_timestamps ?=.*$/opcache.validate_timestamps = 0/' | \
        sed -E 's/expose_php = On/expose_php = Off/' | \
        sed -E 's/^.*realpath_cache_size ?=.*$/realpath_cache_size = 4096k/' | \
        sed -E 's/^.*realpath_cache_ttl ?=.*$/realpath_cache_size = 120/' | \
        sed -E 's/^.*upload_max_filesize ?=.*$/upload_max_filesize = 32M/' | \
        sed -E 's/^.*post_max_size ?=.*$/post_max_size = 32M/' > $PHP_INI_DIR/php.ini) && \
        apt-get clean
