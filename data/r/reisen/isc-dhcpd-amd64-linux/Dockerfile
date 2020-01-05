FROM debian:latest

RUN apt-get update \
 && apt-get install -y isc-dhcp-server \
 && rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh /usr/sbin
RUN chmod 755 /usr/sbin/entrypoint.sh
COPY isc-dhcp-server /etc/default

ENTRYPOINT ["/usr/sbin/entrypoint.sh"]
