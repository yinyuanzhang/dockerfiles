FROM php:7.2-fpm-alpine

MAINTAINER Cristian Mello <cristianc.mello@gmail.com>

RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories \
    && apk --no-cache update \
    && apk --no-cache upgrade \
    && apk add --no-cache --virtual \
        .build-deps \
        $PHPIZE_DEPS \
        gcc g++ make \
        autoconf \
        libc-dev \
        curl-dev \
        imagemagick-dev \
        libtool \
        libxml2-dev \
        sqlite-dev \
    && apk add --no-cache \
        libmcrypt-dev \
        mysql-client \
        nodejs \
        nodejs-npm \
        yarn \
        curl \
        freetype libpng libjpeg-turbo freetype-dev libpng-dev libjpeg-turbo-dev libwebp-dev \
        supervisor \
        bash \
        nginx \
        pngquant jpegoptim \
        zip \
        icu-dev libxml2-dev \
        dcron wget rsync ca-certificates \
    && NPROC=$(getconf _NPROCESSORS_ONLN) \
    && docker-php-ext-install -j${NPROC} \
        exif \
        json \
        intl \
        mbstring \
        mysqli \
        pdo \
        pdo_mysql \
        pdo_sqlite \
        zip \
        xml \
        bcmath \
        pcntl \
        tokenizer \
        iconv \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ --with-png-dir=/usr/include/ --with-webp-dir=/usr/include/ \
    && docker-php-ext-install -j${NPROC} gd \
    && pecl install apcu \
    && docker-php-ext-enable --ini-name 05-opcache.ini opcache \
    && docker-php-ext-enable --ini-name 20-apcu.ini apcu \
    && apk del --no-cache gcc g++ make libc-dev libtool libxml2-dev sqlite-dev imagemagick-dev freetype-dev libpng-dev libjpeg-turbo-dev curl-dev .build-deps \
    # https://github.com/docker-library/php/issues/443
    && pecl update-channels \
    && rm -rf /tmp/pear ~/.pearrc

# Install composer
RUN curl -s https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin/ --filename=composer
ENV COMPOSER_ALLOW_SUPERUSER=1
ENV PATH="./vendor/bin:$PATH"
