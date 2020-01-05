FROM alpine:edge
MAINTAINER brantje <brantje@gmail.com>

ARG GNU_LIBICONV_VERSION=1.14

ENV UID=991 GID=991 \
    UPLOAD_MAX_SIZE=10G \
    APC_SHM_SIZE=128M \
    OPCACHE_MEM_SIZE=128 \
    REDIS_MAX_MEMORY=64mb \
    CRON_PERIOD=15m \
    TZ=Etc/UTC \
    DB_TYPE=sqlite3 \
    ADMIN_USER=admin \
    ADMIN_PASSWORD=admin \
    MYSQL_RANDOM_ROOT_PASSWORD=yes


RUN echo "@commuedge https://nl.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories \
 && echo "@testing https://nl.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories \
 && BUILD_DEPS=" \
    tar \
    build-base \
    autoconf \
    automake \
    libtool" \
 && apk -U add \
    ${BUILD_DEPS} \
    nginx \
    s6 \
    bash \
    libressl \
    ca-certificates \
    libsmbclient \
    samba-client \
    su-exec \
    tzdata \
    bash \
    redis \
    mariadb \
    mariadb-client \
    php7@commuedge \
    php7-fpm@commuedge \
    php7-intl@commuedge \
    php7-mbstring@commuedge \
    php7-curl@commuedge \
    php7-gd@commuedge \
    php7-mcrypt@commuedge \
    php7-opcache@commuedge \
    php7-json@commuedge \
    php7-session@commuedge \
    php7-pdo@commuedge \
    php7-dom@commuedge \
    php7-ctype@commuedge \
    php7-pdo_mysql@commuedge \
    php7-pdo_pgsql@commuedge \
    php7-pgsql@commuedge \
    php7-pdo_sqlite@commuedge \
    php7-sqlite3@commuedge \
    php7-zlib@commuedge \
    php7-zip@commuedge \
    php7-xmlreader@commuedge \
    php7-posix@commuedge \
    php7-openssl@commuedge \
    php7-ldap@commuedge \
    php7-ftp@commuedge \
    php7-pcntl@commuedge \
    php7-apcu@testing \
    php7-redis@testing \
    php7-pear@commuedge \
    php7-dev@commuedge \
 && mkdir /nextcloud && cd /tmp \
 && wget -q http://ftp.gnu.org/pub/gnu/libiconv/libiconv-${GNU_LIBICONV_VERSION}.tar.gz \
 && tar xzf libiconv-${GNU_LIBICONV_VERSION}.tar.gz && cd libiconv-${GNU_LIBICONV_VERSION} \
 && ./configure --prefix=/usr/local \
 && wget -q https://raw.githubusercontent.com/mxe/mxe/7e231efd245996b886b501dad780761205ecf376/src/libiconv-1-fixes.patch \
 && patch -p1 -u < libiconv-1-fixes.patch \
 && make && make install && libtool --finish /usr/local/lib && cd /tmp \
 && wget -q http://is1.php.net/get/php-7.0.12.tar.gz/from/this/mirror -O php7.tar.gz \
 && tar xzf php7.tar.gz && cd /tmp/php-7.0.12/ext/iconv && phpize7 \
 && ./configure --with-iconv=/usr/local --with-php-config=/usr/bin/php-config7 \
 && make && cp modules/iconv.so /usr/lib/php7/modules && cd /tmp \
 && echo "extension=iconv.so" > /etc/php7/conf.d/00_iconv.ini \
 && wget -q https://download.nextcloud.com/server/daily/latest.tar.bz2 \
 && tar xjf latest.tar.bz2 --strip 1 -C /nextcloud \
 && apk del ${BUILD_DEPS} php7-pear php7-dev \
 && wget https://github.com/nextcloud/passman/archive/master.zip \
 && rm -rf /var/cache/apk/* /tmp/*
COPY nginx.conf /etc/nginx/nginx.conf
COPY php-fpm.conf /etc/php7/php-fpm.conf
COPY opcache.ini /etc/php7/conf.d/00_opcache.ini
COPY apcu.ini /etc/php7/conf.d/apcu.ini
COPY redis.conf /etc/redis.conf
COPY run.sh /usr/local/bin/run.sh
COPY setup.sh /usr/local/bin/setup.sh
COPY occ /usr/local/bin/occ
COPY startup /usr/local/bin/startup
COPY s6.d /etc/s6.d
COPY setup_mysql.sh /usr/local/bin/setup_mysql.sh
RUN chmod -R +x /usr/local/bin/* /etc/s6.d/*/* /etc/s6.d/.s6-svscan/*
VOLUME /data /config /apps2 /var/lib/redis /var/lib/mysql /ssl

EXPOSE 8888
EXPOSE 8443

LABEL description="A server software for creating file hosting services" \
      nextcloud="Nextcloud daily build"

CMD ["run.sh"]
