FROM alpine
MAINTAINER Artem Silenkov <artem.silenkov@gmail.com>

ENV POWERDNS_RECURSOR_VERSION=4.1.3

RUN apk --update add libstdc++ libgcc boost lua-dev && \
    apk add --virtual build-deps \
      g++ make curl boost-dev lua-dev libressl-dev && \
      mkdir /tmp/pdns-recursor && \
    curl -sSL https://downloads.powerdns.com/releases/pdns-recursor-$POWERDNS_RECURSOR_VERSION.tar.bz2 | tar xj -C /tmp

COPY libressl-2.7.patch /tmp/pdns-recursor-$POWERDNS_RECURSOR_VERSION

RUN cd /tmp/pdns-recursor-$POWERDNS_RECURSOR_VERSION && \
    ./configure --prefix="" --exec-prefix=/usr --sysconfdir=/etc/pdns && \
    patch -p1 < libressl-2.7.patch && \
    make && make install-strip && cd / && \
    mkdir -p /etc/pdns/conf.d && \
    addgroup -S pdns 2>/dev/null && \
    adduser -S -D -H -h /var/empty -s /bin/false -G pdns -g pdns pdns 2>/dev/null && \
    apk del --purge build-deps && \
    rm -rf /tmp/pdns-recursor-$POWERDNS_RECURSOR_VERSION /var/cache/apk/*

ADD recursor.conf /etc/pdns/
ADD entrypoint.sh /

EXPOSE 53/tcp 53/udp

ENTRYPOINT ["/entrypoint.sh"]
