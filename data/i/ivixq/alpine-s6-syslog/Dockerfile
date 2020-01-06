FROM ivixq/alpine-s6:3.9
LABEL maintainer=ivixq

ARG LOGANALYZER_VERSION=4.1.7
ENV ZABBIX_HOSTNAME=syslog

## Install syslog-ng php5 apache
RUN echo 'https://mirrors.aliyun.com/alpine/v3.8/community' >> /etc/apk/repositories ; \
    apk --no-cache update ; \
    apk upgrade --available ; \
    apk add --update \
        rsyslog rsyslog-mysql mariadb-client ttf-dejavu \
        php5-apache2 php5-gd php5-mysqli ; \
    rm -rf /var/cache/apk/* ; \
## Install Loganalyzer
    curl -sSL http://download.adiscon.com/loganalyzer/loganalyzer-${LOGANALYZER_VERSION}.tar.gz | tar xfz - -C / ; \
    mkdir -p /var/www/html/loganalyzer ; \
    cd /loganalyzer-${LOGANALYZER_VERSION} ; \
    cp -r src/* /var/www/html/loganalyzer ; \
    cp -r contrib/* /var/www/html/loganalyzer ; \
    rm -rf /loganalyzer-${LOGANALYZER_VERSION}

COPY rootfs /

RUN touch /var/www/html/loganalyzer/config.php ; \
    chmod 666 /var/www/html/loganalyzer/config.php ; \
    chmod +x /var/www/html/loganalyzer/configure.sh ; \
    chmod +x /var/www/html/loganalyzer/secure.sh ; \
    . /var/www/html/loganalyzer/configure.sh ; \
    . /var/www/html/loganalyzer/secure.sh

## Export volumes directory
#VOLUME ["/cfg"]

## Export ports
EXPOSE 514/udp
