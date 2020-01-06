# FROM alpine-s6-edge
FROM ivixq/alpine-s6-edge
MAINTAINER ivixq

ARG LOGANALYZER_VERSION=4.1.7

## Install syslog-ng php5 apache
RUN apk --update add rsyslog rsyslog-mysql mariadb-client \
          php5-apache2 php5-gd php5-mysqli ttf-dejavu && \
    rm -rf /var/cache/apk/*

## Install Loganalyzer
RUN curl -sSL http://download.adiscon.com/loganalyzer/loganalyzer-${LOGANALYZER_VERSION}.tar.gz | tar xfz - -C / && \
    mkdir -p /var/www/html/loganalyzer && \
    cd /loganalyzer-${LOGANALYZER_VERSION} && \
    cp -r src/* /var/www/html/loganalyzer && \
    cp -r contrib/* /var/www/html/loganalyzer && \
    rm -rf /loganalyzer-${LOGANALYZER_VERSION}

COPY rootfs /

RUN touch /var/www/html/loganalyzer/config.php && \
    chmod 666 /var/www/html/loganalyzer/config.php && \
    chmod +x /var/www/html/loganalyzer/configure.sh && \
    chmod +x /var/www/html/loganalyzer/secure.sh && \
    . /var/www/html/loganalyzer/configure.sh && \
    . /var/www/html/loganalyzer/secure.sh

## Export volumes directory
#VOLUME ["/cfg"]

## Export ports
EXPOSE 10514/tcp 514/udp


