FROM php:7.1-alpine

MAINTAINER Vicampo.de Devops Team <devops@vicampo.de>

#RUN php -i | grep curl && php -m | grep curl
#RUN php -i | grep mysql && php -m | grep mysql

RUN apk add --update freetype-dev libpng-dev curl libcurl curl-dev libjpeg-turbo-dev libxml2-dev autoconf g++ imagemagick-dev libtool make pcre-dev \

    # bash is needed for some scripts
    && apk add bash git supervisor openssh \

    && docker-php-ext-install sockets \

    # ext gd
    && docker-php-ext-install gd \
    && docker-php-ext-configure gd \
        --with-gd \
        --with-freetype-dir=/usr/include/ \
        --with-png-dir=/usr/include/ \
        --with-jpeg-dir=/usr/include/ \

    && docker-php-ext-install soap \

    # mysql (pdo needed for phinx, illuminate uses mysqlnd)
    && apk add mysql-client \
    && docker-php-ext-install mysqli \
    && docker-php-ext-install pdo_mysql \

    # optcode cache
    && docker-php-ext-install opcache \
    && docker-php-ext-enable opcache \

    # apcu cache
    && pecl install apcu \
    && docker-php-ext-enable apcu \

    # php-ds (datastructures)
    && pecl install ds \
    && docker-php-ext-enable ds \

    # imagemagick
    && pecl install imagick \
    && docker-php-ext-enable imagick \

    # solr
    && pecl install solr \
    && docker-php-ext-enable solr \

    # redis
    && pecl install redis \
    && docker-php-ext-enable redis \

    # pcntl - multithreading
    && docker-php-ext-install pcntl \
    && docker-php-ext-enable pcntl \

    # xdebug - disabled by default
    && pecl install xdebug \

    # socket lib
    && docker-php-ext-install sockets \
    && docker-php-ext-enable sockets \

    # libevent needs sockets to be loaded. but 'l' is before 's' in alphnum
    # rename ini to prevent php-startup-errors
    && mv \
      /usr/local/etc/php/conf.d/docker-php-ext-sockets.ini \
      /usr/local/etc/php/conf.d/01_docker-php-ext-sockets.ini \

    # libevent - performance to scheduled events
    && apk add --update \
      libevent-dev \
      openssl-dev \
    && pecl install event \
    && docker-php-ext-enable event \

    # remove dev-packaged
    && apk del autoconf g++ libtool make \

    # remove tmp-data
    && rm -rf /tmp/* /var/cache/apk/*


COPY php.production.ini /usr/local/etc/php/conf.d/01-base.ini

# Install Composer and make it available in the PATH
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/ --filename=composer
