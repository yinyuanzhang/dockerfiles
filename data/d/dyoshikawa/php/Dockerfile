FROM php:7.2-alpine
MAINTAINER dyoshikawa

# make PHP environment
# install packages
RUN apk add -U --no-cache bash git curl-dev libxml2-dev postgresql-dev libpng-dev libjpeg-turbo-dev

# install PHP extensions
RUN docker-php-source extract
RUN cp /usr/src/php/ext/openssl/config0.m4 /usr/src/php/ext/openssl/config.m4
RUN docker-php-ext-configure gd --with-png-dir=/usr/include --with-jpeg-dir=/usr/include
RUN docker-php-ext-install pdo pdo_mysql mysqli pdo_pgsql pgsql mbstring curl \
    ctype xml json tokenizer openssl gd zip

# install zip, unzip and composer
RUN apk add --no-cache zip unzip \
    && curl -sS https://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer

# install composer plugin
RUN composer global require hirak/prestissimo
RUN composer global require phpstan/phpstan:@dev

# install dockerize
ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz
