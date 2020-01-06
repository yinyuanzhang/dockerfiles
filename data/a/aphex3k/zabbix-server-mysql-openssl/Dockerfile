FROM zabbix/zabbix-server-mysql:latest
LABEL maintainer "Michael Henke <433270+aphex3k@users.noreply.github.com>"

USER root
# Install wget and curl with ssl support
RUN apk --no-cache add openssl curl wget ca-certificates

COPY ["alertscripts/prowl.sh", "/usr/lib/zabbix/alertscripts/"]
COPY ["alertscripts/prowl", "/usr/lib/zabbix/alertscripts/"]
