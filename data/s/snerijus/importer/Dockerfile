FROM php:7.3-alpine

RUN apk add --update \
    && docker-php-ext-install mysqli \
    && rm -rf /tmp/* /var/cache/apk/* \
    && echo 'mysqli.allow_local_infile = On' > $PHP_INI_DIR/conf.d/mysql_php.ini

COPY ./src /usr/src/importer
WORKDIR /usr/src/importer

CMD [ "php", "./importer.php", "-c", "/config/config.conf" ]
