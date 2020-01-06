FROM php:7.3-apache
MAINTAINER Thomas Cheng <thomas@beamstyle.com.hk>

# Fix the following weird error when installing pdftk
# update-alternatives: error: error creating symbolic link '/usr/share/man/man1/rmid.1.gz.dpkg-tmp': No such file or directory
RUN mkdir -p /usr/share/man/man1

RUN apt-get update && apt-get install -y \
        git \
        zlib1g-dev \
        libicu-dev \
        libzip-dev \
        g++ \
        libsqlite3-dev \
        pdftk \
        && apt-get --purge autoremove \
        && rm -rf /var/lib/apt/lists/*

# Basic lumen packages
RUN docker-php-ext-install \
        pdo \
        pdo_mysql \
        pdo_sqlite \
        opcache \
        intl \
        mbstring \
        mysqli \
        tokenizer \
        zip

# GD library
RUN apt-get update && apt-get install -y \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libpng-dev \
    libwebp-dev \
    && apt-get --purge autoremove

RUN docker-php-ext-configure gd \
    --with-freetype-dir=/usr/include/ \
    --with-jpeg-dir=/usr/include/ \
    --with-png-dir=/usr/include/ \
    --with-webp-dir=/usr/include/

RUN docker-php-ext-install \
    gd

# Add php.ini for production
COPY php/php.ini-production $PHP_INI_DIR/php.ini
COPY apache/apache2.conf /etc/apache2/apache2.conf

#  Configuring Apache
RUN  rm /etc/apache2/sites-available/000-default.conf \
         && rm /etc/apache2/sites-enabled/000-default.conf

# Enable rewrite module
RUN a2enmod rewrite
RUN a2enmod expires
RUN a2enmod headers

WORKDIR /var/www/html

# Download and Install Composer
RUN curl -s http://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer

# Add vendor binaries to PATH
ENV PATH=/var/www/html/vendor/bin:$PATH
