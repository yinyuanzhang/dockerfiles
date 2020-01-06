#
# php 7.2 with fpm enabled
#
# extra enabled extensions:
#   amqp bcmath calendar gd grpc mcrypt pdo_mysql phpiredis protobuf opcache zip
#
FROM php:7.2-fpm

RUN apt-get update \
    && apt-get install -y \
        rsync \
        unzip \
        libmemcached-dev \
        librabbitmq-dev \
        libhiredis-dev \
        zlib1g-dev \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN docker-php-ext-install -j$(nproc) bcmath \
    && docker-php-ext-configure sockets --enable-sockets \
    && docker-php-ext-install -j$(nproc) sockets \
    && docker-php-ext-install -j$(nproc) calendar \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd \
    && docker-php-ext-configure pdo_mysql --with-pdo-mysql=mysqlnd \
    && docker-php-ext-install -j$(nproc) pdo_mysql \
    && docker-php-ext-configure zip --enable-zip \
    && docker-php-ext-install -j$(nproc) zip \
    && docker-php-ext-configure opcache --enable-opcache \
    && docker-php-ext-install -j$(nproc) opcache \
    && pecl install mcrypt-1.0.2 memcached protobuf grpc-1.26.0 \
    && echo "/usr" | pecl install amqp \
    && ( \
        mkdir /tmp/sources \
        && cd /tmp/sources \
        && curl -fsSL https://github.com/nrk/phpiredis/archive/v1.0.0.zip -o phpiredis.zip \
        && unzip phpiredis.zip \
        && cd phpiredis-1.0.0/ \
        && phpize && ./configure --enable-phpiredis \
        && make -j$(nproc) && make install \
        && rm -rf /tmp/sources \
    ) \
    && docker-php-ext-enable memcached protobuf grpc amqp phpiredis

# vim:ft=dockerfile
