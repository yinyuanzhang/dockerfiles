FROM alpine:3.10

LABEL maintainer="xxz <xiao_xiao_zi@qq.com>"

ARG TZ='Asia/Shanghai'

ENV TZ ${TZ}
ENV KCP_MODULE kcpclient
ENV KCP_CONFIG -l :60833 -r SERVER_IP:60833 -key "kcptun" -crypt aes-128 -nocomp -datashard 10 -parityshard 3 -mtu 1350 -sndwnd 1024 -rcvwnd 1024 -dscp 46 -keepalive 10 -sockbuf 16777217 -mode fast3
ENV KCP_DOWNLOAD_URL 'https://github.com/xtaci/kcptun/releases/download/v20190910/kcptun-linux-amd64-20190910.tar.gz'

RUN apk upgrade \
    && apk add bash tzdata runit \
    && apk add --virtual .build-deps \
        curl \
        tar \
    && curl -o kcptun.tar.gz -sSLO ${KCP_DOWNLOAD_URL} \
    && tar -zxf kcptun.tar.gz \
    && mv server_linux_amd64 /usr/bin/kcpserver \
    && mv client_linux_amd64 /usr/bin/kcpclient \
    && ln -sf /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo ${TZ} > /etc/timezone \
    && adduser -h /tmp -s /sbin/nologin -S -D -H kcptun \
    && apk del .build-deps \
    && rm -rf kcptun.tar.gz \
        /etc/service \
        /var/cache/apk/*

SHELL ["/bin/bash"]

COPY runit /etc/service
COPY entrypoint.sh /entrypoint.sh

RUN ["chmod", "777", "/etc/service", "-R"]
RUN ["chmod", "+x", "/entrypoint.sh"]

ENTRYPOINT ["/entrypoint.sh"]
