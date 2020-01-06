FROM php:7.3-cli-buster

RUN addgroup --system magento --gid 82 \
    && adduser --system --ingroup magento --uid 82 magento

RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
        libfreetype6-dev \
        libgmp-dev \
        libicu-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng-dev \
        libxslt-dev \
        libzip-dev \
    ; \
    rm -rf /var/lib/apt/lists/*

RUN set -eux; \
    docker-php-ext-configure \
        gd --with-jpeg-dir=/usr/include/ --with-freetype-dir=/usr/include/ \
    ; \
    docker-php-ext-install -j$(nproc) \
        bcmath \
        gd \
        gmp \
        intl \
        opcache \
        pcntl \
        pdo_mysql \
        soap \
        sockets \
        xsl \
        zip \
    ; \
    pecl install redis; \
    docker-php-ext-enable \
        redis \
    ;

COPY php.ini-* "$PHP_INI_DIR/"

RUN set -eux; \
    cp "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"
