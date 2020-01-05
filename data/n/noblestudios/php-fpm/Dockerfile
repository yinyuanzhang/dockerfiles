FROM php:7.3-fpm

# Install some required tools
RUN apt-get update && apt-get install -y sudo less

# Install PHP Extensions
RUN apt-get update && apt-get install -y \
    bzip2 \
    libzip-dev \
    libbz2-dev \
    libc-client2007e-dev \
    libjpeg-dev \
    libkrb5-dev \
    libldap2-dev \
    libmagickwand-dev \
    libpng-dev \
    libpq-dev \
    libxml2-dev \
    mysql-client-* \
    imagemagick \
    xfonts-base \
    xfonts-75dpi \
    libmemcached-dev \
    && pecl install imagick \
    && pecl install oauth-2.0.2 \
    && pecl install redis-3.1.6 \
    && pecl install xdebug \
    && pecl install memcached \
    && docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
    && docker-php-ext-configure imap --with-imap-ssl --with-kerberos \
    && docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \
    && docker-php-ext-enable imagick \
    && docker-php-ext-enable oauth \
    && docker-php-ext-enable redis \
    && docker-php-ext-enable xdebug \
    && docker-php-ext-enable memcached \
    && docker-php-ext-install \
    bcmath \
    bz2 \
    calendar \
    gd \
    imap \
    ldap \
    mbstring \
    mysqli \
    opcache \
    pdo \
    pdo_mysql \
    soap \
    zip \
    && apt-get -y clean \
    && apt-get -y autoclean \
    && apt-get -y autoremove \
    && rm -rf /var/lib/apt/lists/* && rm -rf && rm -rf /var/lib/cache/* && rm -rf /var/lib/log/* && rm -rf /tmp/*

# Custom PHP Conf
COPY ./php.ini /usr/local/etc/php/conf.d/custom.ini

# WP-CLI
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar \
&& mv wp-cli.phar /usr/local/bin \
&& chmod +x /usr/local/bin/wp-cli.phar \
&& ln -s /usr/local/bin/wp-cli.phar /usr/local/bin/wp

# Run this container as "webuser"
RUN groupadd -r -g 1000 webuser && useradd -r -u 1000 -g webuser webuser
RUN usermod -aG www-data webuser
USER webuser
