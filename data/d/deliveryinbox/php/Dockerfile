FROM php:fpm-alpine

LABEL maintainer="Filipe Sarturi <filipesarturi@gmail.com>"

RUN addgroup -S www
RUN adduser -D -S -G www php

# Fix work iconv library with Alphine
RUN apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/community/ --allow-untrusted gnu-libiconv
ENV LD_PRELOAD /usr/lib/preloadable_libiconv.so php

# RUN apk add --no-cache --virtual .dependencies \
RUN apk add --no-cache \
        zlib \
        zlib-dev \
        libwebp-dev \
        libjpeg-turbo-dev \
        libpng \
        libpng-dev
    
RUN docker-php-ext-configure gd \
        --with-gd \
        --with-webp-dir=/usr/ \
        --with-jpeg-dir=/usr/ \
        --with-png-dir=/usr/ \
        --with-zlib-dir=/usr/
        
RUN docker-php-ext-install -j$(getconf _NPROCESSORS_ONLN) \
        iconv \
        opcache \
        mysqli \
        bcmath \
        gd \
        mbstring

#####################################
# Xdebug:
#####################################
ARG PHP_INSTALL_XDEBUG=false
RUN if [ ${PHP_INSTALL_XDEBUG} = true ]; then \
        apk add --no-cache --update --virtual .xdebugDeps autoconf pcre-dev ${PHPIZE_DEPS} && \
        pecl install xdebug && \
        docker-php-ext-enable xdebug && \
        apk del .xdebugDeps \
;fi

# Use the default production configuration
RUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"

# Permissions
RUN chown -R root:www /var/www
RUN chmod u+rwx,g+rx,o+rx /var/www
RUN find /var/www -type d -exec chmod u+rwx,g+rx,o+rx {} +
RUN find /var/www -type f -exec chmod u+rw,g+rw,o+r {} +

# Install node
RUN apk add --no-cache --update nodejs-current npm

EXPOSE 9000

CMD ["php-fpm"]