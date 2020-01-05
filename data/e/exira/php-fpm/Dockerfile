FROM exira/base:3.3.3

MAINTAINER exira.com <info@exira.com>

ENV TIMEZONE=UTC \
    PHP_VERSION=5.6.21

RUN \
    # Pin bison to a pre 3 version, since PHP5 does not support it anymore
    echo 'http://dl-cdn.alpinelinux.org/alpine/v2.6/main' >> /etc/apk/repositories && \

    # Install build and runtime packages
    build_pkgs="build-base re2c file readline-dev autoconf binutils libxml2-dev curl-dev freetype-dev openssl-dev libjpeg-turbo-dev libpng-dev libmcrypt-dev gmp-dev icu-dev libmemcached-dev wget git tzdata" && \
    runtime_pkgs="curl zlib bzip2 bzip2-dev tar make libxml2 readline freetype openssl libjpeg-turbo libpng libmcrypt icu musl ssmtp" && \
    apk update && \
    apk upgrade && \
    apk --no-cache add bison==2.7.1-r0 && \
    apk --update --no-cache add ${build_pkgs} ${runtime_pkgs} && \

    # download unpack php-src
    mkdir /tmp/php && \
    cd /tmp/php && \
    wget https://github.com/php/php-src/archive/php-${PHP_VERSION}.tar.gz --no-check-certificate && \
    tar xzf php-${PHP_VERSION}.tar.gz && \
    cd php-src-php-${PHP_VERSION} && \

    # compile
    cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && \
    echo "${TIMEZONE}" > /etc/timezone && \
    ./buildconf --force && \
    ./configure \
        --prefix=/usr \
        --sysconfdir=/etc/php \
        --with-config-file-path=/etc/php \
        --with-config-file-scan-dir=/etc/php/conf.d \
        --enable-fpm --with-fpm-user=www-data --with-fpm-group=www-data \
        --enable-cli \
        --enable-mbstring \
        --enable-zip \
        --enable-ftp \
        --enable-bcmath \
        --enable-opcache \
        --enable-pcntl \
        --enable-mysqlnd \
        --enable-gd-native-ttf \
        --enable-sockets \
        --enable-exif \
        --enable-soap \
        --enable-calendar \
        --enable-intl \
        --enable-json \
        --enable-dom \
        --enable-libxml --with-libxml-dir=/usr \
        --enable-xml \
        --enable-xmlreader \
        --enable-phar \
        --enable-session \
        --enable-sysvmsg \
        --enable-sysvsem \
        --enable-sysvshm \
        --disable-cgi \
        --disable-debug \
        --disable-rpath \
        --disable-static \
        --disable-phpdbg \
        --with-libdir=/lib/x86_64-linux-gnu \
        --with-curl \
        --with-mcrypt \
        --with-iconv \
        --with-gd --with-jpeg-dir=/usr --with-png-dir=/usr \
        --with-freetype-dir=/usr \
        --with-zlib --with-zlib-dir=/usr \
        --with-bz2=/usr \
        --with-openssl \
        --with-mhash \
        --with-pcre-regex \
        --with-pdo-mysql \
        --with-mysqli \
        --with-mysql \
        --with-readline \
        --with-xmlrpc \
        --with-pear && \
    make && \
    make install && \
    make clean && \

    # strip debug symbols from the binary (GREATLY reduces binary size)
    strip -s /usr/bin/php && \

    # remove PHP dev dependencies
    apk del bison ${build_pkgs} && \

    # create session dir
    mkdir -p /var/lib/php7/sessions && \

    # add www-data user
    mkdir -p /home/www-data && \
    addgroup -g 433 -S www-data && \
    adduser -u 431 -S -D -G www-data -h /home/www-data -s /sbin/nologin www-data && \
    chown -R www-data:www-data /home/www-data && \

    # other clean up
    cd / && \
    rm -rf /var/cache/apk/* && \
    rm -rf /tmp/* && \
    rm -rf /var/www/*

ADD root /

RUN chown -R www-data:www-data /var/www && \
    chown -R www-data:www-data /var/lib/php7/sessions

RUN sed -i "s|;date.timezone =.*|date.timezone = ${TIMEZONE}|" /etc/php/php.ini

WORKDIR /var/www/

VOLUME /var/www/

EXPOSE 9000
