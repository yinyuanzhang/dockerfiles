FROM ivixq/alpine-s6:3.11
LABEL maintainer=ivixq

ENV ZABBIX_HOSTNAME=mariadb

RUN apk --no-cache update ; \
    apk --no-cache upgrade ; \
    apk --no-cache add \
        mariadb \
        mariadb-client \
        pwgen \
        ; \   
    rm -rf /var/cache/apk/* 

COPY rootfs /

ENV TERM xterm

EXPOSE 3306
