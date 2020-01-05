FROM php:7.1-fpm

RUN apt-get update && apt-get install -y \
        git \
        zip \ 
        unzip \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
        libmemcached-dev \
        libssl-dev \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd \
    && docker-php-ext-install -j$(nproc) iconv mcrypt \
    && docker-php-ext-install -j$(nproc) opcache \
    && docker-php-ext-install -j$(nproc) mysqli pdo_mysql \
    && pecl install memcached \
    && pecl install apcu \
    && pecl install mongodb \
    && docker-php-ext-enable memcached \
    && docker-php-ext-enable mongodb \
    && docker-php-ext-enable apcu &&\
    php -r "readfile('http://getcomposer.org/installer');" | php -- --install-dir=/usr/bin/ --filename=composer && \
    apt-get -y autoremove && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*