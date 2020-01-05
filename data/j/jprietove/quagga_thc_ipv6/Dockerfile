# Quagga with thc_ipv6
# For use with GNS3 as a Quagga Router
FROM debian:jessie
MAINTAINER Javier Prieto <javier.prieto.edu@juntadeandalucia.es>

LABEL Title="Quagga" \
      Description="For use with GNS3 as a Quagga Router"

ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y quagga 

COPY config/* /etc/quagga/
RUN chown quagga:quagga /etc/quagga/* && chmod 640 /etc/quagga/*
RUN echo "net.ipv6.conf.all.forwarding=1" >> /etc/sysctl.conf

VOLUME [ "/etc/quagga/" ]

RUN apt-get install -y git libpcap-dev libssl-dev libnetfilter-queue-dev iptables build-essential
RUN git clone https://github.com/vanhauser-thc/thc-ipv6.git 
WORKDIR /thc-ipv6
RUN make all && make install

ENTRYPOINT export VTYSH_PAGER=more && /etc/init.d/quagga start &&  sysctl -p && bash


