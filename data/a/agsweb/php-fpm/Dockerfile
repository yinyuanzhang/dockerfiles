FROM php:7.2-fpm

COPY php.ini /usr/local/etc/php/

# Install system dependencies
RUN apt-get update -y && \
    apt-get install -y \
    libmcrypt-dev \
    sqlite \
    libsqlite3-0 \
    libsqlite3-dev \
    openssl \
    libicu-dev \
    libpng-dev \
    zip \
    unzip

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Make sure not old version of node cause problems
RUN apt-get remove nodejs
# Install nodejs
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - && apt-get install -y nodejs

# Set ini location for pecl
RUN pecl config-set php_ini /usr/local/etc/php/php.ini

# Install Pecl Extensions
RUN pecl install redis
RUN docker-php-ext-enable redis

# Install PHP Extensions
RUN docker-php-ext-install mbstring pdo_mysql pdo_sqlite gd intl bcmath zip sockets
