FROM php:7.3.9-fpm-alpine

ENV LIBRARY_PATH=/lib:/usr/lib

RUN apk --virtual .build-dependencies --no-cache add libzip-dev zlib-dev openldap-dev \
    && apk add libzip libldap \
    && docker-php-ext-install -j$(nproc) zip pdo pdo_mysql ldap \
    && apk del .build-dependencies
