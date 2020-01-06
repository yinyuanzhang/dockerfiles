############################################################

# Dockerfile to build laravel container images

# Based on php:7-fpm 创建一个独立的镜像

# extension: mysql、mongo、compose: https://mirrors.aliyun.com/composer/

############################################################
# base
FROM php:7-fpm

USER root
RUN useradd --create-home --no-log-init --shell /bin/bash lewis
# RUN adduser lewis sudoRUN echo 'lewis:123456' | chpasswd

RUN apt-get update && apt-get install -y \
    && apt-get install -y libcurl4-openssl-dev pkg-config libssl-dev \
    && apt-get install libzip-dev -y \
    && docker-php-ext-install zip \
    && docker-php-ext-enable zip \
    && apt-get install git -y \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# install mysql ext
RUN apt-get update \
    && apt-get install -y iputils-ping \
    && docker-php-ext-install mysqli && docker-php-ext-enable mysqli

# install mongodb ext
RUN pecl install mongodb
RUN docker-php-ext-enable mongodb

# install composer
RUN apt-get update \
    && apt-get install curl \
    && curl -sS https://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer

# workdir
USER lewis
WORKDIR /var/www/html
# RUN /usr/local/bin/composer install
RUN /usr/local/bin/composer config -g repo.packagist composer https://mirrors.aliyun.com/composer/

CMD ["php-fpm"]

### end