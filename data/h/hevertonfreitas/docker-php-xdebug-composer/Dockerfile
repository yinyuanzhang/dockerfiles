FROM php:7.0

RUN apt-get update && apt-get install --no-install-recommends -y \
  git \
  libpq-dev \
  libmcrypt-dev \
  libreadline-dev \
  curl \
  zip \
  unzip \
  libpng-dev \
  zlib1g-dev \
  libicu-dev \
  g++ \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
 
RUN docker-php-ext-configure intl
RUN docker-php-ext-install \
  mbstring \
  pdo \
  mcrypt \
  gd \
  intl \
  pdo_mysql \
  pdo_pgsql
RUN docker-php-source extract
RUN pecl install xdebug
RUN docker-php-ext-enable xdebug
RUN docker-php-source delete

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
RUN php composer-setup.php
RUN php -r "unlink('composer-setup.php');"
RUN mv composer.phar /usr/local/bin/composer
