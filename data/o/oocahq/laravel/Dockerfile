FROM php:7.2-fpm-alpine3.9

RUN apk add --no-cache freetype libpng libjpeg-turbo freetype-dev libpng-dev libjpeg-turbo-dev wget curl git php php-curl php-openssl php-json php-phar php-dom && \
    docker-php-ext-configure gd \
        --with-gd \
        --with-freetype-dir=/usr/include/ \
        --with-png-dir=/usr/include/ \
        --with-jpeg-dir=/usr/include/ && \
    NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) && \
    docker-php-ext-install -j${NPROC} gd

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer 

RUN apk add --no-cache gmp-dev
RUN apk add --no-cache curl-dev
RUN apk add --no-cache libxml2
RUN apk add --no-cache libgcrypt-dev
RUN apk add --no-cache libxml2-dev
RUN docker-php-ext-install dom
RUN docker-php-ext-install mysqli
RUN docker-php-ext-install pdo 
RUN docker-php-ext-install pdo_mysql 
RUN docker-php-ext-install mbstring 
RUN docker-php-ext-install json 
RUN docker-php-ext-install tokenizer
RUN docker-php-ext-install gmp
RUN docker-php-ext-install curl
RUN apk add --no-cache bzip2-dev
RUN docker-php-ext-install bz2 
RUN docker-php-ext-install phar 
RUN docker-php-ext-install sockets 
RUN docker-php-ext-install exif 
RUN docker-php-ext-install bcmath
RUN docker-php-ext-install ctype 
RUN apk add --no-cache libzip-dev
RUN docker-php-ext-install zip 
