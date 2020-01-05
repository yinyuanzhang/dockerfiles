FROM alpine:3.9

LABEL maintainer="HYec <i@hyec.me>"

ENV STRONGSWAN_VERSION 5.7.2

RUN STRONGSWAN_SOURCE="https://download.strongswan.org/strongswan-$STRONGSWAN_VERSION.tar.bz2" \
    && CONFIG=" \
        --prefix=/usr \
        --sysconfdir=/etc \
        --libexecdir=/usr/lib \
        --with-ipsecdir=/usr/lib/strongswan \
        --enable-aesni \
        --enable-chapoly \
        --enable-cmd \
        --enable-curl \
        --enable-dhcp \
        --enable-eap-dynamic \
        --enable-eap-identity \
        --enable-eap-md5 \
        --enable-eap-mschapv2 \
        --enable-eap-radius \
        --enable-eap-tls \
        --enable-farp \
        --enable-files \
        --enable-gcm \
        --enable-md4 \
        --enable-newhope \
        --enable-ntru \
        --enable-openssl \
        --enable-sha3 \
        --enable-shared \
        --disable-aes \
        --disable-des \
        --disable-gmp \
        --disable-hmac \
        --disable-ikev1 \
        --disable-md5 \
        --disable-rc2 \
        --disable-sha1 \
        --disable-sha2 \
        --disable-static \
    " \
    && apk add --no-cache \ 
        openssl \
        libcurl \
        iptables \
        ip6tables \
    && apk add --no-cache --virtual .build-deps \
        gcc \
        curl \
        make \
        linux-headers \
        libc-dev \
        openssl-dev \
        curl-dev \
    && curl -fSL $STRONGSWAN_SOURCE -o /tmp/strongswan.tar.bz2 \
    && mkdir -p /usr/src \
    && tar -jxC /usr/src -f /tmp/strongswan.tar.bz2 \
    && rm /tmp/strongswan.tar.bz2 \
    && cd /usr/src/strongswan-$STRONGSWAN_VERSION \
    && ./configure $CONFIG \
    && make \
    && make install \
    && rm -rf /usr/src/strongswan-$STRONGSWAN_VERSION \
    && apk del .build-deps \
    && mkdir -p /lib/modules

EXPOSE 500/udp \
       4500/udp

CMD ["/usr/sbin/ipsec", "start", "--nofork"]

