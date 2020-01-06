FROM zabbix/zabbix-proxy-mysql:alpine-latest

USER root
RUN apk add --update python python-dev py-pip build-base
RUN pip install pysnmp
RUN pip install requests
RUN pip install workalendar

USER zabbix