FROM php:7.3-fpm

MAINTAINER Nicolas Thal <nico.th4l@gmail.com>
MAINTAINER Jérémy GIGNON <jeremy@gignon.fr>

COPY config/php.ini /usr/local/etc/php/

RUN pecl install redis-3.1.4 \
    && docker-php-ext-enable redis

RUN docker-php-ext-install opcache
RUN docker-php-ext-enable opcache

WORKDIR /tmp

RUN apt-get update \
    && apt-get install -y wget gnupg2 \
    && wget -O - https://packagecloud.io/gpg.key | apt-key add - \
    && wget -q -O - https://packages.blackfire.io/gpg.key | apt-key add - \
    && echo "deb http://packages.blackfire.io/debian any main" | tee /etc/apt/sources.list.d/blackfire.list \
    && apt-get update \
    && apt-get install -y blackfire-agent blackfire-php git libgeoip-dev libicu-dev

# Install GeoIP
RUN git clone https://github.com/Zakay/geoip.git \
    && cd geoip \
    && phpize \
    && ./configure \
    && make \
    && make install \
    && docker-php-ext-enable geoip

# Install intl
RUN docker-php-ext-configure intl \
  && docker-php-ext-install intl

# Install gmp
RUN apt-get update && apt-get install -y libgmp-dev
RUN ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h
RUN docker-php-ext-install gmp

# Install zip / zlib
RUN apt-get update && apt-get install -y zip unzip libzip-dev
RUN docker-php-ext-install zip

COPY --from=composer:1.8 /usr/bin/composer /usr/bin/composer
