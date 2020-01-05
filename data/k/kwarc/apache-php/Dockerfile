# Start from a normal apache php image
FROM php:7-apache-stretch

ADD errorlevel.ini /usr/local/etc/php/conf.d

## And the extensions we need, some may already be loaded
RUN apt-get update \
    && apt-get install -y libedit-dev libreadline-dev libxml2-dev \
    && rm -rf /var/lib/apt/lists/* \
    && docker-php-ext-install json opcache readline xml \
    && docker-php-ext-enable json opcache readline xml

# We are serving our website under port 80
EXPOSE 80
VOLUME /var/www/html