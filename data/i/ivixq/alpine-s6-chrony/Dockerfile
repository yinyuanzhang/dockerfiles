FROM ivixq/alpine-s6:3.11
LABEL maintainer=ivixq

ENV ZABBIX_HOSTNAME=chrony

RUN apk --no-cache upgrade ; \
    apk --no-cache add \
        chrony \
	; \
    rm -rf /var/cache/apk/*

COPY rootfs /

EXPOSE 123/udp

