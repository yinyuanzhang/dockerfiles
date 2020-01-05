FROM alpine:latest
MAINTAINER IRoN <pety3bi@gmail.com>

ENV LISTEN_IP 0.0.0.0
ENV LISTEN_PORT 443
ENV SSH_HOST localhost
ENV SSH_PORT 22
ENV OPENVPN_HOST localhost
ENV OPENVPN_PORT 1194
ENV HTTPS_HOST localhost
ENV HTTPS_PORT 443
ENV SOCKS_HOST localhost
ENV SOCKS_PORT 1080
ENV MTPROTO_HOST localhost
ENV MTPROTO_PORT 443

RUN apk update && \
    apk add --update-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing/ sslh && \
    rm -rf /var/cache/apk/*

ADD entry.sh /usr/local/bin/entry.sh
RUN chmod +x /usr/local/bin/entry.sh

ENTRYPOINT ["/usr/local/bin/entry.sh"]
