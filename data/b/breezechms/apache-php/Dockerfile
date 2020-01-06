FROM php:5.6-apache

MAINTAINER Alex Ortiz-Rosado <alex@breezechms.com>

RUN apt-get update -qq && apt-get install -qqy \
      openssl \
      mysql-client \
      zlib1g-dev \
      libgd-dev \
      libpng-dev \
      libjpeg62-turbo-dev \
      libfreetype6-dev \
      libtidy-dev \
      libz-dev \
      libmemcached-dev \
  && rm -rf /var/lib/apt/lists/*

COPY php.ini /usr/local/etc/php/

RUN docker-php-ext-configure pdo_mysql --with-pdo-mysql=mysqlnd \
  && docker-php-ext-configure mysql --with-mysql=mysqlnd \
  && docker-php-ext-configure mysqli --with-mysqli=mysqlnd \
  && docker-php-ext-configure zip --enable-zip \
  && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \
                                 --with-jpeg-dir=/usr/include/

RUN pecl install memcached-2.2.0
RUN echo extension=memcached.so >> /usr/local/etc/php/conf.d/memcached.ini

RUN pear channel-discover zenovich.github.io/pear \
  && pecl install zenovich/runkit
RUN echo extension=runkit.so >> /usr/local/etc/php/php.ini

RUN pecl install xdebug-2.5.5 \
    && echo zend_extension=xdebug.so >> /usr/local/etc/php/php.ini \
    && echo xdebug.remote_enable=on >> /usr/local/etc/php/php.ini \
    && echo xdebug.remote_autostart=off >> /usr/local/etc/php/php.ini

RUN docker-php-ext-install  -j$(nproc) \
    pdo_mysql \
    mysqli \
    mysql \
    zip \
    gd \
    exif \
    tidy

RUN a2enmod rewrite headers ssl
RUN a2ensite default-ssl

RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/ssl/private/ssl-cert-snakeoil.key \
    -out /etc/ssl/certs/ssl-cert-snakeoil.pem \
    -subj "/C=US/ST=Michigan/L=Grand Rapids/O=BreezeChMS/OU=Org/CN=breezechms.docker"
