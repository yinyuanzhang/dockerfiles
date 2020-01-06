FROM php:5.6.37-cli-alpine3.8

LABEL maintainer="potter.he@gmail.com"

RUN set -xe \
        && apk add --no-cache \
            $PHPIZE_DEPS \
            libmcrypt \
            libmcrypt-dev \
            librdkafka \
            librdkafka-dev \
            \
        && pecl install msgpack-0.5.7 \
        && pecl install redis-4.1.1 \
        && pecl install protocolbuffers-0.2.6 \
        && pecl install rdkafka-3.0.5 \
        && docker-php-ext-enable msgpack redis protocolbuffers rdkafka \
#        && docker-php-ext-configure mcrypt --with-mcrypt \
        && docker-php-ext-install pcntl mcrypt mysqli pdo_mysql sockets bcmath sysvmsg sysvsem sysvshm shmop \
        && apk del $PHPIZE_DEPS
