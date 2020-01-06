FROM php:7.2-cli-alpine3.8

LABEL maintainer "https://github.com/hurtom/"

RUN curl -L https://getcomposer.org/installer -o composer-setup.php \
    && php composer-setup.php --install-dir=/usr/local/bin --filename=composer \
    && rm -f composer-setup.php

RUN apk add --no-cache --virtual .build-deps \
            $PHPIZE_DEPS \
            freetype-dev \
            gettext-dev \
            libjpeg-turbo-dev \
            libpng-dev \
            zlib-dev \
    && pecl install redis xdebug \
    && docker-php-ext-enable redis xdebug \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install bcmath gd gettext mysqli opcache pdo_mysql zip \
    && apk del .build-deps

RUN apk add --no-cache \
            ca-certificates \
            freetype \
            git \
            libjpeg-turbo \
            libintl \
            libpng \
            tzdata \
            unzip

RUN cp /usr/share/zoneinfo/Europe/Kiev /etc/localtime \
    && echo "Europe/Kiev" > /etc/timezone

RUN sed -ri 's/^www-data:x:82:82:/www-data:x:1000:1000:/' /etc/passwd
