FROM hypriot/rpi-alpine:3.6

MAINTAINER cola <colachg@gmail.com>

ARG KCP_VER=v20180922
ARG KCP_URL=https://github.com/xtaci/kcptun/releases/download/$KCP_VER/kcptun-linux-arm-$KCP_VER.tar.gz

RUN set -ex &&\
    apk add --no-cache --virtual .build curl &&\
    curl -sSL $KCP_URL | tar xz -C /usr/local/bin/ client_linux_arm7 &&\
    apk del --purge .build &&\
    rm -rf /var/cache/* /tmp/*

WORKDIR /kcptun

EXPOSE 2000/udp

ENTRYPOINT ["/usr/local/bin/client_linux_arm7"]

CMD ["-c", "kcptun.json"]
