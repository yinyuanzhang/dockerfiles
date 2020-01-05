FROM php:7.1.7-fpm
MAINTAINER Bob van der Linden
RUN apt-get update -yqq && \
    (curl -sL https://deb.nodesource.com/setup_7.x | bash -) && \
    apt-get install git nodejs libcurl4-gnutls-dev libicu-dev libmcrypt-dev libvpx-dev libjpeg-dev libpng-dev libxpm-dev zlib1g-dev libfreetype6-dev libxml2-dev libexpat1-dev libbz2-dev libgmp3-dev libldap2-dev unixodbc-dev libpq-dev libsqlite3-dev libaspell-dev libsnmp-dev libpcre3-dev libtidy-dev -yqq && \
    rm -rf /var/lib/apt/lists/*
RUN docker-php-ext-install mbstring mcrypt pdo_mysql curl json intl gd xml zip bz2 opcache pdo_pgsql
RUN mkdir /tmp/composer && \
    cd /tmp/composer && \
    (curl -sS https://getcomposer.org/installer | php) && \
    cp composer.phar /usr/local/bin/composer && \
    chmod a+x /usr/local/bin/composer
