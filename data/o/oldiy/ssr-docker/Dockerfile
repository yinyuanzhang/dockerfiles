FROM alpine:3.8
MAINTAINER oldiy <oldiy@163.com>

ENV SSR_URL https://github.com/oldiy/shadowsocksr/archive/akkariiin/master.tar.gz
ENV SSR_DIR shadowsocksr-akkariiin-master

WORKDIR /etc

RUN set -ex \
    && apk --update add --no-cache python libsodium rng-tools curl \
    && curl -sSL $SSR_URL | tar xz \
    && apk del curl \
    && rm -rf /var/cache/apk

ENV SERVER_ADDR 0.0.0.0
ENV SERVER_PORT 21618
ENV PASSWORD    oldiy
ENV METHOD      rc4-md5
ENV PROTOCOL    auth_sha1_v4
ENV OBFS        tls1.2_ticket_auth
ENV TIMEOUT     300

EXPOSE $SERVER_PORT/tcp
EXPOSE $SERVER_PORT/udp

WORKDIR /etc/$SSR_DIR/shadowsocks

CMD python server.py \
           -s $SERVER_ADDR \
           -p $SERVER_PORT \
           -k $PASSWORD    \
           -m $METHOD      \
           -O $PROTOCOL    \
           -o $OBFS        \
           -t $TIMEOUT