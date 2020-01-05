FROM php:5.6-apache
RUN docker-php-ext-install mysqli
# allow .htaccess with RewriteEngine
RUN a2enmod rewrite
RUN a2enmod headers
# RUN a2enmod ssl
RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng-dev \
        iputils-ping \
        net-tools \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd
# autorise .htaccess files
RUN sed -i '/<Directory \/var\/www\/>/,/<\/Directory>/ s/AllowOverride None/AllowOverride All/' /etc/apache2/apache2.conf
RUN sed -i 's/;date.timezone =/date.timezone = "Asia\/Hong_Kong"/g' /usr/local/etc/php/php.ini-production
RUN cp /usr/local/etc/php/php.ini-production /usr/local/etc/php/php.ini
