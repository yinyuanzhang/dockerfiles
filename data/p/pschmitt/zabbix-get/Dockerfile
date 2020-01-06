FROM alpine:latest

LABEL MAINTAINER Philipp Schmitt <philipp@schmitt.co>

RUN apk add --no-cache zabbix-utils

ENTRYPOINT ["/usr/bin/zabbix_get"]
