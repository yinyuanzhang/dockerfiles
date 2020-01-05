FROM alpine
MAINTAINER Artem Silenkov <artem.silenkov@gmail.com>

ENV POWERDNS_VERSION=4.1.3 \
    MYSQL_AUTOCONF=true \
    MYSQL_HOST="mysql" \
    MYSQL_PORT="3306" \
    MYSQL_USER="root" \
    MYSQL_PASS="root" \
    MYSQL_DB="pdns"

RUN apk --update add mysql-client mariadb-dev libpq sqlite-libs libstdc++ libgcc && \
    apk add --virtual build-deps \
      g++ make mariadb-dev postgresql-dev sqlite-dev curl boost-dev && \
      mkdir /tmp/pdns && \
    curl -sSL https://downloads.powerdns.com/releases/pdns-$POWERDNS_VERSION.tar.bz2 | tar xj -C /tmp
    

COPY libressl-2.7.patch /tmp/pdns-$POWERDNS_VERSION

RUN cd /tmp/pdns-$POWERDNS_VERSION && \
    patch -p1 < libressl-2.7.patch && \
    ./configure --prefix="" --exec-prefix=/usr --sysconfdir=/etc/pdns \
      --with-modules="bind gmysql gpgsql gsqlite3" --without-lua && \
    make && make install-strip && cd / && \
    mkdir -p /etc/pdns/conf.d && \
    addgroup -S pdns 2>/dev/null && \
    adduser -S -D -H -h /var/empty -s /bin/false -G pdns -g pdns pdns 2>/dev/null && \
    apk del --purge build-deps && \
    rm -rf /tmp/pdns-$POWERDNS_VERSION /var/cache/apk/*

ADD schema.sql pdns.conf /etc/pdns/
ADD entrypoint.sh /

EXPOSE 54/tcp 54/udp 8081/tcp

ENTRYPOINT ["/entrypoint.sh"]
