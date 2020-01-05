FROM php:7.3-cli
RUN apt-get update && apt-get install -y \
        gcc make autoconf libc-dev pkg-config unzip \
        openssl \
        libpcre3-dev \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng-dev \
        zlib1g-dev \
        libmemcached-dev \
    && docker-php-ext-install -j$(nproc) bcmath \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include --with-jpeg-dir=/usr/include \
    && docker-php-ext-install -j$(nproc) gd \
    && docker-php-ext-install pdo_mysql mysqli\
    # Install php-memcached
    && pecl install memcached \
    && docker-php-ext-enable memcached \
    && docker-php-ext-enable opcache \
    # Install redis
    && pecl install redis \
    && docker-php-ext-enable redis \
    && pecl install xdebug \
    && docker-php-ext-enable xdebug \
    # Install phalcon.so
    && curl -L -o cphalcon-3.4.2.zip https://github.com/phalcon/cphalcon/archive/v3.4.2.zip \
    && unzip cphalcon-3.4.2.zip && cd cphalcon-3.4.2/build && ./install \
    && docker-php-ext-enable phalcon \
    && cd ../.. && rm -rf cphalcon-3.4.2 \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

RUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"

ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8
ENV LANGUAGE en_US.UTF-8  
