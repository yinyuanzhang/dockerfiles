FROM nediiii/alpine

LABEL maintainer="nediiii <varnediiii@gmail.com>"

ENV SERVER_ADDR=0.0.0.0 \
    SERVER_PORT=8388 \
    PASSWORD= \
    METHOD=aes-256-gcm \
    TIMEOUT=300 \
    DNS_ADDRS=8.8.8.8,8.8.4.4 \
    ARGS=

# RUN echo "@edge https://mirrors.tuna.tsinghua.edu.cn/alpine/edge/main">> /etc/apk/repositories
# RUN echo "@edgecommunity https://mirrors.tuna.tsinghua.edu.cn/alpine/edge/community">> /etc/apk/repositories

# RUN echo "@testing https://mirrors.tuna.tsinghua.edu.cn/alpine/edge/testing" >> /etc/apk/repositories && \
# apk add --no-cache shadowsocks-libev@testing

RUN apk add --no-cache -X https://mirrors.tuna.tsinghua.edu.cn/alpine/edge/testing shadowsocks-libev

CMD exec ss-server \
    -s $SERVER_ADDR \
    -p $SERVER_PORT \
    -k ${PASSWORD:-$(hostname)} \
    -m $METHOD \
    -t $TIMEOUT \
    -d $DNS_ADDRS \
    -u \
    --fast-open \
    $ARGS
# docker build . -t nediiii/shadowsocks-libev
# docker run -d -p 8388:8388
