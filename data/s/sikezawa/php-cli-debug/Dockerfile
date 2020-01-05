FROM php:7.3.2-cli-alpine3.9

RUN apk --no-cache add --virtual build-deps \
        build-base \
        autoconf \
    && pecl install channel://pecl.php.net/xdebug-2.7.0RC2 \
    && apk del build-deps

COPY ./xdebug.ini $PHP_INI_DIR/conf.d/xdebug.ini
COPY ./php.ini $PHP_INI_DIR/php.ini

WORKDIR /app
ENTRYPOINT [ "php" ]
CMD [ "-v" ]
