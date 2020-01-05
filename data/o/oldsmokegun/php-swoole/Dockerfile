FROM php:7.4.0-cli

ENV PHP_REDIS_VERSION 5.0.0
ENV PHP_MEMCACHED_VERSION 3.1.4
ENV PHP_INOTIFY_VERSION 2.0.0
ENV PHP_SWOOLE_VERSION 4.4.12

# 时区
RUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo 'Asia/Shanghai' > /etc/timezone

# 依赖
RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng-dev \
        libssl-dev \
        libmemcached-dev \
    && apt-get autoclean && apt-get clean

# 扩展
RUN docker-php-ext-configure gd --with-freetype --with-jpeg \
    && docker-php-ext-install -j$(nproc) gd \
    # php-redis 扩展
    && pecl install redis-$PHP_REDIS_VERSION \
    # php-memcached 扩展
    && pecl install memcached-$PHP_MEMCACHED_VERSION \
    # php-notify 扩展
    && pecl install inotify-$PHP_INOTIFY_VERSION \
    # swoole 扩展
    && pecl install swoole-$PHP_SWOOLE_VERSION \
    && docker-php-ext-enable redis memcached inotify swoole \
    && docker-php-ext-install pdo_mysql \
    && docker-php-ext-install mysqli \
    && docker-php-ext-install opcache \
    && docker-php-ext-install bcmath \
    # php.ini 文件
    && cp "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"

# Composer
RUN curl -sS https://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer \
    && chmod +x /usr/local/bin/composer \
    && composer config -g repo.packagist composer https://mirrors.aliyun.com/composer/

WORKDIR /www/wwwroot