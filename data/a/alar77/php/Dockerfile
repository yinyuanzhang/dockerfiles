FROM php:7.2-alpine

RUN apk add --no-cache git rsync openssh bash
RUN docker-php-ext-install -j$(nproc) mysqli pdo pdo_mysql bcmath &&  docker-php-source delete
