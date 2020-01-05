FROM composer AS builder

COPY ./httpdocs /app/httpdocs/
COPY ./src /app/src/
COPY ./bootstrap.php /app/
COPY ./composer.* /app/

WORKDIR /app
RUN composer install --no-dev --ignore-platform-reqs


FROM php:apache

ENV APACHE_DOCUMENT_ROOT /app/httpdocs

RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-available/*.conf && \
    sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf

RUN a2enmod rewrite

RUN docker-php-ext-install pdo_mysql

COPY --from=builder /app /app