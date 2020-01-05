FROM composer:1.8 AS composer

RUN composer global require hirak/prestissimo

COPY composer.json composer.json
COPY stubs stubs
RUN  composer install --no-dev --optimize-autoloader --prefer-dist


FROM php:7.4-cli
WORKDIR /rector

COPY . .
COPY --from=composer /app .

ENTRYPOINT [ "bin/rector" ]
