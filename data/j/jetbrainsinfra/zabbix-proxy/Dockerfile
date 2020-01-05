# Instal additional packages for zabbix checks
# Based on zabbix-proxy-mysql:latest

# Instal additional packages for zabbix checks
# Based on zabbix-proxy-mysql:latest

FROM zabbix/zabbix-proxy-mysql:alpine-4.2.5
MAINTAINER Stanislav Osipov <stanislav.osipov@jetbrains.com>
USER root
RUN apk update && apk upgrade &&\
    apk add openssl openssh bc jq curl git grep net-snmp-tools git perl perl-json py-pip grep docker && \
    rm -rf /var/cache/apk/*
