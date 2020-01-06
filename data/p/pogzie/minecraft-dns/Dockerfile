FROM alpine:latest

MAINTAINER Pogz Ortile <pogz@outlook.com>

WORKDIR /etc/bind

COPY etc ./

RUN apk --update add bind

EXPOSE 53

CMD ["named", "-c", "/etc/bind/named.conf", "-g", "-u", "named"]