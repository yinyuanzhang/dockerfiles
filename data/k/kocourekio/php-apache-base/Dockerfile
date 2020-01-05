FROM php:7.0-apache

# Install GD
RUN apt-get update \
    && apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libpng-dev \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd

# Install Intl
RUN apt-get update \
    && apt-get install -y libicu-dev \
    && docker-php-ext-install -j$(nproc) intl

# Install Mysql
RUN docker-php-ext-install -j$(nproc) mysqli pdo_mysql

# Install Git and some additional utilities
RUN apt-get update \
    && apt-get install -y git wget nano zip unzip

# Install Exif and BCMath
RUN docker-php-ext-install -j$(nproc) exif bcmath

# Define PHP_TIMEZONE env variable
ENV PHP_TIMEZONE Europe/Prague

# Configure Apache Document Root & Server Name
ENV APACHE_DOC_ROOT /var/www/html/www
ENV APACHE_SRV_NAME localhost

# Enable Apache mod_rewrite & mod_ssl
RUN a2enmod rewrite ssl

# Additional PHP ini configuration
COPY ./999-php.ini /usr/local/etc/php/conf.d/

# Install Composer
COPY ./install-composer /usr/local/bin
RUN install-composer

# Start!
COPY ./start /usr/local/bin
CMD ["start"]
