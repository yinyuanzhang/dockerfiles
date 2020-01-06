#
# Dockerfile for shadowsocks-privoxy
#

FROM shadowsocks/shadowsocks-libev:latest
MAINTAINER fobitfk <fobitfk@gmail.com>

#ss-local config
ENV SERVER_HOST=0.0.0.0
ENV SERVER_PORT=8081
ENV LOCAL_PORT=1080
ENV PASSWORD=
ENV ENCRYPT_METHOD=aes-256-cfb
ENV TIMEOUT=30
ENV LOCAL_ADDRESS=0.0.0.0
ENV ARGS=

#privoxy config
ENV LISTEN_ADDRESS=0.0.0.0:8118
ENV FORWARD_SOCKS5T=127.0.0.1:1080

USER root

COPY rootfs /

RUN \
  apk --update --upgrade add privoxy \
  && rm /var/cache/apk/* \
  && chmod u+x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
