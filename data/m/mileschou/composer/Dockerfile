#
# NOTE: THIS DOCKERFILE IS GENERATED VIA "update.sh"
#
# PLEASE DO NOT EDIT IT DIRECTLY.
#
FROM php:7.1-alpine

LABEL repository="https://github.com/MilesChou/composer-action" \
    maintainer="MilesChou <jangconan@gmail.com>"

RUN set -xe && \
    apk add --no-cache \
        libzip \
    && \
    apk add --no-cache --virtual .build-deps \
        libzip-dev \
        zlib-dev \
    && \
    docker-php-ext-install -j "$(getconf _NPROCESSORS_ONLN)" \
        zip \
    && \
    apk del --no-cache .build-deps \
    && \
    php -m

ENV COMPOSER_ALLOW_SUPERUSER=1 \
    COMPOSER_MEMORY_LIMIT=-1 \
    COMPOSER_HOME=/tmp \
    COMPOSER_PATH=/usr/local/bin/composer \
    COMPOSER_VERSION=1.9.1

COPY --from=composer:1.9.1 /usr/bin/composer /usr/local/bin/composer

RUN set -xe && \
        composer global require hirak/prestissimo && \
        composer clear-cache

COPY docker-entrypoint /usr/local/bin/docker-entrypoint

WORKDIR /app

ENTRYPOINT ["/usr/local/bin/docker-entrypoint"]

CMD ["--info"]
