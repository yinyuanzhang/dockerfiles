FROM alpine

MAINTAINER Chen Augus <tianhao.chen@gmail.com>

RUN apk update && apk --no-cache add bind && mkdir -p /var/bind/log && rm -rf /var/cache/apk/*

COPY named.conf /etc/bind/named.conf

EXPOSE 53/udp

CMD /usr/sbin/named -f -c /etc/bind/named.conf
