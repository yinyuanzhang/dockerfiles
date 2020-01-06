FROM php:7.3.4
RUN apt-get update && apt-get install -y unzip zlib1g-dev libzip-dev zip git
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN docker-php-ext-install bcmath mysqli pdo pdo_mysql sockets zip
RUN pecl install xdebug
RUN docker-php-ext-enable xdebug
