FROM php:7.1-fpm-alpine

# Адрес файла с переменными окружения от корня проекта.
ENV ENV_PATH=.env \
    PHP_REDIS_VERSION=3.1.6

RUN apk update \
    && apk --no-cache --progress add \
        nginx \
        libressl \
        pcre \
        supervisor \
        sed \
        re2c \
        m4 \
        ca-certificates \
        py-pip \
    && mkdir -p /run/nginx/ \
    && chmod ugo+w /run/nginx/ \
    && rm -f /etc/nginx/nginx.conf \
    && mkdir -p /etc/nginx/conf.d \
    && mkdir -p /srv/app/ \
    && chmod -R 775 /srv/app/ \
    && chown -R nginx:nginx /var/www/ \
    && pip install --upgrade pip \
    && pip install supervisor-stdout \
    \
    # Bring in gettext so we can get `envsubst`, then throw
    # the rest away. To do this, we need to install `gettext`
    # then move `envsubst` out of the way so `gettext` can
    # be deleted completely, then move `envsubst` back.
    && apk add --no-cache --virtual .gettext gettext \
    && mv /usr/bin/envsubst /tmp/ \
    \
    && runDeps="$( \
    scanelf --needed --nobanner /usr/sbin/nginx /usr/lib/nginx/modules/*.so /tmp/envsubst \
      | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
      | sort -u \
      | xargs -r apk info --installed \
      | sort -u \
    )" \
    && apk add --no-cache --virtual .nginx-rundeps $runDeps \
    && apk del .gettext \
    && mv /tmp/envsubst /usr/local/bin/

RUN apk add --no-cache --virtual .persistent-deps \
    git \
    icu-libs

RUN set -xe \
    && apk add --no-cache --virtual .build-deps \
        $PHPIZE_DEPS \
        icu-dev \
        zlib-dev \
        libsasl \
    && docker-php-ext-install \
        intl \
        mbstring \
        bcmath \
        pcntl \
        zip \
        mysqli \
        pdo_mysql \
    && yes | pecl install -o -f \
        igbinary-2.0.8 \
        redis-$PHP_REDIS_VERSION \
        xdebug-2.5.5 \
    && docker-php-ext-enable \
        igbinary \
        redis \
    && apk del .build-deps

WORKDIR /app

COPY ./common/root/ /

RUN chmod 755 /entrypoint.sh \
    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin/ --filename=composer

EXPOSE 443 80

CMD ["/bin/sh", "/entrypoint.sh"]
