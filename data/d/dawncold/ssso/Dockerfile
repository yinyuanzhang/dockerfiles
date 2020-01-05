#
# Dockerfile for shadowsocks-libev
#

FROM alpine
LABEL maintainer=dc

ENV SERVER_ADDR 0.0.0.0
ENV SERVER_PORT 8388
ENV PASSWORD=
ENV METHOD      aes-256-gcm
ENV TIMEOUT     300
ENV DNS_ADDRS    8.8.8.8,8.8.4.4
ENV ARGS=

RUN set -ex \
 # Build environment setup
 && apk add --no-cache --virtual .build-deps \
    git \
    autoconf \
    automake \
    build-base \
    c-ares-dev \
    libev-dev \
    libtool \
    libsodium-dev \
    linux-headers \
    mbedtls-dev \
    pcre-dev \
 # Build & install
 && git clone https://github.com/shadowsocks/shadowsocks-libev.git /tmp/repo \
 && cd /tmp/repo \
 && git submodule init && git submodule update \
 && ./autogen.sh \
 && ./configure --prefix=/usr --disable-documentation \
 && make install \
 && apk del .build-deps \
 # Runtime dependencies setup
 && apk add --no-cache \
      rng-tools \
      $(scanelf --needed --nobanner /usr/bin/ss-* \
      | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
      | sort -u) \
 && rm -rf /tmp/repo

 RUN set -ex \
 # Build environment for simple-obfs
 && apk add --no-cache --virtual .build-deps \
    git \
    gcc \
    autoconf \
    make \
    libtool \
    automake \
    zlib-dev \
    openssl \
    asciidoc \
    xmlto \
    libpcre32 \
    libev-dev \
    g++ \
    linux-headers \
&& git clone https://github.com/shadowsocks/simple-obfs.git /tmp/simple-obfs \
&& cd /tmp/simple-obfs \
&& git submodule update --init --recursive \
&& ./autogen.sh \
&& ./configure && make \
&& make install \
&& apk del .build-deps \
&& rm -rf /tmp/simple-obfs

USER nobody

CMD exec ss-server \
      -s $SERVER_ADDR \
      -p $SERVER_PORT \
      -k ${PASSWORD:-$(hostname)} \
      -m $METHOD \
      -t $TIMEOUT \
      -d $DNS_ADDRS \
      -u \
      --plugin obfs-server \
      --plugin-opts "obfs=tls" \
      $ARGS