FROM alpine:3.8

RUN set -x \
 && apk add --no-cache \
        php7 \
        php7-ctype \
        php7-simplexml \
        php7-tokenizer \
        php7-xmlwriter \
 && apk add --no-cache -t .build-deps \
        curl \
        php7-json \
        php7-openssl \
        php7-phar \
 && curl -Lo /usr/local/bin/composer https://getcomposer.org/composer.phar \
 && chmod +x /usr/local/bin/composer \
 && composer global require \
        'squizlabs/php_codesniffer=3.5.2' \
    # Clean-up
 && rm /usr/local/bin/composer \
 && apk del --purge .build-deps \
    # Default directory
 && mkdir -p /code

ENV PATH=$PATH:/root/.composer/vendor/bin/

WORKDIR /code
VOLUME /code
