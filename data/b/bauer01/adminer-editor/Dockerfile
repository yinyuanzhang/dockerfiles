FROM php

RUN docker-php-ext-install pdo_mysql

WORKDIR /var/www
RUN rm -rf html
COPY . .

CMD	[ "php", "-S", "[::]:80", "-t", "/var/www/html" ]

EXPOSE 80
