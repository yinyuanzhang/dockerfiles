FROM php:7.3-fpm-alpine

ENV LOG_PREFIX /var/log/php-fpm
ENV TEMP_PREFIX /tmp
ENV CACHE_PREFIX /var/cache

COPY php-ini-overrides.ini /usr/local/etc/php/conf.d/90-overrides.ini

RUN set -x \
    && mkdir -p /var/run \
    && mkdir -p ${LOG_PREFIX} \
    && touch ${LOG_PREFIX}/access.log \
    && touch ${LOG_PREFIX}/error.log \
    && ln -sf /dev/stdout ${LOG_PREFIX}/access.log \
    && ln -sf /dev/stderr ${LOG_PREFIX}/error.log

RUN apk update \
    && apk add --no-cache bash openssh-client git gmp-dev libmemcached-dev zlib-dev libzip-dev libxml2-dev\
    && apk add --no-cache ${PHPIZE_DEPS} \
    && pecl install xdebug-2.7.1 memcached \
    && docker-php-ext-install mbstring mysqli pdo pdo_mysql gmp bcmath opcache zip simplexml xml soap \
    && docker-php-ext-enable xdebug memcached \
    && rm -rf ${TEMP_PREFIX}/* \
    && rm -rf ${CACHE_PREFIX}/apk/*

COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

RUN COMPOSER_CACHE_DIR=/dev/null composer global require codeception/codeception squizlabs/php_codesniffer
ENV PATH $PATH:/root/.composer/vendor/bin

COPY script/docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

EXPOSE 9000
EXPOSE 9001

ENTRYPOINT ["/docker-entrypoint.sh"]