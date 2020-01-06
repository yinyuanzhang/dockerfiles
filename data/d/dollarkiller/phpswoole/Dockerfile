FROM php:7.2-fpm-alpine
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
    && apk update && apk upgrade \
    && apk add m4 autoconf make gcc g++ linux-headers \
    && pecl install swoole-4.2.1 \
    && docker-php-ext-enable swoole
CMD ["php","-m"]