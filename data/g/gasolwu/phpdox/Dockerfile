FROM composer:1.8.4 as composer
FROM php:7.2-alpine as builder

RUN apk add --no-cache libxslt-dev=1.1.32-r0 \
	    && docker-php-ext-install xsl

FROM php:7.2-alpine

LABEL maintainer="gasol.wu@gmail.com"

ARG VERSION

COPY --from=builder /usr/local/lib/php/extensions/no-debug-non-zts-20170718/xsl.so /usr/local/lib/php/extensions/no-debug-non-zts-20170718/xsl.so
COPY --from=builder /usr/local/etc/php/conf.d/docker-php-ext-xsl.ini /usr/local/etc/php/conf.d/docker-php-ext-xsl.ini
COPY --from=composer /usr/bin/composer /usr/bin/composer

RUN apk add --no-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing \
	    gnu-libiconv=1.15-r2 \
	    libxslt=1.1.32-r0

RUN COMPOSER_HOME="/composer" COMPOSER_VENDOR_DIR="/composer/vendor" composer require --prefer-dist --no-progress --dev theseer/phpdox:$VERSION

ENV PATH /composer/vendor/bin:${PATH}
ENV LD_PRELOAD /usr/lib/preloadable_libiconv.so php # See https://github.com/docker-library/php/issues/240

WORKDIR /app

CMD ["phpdox"]
