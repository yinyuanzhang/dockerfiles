FROM fernandoenzo/debian:10s-min
MAINTAINER Fernando Enzo Guarini (fernandoenzo@gmail.com)

COPY scripts/basics /tmp
RUN bash /tmp/basics

COPY static/db.generic /etc/bind/
COPY static/named.conf.local /etc/bind/
COPY static/named.conf.options /etc/bind/

COPY scripts/boot /usr/local/boot

EXPOSE 53/udp

