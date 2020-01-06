FROM php:7.2.18-fpm

COPY config/swift.ini /usr/local/etc/php/conf.d/za-swift.ini
COPY config/www.conf /usr/local/etc/php-fpm.d/www.conf
COPY run-perms-php /usr/local/bin

RUN chmod 755 /usr/local/bin/run-perms-php

RUN usermod -u 1000 -s /bin/bash www-data

RUN apt-get update && apt-get install -y \
        libfreetype6 \
        libpng16-16 \
        libgssrpc4 \
        libjpeg62-turbo \
        libicu57 \
        libpq5 \
        libkdb5-8 \
        libevent-2.0 \
    --no-install-recommends && rm -r /var/lib/apt/lists/*

RUN set -xe \
        && buildDeps=" \
            zlib1g-dev \
            libicu-dev \
            libpq-dev \
            libxml2-dev \
            libfreetype6-dev \
            libjpeg62-turbo-dev \
            libpng-dev \
        " \
        && apt-get update && apt-get install -y $buildDeps --no-install-recommends \
        && rm -rf /var/lib/apt/lists/* \
        && docker-php-ext-enable opcache \
        && docker-php-ext-install -j$(nproc) zip \
        && docker-php-ext-install -j$(nproc) intl \
        && docker-php-ext-install -j$(nproc) pdo_pgsql \
        && docker-php-ext-install -j$(nproc) iconv \
        && docker-php-ext-install -j$(nproc) bcmath \
        && docker-php-ext-install -j$(nproc) soap \
        && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
        && docker-php-ext-install -j$(nproc) gd \
        && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false -o APT::AutoRemove::SuggestsImportant=false $buildDeps

RUN set -xe\
    && buildDeps=" \
        git \
        libsasl2-dev \
        zlib1g-dev  \
        libevent-dev \
    " \
    && apt-get update && apt-get install -y $buildDeps --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir /tmp/libmemcached \
    && cd /tmp/libmemcached \
    && git clone https://github.com/awslabs/aws-elasticache-cluster-client-libmemcached.git \
    && cd /tmp/libmemcached/aws-elasticache-cluster-client-libmemcached \
    && touch configure.ac aclocal.m4 configure Makefile.am Makefile.in \
    && mkdir BUILD \
    && cd BUILD \
    && ../configure --prefix=/tmp/libmemcached --with-pic \
    && make \
    && make install \
    && cd /tmp \
    && git clone https://github.com/awslabs/aws-elasticache-cluster-client-memcached-for-php.git \
    && cd aws-elasticache-cluster-client-memcached-for-php/ \
    && git checkout php7 \
    && docker-php-ext-configure /tmp/aws-elasticache-cluster-client-memcached-for-php --with-libmemcached-dir=/tmp/libmemcached --disable-memcached-sasl \
    && sed -i "s#-lmemcached#/tmp/libmemcached/lib/libmemcachedutil.a /tmp/libmemcached/lib/libmemcached.a -lcrypt -lpthread -lm -lstdc++ -lsasl2#" Makefile \
    && sed -i "s#-lmemcachedutil##" Makefile \
    && sed -i "s#-L/tmp/libmemcached/lib##" Makefile \
    && docker-php-ext-install /tmp/aws-elasticache-cluster-client-memcached-for-php \
    && rm -rf /tmp/libmemcached /tmp/aws-elasticache-cluster-client-memcached-for-php \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false -o APT::AutoRemove::SuggestsImportant=false $buildDeps

ENV NODE_VERSION 8.11.1

RUN ARCH= && dpkgArch="$(dpkg --print-architecture)" \
  && case "${dpkgArch##*-}" in \
    amd64) ARCH='x64';; \
    ppc64el) ARCH='ppc64le';; \
    s390x) ARCH='s390x';; \
    arm64) ARCH='arm64';; \
    armhf) ARCH='armv7l';; \
    i386) ARCH='x86';; \
    *) echo "unsupported architecture"; exit 1 ;; \
  esac \
  && curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-$ARCH.tar.xz" \
  && tar -xJf "node-v$NODE_VERSION-linux-$ARCH.tar.xz" -C /usr/local --strip-components=1 --no-same-owner \
  && rm "node-v$NODE_VERSION-linux-$ARCH.tar.xz" \
  && ln -s /usr/local/bin/node /usr/local/bin/nodejs

RUN ln -s /usr/local/bin/node /usr/bin/nodejs \
  && npm install -g less

RUN curl -SL -o "datadog-php-tracer.deb" "https://github.com/DataDog/dd-trace-php/releases/download/0.23.0/datadog-php-tracer_0.23.0_amd64.deb" \
  && dpkg -i datadog-php-tracer.deb \
  && rm "datadog-php-tracer.deb"

CMD ["/usr/local/bin/run-perms-php"]

