FROM php:7.3-fpm-alpine3.10

ARG USER=app
ARG UID=1000
ARG GID=1000
ENV USER=$USER
ENV TERM=xterm-256color

RUN apk upgrade --no-cache &&  \
    apk add --no-cache \
        nginx \
        runit \
        ssmtp \
        icu-libs \
        libzip \
    && \
    apk add --no-cache --virtual .build-deps \
        $PHPIZE_DEPS \
        icu \
        icu-dev \
        libzip-dev \
    && \
    pecl install xdebug redis && \
    docker-php-ext-enable redis && \
    pecl clear-cache && \
    docker-php-ext-install opcache pdo_mysql mysqli intl zip && \
    apk del --no-network .build-deps && \
    addgroup -g $GID $USER && \
    adduser -u $UID -G $USER -D $USER

COPY ./source /

CMD ["sh", "/sbin/boot.sh"]
