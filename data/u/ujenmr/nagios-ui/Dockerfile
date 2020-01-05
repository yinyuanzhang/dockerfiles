FROM php:5-apache

ENV NAGIOS_VERSION 4.2.0

WORKDIR /tmp
RUN useradd nagios && \
    groupadd nagcmd && \
    usermod -a -G nagcmd nagios && \
    usermod -a -G nagcmd www-data && \
    apt-get update && \
    apt-get install -y --no-install-recommends wget build-essential unzip && \
    wget http://prdownloads.sourceforge.net/sourceforge/nagios/nagios-${NAGIOS_VERSION}.tar.gz && \
    tar -zxvf nagios-${NAGIOS_VERSION}.tar.gz && \
    cd nagios-${NAGIOS_VERSION} && \
    ./configure --prefix=/opt/nagios --sysconfdir=/etc/nagios --localstatedir=/var/lib/nagios --with-nagios-group=nagios --with-command-group=nagcmd --with-httpd-conf=/etc/apache2/conf-enabled && \
    make all && \
    make install && \
    make install-webconf && \
    make install-commandmode && \
    mkdir -p /etc/nagios && \
    a2enmod cgi && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /var/www
