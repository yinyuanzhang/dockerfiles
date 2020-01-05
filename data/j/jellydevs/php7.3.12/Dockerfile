FROM php:7.3.12

RUN dpkg --configure -a
RUN apt-get update && apt-get install -y g++ git unzip zlib1g-dev libicu-dev libzip-dev libpng-dev libjpeg-dev libfreetype6-dev libjpeg62-turbo-dev libpng-dev postgresql libpq-dev gnupg2

RUN docker-php-ext-install gd
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/
RUN docker-php-ext-install -j$(nproc) gd
RUN docker-php-ext-install pdo pdo_pgsql
RUN docker-php-ext-install zip
RUN docker-php-ext-enable zip
RUN docker-php-ext-install intl

# Install dependencies
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer