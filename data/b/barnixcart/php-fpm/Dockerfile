FROM php:5.6-fpm

LABEL maintainer="Pavel Gavrilenko <paulgavrilenko@gmail.com>"

RUN apt-get update && \
  apt-get upgrade -y && \
  apt-get install -y --no-install-recommends \
    curl \
    libjpeg-dev \
    libpng-dev \
    libfreetype6-dev \
    libmcrypt-dev \
  && rm -rf /var/lib/apt/lists/*

RUN docker-php-ext-install mcrypt

RUN docker-php-ext-install pdo_mysql \
  && docker-php-ext-install mysqli

RUN docker-php-ext-configure gd \
  --with-freetype-dir=/usr/include/freetype2 \
  --with-jpeg-dir=/usr/include \
  && docker-php-ext-install gd
    
RUN apt-get update && apt-get install -y libmagickwand-dev --no-install-recommends \
  && rm -rf /var/lib/apt/lists/*
  
RUN printf "\n" | pecl install imagick
RUN docker-php-ext-enable imagick

RUN pecl install xdebug-2.5.5 && \
  docker-php-ext-enable xdebug

RUN apt-get update && apt-get install -y wget \
  && rm -rf /var/lib/apt/lists/*
  
RUN wget https://github.com/mailhog/mhsendmail/releases/download/v0.2.0/mhsendmail_linux_amd64 \
 && chmod +x mhsendmail_linux_amd64 \
 && mv mhsendmail_linux_amd64 /usr/local/bin/mhsendmail

COPY ./php/xc4.0/php.ini /usr/local/etc/php/php.ini
