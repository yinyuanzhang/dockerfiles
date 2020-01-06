ARG PHP_VERSION=7.0

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
    libressl-dev \
    libmcrypt-dev \
    libpng-dev \
    jpeg-dev \
    libjpeg \
    --no-cache autoconf gcc g++ imagemagick6-dev libtool make \
    && pecl install imagick-3.4.3 \
    && docker-php-ext-enable imagick \
    && apk del autoconf g++ libtool make

# Install PHP extensions
RUN docker-php-ext-install \
    mbstring \
    zip \
    exif \
    pcntl \
    bcmath \
    mcrypt \
    pdo \
    pdo_mysql \
    mysqli \
    calendar \
    ctype \
    dba \
    ftp \
    iconv \
    tokenizer
RUN docker-php-ext-configure gd --with-jpeg-dir=/usr/include/ --with-png-dir=/usr/include/ 
RUN docker-php-ext-install gd

ENV PHPREDIS_VERSION 3.0.0
RUN mkdir -p /usr/src/php/ext/redis \
    && curl -L https://github.com/phpredis/phpredis/archive/$PHPREDIS_VERSION.tar.gz | tar xvz -C /usr/src/php/ext/redis --strip 1 \
    && echo 'redis' >> /usr/src/php-available-exts \
    && docker-php-ext-install redis \
    && rm -rf /tmp/pear \
    && docker-php-ext-enable redis

# Copy existing application directory contents
COPY . /var/www

# Expose port 9000
EXPOSE 9000

# Start php-fpm
CMD ["php-fpm"]