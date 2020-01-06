FROM php:7.1-alpine

LABEL maintainer="jason@ciandt.com"

ENV DRUSH_VERSION 8.1.18
ENV DRUSH_LAUNCHER_VERSION 0.6.0
ENV DRUSH_LAUNCHER_FALLBACK "/usr/local/drush/drush"
ENV MEMCACHED_DEPS zlib-dev libmemcached-dev cyrus-sasl-dev

RUN set -xe \
    && apk --update add \
            freetype \
            libpng \
            libjpeg-turbo \
            freetype-dev \
            libpng-dev \
            libjpeg-turbo-dev \
            build-base \
            libpq \
            mysql-client \
            postgresql-client \
            postgresql-dev \
            php7-pear \
            patch \
            tar && \
            docker-php-ext-configure gd \
                --with-gd \
                --with-freetype-dir=/usr/include/ \
                --with-png-dir=/usr/include/ \
                --with-jpeg-dir=/usr/include/ && \
            NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) && \
            docker-php-ext-install -j${NPROC} gd && \
            docker-php-ext-install mysqli pgsql pdo_mysql pdo_pgsql && \
            apk del build-base postgresql-dev freetype-dev libpng-dev libjpeg-turbo-dev && \
            rm -rf /var/cache/apk/* \
    # Install memcache extension
    && apk add --no-cache --update libmemcached-libs zlib \
    && apk add --no-cache --update --virtual .phpize-deps $PHPIZE_DEPS \
    && apk add --no-cache --update --virtual .memcached-deps $MEMCACHED_DEPS \
    && pecl install memcached \
    && echo "extension=memcached.so" > /usr/local/etc/php/conf.d/20_memcached.ini \
    && rm -rf /usr/share/php7 \
    && rm -rf /tmp/* \
    && apk del .memcached-deps .phpize-deps \
    # Install Drush.
    && mkdir -p /usr/local/drush \
    && curl -fsSL -o /usr/local/drush/drush "https://github.com/drush-ops/drush/releases/download/$DRUSH_VERSION/drush.phar" \
    && curl -fsSL -o /usr/local/bin/drush https://github.com/drush-ops/drush-launcher/releases/download/${DRUSH_LAUNCHER_VERSION}/drush.phar \    
    && chmod +x /usr/local/drush/drush /usr/local/bin/drush \
    && drush --version

# Update the entry point for drush
ENTRYPOINT ["drush"]
