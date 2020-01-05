FROM php:7.3-cli-alpine

ENV TZ Europe/Riga

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

RUN set -xe \
    && apk add --update \
        ${PHPIZE_DEPS} \
        postgresql-dev \
        mysql-dev \
        zlib-dev \ 
        libzip-dev \
        libzip \
    && pecl install xdebug apcu \
    && docker-php-ext-configure zip --with-libzip=/usr/include \
    && docker-php-ext-install pdo pdo_pgsql opcache zip pdo_mysql mysqli \
    && docker-php-ext-enable pdo pdo_pgsql opcache zip apcu xdebug pdo_mysql mysqli \
    && apk del \
        postgresql-libs \
        libsasl \
        db \
        zlib-dev \
        libzip-dev \
        mysql-dev \
        ${PHPIZE_DEPS}

RUN set -xe \
    && apk add --update tzdata \
    && cp /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo "${TZ}" > /etc/timezone \
    && echo "date.timezone=${TZ}" > /usr/local/etc/php/conf.d/timezone.ini \
    && apk del tzdata

RUN mv "$PHP_INI_DIR/php.ini-development" "$PHP_INI_DIR/php.ini"

CMD ["php", "-a"]