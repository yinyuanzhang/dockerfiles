FROM php:7.4-fpm-alpine

LABEL maintainer="Engenharia Arquivei <engenharia@arquivei.com.br>"
ARG RDKAFKA_VERSION="1.1.0"
ARG RDKAFKA_PECL_VERSION="3.1.2"

RUN set -xe \
    && apk update \
# Install build dependencies
    && apk --no-cache --virtual .build-deps add \
        autoconf bash build-base pcre-dev python \
# Install PHP extensions dependencies
    && apk --no-cache add libzip-dev libxml2-dev postgresql-dev libstdc++ \
    && docker-php-ext-install bcmath pdo_pgsql pdo_mysql soap zip

RUN pecl install grpc && docker-php-ext-enable grpc \
    # && pecl install protobuf && docker-php-ext-enable protobuf \
    && pecl install redis && docker-php-ext-enable redis

# Build, install and enable PHP rdkafka extension
RUN mkdir -p /tmp/librdkafka \
    && cd /tmp \
    && curl -L https://github.com/edenhill/librdkafka/archive/v${RDKAFKA_VERSION}.tar.gz | tar xz -C /tmp/librdkafka --strip-components=1 \
    && cd librdkafka \
    && ./configure \
    && make \
    && make install \
    && pecl install rdkafka-${RDKAFKA_PECL_VERSION} \
    && docker-php-ext-enable rdkafka \
    && rm -rf /tmp/librdkafka \
# Remove build dependencies. MUST BE LAST COMMAND!
    && apk del .build-deps