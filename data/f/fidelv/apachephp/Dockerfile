FROM php:5.6-apache

RUN r="libmcrypt-dev g++ libicu-dev libmcrypt4" \
    && apt-get update && apt-get install -y $r \
    && docker-php-ext-install pdo_mysql \
    && docker-php-ext-install mcrypt \
    && docker-php-ext-install mbstring \
    && docker-php-ext-install bcmath \
    && docker-php-ext-install intl \
    && rd="libmcrypt-dev g++ libicu-dev" \
    && apt-get purge --auto-remove -y $rd \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer \
    && apt-get update \
    && apt-get install -y zlib1g-dev git \
    && docker-php-ext-install zip \
    && apt-get purge -y --auto-remove zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y libpq-dev \
    && docker-php-ext-install pdo_pgsql

VOLUME "/var/www/html"  

RUN a2enmod rewrite

RUN usermod -u 1000 www-data
