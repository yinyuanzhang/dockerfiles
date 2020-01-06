FROM php:7-apache
RUN apt -yqq update
RUN apt -yqq install libxml2-dev zlib1g-dev libzip-dev libpng-dev libjpeg-dev libmagickwand-dev libmcrypt-dev
RUN docker-php-ext-install pdo_mysql
RUN docker-php-ext-install mysqli
RUN docker-php-ext-install xml
RUN docker-php-ext-install zip
RUN docker-php-ext-install exif
RUN docker-php-ext-install bcmath
RUN docker-php-ext-configure gd --with-jpeg-dir=/usr/include/ && docker-php-ext-install gd
RUN pecl install mcrypt-1.0.2 && docker-php-ext-enable mcrypt
RUN pecl install imagick && docker-php-ext-enable imagick
RUN a2enmod rewrite
RUN a2enmod expires
RUN a2enmod env
RUN mv $PHP_INI_DIR/php.ini-production $PHP_INI_DIR/php.ini
