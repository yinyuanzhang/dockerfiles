FROM php:7.1-cli-alpine

RUN apk --no-cache add libmcrypt-dev git zlib-dev icu-dev $PHPIZE_DEPS openssl-dev

RUN docker-php-ext-configure intl \
    && docker-php-ext-install bcmath mbstring mcrypt zip intl