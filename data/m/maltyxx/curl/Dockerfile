FROM alpine:3.10

LABEL maintainer="Yoann VANITOU <yvanitou@gmail.com>"

ARG CURL_VERSION=7.67.0

RUN set -x \
    && apk add --no-cache --virtual mybuild \
        build-base \
    && apk add --no-cache \
        openssl \
        openssl-dev \
        nghttp2-dev \
        ca-certificates \
        tzdata \
    && cd /tmp \
    && wget "https://curl.haxx.se/download/curl-$CURL_VERSION.tar.bz2" \
    && tar xjvf curl-$CURL_VERSION.tar.bz2 \
    && cd curl-$CURL_VERSION \
    && ./configure \
        --with-nghttp2=/usr \
        --prefix=/usr \
        --with-ssl \
        --enable-ipv6 \
        --enable-unix-sockets \
        --without-libidn \
        --disable-static \
        --with-pic \
    && make -j$(nproc) \
    && make install \
    && cd \
    && rm -rf /tmp/* \
    && apk del mybuild

COPY entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]

CMD ["curl", "--help"]
