FROM php:5-fpm

RUN apt-get update && apt-get install -y \
      libfreetype6-dev \
      libjpeg62-turbo-dev \
      libmcrypt-dev \
      libpng-dev \
      git \
    && rm -rf /var/lib/apt/lists/*

RUN docker-php-ext-configure gd \
      --with-freetype-dir=/usr/include/ \
      --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install \
      gd \
      mcrypt \
      opcache \
      pcntl \
      pdo_mysql \
      sockets zip

COPY --from=composer:latest /usr/bin/composer /usr/bin/composer
