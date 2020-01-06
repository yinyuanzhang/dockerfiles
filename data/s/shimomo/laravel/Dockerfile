#
#--------------------------------------------------------------------------
# Image Setup
#--------------------------------------------------------------------------
#

FROM php:7.3.3-apache

LABEL maintainer="shimomo <yuichi@shimomo.net>"

WORKDIR /var/www/laravel

#
#--------------------------------------------------------------------------
# PHP Setup
#--------------------------------------------------------------------------
#

# Install the tools
RUN apt-get update
RUN apt-get install -y libgmp10 libgmp-dev libpq-dev libxml2-dev libzip-dev zlib1g-dev zip unzip

# Install the PHP gmp extension
RUN docker-php-ext-install gmp

# Install the PHP xml extension
RUN docker-php-ext-install xml

# Install the PHP zip extension
RUN docker-php-ext-install zip

# Install the PHP bcmath extension
RUN docker-php-ext-install bcmath

# Install the PHP mbstring extension
RUN docker-php-ext-install mbstring

# Install the PHP pdo_mysql extension
RUN docker-php-ext-install pdo_mysql

# Install the PHP pdo_pgsql extension
RUN docker-php-ext-install pdo_pgsql

# Install the PHP composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

#
#--------------------------------------------------------------------------
# Node.js Setup
#--------------------------------------------------------------------------
#

# Install the gnupg
RUN apt-get install -y gnupg

# Install the Node.js
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y nodejs

#
#--------------------------------------------------------------------------
# Apache Setup
#--------------------------------------------------------------------------
#

COPY ./000-default.conf /etc/apache2/sites-available/000-default.conf
COPY ./001-default-ssl.conf /etc/apache2/sites-available/001-default-ssl.conf

RUN usermod -u 1000 www-data
RUN groupmod -g 1000 www-data

RUN apt-get install -y ssl-cert
RUN make-ssl-cert generate-default-snakeoil

RUN a2enmod ssl
RUN a2enmod rewrite

RUN a2ensite 001-default-ssl.conf

#
#--------------------------------------------------------------------------
# Port Setup
#--------------------------------------------------------------------------
#

EXPOSE 80
EXPOSE 443
