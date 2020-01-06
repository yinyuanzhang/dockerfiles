FROM php:7.2-fpm-alpine

ENV S3CMD_VERSION 1.6.1

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) bcmath

RUN apk add --no-cache --virtual .other-php-ext-deps \
    bzip2-dev && \
    docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) bz2 && \
    rm -rf /tmp/* /var/cache/apk/*

RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) calendar
RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) ctype

RUN apk add --no-cache --virtual .phpize-deps-1 $PHPIZE_DEPS \
    curl-dev && \
    docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) curl && \
    apk del .phpize-deps-1 && \
    rm -rf /tmp/* /var/cache/apk/*

#RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) dba

RUN apk add --no-cache --virtual .phpize-deps-1 $PHPIZE_DEPS \
    libxml2-dev && \
    docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) dom && \
    apk del .phpize-deps-1 && \
    rm -rf /tmp/* /var/cache/apk/*

#RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) enchant
RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) exif
RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) fileinfo
#RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) filter
#RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) ftp

RUN apk add --no-cache --virtual .phpize-deps-1 $PHPIZE_DEPS \
    freetype-dev libpng-dev libjpeg-turbo-dev && \
    docker-php-ext-configure gd \
        --with-gd \
        --with-freetype-dir=/usr/include/ \
        --with-png-dir=/usr/include/ \
        --with-jpeg-dir=/usr/include/ && \
    docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) gd && \
    apk del .phpize-deps-1 && \
    rm -rf /tmp/* /var/cache/apk/*

RUN apk add --no-cache --virtual .phpize-deps-1 $PHPIZE_DEPS \
    gettext gettext-libs gettext-dev && \
    docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) gettext && \
    apk del .phpize-deps-1 && \
    rm -rf /tmp/* /var/cache/apk/*

#RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) gmp
RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) hash
RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) iconv

RUN apk add --no-cache --virtual .phpize-deps-1 $PHPIZE_DEPS libtool imagemagick-dev && \
    apk add --no-cache --virtual .imagick-runtime-deps imagemagick && \
    pecl install imagick && \
    docker-php-ext-enable imagick && \
    apk del .phpize-deps-1 && \
    rm -rf /tmp/* /var/cache/apk/*

RUN apk add --no-cache --virtual .phpize-deps-1 $PHPIZE_DEPS \
    openssl-dev imap-dev && \
    docker-php-ext-configure imap --with-imap --with-imap-ssl && \
    docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) imap && \
    apk del .phpize-deps-1 && \
    rm -rf /tmp/* /var/cache/apk/*

#RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) interbase
RUN apk add --no-cache --virtual .phpize-deps-1 $PHPIZE_DEPS \
    icu icu-libs icu-dev && \
    apk add --no-cache --virtual .other-php-ext-deps icu-libs && \
    docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) intl && \
    apk del .phpize-deps-1 && \
    rm -rf /tmp/* /var/cache/apk/*

RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) json

#RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) ldap
RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) mbstring

#RUN apk add --no-cache --virtual .phpize-deps-1 $PHPIZE_DEPS \
#    libmcrypt-dev && \
#    apk add --no-cache --virtual .other-php-ext-deps libmcrypt && \
#    docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) mcrypt && \
#    apk del .phpize-deps-1 && \
#    rm -rf /tmp/* /var/cache/apk/*

RUN apk add --no-cache --virtual .phpize-deps-1 $PHPIZE_DEPS \
    openssl-dev && \
    pecl install mongodb && \
    docker-php-ext-enable mongodb && \
    apk del .phpize-deps-1 && \
    rm -rf /tmp/* /var/cache/apk/*

#RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) mysql
RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) mysqli
#RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) oci8
#RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) odbc
RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) opcache
RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) pcntl
RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) pdo
#RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) pdo_dblib
#RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) pdo_firebird
RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) pdo_mysql
#RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) pdo_oci
#RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) pdo_odbc
#RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) pdo_pgsql
#RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) pdo_sqlite
#RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) pgsql
#RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) phar

RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) posix

#RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) pspell

#RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) readline

#RUN apk add --no-cache --virtual .phpize-deps-1 $PHPIZE_DEPS recode-dev && \
#    apk add --no-cache --virtual .other-php-ext-deps recode && \
#    docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) recode && \
#    apk del .phpize-deps-1 && \
#    rm -rf /tmp/* /var/cache/apk/*

#RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) reflection

RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) session

RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) shmop

RUN apk add --no-cache --virtual .phpize-deps-1 $PHPIZE_DEPS \
    libxml2-dev && \
    docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) simplexml && \
    apk del .phpize-deps-1 && \
    rm -rf /tmp/* /var/cache/apk/*

#RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) snmp

#RUN apk add --no-cache --virtual .phpize-deps-1 $PHPIZE_DEPS libxml2-dev libsodium-dev && \
#    pecl install libsodium-1.0.6 && \
#    docker-php-ext-enable libsodium && \
#    apk del .phpize-deps-1 && \
#    rm -rf /tmp/* /var/cache/apk/*

RUN apk add --no-cache --virtual .phpize-deps-1 $PHPIZE_DEPS \
    libxml2-dev && \docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) soap && \
    apk del .phpize-deps-1 && \
    rm -rf /tmp/* /var/cache/apk/*

RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) sockets

#RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) spl

#RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) standard

RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) sysvmsg

RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) sysvsem

RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) sysvshm

#RUN apk add --no-cache --virtual .phpize-deps-1 $PHPIZE_DEPS \
#    apk add --no-cache --virtual .other-php-ext-deps tidyhtml-libs && \
#    docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) tidy && \
#    apk del .phpize-deps-1 && \
#    rm -rf /tmp/* /var/cache/apk/*

RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) tokenizer

RUN apk add --no-cache --virtual .phpize-deps-1 $PHPIZE_DEPS libxml2-dev && \
    docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) wddx && \
    apk del .phpize-deps-1 && \
    rm -rf /tmp/* /var/cache/apk/*

RUN apk add --no-cache --virtual .phpize-deps-1 $PHPIZE_DEPS && \
    pecl install xdebug && \
    docker-php-ext-enable xdebug && \
    apk del .phpize-deps-1 && \
    rm -rf /tmp/* /var/cache/apk/*

RUN apk add --no-cache --virtual .phpize-deps-1 $PHPIZE_DEPS libxml2-dev && \
    docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) xml && \
    apk del .phpize-deps-1 && \
    rm -rf /tmp/* /var/cache/apk/*

#RUN apk add --no-cache --virtual .phpize-deps-1 $PHPIZE_DEPS libxml2-dev && \
#    docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) xmlreader && \
#    apk del .phpize-deps-1 && \
#    rm -rf /tmp/* /var/cache/apk/*

RUN apk add --no-cache --virtual .phpize-deps-1 $PHPIZE_DEPS libxml2-dev && \
    docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) xmlrpc && \
    apk del .phpize-deps-1 && \
    rm -rf /tmp/* /var/cache/apk/*

#RUN apk add --no-cache --virtual .phpize-deps-1 $PHPIZE_DEPS libxml2-dev && \
#    docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) xmlwriter && \
#    apk del .phpize-deps-1 && \
#    rm -rf /tmp/* /var/cache/apk/*

RUN apk add --no-cache --virtual .phpize-deps-1 $PHPIZE_DEPS libxslt-dev && \
    apk add --no-cache --virtual .other-php-ext-deps libxslt && \
    docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) xsl && \
    apk del .phpize-deps-1 && \
    rm -rf /tmp/* /var/cache/apk/*

RUN apk add --no-cache --virtual .phpize-deps-1 $PHPIZE_DEPS yaml-dev && \
    apk add --no-cache --virtual .other-php-ext-deps yaml && \
    pecl install yaml-2.0.0 && \
    docker-php-ext-enable yaml && \
    apk del .phpize-deps-1 && \
    rm -rf /tmp/* /var/cache/apk/*

RUN apk add --no-cache --virtual .phpize-deps-1 $PHPIZE_DEPS zlib-dev && \
    docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) zip && \
    apk del .phpize-deps-1 && \
    rm -rf /tmp/* /var/cache/apk/*

RUN apk add --no-cache libssl1.1

# create symlink to support standard /usr/bin/php
RUN ln -s /usr/local/bin/php /usr/bin/php

RUN rm /usr/local/etc/php-fpm.d/zz-docker.conf
RUN rm /usr/local/etc/php-fpm.d/docker.conf

RUN rm /usr/local/etc/php-fpm.conf

# Adjust some php settings
ADD etc/php/conf.d/* /usr/local/etc/php/conf.d/
ADD etc/php/php-fpm.conf /usr/local/etc/php-fpm.conf
ADD etc/php/php-fpm.d/* /usr/local/etc/php-fpm.d/
ADD etc/php/opcache-blacklist.txt /usr/local/etc/php/opcache-blacklist.txt

COPY docker-php-entrypoint /usr/local/bin/

RUN chmod a+x /usr/local/bin/docker-php-entrypoint

ENTRYPOINT ["docker-php-entrypoint"]

RUN rm -rf /var/www/localhost
RUN rm -rf /var/www/html
RUN mkdir -p /var/www/web

RUN mkdir -p /var/sessions

RUN chown nobody:nobody /var/sessions

WORKDIR /var/www/web

EXPOSE 9000
CMD ["php-fpm", "--allow-to-run-as-root"]
