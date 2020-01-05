# build image

FROM php:7.2-cli-alpine3.9

# Maintainer: docker_user <docker_user at email.com> (@docker_user)
MAINTAINER zengyu 284141050@qq.com

#
WORKDIR /app

RUN apk add unrar

# mysql 
RUN docker-php-ext-install -j$(nproc) pdo_mysql

ADD extension /tmp/extension

# https://github.com/nodegit/nodegit/issues/1361
# --virtual xxxx [eg: vir-package mean run "apk del vir-package" to del the packages this command when you want to delete package]
# apcu swoole inotify
RUN apk add --update --no-cache --virtual .build-deps \
    g++ \
    gcc \
    make \
    autoconf \
    && pecl install inotify && docker-php-ext-enable inotify \
    && pecl install redis && docker-php-ext-enable redis \
    && php /tmp/extension/ExtInstaller.php -n apcu \
    && php /tmp/extension/ExtInstaller.php -n swoole \
    && rm -rf /tmp/extension \
    && apk del .build-deps

RUN apk add --no-cache libzip-dev && docker-php-ext-configure zip --with-libzip=/usr/include && docker-php-ext-install zip


RUN chown -R www-data:www-data /app

ENV SWOOLE_SERVER_GROUP www-data \
    SWOOLE_SERVER_USER www-data

# composer
RUN cd /usr/local/bin \
    && curl -sS https://getcomposer.org/installer | php \
    && mv composer.phar composer \ 
    && composer -V


# Commands to update the image

# Commands when creating a new container
CMD ["php","-i"]