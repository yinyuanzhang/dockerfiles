FROM php:7.2.12

MAINTAINER Igor Chepurnoi <chepurnoi.igor@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN echo America/New_York > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata

RUN apt-get update && apt-get install -y apt-utils \
    && apt-get install -y \
        zlib1g-dev \
        libicu-dev \
        libpq-dev \
        libpcre3-dev \
        git \
        nano \
        zip \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng-dev \
        libmagickwand-dev \
        supervisor \
        mysql-client \
        pngquant \
        cron \
        wget \
        gnupg \
        libxpm-dev \
        libvpx-dev \
        libwebp-dev \
        iproute2 \
    && docker-php-ext-install -j$(nproc) iconv intl zip pdo_mysql exif bcmath \
    && pecl install mcrypt-1.0.1 && docker-php-ext-enable mcrypt.so \
    && docker-php-ext-configure gd \
        --with-png-dir=/usr \
        --with-jpeg-dir=/usr \
        --with-freetype-dir=/usr \
        --with-xpm-dir=/usr \
        --with-webp-dir=/usr \
        --with-vpx-dir=/usr; \
    docker-php-ext-install gd \
    && pecl install imagick \
    && docker-php-ext-enable imagick \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install Node.js
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - \
    && DEBIAN_FRONTEND=noninteractive apt-get install nodejs --no-install-recommends -yqq

# Install yarn, pm2 and gulp
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install yarn && yarn global add pm2 gulp

# Install composer
RUN set -x && curl -sS https://getcomposer.org/installer | php && mv composer.phar /usr/local/bin/composer
