# build image

FROM php:7.2-cli-alpine3.9

# Maintainer: docker_user <docker_user at email.com> (@docker_user)
MAINTAINER zengyu 284141050@qq.com

#
WORKDIR /app

RUN apk add unrar


ADD extension /tmp/extension

# https://github.com/nodegit/nodegit/issues/1361
# --virtual xxxx [eg: vir-package mean run "apk del vir-package" to del the packages this command when you want to delete package]
# apcu swoole inotify
RUN apk add --update --no-cache --virtual .build-deps \
    g++ \
    gcc \
    make \
    autoconf \
    openssl-dev \
    && pecl install redis && docker-php-ext-enable redis \
    && php /tmp/extension/ExtInstaller.php -n apcu \
    && php /tmp/extension/ExtInstaller.php -n swoole \
    && rm -rf /tmp/extension \
    && apk del .build-deps


RUN apk add --no-cache freetype-dev libpng-dev libjpeg-turbo-dev libzip-dev --virtual .gd-deps \
    && apk add --no-cache  freetype libpng libjpeg-turbo libzip \
    && docker-php-ext-configure gd \
    --with-gd \
    --with-freetype-dir=/usr/include/ \
    --with-png-dir=/usr/include/ \
    --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-configure zip --with-libzip=/usr/include \
    && docker-php-ext-install -j$(nproc) zip gd pdo_mysql \
    && apk del .gd-deps

RUN chown -R www-data:www-data /app


# composer


# Commands to update the image

# Commands when creating a new container
CMD ["php","-i"]