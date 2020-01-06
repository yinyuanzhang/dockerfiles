FROM php:7.0-apache

RUN apt-get update
RUN docker-php-ext-install pdo_mysql mbstring
RUN echo 'error_reporting = E_ALL' >> /usr/local/etc/php/conf.d/99_myconf.ini
RUN echo 'date.timezone = Asia/Tokyo' >> /usr/local/etc/php/conf.d/99_myconf.ini

COPY apache2.conf /etc/apache2/apache2.conf
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf

RUN a2enmod rewrite
RUN /etc/init.d/apache2 restart
RUN chown -R www-data.www-data /var/www/html/
