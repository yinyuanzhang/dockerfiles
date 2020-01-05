FROM php:fpm-alpine
MAINTAINER Nocturlab
VOLUME /app
#WORKDIR /app

RUN   apk update \
  &&   apk add ca-certificates wget php-mysqli php-mysqlnd \
  &&   update-ca-certificates
RUN docker-php-ext-install mysqli && \
    docker-php-ext-install pdo_mysql
