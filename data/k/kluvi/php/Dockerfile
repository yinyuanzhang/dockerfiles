FROM php:7.3-apache

ADD php.ini $PHP_INI_DIR/php.ini
ADD apache2.conf /etc/apache2/apache2.conf
RUN a2enmod rewrite