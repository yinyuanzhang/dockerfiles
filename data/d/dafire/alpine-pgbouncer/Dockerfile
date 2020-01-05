FROM gliderlabs/alpine:3.3

ADD etc/* /etc/pgbouncer/

RUN \
  apk --update add autoconf autoconf-doc automake c-ares c-ares-dev curl gcc libc-dev libevent libevent-dev libtool make man openssl-dev pkgconfig && \
  curl -o  /tmp/pgbouncer-1.7.2.tar.gz -L https://pgbouncer.github.io/downloads/files/1.7.2/pgbouncer-1.7.2.tar.gz && \
  cd /tmp && \
  tar xvfz /tmp/pgbouncer-1.7.2.tar.gz && \
  cd pgbouncer-1.7.2 && \
  ./configure --prefix=/usr && \
  make && \
  cp pgbouncer /usr/bin && \
  mkdir -p /etc/pgbouncer /var/log/pgbouncer /var/run/pgbouncer && \
  adduser -D -S pgbouncer && \
  chown -R pgbouncer /var/run/pgbouncer /var/log/pgbouncer /etc/pgbouncer/ && \
  cd /tmp && \
  rm -rf /tmp/pgbouncer*  && \
  apk del --purge autoconf autoconf-doc automake c-ares-dev curl gcc libc-dev libevent-dev libtool make man openssl-dev pkgconfig

ENV PG_USER=postgres PG_PASSWD=postgres PG_DBNAME=template1 PG_HOST=172.17.0.1 PG_PORT=5432

ADD start.sh /start.sh

USER pgbouncer
VOLUME /etc/pgbouncer
EXPOSE 6432
CMD /start.sh
