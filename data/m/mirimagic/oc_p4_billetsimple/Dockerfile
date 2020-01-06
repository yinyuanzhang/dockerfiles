FROM php:7.3.7-apache
RUN docker-php-ext-install mysqli pdo pdo_mysql
RUN a2enmod rewrite

COPY src/ /var/www/html/

COPY docker/apache/billet-simple.conf /etc/apache2/sites-enabled/billet-simple.conf

RUN chown -R root:www-data /var/www/html/Web
RUN chmod -R 775 /var/www/html/Web/images/uploads
