FROM php:7.1.10-fpm

ENV DEBIAN_FRONTEND noninteractive
ENV LC_ALL en_US.UTF-8
ENV LANGUAGE en_US:en

RUN \
 apt-get update &&\
 apt-get -y --no-install-recommends install curl locales apt-utils &&\
 echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen &&\
 locale-gen en_US.UTF-8 &&\
 /usr/sbin/update-locale LANG=en_US.UTF-8 &&\
    apt-get install -y --no-install-recommends \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
        libcurl4-gnutls-dev \
        libgmp-dev \
        unzip \
        git \
        libssl-dev &&\
    pecl install mongodb &&\
    echo "extension=mongodb.so" > /usr/local/etc/php/conf.d/ext-mongodb.ini &&\
    docker-php-ext-install -j$(nproc) gd iconv mcrypt pdo_mysql json mbstring curl exif zip gmp &&\
    docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ &&\
    pecl install xdebug &&\
    docker-php-ext-enable xdebug &&\
    rm -rf /var/lib/apt/lists/* &&\
    apt-get autoclean && apt-get clean && apt-get autoremove

RUN \
 curl -sSL https://getcomposer.org/installer | php -- --filename=composer --install-dir=/usr/bin &&\
 curl -sSL https://phar.phpunit.de/phpunit.phar -o /usr/bin/phpunit  && chmod +x /usr/bin/phpunit  &&\
 curl -sSL http://codeception.com/codecept.phar -o /usr/bin/codecept && chmod +x /usr/bin/codecept &&\
 rm -rf /root/.composer /tmp/* /var/lib/apt/lists/*
