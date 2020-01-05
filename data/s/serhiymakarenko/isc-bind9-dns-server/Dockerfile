# The MIT License
#
# Copyright (c) 2019, Serhiy Makarenko

FROM debian:10-slim
LABEL maintainer="serhiy.makarenko@me.com"

ARG DEBIAN_FRONTEND=noninteractive

ENV APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=DontWarn

RUN apt-get update && \
    apt-get install -y --no-install-recommends --no-install-suggests \
    apt-utils gnupg curl debian-keyring apt-transport-https ca-certificates && \
    curl -1sLf 'https://packages.sury.org/bind/apt.gpg' | apt-key add - && \
    echo 'deb https://packages.sury.org/bind/ buster main' > /etc/apt/sources.list.d/isc-bind.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends --no-install-suggests bind9=1:9.14.9-1+0~20191219.21+debian10~1.gbp6b8881 && \
    chown -R bind:bind /etc/bind && \
    apt-get purge -y --auto-remove apt-utils gnupg curl debian-keyring apt-transport-https ca-certificates && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 53/udp 53/tcp

ENTRYPOINT ["/usr/sbin/named"]
CMD ["-c", "/etc/bind/named.conf", "-g", "-u", "bind"]
