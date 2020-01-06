#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
# 拡張モジュールビルドステージ： bz2
#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
FROM php:7.1-fpm-alpine AS build-bz2
RUN set -xe && apk add --update-cache --no-cache autoconf dpkg-dev dpkg file g++ gcc libc-dev make pkgconf re2c
RUN set -xe && apk add --update-cache --no-cache bzip2-dev && docker-php-ext-install bz2

#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
# 拡張モジュールビルドステージ： calendar
#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
FROM php:7.1-fpm-alpine AS build-calendar
RUN set -xe && apk add --update-cache --no-cache autoconf dpkg-dev dpkg file g++ gcc libc-dev make pkgconf re2c
RUN set -xe && docker-php-ext-install calendar

#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
# 拡張モジュールビルドステージ： exif
#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
FROM php:7.1-fpm-alpine AS build-exif
RUN set -xe && apk add --update-cache --no-cache autoconf dpkg-dev dpkg file g++ gcc libc-dev make pkgconf re2c
RUN set -xe && docker-php-ext-install exif

#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
# 拡張モジュールビルドステージ： gettext
#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
FROM php:7.1-fpm-alpine AS build-gettext
RUN set -xe && apk add --update-cache --no-cache autoconf dpkg-dev dpkg file g++ gcc libc-dev make pkgconf re2c
RUN set -xe && apk add --update-cache --no-cache gettext-dev && docker-php-ext-install gettext

#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
# 拡張モジュールビルドステージ： gmp
#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
FROM php:7.1-fpm-alpine AS build-gmp
RUN set -xe && apk add --update-cache --no-cache autoconf dpkg-dev dpkg file g++ gcc libc-dev make pkgconf re2c
RUN set -xe && apk add --update-cache --no-cache gmp-dev && docker-php-ext-install gmp

#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
# 拡張モジュールビルドステージ： mysqli
#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
FROM php:7.1-fpm-alpine AS build-mysqli
RUN set -xe && apk add --update-cache --no-cache autoconf dpkg-dev dpkg file g++ gcc libc-dev make pkgconf re2c
RUN set -xe && docker-php-ext-install mysqli

#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
# 拡張モジュールビルドステージ： shmop
#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
FROM php:7.1-fpm-alpine AS build-shmop
RUN set -xe && apk add --update-cache --no-cache autoconf dpkg-dev dpkg file g++ gcc libc-dev make pkgconf re2c
RUN set -xe && docker-php-ext-install shmop

#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
# 拡張モジュールビルドステージ： opcache
#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
FROM php:7.1-fpm-alpine AS build-opcache
RUN set -xe && apk add --update-cache --no-cache autoconf dpkg-dev dpkg file g++ gcc libc-dev make pkgconf re2c
RUN set -xe && docker-php-ext-install opcache

#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
# 拡張モジュールビルドステージ： pcntl
#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
FROM php:7.1-fpm-alpine AS build-pcntl
RUN set -xe && apk add --update-cache --no-cache autoconf dpkg-dev dpkg file g++ gcc libc-dev make pkgconf re2c
RUN set -xe && docker-php-ext-install pcntl

#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
# 拡張モジュールビルドステージ： pdo_mysql
#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
FROM php:7.1-fpm-alpine AS build-pdo_mysql
RUN set -xe && apk add --update-cache --no-cache autoconf dpkg-dev dpkg file g++ gcc libc-dev make pkgconf re2c
RUN set -xe && docker-php-ext-install pdo_mysql

#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
# 拡張モジュールビルドステージ： sockets
#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
FROM php:7.1-fpm-alpine AS build-sockets
RUN set -xe && apk add --update-cache --no-cache autoconf dpkg-dev dpkg file g++ gcc libc-dev make pkgconf re2c
RUN set -xe && docker-php-ext-install sockets

#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
# 拡張モジュールビルドステージ： wddx
#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
FROM php:7.1-fpm-alpine AS build-wddx
RUN set -xe && apk add --update-cache --no-cache autoconf dpkg-dev dpkg file g++ gcc libc-dev make pkgconf re2c
RUN set -xe && apk add --update-cache --no-cache libxml2-dev && docker-php-ext-install wddx

#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
# 拡張モジュールビルドステージ： xsl
#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
FROM php:7.1-fpm-alpine AS build-xsl
RUN set -xe && apk add --update-cache --no-cache autoconf dpkg-dev dpkg file g++ gcc libc-dev make pkgconf re2c
RUN set -xe && apk add --update-cache --no-cache libxslt-dev && docker-php-ext-install xsl

#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
# 拡張モジュールビルドステージ： zip
#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
FROM php:7.1-fpm-alpine AS build-zip
RUN set -xe && apk add --update-cache --no-cache autoconf dpkg-dev dpkg file g++ gcc libc-dev make pkgconf re2c
RUN set -xe && apk add --update-cache --no-cache zlib-dev libzip-dev && docker-php-ext-install zip

