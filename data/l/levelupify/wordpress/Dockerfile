FROM php:5.6-apache

RUN a2enmod rewrite

# install the PHP extensions we need
RUN apt-get update && apt-get install -y libpng-dev libjpeg-dev && rm -rf /var/lib/apt/lists/* \
  && docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
  && docker-php-ext-install gd
RUN docker-php-ext-install mysqli
RUN pecl install redis && docker-php-ext-enable redis

CMD ["apache2-foreground"]