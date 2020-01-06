FROM alpine:edge
MAINTAINER ivixq

ARG TZ=Asia/Shanghai 
ARG S6_OVERLAY_VERSION=v1.21.7.0

ENV DEBUG_MODE=FALSE \ 
    ENABLE_ZABBIX=TRUE \
    ENABLE_CRON=TRUE \
    TERM=xterm

RUN apk update && apk upgrade --available && \
    apk add --update  \
        bash \
        curl \
        su-exec \
        sudo \
        zabbix-agent \
        zabbix-utils \
        tzdata && \
    rm -rf /var/cache/apk/* && \
    cp /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone && \
    echo '%zabbix ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && \
    mkdir -p /usr/src && \
 
    curl -sSL https://github.com/just-containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-amd64.tar.gz | tar xfz - -C / && \

    mkdir -p /setup/cron
    
COPY rootfs /

EXPOSE 10050/TCP

ENTRYPOINT [ "/init" ]

CMD []

