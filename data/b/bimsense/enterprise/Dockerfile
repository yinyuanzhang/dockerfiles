FROM php:7.2.7-apache

# Enable reqrite module
RUN a2enmod rewrite

# Install php pgsql extension
RUN apt-get update && apt-get install -y libpq-dev && docker-php-ext-install pdo pdo_pgsql

# Install Yarn package manager
RUN apt-get update && apt-get install -y yarn

ADD ./apache2/httpd.conf /etc/apache2/sites-available/000-default.conf