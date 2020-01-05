FROM debian:stable
RUN apt-get update && apt-get install -y bind9
RUN rm -rf /etc/bind/*
RUN mkdir -p /var/run/named && chown bind:bind /var/run/named
ENTRYPOINT ["/usr/sbin/named", "-f", "-c", "/etc/bind/named.conf"]
