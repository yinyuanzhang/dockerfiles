FROM php:7.1.22-alpine

RUN apk --no-cache add \
    postgresql-dev \
    libmcrypt-dev \
    icu-dev \
    curl-dev \
    libcurl \
    libxml2-dev \
    git \
    zip \
    unzip \
&& \
    docker-php-ext-install \
        pdo_pgsql \
        opcache \
        mbstring \
        mcrypt \
        json \
        intl \
        curl \
        xml \
        soap 

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer

WORKDIR /app

ENV SYMFONY_ENV=prod