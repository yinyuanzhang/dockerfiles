FROM php:7.2-fpm

MAINTAINER "The Doalitic Team" <devops@doalitic.com>

WORKDIR /var/www/

RUN apt-get update && apt-get install -y locales-all git libpng-dev libzip-dev libxml2-dev \
    && docker-php-ext-install bcmath gd mbstring pdo_mysql soap sockets zip intl pcntl

RUN sh -c 'curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer'

ENV DOCKERIZE_VERSION v0.6.1
RUN apt-get update && apt-get install -y wget && wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

RUN mkdir -p /etc/container/templates

ADD ./php-fpm.conf.tpl /etc/container/templates/

EXPOSE 9000

CMD ["dockerize", "-template", "/etc/container/templates/php-fpm.conf.tpl:/usr/local/etc/php-fpm.conf", "php-fpm"]
