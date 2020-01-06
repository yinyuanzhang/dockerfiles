FROM centos:7

ENV DNSPORT=53 TIMEOUT=3600

RUN yum -y install dnsmasq ipset &&\
    yum clean all

COPY dnsmasq.conf /etc/
COPY entrypoint.sh /

WORKDIR /

ENTRYPOINT ["/usr/bin/bash", "entrypoint.sh"] 
