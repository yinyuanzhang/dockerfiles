FROM php:7.2.19-fpm-alpine3.9

LABEL maintainer="Jade <hmy940118@gmail.com>"

# php.ini
ENV TIMEZONE            Asia/Shanghai
ENV PHP_MEMORY_LIMIT    512M
ENV MAX_UPLOAD          50M
ENV PHP_MAX_FILE_UPLOAD 200
ENV PHP_MAX_POST        100M
ENV COMPOSER_ALLOW_SUPERUSER 1

# phpize env
ENV PHPIZE_DEPS \
        autoconf \
        dpkg-dev dpkg \
        file \
        g++ \
        gcc \
        libc-dev \
        make \
        pkgconf \
        re2c

# php module
RUN apk add libmcrypt-dev \
        libxml2-dev \
        libxslt-dev \
    && docker-php-ext-install soap\
        xsl \
        xmlrpc \
        zip \
        pcntl \
        pdo_mysql \
        mysqli \
        exif \
        bcmath \
        sockets \
        shmop \
        sysvsem \
        opcache

# gd
RUN apk add libwebp-dev \
        libpng-dev \
        libjpeg-turbo-dev \
        freetype-dev \
    && docker-php-ext-configure gd \
        --enable-gd-native-ttf \
        --with-freetype-dir \
        --with-jpeg-dir \
    && docker-php-ext-install gd

# imagick
RUN apk add --no-cache --virtual .phpize-deps-configure $PHPIZE_DEPS \
    && apk add imagemagick-dev \
    && printf '\n' | pecl install imagick \
    && docker-php-ext-enable imagick \
    && rm -rf /tmp/pear \
    && apk del .phpize-deps-configure

# redis
RUN apk add --no-cache --virtual .phpize-deps-configure $PHPIZE_DEPS \
    && printf '\n' | pecl install redis \
    && docker-php-ext-enable redis \
    && rm -rf /tmp/pear \
    && apk del .phpize-deps-configure

# swoole
RUN apk add --no-cache --virtual .phpize-deps-configure $PHPIZE_DEPS \
    && printf '\n' | pecl install swoole \
    && docker-php-ext-enable swoole \
    && rm -rf /tmp/pear \
    && apk del .phpize-deps-configure

RUN mv $PHP_INI_DIR/php.ini-production $PHP_INI_DIR/php.ini
RUN sed -i "s|;*date.timezone =.*|date.timezone = ${TIMEZONE}|i" $PHP_INI_DIR/php.ini && \
    sed -i "s|;*memory_limit =.*|memory_limit = ${PHP_MEMORY_LIMIT}|i" $PHP_INI_DIR/php.ini && \
    sed -i "s|;*upload_max_filesize =.*|upload_max_filesize = ${MAX_UPLOAD}|i" $PHP_INI_DIR/php.ini && \
    sed -i "s|;*max_file_uploads =.*|max_file_uploads = ${PHP_MAX_FILE_UPLOAD}|i" $PHP_INI_DIR/php.ini && \
    sed -i "s|;*post_max_size =.*|post_max_size = ${PHP_MAX_POST}|i" $PHP_INI_DIR/php.ini && \
    sed -i "s|;*cgi.fix_pathinfo=.*|cgi.fix_pathinfo= 0|i" $PHP_INI_DIR/php.ini


# Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/ --filename=composer
# Composer aliyun mirror
RUN composer config -g repo.packagist composer https://mirrors.aliyun.com/composer/

WORKDIR /data/www

CMD ["php-fpm", "-R"]