FROM ubuntu:17.10

RUN apt-get update -y && apt-get install -y \
    bind9 \
    dnsutils \
     make \
     nmap \
 && apt-get -y autoremove && rm -rf /var/lib/apt/lists/*

ENV DOMAIN_NAME=docker.local
COPY files /mnt/bind
RUN sed -i -e 's/-u bind/-4 -u bind/' /etc/default/bind9

EXPOSE 53/udp 53/tcp
WORKDIR /mnt/bind

CMD ["/mnt/bind/docker-entry.sh"]