#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
# 拡張モジュールビルドステージ： apcu
#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
#FROM php:7.1-fpm-alpine AS build-apcu
#RUN set -xe && apk add --update-cache --no-cache autoconf dpkg-dev dpkg file g++ gcc libc-dev make pkgconf re2c
#RUN set -xe && yes '' | pecl install apcu && docker-php-ext-enable apcu

#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
# 拡張モジュールビルドステージ： redis
#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
#FROM php:7.1-fpm-alpine AS build-redis
#RUN set -xe && apk add --update-cache --no-cache autoconf dpkg-dev dpkg file g++ gcc libc-dev make pkgconf re2c
#RUN set -xe && yes '' | pecl install redis && docker-php-ext-enable redis

#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
# 拡張モジュールビルドステージ： memcached
#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
#FROM php:7.1-fpm-alpine AS build-memcached
#RUN set -xe && apk add --update-cache --no-cache autoconf dpkg-dev dpkg file g++ gcc libc-dev make pkgconf re2c
#RUN set -xe && apk add --update-cache --no-cache zlib-dev libmemcached-dev && yes '' | pecl install memcached && docker-php-ext-enable memcached

#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
# 稼働用イメージ構築ステージ
#===+====1====+====2====+====3====+====4====+====5====+====6====+====7====+====8====+====9====+====0
FROM php:7.1-fpm-alpine

ARG PHP_EXTENSION_PATH="/usr/local/lib/php/extensions/no-debug-non-zts-20160303"
ARG PHP_CONFIG_PATH="/usr/local/etc/php/conf.d"

#---+----1----+----2----+----3----+----4----+----5----+----6----+----7----+----8----+----9----+----0
# PHP環境ビルドステージからPHP動作環境をコピー
#---+----1----+----2----+----3----+----4----+----5----+----6----+----7----+----8----+----9----+----0
# 拡張モジュールインストール： bz2
COPY --from=build-bz2 ${PHP_EXTENSION_PATH}/bz2.so ${PHP_EXTENSION_PATH}/bz2.so
COPY --from=build-bz2 ${PHP_CONFIG_PATH}/docker-php-ext-bz2.ini ${PHP_CONFIG_PATH}/docker-php-ext-bz2.ini

# 拡張モジュールインストール： calendar
COPY --from=build-calendar ${PHP_EXTENSION_PATH}/calendar.so ${PHP_EXTENSION_PATH}/calendar.so
COPY --from=build-calendar ${PHP_CONFIG_PATH}/docker-php-ext-calendar.ini ${PHP_CONFIG_PATH}/docker-php-ext-calendar.ini

# 拡張モジュールインストール： exif
COPY --from=build-exif ${PHP_EXTENSION_PATH}/exif.so ${PHP_EXTENSION_PATH}/exif.so
COPY --from=build-exif ${PHP_CONFIG_PATH}/docker-php-ext-exif.ini ${PHP_CONFIG_PATH}/docker-php-ext-exif.ini

# 拡張モジュールインストール： gettext
COPY --from=build-gettext ${PHP_EXTENSION_PATH}/gettext.so ${PHP_EXTENSION_PATH}/gettext.so
COPY --from=build-gettext ${PHP_CONFIG_PATH}/docker-php-ext-gettext.ini ${PHP_CONFIG_PATH}/docker-php-ext-gettext.ini

# 拡張モジュールインストール： gmp
COPY --from=build-gmp ${PHP_EXTENSION_PATH}/gmp.so ${PHP_EXTENSION_PATH}/gmp.so
COPY --from=build-gmp ${PHP_CONFIG_PATH}/docker-php-ext-gmp.ini ${PHP_CONFIG_PATH}/docker-php-ext-gmp.ini

# 拡張モジュールインストール： mysqli
COPY --from=build-mysqli ${PHP_EXTENSION_PATH}/mysqli.so ${PHP_EXTENSION_PATH}/mysqli.so
COPY --from=build-mysqli ${PHP_CONFIG_PATH}/docker-php-ext-mysqli.ini ${PHP_CONFIG_PATH}/docker-php-ext-mysqli.ini

# 拡張モジュールインストール： shmop
COPY --from=build-shmop ${PHP_EXTENSION_PATH}/shmop.so ${PHP_EXTENSION_PATH}/shmop.so
COPY --from=build-shmop ${PHP_CONFIG_PATH}/docker-php-ext-shmop.ini ${PHP_CONFIG_PATH}/docker-php-ext-shmop.ini

