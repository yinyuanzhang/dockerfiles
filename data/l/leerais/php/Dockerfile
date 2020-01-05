FROM php:7.4-fpm
MAINTAINER leerais <leerais@gmail.com>

ENV TERM xterm

# Dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        libzip-dev \
        libmemcached-dev \
        libz-dev \
        libpq-dev \
        libjpeg-dev \
        libpng-dev \
        libfreetype6-dev \
        libssl-dev \
        libmcrypt-dev \
        libicu-dev \
        libyaml-dev

# Buildin extensions
RUN docker-php-ext-configure gd --with-freetype --with-jpeg \
    && docker-php-ext-install -j$(nproc) gd pcntl pdo_mysql pdo_pgsql intl opcache bcmath

# Pecl extensions
RUN pecl install zip-1.15.5 \
    && pecl install yaml-2.0.4 \
    && pecl install mcrypt-1.0.3 \
    && docker-php-ext-enable zip yaml mcrypt

# Security updates
RUN apt-get -s dist-upgrade | grep "^Inst" | grep -i securi | awk -F " " {'print $2'} | xargs apt-get install

# Clean
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# User & directory
RUN usermod -u 1000 www-data
RUN mkdir -p /var/www
WORKDIR /var/www

CMD ["php-fpm"]
EXPOSE 9000
