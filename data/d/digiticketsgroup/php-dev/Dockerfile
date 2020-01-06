FROM digiticketsgroup/php:7.0

MAINTAINER Warrick Hill <warrick.hill@digitickets.co.uk>

ENV PHP_EXTENTIONS="" \
    PECL_EXTENTIONS="xdebug"

RUN set -xe \
  && NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \
  && apk add -U -u --no-cache --virtual .build-deps \
      $PHPIZE_DEPS \
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
  && rm -rf /tmp/*

COPY config/xdebug.ini /usr/local/etc/php/conf.d/xdebug.ini

RUN chmod +x /usr/local/bin/entrypoint