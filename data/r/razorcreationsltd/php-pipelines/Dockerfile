FROM php:7.1

ENV COMPOSER_HOME=/root/.composer \
    PATH=$PATH:$COMPOSER_HOME/vendor/bin

RUN apt-get update \
 && apt-get install -y \
    g++ \
    git \
    gnupg \
    libpng-dev \
    make \
    unzip \
 && docker-php-ext-install -j$(nproc) \
    gd \
    pdo_mysql \
 && pecl install xdebug \
 && echo "zend_extension=/usr/local/lib/php/extensions/no-debug-non-zts-20160303/xdebug.so" > /usr/local/etc/php/conf.d/xdebug.ini \
 && curl -sS https://getcomposer.org/installer | php -- --install-dir=/bin --filename=composer \
 && curl -sL https://deb.nodesource.com/setup_9.x | bash - \
 && apt-get install -y nodejs
