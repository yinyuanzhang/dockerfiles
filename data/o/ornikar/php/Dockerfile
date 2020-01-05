FROM php:7.4-fpm-alpine3.10

# Maintainers.
LABEL maintainer="Julien BREUX <julien.breux@ornikar.com>"

# Quick fix iconv 1/2 (https://github.com/docker-library/php/issues/240#issuecomment-305038173).
ENV LD_PRELOAD /usr/lib/preloadable_libiconv.so php

RUN NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \
# Add missing Alpine packages.
    && apk update \
    && apk upgrade \
    && apk add \
        ca-certificates \
        freetds \
        freetype \
        git \
        icu \
        imap-dev \
        libintl \
        libldap \
        libjpeg \
        libmcrypt \
        libpng \
        libzip \
        libpq \
        tzdata \
# Add temporary deps.
    && DEV_DEPS=" \
    autoconf \
    binutils \
    curl-dev \
    freetds-dev \
    freetype-dev \
    g++ \
    gcc \
    gettext-dev \
    icu-dev \
    jpeg-dev \
    libc-dev \
    libstdc++ \
    libgcc \
    libmcrypt-dev \
    oniguruma-dev \
    libpng-dev \
    libwebp-dev \
    libxml2-dev \
    libzip-dev \
    zlib-dev \
    make \
    openssl-dev \
    postgresql-dev" \
    && apk add $DEV_DEPS \
# Quick fix iconv 2/2 (https://github.com/docker-library/php/issues/240#issuecomment-305038173).
    && apk add --no-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing gnu-libiconv \
# Install missing PHP extensions via PECL.
    && pecl install \
        redis-5.0.2 \
# Configure, install and enable missing PHP extensions via Image helper.
    && docker-php-ext-configure gd \
        --with-gd \
        --with-freetype-dir=/usr/include/ \
        --with-png-dir=/usr/include/ \
        --with-jpeg-dir=/usr/include/ \
    && PHP_OPENSSL=yes docker-php-ext-configure imap \
        --with-imap \
        --with-imap-ssl \
    && docker-php-ext-configure zip \
        --with-libzip=/usr/include/ \
# Install PHP extensions.
    && docker-php-ext-install -j${NPROC} \
        bcmath \
        curl \
        exif \
        gd \
        gettext \
        iconv \
        imap \
        intl \
        iconv \
        mbstring \
        mysqli \
        opcache \
        pdo_mysql \
        pdo_pgsql \
        pgsql \
        pcntl \
        xmlrpc \
        zip \
        soap \
# Enable PHP extensions.
    && docker-php-ext-enable \
        opcache \
        redis \
# Remove sources
    && docker-php-source delete \
# Configure PHP.
    && { \
        echo 'memory_limit = 512M'; \
    } | tee /usr/local/etc/php/conf.d/zz-custom-memory.ini \
    && { \
        echo 'expose_php = Off'; \
    } | tee /usr/local/etc/php/conf.d/zz-custom-expose.ini \
# Timezone.
    && { \
        echo "date.timezone = Europe/Paris"; \
    } | tee /usr/local/etc/php/conf.d/zz-custom-timezone.ini \
    && cp /usr/share/zoneinfo/Europe/Paris /etc/localtime \
    && echo "Europe/Paris" > /etc/timezone \
# Clean.
    && apk del $DEV_DEPS \
    && pecl clear-cache \
    && rm -rf /tmp/pear ~/.pearrc /var/cache/apk/* \
# Display installation summary.
    && php --ini \
    && php --version \
    && php -m
