FROM php:7.1

RUN apt-get update && apt-get install -y \
    git \
    wget \
    libpng-dev \
    zip \
    unzip \
    libicu-dev

RUN docker-php-ext-install gd
RUN docker-php-ext-install mysqli
RUN docker-php-ext-configure intl
RUN docker-php-ext-install intl

RUN wget http://xdebug.org/files/xdebug-2.6.1.tgz \
    && tar -xvzf xdebug-2.6.1.tgz \
    && cd xdebug-2.6.1 \
    && phpize \
    && ./configure \
    && make \
    && cp modules/xdebug.so /usr/local/lib/php/extensions/no-debug-non-zts-20160303 \
    && echo "zend_extension = /usr/local/lib/php/extensions/no-debug-non-zts-20160303/xdebug.so" > /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.coverage_enable=1" >> /usr/local/etc/php/conf.d/xdebug.ini \
    && cd .. \
    && rm -rf xdebug*
