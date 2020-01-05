
ARG PHP_TAG="7.2-cli-alpine3.9"

FROM php:$PHP_TAG

ENV COMPOSER_ALLOW_SUPERUSER 1

RUN set -ex \
  	&& apk update \
    && apk add --no-cache --virtual .build-deps curl git gcc g++ make automake build-base autoconf pkgconfig \
    && apk add libstdc++ libtool openssl-dev \
    && git clone https://github.com/zeromq/zeromq4-x.git \
    && cd zeromq4-x && ./autogen.sh && ./configure && make && make install \
    && docker-php-ext-install sockets pcntl\
    && docker-php-source extract \
    && printf "/usr/local/lib\n" | pecl install zmq-1.1.3 \
    && docker-php-ext-enable zmq \
    && docker-php-source delete \
    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
    && apk del .build-deps \
    && rm -rf /tmp/* 

WORKDIR /usr/src/app
COPY . ./
EXPOSE 5559 5560
CMD ["php", "test.php"]