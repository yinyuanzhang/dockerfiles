FROM php:7.2-fpm

RUN apt-get update -y && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    bash \
    git \
    autoconf \
    libjpeg-dev \
    libpng-dev \
    libfreetype6-dev \
    libwebp-dev \
    curl \
    g++ \
    gcc \
    gettext \
    libxml2 \
    make \
    openssl \
    automake \
    libtool \
    nasm \
    python \
    libldap2-dev \
    freetds-dev \
    libpcre3-dev \
    libsasl2-dev \
    libcurl4-openssl-dev \
    libssl-dev \
    libicu-dev \
    libpq-dev \
    libxml2-dev \
    gnupg2 \
    unzip \
    gettext \
    libmcrypt-dev \
    libgmp-dev \
    libmagickwand-dev \
    && rm -rf /var/lib/apt/lists/*

# Add customize php.ini to allow long time execution
ADD php.ini /usr/local/etc/php/

RUN docker-php-ext-configure gd --with-jpeg-dir=usr/ --with-freetype-dir=usr/ --with-webp-dir=usr/
RUN docker-php-ext-configure ldap --with-libdir=lib/
RUN ln -s /usr/lib/x86_64-linux-gnu/libsybdb.so /usr/lib/
RUN docker-php-ext-configure pdo_dblib --with-libdir=lib/
RUN ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/lib/
RUN docker-php-ext-configure gmp --with-libdir=lib/

# Install MongoDB extension
RUN pecl install mongodb-1.3.4 && docker-php-ext-enable mongodb

# Install imageick
RUN pecl install imagick-3.4.3 && docker-php-ext-enable imagick

# Install other extensions
RUN docker-php-ext-install \
    curl \
    exif \
    gd \
    gettext \
    intl \
    ldap \
    pdo \
    pdo_dblib \
    pdo_mysql \
    pdo_pgsql \
    xmlrpc \
    zip \
    gmp

# Install xdebug
RUN pecl install xdebug && docker-php-ext-enable xdebug

# Download trusted certs
RUN mkdir -p /etc/ssl/certs && update-ca-certificates

# Install composer
RUN php -r "readfile('https://getcomposer.org/installer');" | php && \
   mv composer.phar /usr/bin/composer && \
   chmod +x /usr/bin/composer

# Install PHPUnit
RUN curl -sSL -o /usr/bin/phpunit https://phar.phpunit.de/phpunit.phar && chmod +x /usr/bin/phpunit

# Install node 10.x
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y nodejs && rm -rf /var/lib/apt/lists/*

# Install latest NPM
RUN curl -s -0 -L npmjs.org/install.sh | sh

RUN apt autoremove

WORKDIR /var/www
