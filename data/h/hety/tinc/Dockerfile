FROM hety/alpine

ARG tincversion=1.1pre17

RUN apk add --no-cache readline-dev zlib-dev lzo-dev openssl-dev linux-headers gcc g++ make ncurses-dev libpcap-dev readline zlib lzo libpcap && \
  wget -q -O - "$@" https://www.tinc-vpn.org/packages/tinc-${tincversion}.tar.gz | tar -xzC /tmp/ && \
  cd /tmp/tinc-${tincversion} && ./configure --prefix=/usr --enable-jumbograms --enable-tunemu --sysconfdir=/etc --localstatedir=/var && \
  make && make install src && \
  cd / && rm -rfv /tmp/tinc-${tincversion} && apk del --no-cache --purge readline-dev zlib-dev lzo-dev openssl-dev linux-headers gcc g++ make ncurses-dev libpcap-dev libc-utils

EXPOSE 655/tcp 655/udp
VOLUME /etc/tinc
