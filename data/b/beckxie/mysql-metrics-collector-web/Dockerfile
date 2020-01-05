FROM php:7.3
RUN docker-php-ext-install mysqli
RUN pecl install redis \
    && docker-php-ext-enable redis
COPY . /var/www/html
WORKDIR /var/www/html
EXPOSE 5566
ENTRYPOINT ["php", "-S", "0.0.0.0:5566"]