FROM hikarushindo/alpine:3.5

MAINTAINER Pascal Nitsche

ENV GPG_KEYS="528995BFEDFBA7191D46839EF9BA0ADA31CBD89E"

ENV PHP_VERSION="7.1.1"
ENV PHP_URL="https://secure.php.net/get/php-$PHP_VERSION.tar.xz/from/this/mirror" PHP_ASC_URL="https://secure.php.net/get/php-$PHP_VERSION.tar.xz.asc/from/this/mirror"
ENV PHP_SHA256="b3565b0c1441064eba204821608df1ec7367abff881286898d900c2c2a5ffe70" PHP_MD5="65eef256f6e7104a05361939f5e23ada"
ENV PHP_INI_DIR="/usr/local/etc/php"
ENV PHP_EXTRA_CONFIGURE_ARGS="--enable-fpm --with-fpm-user=www-data --with-fpm-group=www-data"

ENV ADDITIONAL_PACKAGES \
    imagemagick

ENV PHP_PECL_EXTENSIONS \
    imagick \
    apcu

ENV PHP_ENABLE_EXTENSIONS \
    apcu \
    bz2 \
    gd \
    gettext \
    gmp \
    imagick \
    ldap \
    mcrypt \
    mysqli \
    pdo_mysql \
    pdo_pgsql \
    pgsql \
    pspell \
    tidy \
    xmlrpc \
    xsl

ENV PHP_ENABLE_ZEND_EXTENSIONS \
    opcache

ENV PHPIZE_DEPS \
    autoconf \
    file \
    g++ \
    gcc \
    libc-dev \
    make \
    pkgconf \
    re2c \
    icu-dev \
    postgresql-dev \
    bzip2-dev \
    freetype-dev \
    libjpeg-turbo-dev \
    libmcrypt-dev \
    libpng-dev \
    gettext-dev \
    gmp-dev \
    imagemagick-dev \
    openldap-dev \
    aspell-dev \
    tidyhtml-dev \
    libxslt-dev

# Apply stack smash protection to functions using local buffers and alloca()
# Make PHP's main executable position-independent (improves ASLR security mechanism, and has no performance impact on x86_64)
# Enable optimization (-O2)
# Enable linker optimization (this sorts the hash buckets to improve cache locality, and is non-default)
# Adds GNU HASH segments to generated executables (this is used if present, and is much faster than sysv hash; in this configuration, sysv hash is also generated)
# https://github.com/docker-library/php/issues/272
ENV PHP_CFLAGS="-fstack-protector-strong -fpic -fpie -O2"
ENV PHP_CPPFLAGS="$PHP_CFLAGS"
ENV PHP_LDFLAGS="-Wl,-O1 -Wl,--hash-style=both -pie"

# ensure www-data user exists
RUN set -x \
  && addgroup -g 82 -S www-data \
  && adduser -u 82 -D -S -G www-data www-data
# 82 is the standard uid/gid for "www-data" in Alpine
# http://git.alpinelinux.org/cgit/aports/tree/main/apache2/apache2.pre-install?h=v3.3.2
# http://git.alpinelinux.org/cgit/aports/tree/main/lighttpd/lighttpd.pre-install?h=v3.3.2
# http://git.alpinelinux.org/cgit/aports/tree/main/nginx-initscripts/nginx-initscripts.pre-install?h=v3.3.2

RUN apk add --no-cache --virtual .persistent-deps \
    ca-certificates \
    curl \
    tar \
    xz \
    icu-libs \
    libltdl \
    $ADDITIONAL_PACKAGES

RUN mkdir -p $PHP_INI_DIR/conf.d

RUN set -xe; \
  \
  apk add --no-cache --virtual .build-deps \
    gnupg \
    wget \
    libressl \
    $PHPIZE_DEPS \
    curl-dev \
    libedit-dev \
    libxml2-dev \
    libressl-dev \
    sqlite-dev \
    libtool \
  ; \
  # Fix tidyhtml error
  ln -s /usr/include/tidybuffio.h /usr/include/buffio.h; \
  \
  mkdir -p /usr/src; \
  cd /usr/src; \
  \
  wget -O php.tar.xz "$PHP_URL"; \
  \
  if [ -n "$PHP_SHA256" ]; then \
    echo "$PHP_SHA256 *php.tar.xz" | sha256sum -c -; \
  fi; \
  if [ -n "$PHP_MD5" ]; then \
    echo "$PHP_MD5 *php.tar.xz" | md5sum -c -; \
  fi; \
  \
  if [ -n "$PHP_ASC_URL" ]; then \
    wget -O php.tar.xz.asc "$PHP_ASC_URL"; \
    export GNUPGHOME="$(mktemp -d)"; \
    for key in $GPG_KEYS; do \
      gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
    done; \
    gpg --batch --verify php.tar.xz.asc php.tar.xz; \
    rm -r "$GNUPGHOME"; \
  fi; \
  \
  export CFLAGS="$PHP_CFLAGS" \
    CPPFLAGS="$PHP_CPPFLAGS" \
    LDFLAGS="$PHP_LDFLAGS" \
  && mkdir -p /usr/src/php \
  && tar -Jxf /usr/src/php.tar.xz -C /usr/src/php --strip-components=1 \
  && cd /usr/src/php \
  && ./configure \
    --with-config-file-path="$PHP_INI_DIR" \
    --with-config-file-scan-dir="$PHP_INI_DIR/conf.d" \
    \
    --disable-cgi \
    \
