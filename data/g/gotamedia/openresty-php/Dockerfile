ARG BASE_IMAGE="alpine"
ARG BASE_TAG="3.9"

FROM ${BASE_IMAGE}:${BASE_TAG} as builder

ENV OPENRESTY_VERSION="1.15.8.1" \
    OPENRESTY_PREFIX="/opt/openresty" \
    PHP_VERSION="7.3.5" \
    PHP_PREFIX="/opt/php" \
    PHP_REDIS_VERSION="4.3.0" \
    OPENSSL_VERSION="1.0.2r" \
    PCRE_VERSION="8.42"

# PHP compile flags
ENV PHP_CFLAGS="-fstack-protector-strong -fpic -fpie -O2"
ENV PHP_CPPFLAGS="-fstack-protector-strong -fpic -fpie -O2"
ENV PHP_LDFLAGS="-Wl,-O1 -Wl,--hash-style=both -pie"

ENV PATH="${PATH}:/opt/php/bin:/opt/openresty/bin"

RUN addgroup http \
 && adduser -u 1000 -H -D -S -G http -h ${OPENRESTY_PREFIX} http \
 && apk update && apk upgrade \
 && apk add --no-cache \
        build-base \
        linux-headers \
        ca-certificates \
        pcre-dev \
        zlib-dev \
        ncurses-dev \
        readline-dev \
        perl-dev \
        curl \
        autoconf \
        dpkg-dev \
        dpkg \
        file \
        g++ \
        gcc \
        libc-dev \
        make \
        pkgconf \
        re2c \
        argon2-dev \
        coreutils \
        curl-dev \
        icu-dev \
        libedit-dev \
        libsodium-dev \
        libxml2-dev \
        libressl-dev \
# Downloading applications for compilation
 && cd /tmp \
 && curl -fsSL https://www.openssl.org/source/openssl-${OPENSSL_VERSION}.tar.gz | tar -xvz \
 && curl -fsSL https://ftp.pcre.org/pub/pcre/pcre-${PCRE_VERSION}.tar.gz | tar -xvz \
 && curl -fsSL https://openresty.org/download/openresty-${OPENRESTY_VERSION}.tar.gz | tar -xvz \
 && curl -fsSL https://www.php.net/get/php-${PHP_VERSION}.tar.xz/from/this/mirror | tar -Jxv \
 && curl -fsSL https://github.com/phpredis/phpredis/archive/${PHP_REDIS_VERSION}.tar.gz | tar -xvz

# Compile OpenResty
RUN cd /tmp/openresty-${OPENRESTY_VERSION} \
 && ./configure \
    --prefix=${OPENRESTY_PREFIX} \
    --with-openssl=/tmp/openssl-${OPENSSL_VERSION} \
    --with-pcre=/tmp/pcre-${PCRE_VERSION} \
    --with-file-aio \
    --with-http_v2_module \
    --with-luajit \
    --with-pcre-jit \
    --with-http_iconv_module \
    --with-http_addition_module \
    --with-http_gzip_static_module \
    --with-http_realip_module \
    --with-http_stub_status_module \
    --with-http_ssl_module \
    --without-http_ssi_module \
    --without-http_userid_module \
    --without-http_uwsgi_module \
    --without-http_scgi_module \
    -j$(nproc) \
 && make -j "$(nproc)" \
 && make install

# Compile PHP
RUN cd /tmp/php-${PHP_VERSION} \
 && ./configure \
    --build="x86_64-linux-musl" \
    --prefix=/opt/php \
    --with-config-file-path="${PHP_PREFIX}/etc" \
    --with-config-file-scan-dir="${PHP_PREFIX}/etc/conf.d" \
    --enable-option-checking=fatal \
    --enable-ftp \
    --enable-bcmath \
    --enable-mbstring \
    --enable-simplexml \
    --enable-opcache \
    --enable-intl \
    --enable-soap \
    --enable-fpm \
    --with-mhash \
    --with-password-argon2 \
    --with-sodium=shared \
    --with-pdo-mysql \
    --with-curl \
    --with-libedit \
    --with-openssl \
    --with-zlib \
    --with-libxml-dir=/usr/lib \
    --with-fpm-user=http \
    --with-fpm-group=http \
    --disable-cgi \
 && make -j "$(nproc)" \
 && find -type f -name '*.a' -delete \
 && make install \
 && make clean \
 && cp -v php.ini-production "${PHP_PREFIX}/etc/" \
 && cd /tmp/phpredis-${PHP_REDIS_VERSION} \
 && /opt/php/bin/phpize \
 && ./configure \
 && make && make install \
 && mkdir -p ${PHP_PREFIX}/etc/conf.d \
 && echo "extension=redis.so" > ${PHP_PREFIX}/etc/conf.d/redis.ini \
 && mv /opt/php/sbin/php-fpm /opt/php/bin/php-fpm \
 && rm -rf /opt/php/bin/pear* \
           /opt/php/bin/phar \
           /opt/php/bin/phar.phar \
           /opt/php/bin/php-config \
           /opt/php/bin/phpdbg \
           /opt/php/bin/phpize \
           /opt/php/sbin \
           /opt/php/php \
           /opt/php/etc/php-fpm.d/www.conf.default

# Now start over with the base image, and copy the
# compiled applications to the fresh image.
FROM ${BASE_IMAGE}:${BASE_TAG}

ENV PATH="${PATH}:/opt/php/bin:/opt/openresty/bin"

RUN addgroup http \
 && adduser -u 1000 -H -D -S -G http http \
 && apk update && apk upgrade \
 && apk add --no-cache \
        supervisor \
        inotify-tools \
        \
        bash \
        curl \
        zlib \
        ca-certificates \
        \
        libedit \
        libsodium \
        libxml2 \
        argon2-libs \
        icu-libs \
        \
        libgcc \
 && mkdir -p /data/log \
 && ln -sf /dev/stdout /data/log/supervisord.log \
 && ln -sf /dev/stdout /data/log/access.log \
 && ln -sf /dev/stderr /data/log/error.log \
 && ln -sf /dev/stderr /data/log/php-fpm.log \
 && ln -sf /dev/stderr /data/log/php-fpm-slow1.log \
 && ln -sf /dev/stderr /data/log/php-fpm-slow2.log

# Copy the compiled applications from /opt
COPY --chown=root:root --from=builder /opt /opt

# Copy container-files into the root
COPY --chown=root:root ./container-files /

CMD ["/usr/bin/supervisord", "-c", "/opt/supervisord/supervisord.conf"]
