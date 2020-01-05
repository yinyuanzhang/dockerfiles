FROM php:7.0

RUN apt-get update && apt-get install -y unzip
RUN pecl install xdebug-2.5.0
RUN docker-php-ext-enable xdebug
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer