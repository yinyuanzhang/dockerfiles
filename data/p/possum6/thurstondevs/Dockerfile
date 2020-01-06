FROM php:7.2-apache
RUN a2enmod rewrite
COPY app/ /var/www/html/
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer