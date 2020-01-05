ARG PHP_VERSION=7.3

FROM php:${PHP_VERSION}-fpm-alpine

WORKDIR /var/www

# Install dependencies
RUN apk update && apk add \
    zip \
    libzip-dev \
    git \
    gcc \
    gd \
    autoconf \
    musl-dev \
    make \
    libressl-dev

# Install from pecl
RUN pecl install mongodb

# Enable PHP extensions
RUN docker-php-ext-enable \
    mongodb

# Install PHP extensions
RUN docker-php-ext-install \
    mbstring \
    zip \
    exif \
    pcntl \
    bcmath

# Copy existing application directory contents
COPY . /var/www

# Expose port 9000
EXPOSE 9000

# Start php-fpm
CMD ["php-fpm"]
