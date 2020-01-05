FROM php:7.2-apache

ENV username fop
ENV groupname fop
ENV userid 1000
ENV groupid 1000

ENV REDIS_VERSION "5.0.2"
ENV XDEBUG_VERSION "2.7.2"

ENV DEBIAN_FRONTEND "noninteractive"

RUN apt-get update && apt-get install -y \
        gettext \
        iproute2 \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng-dev \
        libxml2-dev \
        mc \
        nano \
        redis-tools \
        zlib1g-dev \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

RUN docker-php-ext-install -j4 calendar iconv pdo_mysql soap \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j4 gd

RUN pecl install xdebug-$XDEBUG_VERSION \
    && pecl install redis-$REDIS_VERSION \
    && docker-php-ext-enable redis \
    && docker-php-ext-enable xdebug

RUN groupadd -g $groupid -r $groupname \
	&& useradd -u $userid -g $groupname --shell /bin/bash --create-home $username

RUN chown -R $username:$groupname /var/www

ENV APACHE_RUN_USER=$username
ENV APACHE_RUN_GROUP=$groupname

RUN a2enmod rewrite headers