# --enable-ftp is included here because ftp_ssl_connect() needs ftp to be compiled statically (see https://github.com/docker-library/php/issues/236)
    --enable-ftp \
# --enable-mbstring is included here because otherwise there's no way to get pecl to use it properly (see https://github.com/docker-library/php/issues/195)
    --enable-mbstring \
# --enable-mysqlnd is included here because it's harder to compile after the fact than extensions are (since it's a plugin for several extensions, not an extension in itself)
    --enable-mysqlnd \
    --with-bz2=shared \
    --with-gd=shared \
    --with-gettext=shared \
    --with-gmp=shared \
    --with-ldap=shared \
    --with-mcrypt=shared \
    --with-mysqli=shared \
    --with-opcache=shared \
    --with-pdo_mysql=shared \
    --with-pdo_pgsql=shared \
    --with-pgsql=shared \
    --with-posix=shared \
    --with-pspell=shared \
    --with-soap=shared \
    --with-sockets=shared \
    --with-tidy=shared \
    --with-xmlrpc=shared \
    --with-xsl=shared \
    \
    --enable-bcmath \
    --enable-calendar \
    --enable-exif \
    --enable-intl \
    --enable-shmop \
    --enable-soap \
    --enable-sysvmsg \
    --enable-sysvsem \
    --enable-sysvshm \
    --enable-zip \
    \
    --with-curl \
    --with-libedit \
    --with-openssl \
    --with-zlib \
    \
    $PHP_EXTRA_CONFIGURE_ARGS \
  && make -j "$(getconf _NPROCESSORS_ONLN)" \
  && make install \
  && { find /usr/local/bin /usr/local/sbin -type f -perm +0111 -exec strip --strip-all '{}' + || true; } \
  && make clean \
  \
  && runDeps="$( \
    scanelf --needed --nobanner --recursive /usr/local \
      | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
      | sort -u \
      | xargs -r apk info --installed \
      | sort -u \
  )" \
  && apk add --no-cache --virtual .php-rundeps $runDeps \
  \
  # Install extensions
  && pear channel-discover pear.twig-project.org \
  && for extension in $PHP_PECL_EXTENSIONS; do \
    printf "\n" | pecl install $extension; \
  done \
  \
  && cd /root \
  && rm -rf *.tar.gz* /usr/src /root/.gnupg /usr/include/buffio.h \
  \
  && apk del --purge .build-deps

RUN set -ex \
  && cd /usr/local/etc \
  && echo "[PHP]" > /usr/local/etc/php/php.ini; \
  for extension in $PHP_ENABLE_EXTENSIONS; do \
       echo "extension=$extension.so" >> /usr/local/etc/php/php.ini; \
  done; \
  for extension in $PHP_ENABLE_ZEND_EXTENSIONS; do \
     echo "zend_extension=$extension.so" >> /usr/local/etc/php/php.ini; \
  done; \
  if [ -d php-fpm.d ]; then \
    # for some reason, upstream's php-fpm.conf.default has "include=NONE/etc/php-fpm.d/*.conf"
    sed 's!=NONE/!=!g' php-fpm.conf.default | tee php-fpm.conf > /dev/null; \
    cp php-fpm.d/www.conf.default php-fpm.d/www.conf; \
  else \
    # PHP 5.x doesn't use "include=" by default, so we'll create our own simple config that mimics PHP 7+ for consistency
    mkdir php-fpm.d; \
    cp php-fpm.conf.default php-fpm.d/www.conf; \
    { \
      echo '[global]'; \
      echo 'include=etc/php-fpm.d/*.conf'; \
    } | tee php-fpm.conf; \
  fi \
  && { \
    echo '[global]'; \
    echo 'error_log = /proc/self/fd/2'; \
    echo; \
    echo '[www]'; \
    echo '; if we send this to /proc/self/fd/1, it never appears'; \
    echo 'access.log = /proc/self/fd/2'; \
    echo; \
    echo 'clear_env = no'; \
    echo; \
    echo '; Ensure worker stdout and stderr are sent to the main error log.'; \
    echo 'catch_workers_output = yes'; \
  } | tee php-fpm.d/docker.conf \
  && { \
    echo '[global]'; \
    echo 'daemonize = no'; \
    echo; \
    echo '[www]'; \
    echo 'listen = [::]:9000'; \
  } | tee php-fpm.d/zz-docker.conf

COPY docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["docker-entrypoint.sh"]

WORKDIR /var/www

EXPOSE 9000
CMD ["php-fpm"]
