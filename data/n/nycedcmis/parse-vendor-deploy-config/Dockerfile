FROM composer:1.7
LABEL MAINTAINER="Andrew Lehman <alehman@edc.nyc>"
COPY composer.* /composer/
WORKDIR /composer
RUN composer install --no-interaction --no-dev --optimize-autoloader

FROM php:7.2-cli
WORKDIR /usr/src/app
COPY --from=0 /composer/ .
COPY app ./app
RUN mkdir /output
ENTRYPOINT [ "php", "-f", "app/main.php" ]
