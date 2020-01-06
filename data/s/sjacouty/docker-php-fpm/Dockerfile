FROM php:7-fpm-alpine3.7
MAINTAINER Sylvain JACOUTY

RUN apk -U add php7-gd php7-snmp php7-mcrypt php7-pdo_mysql \
 && rm -rf /var/cache/apk/*

RUN docker-php-ext-install pdo pdo_mysql

EXPOSE 9000
CMD ["php-fpm"]
