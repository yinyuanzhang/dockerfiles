FROM composer:1.8.6 AS composer

FROM giftery/runit-nginx-php-fpm73

ARG composer_auth
ENV COMPOSER_AUTH=${composer_auth}
ENV COMPOSER_ALLOW_SUPERUSER 1
ENV COMPOSER_HOME /tmp

RUN apk add --no-cache git

COPY --from=composer /usr/bin/composer /usr/local/bin/composer

WORKDIR /app

ENTRYPOINT ["composer"]
CMD ["install"]
