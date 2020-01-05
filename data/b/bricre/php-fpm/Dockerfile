ARG     PHP_VERSION="${PHP_VERSION:-7.2}"
FROM	  php:${PHP_VERSION}-fpm-alpine

LABEL	  maintainer="Allan Sun <allan.sun@bricre.com>"

ARG     PHPREDIS_VERSION="${PHPREDIS_VERSION:-4.2.0}"
ENV     PHPREDIS_VERSION="${PHPREDIS_VERSION}"
ENV     PHPIZE_DEPS="${PHPIZE_DEPS}"

RUN     APP_ENVIRONMENT=production       && \
        echo http://dl-cdn.alpinelinux.org/alpine/edge/main >> /etc/apk/repositories  && \
        echo http://dl-cdn.alpinelinux.org/alpine/edge/community >> /etc/apk/repositories  && \
        echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories && \
        apk update                       && \
        \
        apk upgrade                      && \
        \
        docker-php-source extract        && \
        \
        apk add --no-cache                  \
            --virtual .build-dependencies   \
                $PHPIZE_DEPS                \
                zlib-dev                    \
                cyrus-sasl-dev              \
                git                         \
                autoconf                    \
                g++                         \
                libtool                     \
                make                        \
                pcre-dev                 && \
        \
        apk add --no-cache                  \
            libintl                         \
            icu                             \
            libmemcached-libs               \
            zlib                            \
            libssh2                         \
            icu-dev                         \
            libxml2-dev                     \
            freetype-dev                    \
            libjpeg-turbo-dev               \
            libpng-dev                      \
            libmemcached-dev                \
            imagemagick-dev                 \
            libzip-dev                      \
            libssh2-dev                     \
            libxslt-dev                     \
            gearman-dev                     \
            gearman-libs                    \
            php7-gearman                    \
            php7-dev                        \
            boost-dev                       \
            && \
        \
        pecl install redis               && \
        pecl install memcached           && \
        pecl install imagick             && \
        pecl install mongodb             && \
        pecl install rar                 && \
        \
        docker-php-ext-enable               \
          imagick redis memcached mongodb rar &&  \
        \
        docker-php-ext-configure gd                 \
            --with-freetype-dir=/usr/include/       \
            --with-jpeg-dir=/usr/include/       &&  \
        docker-php-ext-configure opcache --enable-opcache    && \
        docker-php-ext-configure pcntl --enable-pcntl   && \
        \
        docker-php-ext-install -j"$(getconf _NPROCESSORS_ONLN)" \
            intl                                                \
            bcmath                                              \
            xsl                                                 \
            zip                                                 \
            soap                                                \
            pdo_mysql                                           \
            opcache                                             \
            pcntl                                               \
            gd                                              &&  \
        \
        apk del .build-dependencies                && \
        docker-php-source delete                   && \
        pecl clear-cache                           && \
        \
        wget https://github.com/DataDog/dd-trace-php/releases/download/0.15.0/datadog-php-tracer_0.15.0_noarch.apk -O /tmp/datadog-php-tracer.apk && \
        apk add /tmp/datadog-php-tracer.apk --allow-untrusted && \
        \
        mv /etc/php7/conf.d/gearman.ini /usr/local/etc/php/conf.d/ && \
        mv /usr/lib/php7/modules/gearman.so /usr/local/lib/php/extensions/no-debug-non-zts-20170718/ && \
        \
        apk del --purge \
            php7-dev \
            build-base \
            boost-dev                       \
            gearman-dev && \
        rm -rf /tmp/* /var/cache/apk/*

# set recommended PHP.ini settings
# https://secure.php.net/manual/en/opcache.installation.php
# also, enable ioncube
COPY    conf.d/* /usr/local/etc/php/conf.d/

CMD     ["php-fpm"]
