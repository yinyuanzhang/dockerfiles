FROM alpine:3.7

RUN \
  apk --update add autoconf autoconf-doc automake c-ares c-ares-dev curl gcc libc-dev libevent libevent-dev libtool make man openssl-dev openssl pkgconfig && \
  curl -o  /tmp/pgbouncer-1.8.1.tar.gz -L https://pgbouncer.github.io/downloads/files/1.8.1/pgbouncer-1.8.1.tar.gz && \
  cd /tmp && \
  tar xvfz /tmp/pgbouncer-1.8.1.tar.gz && \
  cd pgbouncer-1.8.1 && \
  ./configure --prefix=/usr && \
  make && \
  cp pgbouncer /usr/bin && \
  mkdir -p /etc/pgbouncer /var/log/pgbouncer /var/run/pgbouncer && \
  adduser -D -S pgbouncer && \
  chown -R pgbouncer /var/run/pgbouncer /var/log/pgbouncer /etc/pgbouncer/ && \
  cd /tmp && \
  rm -rf /tmp/pgbouncer*  && \
  apk del --purge autoconf autoconf-doc automake c-ares-dev curl gcc libc-dev libevent-dev libtool make man openssl-dev pkgconfig

ENV PG_USER=postgres PG_PASSWD=mysecretpassword PG_DBNAME=postgres PG_HOST=postgres PG_PORT=5432 LISTEN_PORT=6432 LISTEN_ADDR=0.0.0.0

ADD entrypoint.sh /entrypoint.sh

USER pgbouncer
VOLUME /etc/pgbouncer

EXPOSE 6432
CMD /entrypoint.sh
