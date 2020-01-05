FROM php:7.2

#
#--------------------------------------------------------------------------
# Software's Installation
#--------------------------------------------------------------------------
#
# Installing tools and PHP extentions using "apt", "docker-php", "pecl",
#

# Install "curl", "libmemcached-dev", "libpq-dev", "libjpeg-dev",
#         "libpng-dev", "libfreetype6-dev", "libssl-dev", "libmcrypt-dev",
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    curl \
    libmemcached-dev \
    libz-dev \
    libpq-dev \
    libjpeg-dev \
    libpng-dev \
    libxpm-dev \
    libvpx-dev \
    libfreetype6-dev \
    libssl-dev \
    libmcrypt-dev \
    zlib1g-dev \
    libicu-dev \
    g++ \
    git \
    python-pip \
    zip \
    unzip \
    openssh-client \
    libc-client-dev \
    libkrb5-dev \
    poppler-utils \
  && rm -rf /var/lib/apt/lists/*

# Install the PHP extentions
RUN docker-php-ext-install pdo_mysql \
    && docker-php-ext-install pdo_pgsql \
    && docker-php-ext-configure gd \
    --enable-gd-native-ttf \
    --with-jpeg-dir=/usr/lib \
    --with-xpm-dir=/usr/lib \
    --with-png-dir=/usr/lib \
    --with-vpx-dir=/usr/lib \
    --with-freetype-dir=/usr/include/freetype2 \
    && docker-php-ext-install gd \
    && docker-php-ext-install bcmath \
    && docker-php-ext-install intl \
    && docker-php-ext-install zip \
    && docker-php-ext-configure imap --with-kerberos --with-imap-ssl \
    && docker-php-ext-install imap

COPY ./php.ini /usr/local/etc/php/conf.d/custom.ini

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
