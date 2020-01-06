FROM php:fpm-alpine

MAINTAINER Felix Favre <gnomus@gnomus.de>

RUN apk add --no-cache gettext-dev \
    && docker-php-ext-install gettext \
    && docker-php-ext-install mysqli



EXPOSE 9000

ENTRYPOINT ["docker-php-entrypoint"]

CMD ["php-fpm"]
