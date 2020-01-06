FROM ivixq/alpine-s6-edge
MAINTAINER ivixq

ENV ZABBIX_HOSTNAME=mariadb


RUN apk add --update \
        mariadb \
        mariadb-client \
        pwgen && \   
    rm -rf /var/cache/apk/* 

COPY rootfs /

#VOLUME ["/var/lib/mysql"]

ENV TERM xterm

EXPOSE 3306

