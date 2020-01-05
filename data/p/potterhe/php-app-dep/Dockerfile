FROM php:7.2.12-cli-alpine3.8

RUN set -xe \
        && apk add --no-cache \
            $PHPIZE_DEPS \
            libmcrypt \
            libmcrypt-dev \
            librdkafka \
            librdkafka-dev \
            \
        && curl 'http://pecl.php.net/get/mcrypt-1.0.1.tgz' -o /tmp/mcrypt-1.0.1.tgz  \
        && cd /tmp \
        && pecl install mcrypt-1.0.1.tgz \
        && rm -rf mcrypt-1.0.1.tgz \
        && docker-php-ext-enable mcrypt \
        \
        && curl 'http://pecl.php.net/get/rdkafka-3.0.5.tgz' -o /tmp/rdkafka-3.0.5.tgz  \
        && cd /tmp \
        && pecl install rdkafka-3.0.5.tgz \
        && rm -rf rdkafka-3.0.5.tgz \
        && docker-php-ext-enable rdkafka \
        \
        && curl 'http://pecl.php.net/get/msgpack-2.0.2.tgz' -o /tmp/msgpack-2.0.2.tgz  \
        && cd /tmp \
        && pecl install msgpack-2.0.2.tgz \
        && rm -rf msgpack-2.0.2.tgz \
        && docker-php-ext-enable msgpack \
        \
        && curl 'http://pecl.php.net/get/redis-4.2.0.tgz' -o /tmp/redis-4.2.0.tgz  \
        && cd /tmp \
        && pecl install redis-4.2.0.tgz \
        && rm -rf redis-4.2.0.tgz \
        && docker-php-ext-enable redis \
        \
        && docker-php-ext-install pcntl mysqli pdo_mysql sockets bcmath sysvmsg sysvsem sysvshm shmop \
        && apk del $PHPIZE_DEPS

#https://github.com/docker-library/php/issues/240
RUN apk add --no-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing gnu-libiconv
ENV LD_PRELOAD /usr/lib/preloadable_libiconv.so php
