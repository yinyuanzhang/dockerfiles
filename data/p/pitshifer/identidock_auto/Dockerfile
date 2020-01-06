FROM php:7.2-apache

#RUN groupadd -r www && useradd -r -g www www

RUN pecl install redis-4.0.1 \
    && docker-php-ext-enable redis

WORKDIR /var/www/html
COPY app/ /var/www/html/

#EXPOSE 80

#ENV APACHE_RUN_DIR=/var/www/html
#ENV APACHE_RUN_USER=www
#ENV APACHE_RUN_GROUP=www
#ENV APACHE_LOG_DIR=/var/log/apache2
#ENV APACHE_PID_FILE=/var/www/pid

#USER www

#CMD ["apache2", "-D", "FOREGROUND"]
