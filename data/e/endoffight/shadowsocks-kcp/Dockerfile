FROM alpine:3.10

LABEL maintainer "endoffight <endoffight@gmail.com>"
LABEL keyword "shadowsocks kcptun s6"

RUN set -ex && \
    apk add --no-cache --virtual .build-deps \
                                autoconf \
                                build-base \
                                curl \
                                libev-dev \
                                linux-headers \
                                libsodium-dev \
                                mbedtls-dev \
                                pcre-dev \
                                tar \
                                tzdata \
                                c-ares-dev \
                                git \
                                gcc \
                                make \
                                libtool \
                                zlib-dev \
                                automake \
                                openssl \
                                asciidoc \
                                xmlto \
                                libpcre32 \
                                g++ && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    cd /tmp && \
    # kcptun
    v=`curl -I -s https://github.com/xtaci/kcptun/releases/latest | grep Location | sed -n 's/.*\/v\(.*\)/\1/p' | tr -d '\r'` && \
    curl -sSL https://github.com/xtaci/kcptun/releases/download/v$v/kcptun-linux-amd64-$v.tar.gz | tar xz server_linux_amd64 && \
    mv server_linux_amd64 /usr/bin/ && \
    # ss
    mkdir ss && \
    cd ss && \
    v=`curl -I -s https://github.com/shadowsocks/shadowsocks-libev/releases/latest | grep Location | sed -n 's/.*\/v\(.*\)/\1/p' | tr -d '\r'` && \
    curl -sSL https://github.com/shadowsocks/shadowsocks-libev/releases/download/v$v/shadowsocks-libev-$v.tar.gz | tar xz --strip 1 && \
    ./configure --prefix=/usr --disable-documentation && \
    make install && \
    cd /tmp && \
    git clone https://github.com/shadowsocks/simple-obfs.git && \
    cd simple-obfs && \
    git submodule update --init --recursive && \
    ./autogen.sh && \
    ./configure && \
    make && \
    make install && \
    cd .. && \
    runDeps="$( \
        scanelf --needed --nobanner /usr/bin/ss-* \
            | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
            | xargs -r apk info --installed \
            | sort -u \
    )" && \
    apk add --no-cache --virtual .run-deps $runDeps s6 tinyproxy && \
    apk del .build-deps && \
    rm -rf /tmp/*

ENV SERVER_ADDR=0.0.0.0 \
SERVER_PORT=37210 \
PASSWORD=laogao \
METHOD=aes-256-cfb \
TIMEOUT=300 \
FASTOPEN=--fast-open \
UDP_RELAY=-u \
DNS_ADDR=8.8.8.8 \
DNS_ADDR_2=8.8.4.4 \
ARGS='' \
KCP_LISTEN=38240 \
KCP_PASS=phpgao \
KCP_ENCRYPT=aes-192 \
KCP_MODE=fast2 \
KCP_MUT=1350 \
KCP_NOCOMP='' \
KCP_ARGS='' \
HTTP_AUTH='laogaoniubi' \
HTTP_PASSWORD='iThinksotoo'

ADD s6 /s6
RUN chmod a+x /s6/ss/* /s6/kcptun/* /s6/tinyproxy/* /s6/.s6-svscan/* && \
    sed -i -e '/^Allow /s/^/#/' \
        -e '/^ConnectPort /s/^/#/' \
        -e '/^#DisableViaHeader /s/^#//' /etc/tinyproxy/tinyproxy.conf

EXPOSE $SERVER_PORT/tcp $SERVER_PORT/udp $KCP_LISTEN/udp 8888

CMD ["s6-svscan", "/s6"]