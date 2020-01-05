FROM php:5.5-fpm

# Install modules
RUN groupadd -g 10100 fenix \
    && useradd -u 10100 -g 10100 -M -s /sbin/nologin fenix \
    && apt-get update && apt-get install -y \
    libjpeg-dev \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libmcrypt-dev \
    libpng12-dev \
    libxml2-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pecl install timezonedb \
    && docker-php-ext-enable timezonedb \
    && docker-php-ext-install iconv mcrypt \
    && docker-php-ext-install opcache \
    && docker-php-ext-install mbstring \
    && docker-php-ext-install pdo_mysql \
    && docker-php-ext-install mysqli \
    && docker-php-ext-install soap \
    && docker-php-ext-install sockets \
    && docker-php-ext-install zip

COPY config/php.ini /usr/local/etc/php/php.ini
COPY config/php-fpm.conf /usr/local/etc/php-fpm.conf

RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd
