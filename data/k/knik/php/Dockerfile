FROM php:5.6-fpm-stretch

RUN apt-get -y update && apt-get -y install \
        libmcrypt-dev \
        libc-dev \
        libfreetype6 \
        libjpeg-dev \
        libxpm-dev \
        libpng-dev \
        libicu-dev  \
        libxslt-dev \
        libmemcached-dev \
        bzip2 \
        libbz2-dev \
        libxml2-dev \
    --no-install-recommends && rm -r /var/lib/apt/lists/*

RUN docker-php-ext-install bcmath \
        bz2 \
        calendar \
        dba \
        exif \
        gd \
        gettext \
        mysqli \
        pcntl \
        pdo_mysql \
        shmop \
        soap \
        sockets \
        sysvmsg \
        sysvsem \
        sysvshm \
        wddx \
        zip \
        opcache

RUN echo "date.timezone = Europe/Moscow" > /usr/local/etc/php/php.ini
