FROM php:7.2.21-apache

COPY sites/ /etc/apache2/sites-available/

RUN a2enmod \
         alias \
         authz_host \
         deflate dir \
         expires \
         headers \
         mime \
         rewrite \
         autoindex \
         negotiation \
         setenvif \
   && apt-get update \
   && apt-get install -y \
         zlib1g-dev \
         libpng-dev \
         libjpeg-dev \
         libjpeg62-turbo-dev \
         libfreetype6-dev \
         nano \
   && docker-php-ext-configure \
         gd \
             --with-gd \
             --with-jpeg-dir \
             --with-png-dir \
             --with-zlib-dir \
             --with-freetype-dir \
             --enable-gd-native-ttf \
   && docker-php-ext-install \
         gd \
         pdo_mysql \
         mysqli
      
EXPOSE 80
