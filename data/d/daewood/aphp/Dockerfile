FROM daewood/abase
MAINTAINER daewood <daewood@qq.com>

RUN mkdir -p /var/www && \
    addgroup -g 82 -S www-data && \
    adduser -u 82 -S -D -g "" -G www-data www-data && \
    chown -R www-data:www-data /var/www && \
	apk add --update php5 \
        php5-bcmath \
        php5-cli \
        php5-ctype \
        php5-curl \
        php5-fpm \
        php5-gd \
        php5-gettext \
        php5-iconv \
        php5-json \
        php5-mysql \
        php5-opcache \
        php5-openssl \
        php5-pdo \
        php5-pdo_mysql \
        php5-pdo_pgsql \
        php5-pdo_sqlite \
        php5-pgsql \
        php5-sockets \
        php5-sqlite3 \
        php5-xml \
        php5-xmlreader \
        php5-zlib && \
    rm -rf /var/cache/apk/*

COPY rootfs/ /

ENTRYPOINT ["/init"]
CMD []

EXPOSE 9000
VOLUME ["/var/www"]
