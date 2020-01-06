FROM php:7.1-fpm-alpine

MAINTAINER Warrick Hill <warrick.hill@digitickets.co.uk>

ENV PHP_EXTENTIONS="bcmath gd gmp intl mcrypt mysqli pdo_dblib pdo_mysql soap zip" \
    PECL_EXTENTIONS="apcu imagick memcached msgpack redis timezonedb" \
    PHP_INI_TIMEZONE=UTC \
    PHP_INI_MEMORY_LIMIT=512M \
    NEWRELIC_LICENSE="" \
    NEWRELIC_APPNAME=""

# No idea why but need both for imagemagik to work
RUN apk --no-cache add imagemagick-dev imagemagick

RUN set -xe \
  && NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \
  && apk add -U -u --no-cache --virtual .build-deps \
      $PHPIZE_DEPS \
      # gd
      freetype-dev \
      libjpeg-turbo-dev \
      libpng-dev \
      #gmp
      gmp-dev \
      # intl
      icu-dev \
      # mcrypt
      libmcrypt-dev \
      # memcached
      libmemcached-dev \
      # pdo_dblib
      freetds-dev \
      # soap
      libxml2-dev \
  && for EXT in ${PHP_EXTENTIONS}; do docker-php-ext-install -j${NPROC} ${EXT} && ( php -m | grep "^${EXT}$" ); done \
  && for EXT in ${PECL_EXTENTIONS}; do pecl install ${EXT} && EXT=$(echo ${EXT} | cut -f1 -d-) && docker-php-ext-enable ${EXT} && ( php -m | grep "^${EXT}$" ); done \
  && RUN_DEPS="$( \
    scanelf --needed --nobanner --recursive /usr/local \
      | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
      | sort -u \
      | xargs -r apk info --installed \
      | sort -u \
    )" \
  && apk add --no-cache --virtual .php-rundeps ${RUN_DEPS} \
  && apk del .build-deps \
  && rm -rf /tmp/* /usr/local/etc/php-fpm.*

COPY config/ /usr/local/etc/
COPY entrypoint.sh /usr/local/bin/entrypoint

EXPOSE 9000

ENTRYPOINT ["entrypoint"]

CMD ["php-fpm"]
