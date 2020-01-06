FROM php:7.2-fpm-alpine
LABEL mantainer="Giuseppe Iannelli <dev@giuseppeiannelli.it>"
LABEL description="php-fpm image with exif,gd,mcrypt,mysqli,mongodb,pcntl,pdo_mysql,rdkafka,redis,soap,sockets,zip modules and composer"

### CUSTOM ARGUMENTS ###
ARG PECL_MONGO_VERSION=1.5.3
ARG PECL_REDIS_VERSION=4.2.0
ARG PECL_MCRYPT_VERSION=1.0.2
ARG PECL_RBKAFKA_VERSION=3.0.5
ARG LIB_RDKAFKA_VERSION=v0.11.6

### CUSTOM ENVIRONMENTS ###
ENV APP_CWD=/app/code
ENV PHP_MAXEXECUTIONTIME=30
ENV PHP_MEMORYLIMIT=128M
ENV PHP_DISPLAYERRORS=Off
ENV PHP_DISPLASTARTUPERRORS=Off
ENV PHP_ERRORREPORTING='E_ALL & ~E_DEPRECATED & ~E_STRICT'
ENV PHP_VARIABLESORDER=GPCS
ENV PHP_POSTMAXSIZE=8M
ENV PHP_UPLOADMAXFILESIZE=2M
ENV PHP_SHORTOPENTAG=Off

# persistent / runtime deps
RUN set -e \
	&& apk add --no-cache --virtual .build-deps \
    $PHPIZE_DEPS \
    coreutils \
    curl-dev \
    freetype-dev \
    libedit-dev \
    libjpeg-turbo-dev \
    libmcrypt-dev \
    libpng-dev \
		libxml2-dev \
    libwebp-dev \
    openldap-dev \
		openssl-dev \
		sqlite-dev \
    git \
    python \
    bash \
  && $(which docker-php-ext-install) -j$(nproc) \
    pcntl soap sockets \
  && $(which docker-php-ext-configure) exif \
  --with-libdir=/usr/lib \
  && docker-php-ext-install -j$(nproc) exif \
  && $(which docker-php-ext-configure) gd \
  --with-freetype-dir=/usr/lib/ \
  --with-jpeg-dir=/usr/lib \
  --with-png-dir=/usr/lib \
  --with-vpx-dir=/usr/lib \
  --with-webp-dir=/usr/lib \
  && docker-php-ext-install -j$(nproc) gd \
  && $(which docker-php-ext-configure) mysqli \
  --with-mysqli=mysqlnd \
  && docker-php-ext-install -j$(nproc) mysqli \
  && $(which docker-php-ext-configure) pdo_mysql \
  --with-pdo-mysql=mysqlnd \
  && docker-php-ext-install -j$(nproc) pdo_mysql \
  && $(which docker-php-ext-configure) zip \
  --with-libdir=/usr/lib \
  && docker-php-ext-install -j$(nproc) zip \
  && pecl install mongodb-${PECL_MONGO_VERSION} \
  && docker-php-ext-enable mongodb \
  && pecl install redis-${PECL_REDIS_VERSION} \
  && docker-php-ext-enable redis \
  && pecl install mcrypt-${PECL_MCRYPT_VERSION} \
  && docker-php-ext-enable mcrypt \
  && cd /usr/src/ \
  && git clone https://github.com/edenhill/librdkafka.git \
  && cd librdkafka/ \
  && git checkout tags/${LIB_RDKAFKA_VERSION} -b ${LIB_RDKAFKA_VERSION}  \
  && ./configure \
  && make -j"$(getconf _NPROCESSORS_ONLN)" \
  && make install \
  && cd /usr/src/ \
  && rm -rf /usr/src/librdkafka/ \
  && pecl install rdkafka-${PECL_RBKAFKA_VERSION} \
  && docker-php-ext-enable rdkafka \
  && apk del .build-deps \
  && apk add \
    bison \
    freetype \
    gettext \
    libjpeg \
    libldap \
    libmcrypt \
    libpng \
    libsasl \
    libvpx \
    libwebp \
  && rm -rf /var/cache/apk/* \
  && docker-php-source delete \
  && curl -fSL https://getcomposer.org/composer.phar -o /usr/bin/composer && chmod +x /usr/bin/composer

COPY docker /docker
COPY docker-php-entrypoint /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-php-entrypoint

#set workdir
WORKDIR ${APP_CWD}
VOLUME [ "${APP_CWD}" ]

ENTRYPOINT ["/usr/local/bin/docker-php-entrypoint"]
CMD ["php-fpm"]
