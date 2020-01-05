FROM php:7-apache

WORKDIR /var/www/html/mini-tms

COPY mini-tms.conf /etc/apache2/sites-enabled/000-default.conf

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -

RUN apt-get update && apt-get install -y \
    git-core \
    nodejs \
    zip \
    unzip \
    && docker-php-ext-install pdo pdo_mysql \
    && a2enmod rewrite

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer