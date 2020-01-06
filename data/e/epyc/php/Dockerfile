FROM php:7.3-fpm

# Copy the docker-php.ini config file
COPY docker-php.ini /usr/local/etc/php/conf.d/docker-php.ini

# Update apt-get
RUN apt-get update

# Nano (texteditor)
RUN apt-get install -y nano

# Wget
RUN apt-get install -y wget

# Git
RUN apt-get install -y git

# MySQL
RUN apt-get install -y libmcrypt-dev mariadb-client zlib1g-dev && docker-php-ext-install pdo_mysql
RUN docker-php-ext-install mysqli

# mcrypt
RUN pecl install mcrypt-1.0.2
RUN docker-php-ext-enable mcrypt

# bcmath
RUN docker-php-ext-install bcmath
RUN docker-php-ext-enable bcmath

# Soap
# RUN apt-get install -y libxml2-dev php-soap && docker-php-ext-install soap
RUN apt-get install -y libxml2-dev
RUN docker-php-ext-configure soap --enable-soap

# Zip Unzip
RUN apt-get install -y zip unzip zlib1g-dev libzip-dev
RUN docker-php-ext-install zip

# GD
RUN apt-get install -y libpng-dev
RUN docker-php-ext-install mbstring
RUN docker-php-ext-install gd

# Composer
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
RUN php composer-setup.php
RUN php -r "unlink('composer-setup.php');"
RUN mv composer.phar /usr/local/bin/composer
