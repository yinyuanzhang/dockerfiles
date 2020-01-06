FROM ubuntu:latest
MAINTAINER richh@mellanox.com

ENV BIND_USER=bind \
    DHCP_USER=dhcpd \
    DHCP_INTERFACES=" " \
    DATA_DIR=/data

ARG DEBIAN_FRONTEND=noninteractive

RUN rm -rf /etc/apt/apt.conf.d/docker-gzip-indexes \
 && apt-get -q -y update \
 && apt-get -q -y -o "DPkg::Options::=--force-confold" -o "DPkg::Options::=--force-confdef" install \
 vim.tiny wget net-tools ca-certificates unzip gnupg apt-transport-https apt-show-versions \
 && wget http://www.webmin.com/jcameron-key.asc -qO - | apt-key add - \
 && echo "deb http://download.webmin.com/download/repository sarge contrib" >> /etc/apt/sources.list \
 && apt-get -q -y update \
 && apt-get -q -y -o "DPkg::Options::=--force-confold" -o "DPkg::Options::=--force-confdef" install apt-utils \
 && apt-get -q -y -o "DPkg::Options::=--force-confold" -o "DPkg::Options::=--force-confdef" dist-upgrade \
 && apt-get -q -y -o "DPkg::Options::=--force-confold" -o "DPkg::Options::=--force-confdef" install \
 bind9 isc-dhcp-server webmin dnsutils \
 && apt-get -q -y autoremove \
 && apt-get -q -y clean \
 && rm -rf /var/lib/apt/lists/*

## Adjust isc-dhcp-server so that it only will run DHCPv4
RUN sed -i '/INTERFACESv4\=\"\"/c\INTERFACESv4\=\" \"' /etc/default/isc-dhcp-server && \
 sed -i '/INTERFACESv6\=\"\"/c\' /etc/default/isc-dhcp-server

## Install Certificate Manager for Webmin - Future examination for looking at BCP003-01
RUN cd /home \
 && wget http://www.webmin.com/download/modules/certmgr.wbm.gz \
 && /usr/share/webmin/install-module.pl ./certmgr.wbm.gz \
 && rm certmgr.wbm.gz

COPY entrypoint.sh /home/entrypoint.sh
RUN chmod 755 /home/entrypoint.sh

EXPOSE 53/udp 53/tcp 67/udp 68/udp 10000/tcp

#WORKDIR /home/
#ENTRYPOINT ["/home/entrypoint.sh"]
#CMD []
