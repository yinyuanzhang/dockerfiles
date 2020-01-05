FROM php:7.3-fpm

RUN apt-get update \
    && apt-get install -y --no-install-recommends libzip-dev zlib1g-dev libicu-dev g++ libxml2-dev git zip unzip netcat \
    && docker-php-ext-install intl pdo_mysql zip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* || true
