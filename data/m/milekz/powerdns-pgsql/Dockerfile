FROM alpine:3.9

ENV REFRESHED_AT="2019-11-15" \
    POWERDNS_VERSION=4.2.0 \
    PGSQL_AUTOCONF=true \
    PGSQL_HOST="postgres" \
    PGSQL_PORT="5432" \
    PGSQL_USER="postgres" \
    PGSQL_PASS="root" \
    PGSQL_DB="pdns" 

 RUN apk --update add libpq sqlite-libs libstdc++ libgcc mariadb-client mariadb-connector-c postgresql-client && \
    apk add --virtual build-deps \
      g++ make mariadb-dev postgresql-dev sqlite-dev curl boost-dev mariadb-connector-c-dev && \
    curl -sSL https://downloads.powerdns.com/releases/pdns-$POWERDNS_VERSION.tar.bz2 | tar xj -C /tmp && \
    cd /tmp/pdns-$POWERDNS_VERSION && \
    ./configure --prefix="" --exec-prefix=/usr --sysconfdir=/etc/pdns \
      --with-modules="bind gmysql gpgsql gsqlite3" --without-lua --disable-lua-records && \
    make && make install-strip && cd / && \
    mkdir -p /etc/pdns/conf.d && \
    addgroup -S pdns 2>/dev/null && \
    adduser -S -D -H -h /var/empty -s /bin/false -G pdns -g pdns pdns 2>/dev/null && \
    cp /usr/lib/libboost_program_options-mt.so* /tmp && \
    apk del --purge build-deps && \
    mv /tmp/libboost_program_options-mt.so* /usr/lib/ && \
    rm -rf /tmp/pdns-$POWERDNS_VERSION /var/cache/apk/*

ADD schema.pgsql.sql /etc/pdns/
ADD schema.sqlite3.sql /etc/pdns/
COPY pg_pdns.conf /etc/pdns/pdns.conf
ADD pg_entrypoint.sh /

EXPOSE 53/tcp 53/udp 8081/tcp

ENTRYPOINT ["/pg_entrypoint.sh"]
