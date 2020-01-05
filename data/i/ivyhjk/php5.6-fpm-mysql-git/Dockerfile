FROM php:5.6-fpm-alpine

RUN apk update
RUN docker-php-ext-install mysqli pdo pdo_mysql
RUN apk add --no-cache git
