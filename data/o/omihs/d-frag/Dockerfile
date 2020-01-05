FROM php:7-apache
LABEL maintainer "shimo@project-com.com"

WORKDIR /var/www/html

COPY ./src /var/www/html

RUN apt-get update && \
    apt-get install -y git sqlite3 libsqlite3-dev zlib1g-dev && \
    docker-php-ext-install mbstring pdo pdo_sqlite zip && \
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer && \
    composer update
RUN chown -R www-data:www-data /var/www