# 拡張モジュールインストール： opcache
COPY --from=build-opcache ${PHP_EXTENSION_PATH}/opcache.so ${PHP_EXTENSION_PATH}/opcache.so
COPY --from=build-opcache ${PHP_CONFIG_PATH}/docker-php-ext-opcache.ini ${PHP_CONFIG_PATH}/docker-php-ext-opcache.ini

# 拡張モジュールインストール： pcntl
COPY --from=build-pcntl ${PHP_EXTENSION_PATH}/pcntl.so ${PHP_EXTENSION_PATH}/pcntl.so
COPY --from=build-pcntl ${PHP_CONFIG_PATH}/docker-php-ext-pcntl.ini ${PHP_CONFIG_PATH}/docker-php-ext-pcntl.ini

# 拡張モジュールインストール： pdo_mysql
COPY --from=build-pdo_mysql ${PHP_EXTENSION_PATH}/pdo_mysql.so ${PHP_EXTENSION_PATH}/pdo_mysql.so
COPY --from=build-pdo_mysql ${PHP_CONFIG_PATH}/docker-php-ext-pdo_mysql.ini ${PHP_CONFIG_PATH}/docker-php-ext-pdo_mysql.ini

# 拡張モジュールインストール： sockets
COPY --from=build-sockets ${PHP_EXTENSION_PATH}/sockets.so ${PHP_EXTENSION_PATH}/sockets.so
COPY --from=build-sockets ${PHP_CONFIG_PATH}/docker-php-ext-sockets.ini ${PHP_CONFIG_PATH}/docker-php-ext-sockets.ini

# 拡張モジュールインストール： wddx
COPY --from=build-wddx ${PHP_EXTENSION_PATH}/wddx.so ${PHP_EXTENSION_PATH}/wddx.so
COPY --from=build-wddx ${PHP_CONFIG_PATH}/docker-php-ext-wddx.ini ${PHP_CONFIG_PATH}/docker-php-ext-wddx.ini

# 拡張モジュールインストール： xsl
COPY --from=build-xsl ${PHP_EXTENSION_PATH}/xsl.so ${PHP_EXTENSION_PATH}/xsl.so
COPY --from=build-xsl ${PHP_CONFIG_PATH}/docker-php-ext-xsl.ini ${PHP_CONFIG_PATH}/docker-php-ext-xsl.ini

# 拡張モジュールインストール： zip
COPY --from=build-zip ${PHP_EXTENSION_PATH}/zip.so ${PHP_EXTENSION_PATH}/zip.so
COPY --from=build-zip ${PHP_CONFIG_PATH}/docker-php-ext-zip.ini ${PHP_CONFIG_PATH}/docker-php-ext-zip.ini

# 拡張モジュールインストール： apcu
#COPY --from=build-apcu ${PHP_EXTENSION_PATH}/apcu.so ${PHP_EXTENSION_PATH}/apcu.so
#COPY --from=build-apcu ${PHP_CONFIG_PATH}/docker-php-ext-apcu.ini ${PHP_CONFIG_PATH}/docker-php-ext-apcu.ini

# 拡張モジュールインストール： redis
#COPY --from=build-redis ${PHP_EXTENSION_PATH}/redis.so ${PHP_EXTENSION_PATH}/redis.so
#COPY --from=build-redis ${PHP_CONFIG_PATH}/docker-php-ext-redis.ini ${PHP_CONFIG_PATH}/docker-php-ext-redis.ini

# 拡張モジュールインストール： memcached
#COPY --from=build-memcached ${PHP_EXTENSION_PATH}/memcached.so ${PHP_EXTENSION_PATH}/memcached.so
#COPY --from=build-memcached ${PHP_CONFIG_PATH}/docker-php-ext-memcached.ini ${PHP_CONFIG_PATH}/docker-php-ext-memcached.ini

# Composerインストール
COPY --from=composer:latest /usr/bin/composer /usr/local/bin/composer

#---+----1----+----2----+----3----+----4----+----5----+----6----+----7----+----8----+----9----+----0
# 動作用の環境調整
#
# - タイムゾーンをJSTへ変更
# - 拡張モジュール用パッケージインストール
# - Composerの高速化設定
# - Composerのキャッシュクリア
#---+----1----+----2----+----3----+----4----+----5----+----6----+----7----+----8----+----9----+----0
RUN set -xe \
    && apk add --update-cache --no-cache tzdata \
    && cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \
    && echo "Asia/Tokyo" > /etc/timezone \
    && apk del tzdata \
    && apk add --update-cache --no-cache \
        libbz2 \
        libintl \
        libxslt \
        icu \
        sqlite \
        binutils \
        file \
        libgcrypt \
        libtasn1 \
        openldap \
        gmp \
    # module:memcached
    #&& apk add --update-cache --no-cache libmemcached
    && composer config -g repos.packagist composer https://packagist.jp \
    && composer global require hirak/prestissimo \
    && composer global clear-cache
