FROM composer:latest AS composer
FROM php:7.2-apache
#FROM richarvey/nginx-php-fpm:latest

COPY --from=composer /usr/bin/composer /usr/bin/composer
RUN apt update && apt install -y git
WORKDIR /var/www/html

COPY . /var/www/html/
RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng-dev \
    && docker-php-ext-install -j$(nproc) iconv \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd

RUN docker-php-ext-install exif

RUN cd /var/www/html
ENV COMPOSER_ALLOW_SUPERUSER 1
ENV HIDE_NGINX_HEADERS=1
ENV RUN_SCRIPTS=1
#s3 settings
ENV AWS_ACCESS_KEY_ID="you_access_key_id"
ENV AWS_SECRET_ACCESS_KEY="you_secret_key_id"
ENV ENDPOINT_URL="http://example.com"
ENV BUCKET="you_bucket"
#set false in production
ENV DEBUG=1
ENV SECURITY=1
ENV WATERMARK=1
ENV SERVER_KEY="server_key_delete_me_on_production"
ENV SECURITY_SALT="security_salt_delete_me_on_production"
ENV CLIENT_USER="client_user_delete_me_on_production"
ENV CLIENT_PASS="client_pass_delete_me_on_production"


RUN composer update
RUN a2enmod rewrite
RUN service apache2 restart

EXPOSE 80