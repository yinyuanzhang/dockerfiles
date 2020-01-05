FROM php:7.2-apache

COPY . /var/www/html/
RUN chown www-data:www-data -R /var/www/html/

# PHP extensions
RUN a2enmod rewrite && service apache2 restart
RUN docker-php-ext-install pdo_mysql
