FROM ubuntu:18.04

MAINTAINER Wang, Tao <i@miffyliye.org>

RUN apt-get update \
    && apt-get install -y python-pip libsodium-dev \
    && pip install https://github.com/shadowsocks/shadowsocks/archive/master.zip

ENV FORBIDDEN_IP 127.0.0.0/8,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16
ENV SERVER_ADDR 0.0.0.0
ENV SERVER_PORT 2048
ENV PASSWORD example
ENV METHOD chacha20-ietf-poly1305
ENV TIMEOUT 300
ENV VERBOSE 1

CMD VERBOSE_PARAM=""; \
    if [ "$VERBOSE" -ge "2" ]; then VERBOSE_PARAM="-vv"; fi; \
    if [ "$VERBOSE" -eq "1" ]; then VERBOSE_PARAM="-v"; fi; \
    if [ "$VERBOSE" -eq "-1" ]; then VERBOSE_PARAM="-q"; fi; \
    if [ "$VERBOSE" -le "-2" ]; then VERBOSE_PARAM="-qq"; fi; \
    /usr/bin/python /usr/local/bin/ssserver --forbidden-ip="$FORBIDDEN_IP" \
            -s "$SERVER_ADDR" \
            -p "$SERVER_PORT" \
            -k "$PASSWORD" \
            -m "$METHOD" \
            -t "$TIMEOUT" \
            "$VERBOSE_PARAM";
