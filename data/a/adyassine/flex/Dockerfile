FROM php:7.0-fpm

# Install "curl", "libmemcached-dev", "libpq-dev", "libjpeg-dev",
#         "libpng12-dev", "libfreetype6-dev", "libssl-dev", "libmcrypt-dev",
#         "mysql-client",
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git \
        curl \
        libmemcached-dev \
        libz-dev \
        libpq-dev \
        libjpeg-dev \
        libpng12-dev \
        libfreetype6-dev \
        libssl-dev \
        zlib1g-dev \
        libmcrypt-dev \
        mysql-client

# Install the PHP mcrypt extention
RUN docker-php-ext-install mcrypt

# Install the PHP pdo_mysql extention
RUN docker-php-ext-install pdo_mysql


# Install the PHP gd library
RUN docker-php-ext-configure gd \
        --enable-gd-native-ttf \
        --with-jpeg-dir=/usr/lib \
        --with-freetype-dir=/usr/include/freetype2 && \
    docker-php-ext-install gd
    
# Install Xdebug
RUN pecl install xdebug && docker-php-ext-enable xdebug

# Install ZIP
RUN docker-php-ext-install zip

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer