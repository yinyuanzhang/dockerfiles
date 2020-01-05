FROM alpine:edge

LABEL maintainer "Marvin Steadfast <marvin@xsteadfastx.org>"

ARG WALLABAG_VERSION=2.3.6

RUN echo http://dl-2.alpinelinux.org/alpine/edge/community/ >> /etc/apk/repositories
RUN apk --no-cache add shadow

RUN \
usermod -u 99 nobody && \
usermod -g 100 nobody && \
usermod -d /home nobody && \
chown -R nobody:users /home

RUN mkdir -p /config && \
chown -R nobody:users /config && \
chmod 755 -R /config

RUN set -ex \
 && apk update \
 && apk upgrade --available \
 && apk add \
      ansible \
      curl \
      git \
      libwebp \
      mariadb-client \
      nginx \
      pcre \
      php7 \
      php7-amqp \
      php7-bcmath \
      php7-ctype \
      php7-curl \
      php7-dom \
      php7-fpm \
      php7-gd \
      php7-gettext \
      php7-iconv \
      php7-json \
      php7-mbstring \
      php7-openssl \
      php7-pdo_mysql \
      php7-pdo_pgsql \
      php7-pdo_sqlite \
      php7-phar \
      php7-session \
      php7-simplexml \
      php7-tokenizer \
      php7-xml \
      php7-zlib \
      php7-sockets \
      php7-xmlreader \
      php7-tidy \
      py-mysqldb \
      py-psycopg2 \
      py-simplejson \
      rabbitmq-c \
      s6 \
      tar \
 && rm -rf /var/cache/apk/* \
 && ln -sf /dev/stdout /var/log/nginx/access.log \
 && ln -sf /dev/stderr /var/log/nginx/error.log \
 && curl -s https://getcomposer.org/installer | php \
 && mv composer.phar /usr/local/bin/composer \
 && git clone --branch $WALLABAG_VERSION --depth 1 https://github.com/wallabag/wallabag.git /var/www/wallabag

COPY root /

RUN set -ex \
 && cd /var/www/wallabag \
 && SYMFONY_ENV=prod composer install --no-dev -o --prefer-dist \
 && chown -R nobody:nobody /var/www/wallabag

VOLUME ["/var/www/wallabag/app/config","/config"]
VOLUME ["/var/www/wallabag/data","/config/data"]
VOLUME ["/var/www/wallabag/web/assets/images","/config/images"]
EXPOSE 80
ENTRYPOINT ["/entrypoint.sh"]
CMD ["wallabag"]
