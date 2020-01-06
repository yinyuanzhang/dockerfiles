######
# See: https://hub.docker.com/_/php/
######

FROM php:7.1.10-fpm
MAINTAINER rojer <rojerchen@qq.com>

######
# You can install php extensions using docker-php-ext-install
######

RUN apt-get -y update && apt-get -y install \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
        libmemcached-dev \
        zlib1g-dev \
        zip \
        unzip \
        git \
        cron \
        supervisor \
        vim \
    && pecl install memcached \
    && docker-php-ext-enable memcached \
    && docker-php-ext-install -j$(nproc) iconv mcrypt \
    && docker-php-ext-install pdo_mysql \
    && docker-php-ext-install bcmath \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd 
    
  
RUN curl https://dl.laravel-china.org/composer.phar -o /usr/local/bin/composer \
    && chmod a+x /usr/local/bin/composer \
    && composer config -g repo.packagist composer https://packagist.laravel-china.org

RUN mkdir -p /etc/supervisord/log && mkdir -p /etc/supervisord/conf

VOLUME  ["/etc/supervisord"]