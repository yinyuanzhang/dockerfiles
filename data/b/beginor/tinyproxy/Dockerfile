FROM alpine:latest

LABEL MAINTAINER="beginor <beginor@qq.com>"

RUN apk add --no-cache --update tinyproxy

ADD ./tinyproxy.conf /etc/tinyproxy/tinyproxy.conf

EXPOSE 8888

# VOLUME ["/etc/tinyproxy", "/var/log/tinyproxy"]

CMD ["/usr/sbin/tinyproxy", "-d"]
