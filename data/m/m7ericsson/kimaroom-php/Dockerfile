FROM php:5.6.40-fpm-alpine3.8

MAINTAINER m7ericsson <uemoto@ju-net.jp>

COPY ./config/php.ini /usr/local/etc/php/php.ini

RUN apk update -q \
  && apk add --no-cache --virtual .build-deps ${PHPIZE_DEPS} \
  && apk add --no-cache \
    libjpeg-turbo-dev \
    libpng-dev \
    freetype-dev \
    libmcrypt-dev \
    gpgme-dev \
    libmemcached-dev \
    zlib-dev \
    libxml2-dev \
    libxslt-dev \
    git \
    autoconf \
    build-base \
  && pecl install mailparse-2.1.6 \
  && pecl install gnupg \
  && yes '' | pecl install memcached-2.2.0 \
  && yes '' | pecl install APCu-4.0.11 \
  && pecl install xdebug-2.4.0 \
  && docker-php-ext-configure gd        --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
  && docker-php-ext-configure pdo_mysql --with-pdo-mysql=mysqlnd \
  && docker-php-ext-configure opcache   --enable-opcache \
  && docker-php-ext-install -j$(nproc) \
    gd \
    mysql \
    pdo_mysql \
    opcache \
    bcmath \
    mcrypt \
    soap \
    exif \
    xsl \
    zip \
  && docker-php-ext-enable mailparse gnupg memcached apcu xdebug \
  && apk del .build-deps --purge \
  && echo -e "apc.enable_cli=1\napc.filters=\"^phar://\"" >> /usr/local/etc/php/conf.d/docker-php-ext-apcu.ini

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN composer global require friendsofphp/php-cs-fixer:v2.15.0 --dev
ENV PATH $PATH:/root/.composer/vendor/bin
RUN echo $PATH

ENTRYPOINT []
CMD php-fpm