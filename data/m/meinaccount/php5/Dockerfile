FROM php:5-fpm
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpng-dev \
    libjpeg-dev \
    libpq-dev \
    libssl-dev \
    libc-client2007e-dev \
    libkrb5-dev \
    pdftk \
    zlib1g-dev libicu-dev g++ \
 && rm -rf /var/lib/apt/lists/*
RUN docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr
RUN docker-php-ext-configure imap --with-imap-ssl --with-kerberos
RUN docker-php-ext-configure intl
RUN docker-php-ext-install \
    gd \
    mbstring \
    pdo \
    pdo_mysql \
    mysqli \
    imap \
    zip \
    intl

WORKDIR /var/www
COPY php.ini /usr/local/etc/php/

