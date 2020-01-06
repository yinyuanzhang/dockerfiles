# FROM php:7.2-fpm-alpine as local
FROM php:7.2-fpm-alpine
LABEL maintainer="A.M <andares@outlook.com>"

ENV VERSION 1.0
ENV ENTRYPOINT_DELAY 15
ARG scene=default

# CMD ["sh", "-c", "echo", "container build at $scene"]

# 复制配置文件，包括php与fpm
# 复制启动脚本
COPY local/etc /usr/local/etc
COPY etc/init.d /etc/init.d

# 安装基础编译包
# 安装初步依赖
# 安装扩展
# 安装编译依赖
# 安装pecl扩展
# 移除基础编译包
# 安装supervisord
RUN mkdir -p /worker/apps \
    && mkdir -p /worker/logs \
    && mkdir -p /worker/swap \
    && chmod +x /etc/init.d/php-fpm \
    && chmod +x /etc/init.d/fpm \
    && ln -s /etc/init.d/fpm /usr/local/bin/fpm \
    && apk add --no-cache gcc g++ make libffi-dev libxml2-dev openssl-dev libpng-dev imagemagick-dev autoconf libmemcached-dev mosquitto-dev rabbitmq-c-dev libsasl yaml-dev libuuid msgpack-c-dev util-linux-dev \
    && printf "\n" | pecl install -f amqp imagick msgpack memcached mongodb channel://pecl.php.net/mosquitto-0.4.0 redis uuid yaml \
    && docker-php-ext-enable amqp imagick memcached mongodb mosquitto msgpack redis uuid yaml \
    && apk add --no-cache libpng-dev gettext-dev gmp-dev postgresql-dev \
    && docker-php-ext-install bcmath exif gd gettext gmp pcntl pdo_pgsql sockets sysvmsg sysvsem sysvshm zip opcache \
    && apk del --no-cache gcc g++ make libffi-dev libxml2-dev openssl-dev autoconf libsasl libuuid msgpack-c-dev \
    && apk add --no-cache supervisor

# 装nginx实现自举
RUN apk add --no-cache nginx \
    && mkdir -p /run/nginx
COPY etc/nginx /etc/nginx
COPY local/bin /usr/local/bin

RUN apk add --no-cache zsh \
    && chmod +x /usr/local/bin/*

RUN wget -c https://getcomposer.org/composer.phar -O /usr/local/bin/composer \
    && chmod +x /usr/local/bin/composer \
    && mv /usr/local/etc/php-fpm.d/docker.conf /usr/local/etc/php-fpm.d/docker.conf.disabled \
    && mv /usr/local/etc/php-fpm.d/zz-docker.conf /usr/local/etc/php-fpm.d/zz-docker.conf.disabled

RUN chmod +x /etc/init.d/reload \
  && ln -s /etc/init.d/reload /usr/local/bin/reload \
  && chmod +x /usr/local/bin/reload

# baseline 安装支持
RUN apk add --no-cache git openssh

# 设置entrypoint在docker-compose中进行
