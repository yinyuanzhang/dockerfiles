FROM composer:1.7 AS composer
LABEL MAINTAINER="Andrew Lehman <alehman@edc.nyc>"
COPY composer.* /composer/
COPY app/ /composer/app
WORKDIR /composer
RUN composer install --no-interaction --optimize-autoloader --no-dev

FROM php:7.3-cli
COPY app/ /usr/src/app
COPY --from=composer /composer/ /usr/src/
WORKDIR /usr/src/app
CMD ["php", "-f", "main.php"]
