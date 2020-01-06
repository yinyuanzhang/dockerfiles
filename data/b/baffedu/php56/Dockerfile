FROM php:5.6-fpm-alpine
MAINTAINER wish@baffedu.net

# RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories

RUN set x=1 && \
    apk update && \
    apk add --no-cache --virtual .build-deps $PHPIZE_DEPS zlib-dev imagemagick-dev libtool && \
    apk add --no-cache --virtual .tools supervisor rsync && \
    apk add --no-cache --virtual .imagick-runtime-deps imagemagick && \
    apk add --no-cache --virtual .mcrypt libmcrypt-dev && \
    apk add --no-cache --virtual .gd freetype libpng libjpeg-turbo freetype-dev libpng-dev libjpeg-turbo-dev && \
    docker-php-ext-configure gd \
        --with-gd \
        --with-freetype-dir=/usr/include/ \
        --with-png-dir=/usr/include/ \
        --with-jpeg-dir=/usr/include/ && \
    pecl install imagick && \
    docker-php-ext-install -j$(nproc) gd mysql mysqli pdo_mysql bcmath zip opcache mcrypt && \
    docker-php-ext-enable imagick && \
    wget https://getcomposer.org/composer.phar -O /usr/local/bin/composer && \
    chmod a+x /usr/local/bin/composer && \
    apk add --no-cache --virtual .nginx nginx && \
    mkdir -p /run/nginx && \
    mkdir -p /var/log/supervisor && \
    sed -i 's/;pidfile/pidfile/g' /etc/supervisord.conf && \
    sed -i 's/client_max_body_size/#client_max_body_size/g' /etc/nginx/nginx.conf && \
    docker-php-source delete && \
    apk del -f .build-deps freetype-dev libpng-dev libjpeg-turbo-dev && \
    rm -rf /tmp/* /var/cache/apk/*

ADD supervisor /etc/supervisor.d/
ADD nginx /etc/nginx/conf.d/

EXPOSE 80

CMD ["supervisord", "-n", "-c", "/etc/supervisord.conf"]
