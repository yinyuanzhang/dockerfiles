FROM php:5.6.38-fpm-alpine

# Install Supervisor
RUN set -x \
 && apk add --no-cache supervisor \
 && rm -rf /var/cache/apk/* /tmp/*

# Install NGINX
RUN set -x \
 && apk add --no-cache nginx \
 && rm -rf /var/cache/apk/* /tmp/*

# Install PHP module - OPCache
RUN set -x \
 && docker-php-ext-install -j$(nproc) opcache \
 && rm -rf /var/cache/apk/* /tmp/*

# Install PHP module - MySQLi
RUN set -x \
 && docker-php-ext-install -j$(nproc) mysqli \
 && rm -rf /var/cache/apk/* /tmp/*

# Install PHP module - PDO MySQL
RUN set -x \
 && docker-php-ext-install -j$(nproc) pdo_mysql \
 && rm -rf /var/cache/apk/* /tmp/*

# Install PHP module - ZIP
RUN set -x \
 && apk add --no-cache --virtual .zip-build-dependencies zlib-dev \
 && docker-php-ext-install -j$(nproc) zip \
 && apk del --purge .zip-build-dependencies \
 && rm -rf /var/cache/apk/* /tmp/*

# Install PHP module - XSL
RUN set -x \
 && apk add --no-cache --virtual .xsl-runtime-dependencies libxslt \
 && apk add --no-cache --virtual .xsl-build-dependencies libxslt-dev \
 && docker-php-ext-install -j$(nproc) xsl \
 && apk del --purge .xsl-build-dependencies \
 && rm -rf /var/cache/apk/* /tmp/*

# Install PHP module - GD
RUN set -x \
 && apk add --no-cache --virtual .gd-runtime-dependencies \
    freetype \
    libpng \
    libjpeg-turbo \
 && apk add --no-cache --virtual .gd-build-dependencies \
    freetype-dev \
    libpng-dev \
    libjpeg-turbo-dev \
 && docker-php-ext-configure gd \
    --with-gd \
    --with-freetype-dir=/usr/include/ \
    --with-png-dir=/usr/include/ \
    --with-jpeg-dir=/usr/include/ \
 && docker-php-ext-install -j$(nproc) gd \
 && apk del --purge .gd-build-dependencies \
 && rm -rf /var/cache/apk/* /tmp/*

# Install PHP module - ImageMagick
RUN set -x \
 && apk add --no-cache --virtual .imagick-runtime-dependencies \
    imagemagick \
 && apk add --no-cache --virtual .imagick-build-dependencies \
    imagemagick-dev \
 && apk add --no-cache --virtual .phpize-dependencies $PHPIZE_DEPS \
 && printf "\n" | pecl install imagick-3.4.3 \
 && docker-php-ext-enable imagick \
 && apk del --purge .imagick-build-dependencies \
 && apk del --purge .phpize-dependencies \
 && pecl clear-cache \
 && rm -rf /var/cache/apk/* /tmp/*

# Install PHP module - FFmpeg
RUN set -x \
 && apk add --no-cache --virtual .ffmpeg-runtime-dependencies \
    ffmpeg \
 && apk add --no-cache --virtual .ffmpeg-build-dependencies \
    ffmpeg-dev \
 && apk add --no-cache --virtual .phpize-dependencies $PHPIZE_DEPS git \
 && cd /tmp/ \
 && git clone https://github.com/fedotov-as/ffmpeg-php.git \
 && cd ffmpeg-php \
 && phpize \
 && ./configure \
    --enable-shared \
    --prefix=/usr \
 && make -j$(nproc) \
 && make install \
 && docker-php-ext-enable ffmpeg \
 && apk del --purge .ffmpeg-build-dependencies \
 && apk del --purge .phpize-dependencies \
 && rm -rf /var/cache/apk/* /tmp/*

# Fix iconv extension
RUN apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing/ gnu-libiconv \
 && rm -rf /var/cache/apk/* /tmp/*
ENV LD_PRELOAD /usr/lib/preloadable_libiconv.so php

# Install Gettext
RUN set -x \
 && apk add --no-cache gettext \
 && rm -rf /var/cache/apk/* /tmp/*

# Preparation of local environment
RUN mkdir -pvm0777 \
    /var/log/lighthouse \
    /app/cache

# Add configs for additional programs
COPY build_env/config /

# Set current dir
WORKDIR /app

# Background process & entrypoint
CMD ["supervisord", "-c", "/etc/supervisord.conf"]
ENTRYPOINT ["./entrypoint.sh"]
